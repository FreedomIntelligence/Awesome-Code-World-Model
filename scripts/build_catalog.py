#!/usr/bin/env python3
"""Validate the bibliography and build the README, annotated catalogue, and badges."""
import argparse
import datetime as dt
import json
import re
import sys
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from build_classification import outputs as classification_outputs
from build_master_list import outputs as master_list_outputs

ROOT = Path(__file__).resolve().parents[1]
SCOPES = {'core', 'historical', 'enabling', 'benchmark', 'resource', 'comparator', 'adjacent', 'survey'}
DEPTHS = {'targeted_fulltext': 'FT', 'abstract': 'A', 'metadata': 'M'}
ROLES = {'transition', 'observation'}
PRESENTATION = {
    'worldcoder': ('WorldCoder-type · Programmatic Dynamics', 'State-level executable dynamics: transition mechanisms, world-program induction, planning, and model repair, without generated appearance.', False),
    'code_as_world': ('Code-as-World-type · Whitebox Worlds + Generative Rendering', 'Code keeps persistent state and rules over a whitebox/proxy world; a generative renderer supplies appearance.', False),
    'vibeworlding': ('VibeWorlding-type · Agentic 3D World Construction', 'Code specifies the full 3D world (geometry, materials, layout, and optionally physics) for conventional rendering or simulation; static scenes included.', False),
}
OTHER_GROUPS = {
    'gui': {
        'title': 'GUI World Models',
        'description': 'GUI, web, and computer-use world models, including renderable-code screen predictors. Kept outside the three families.',
        'title_zh': 'GUI 世界模型',
        'description_zh': 'GUI、网页与 computer-use 世界模型，包括以可渲染代码预测下一屏的工作；不纳入三类主线。',
    },
    'benchmark': {
        'title': 'Benchmarks',
        'description': 'Benchmarks and diagnostic studies, grouped by what they evaluate.',
        'title_zh': '评测基准',
        'description_zh': '评测基准与诊断研究，按评测对象分组。',
    },
}
UNASSIGNED_GROUPS = {*OTHER_GROUPS, 'survey'}
BENCHMARK_TARGETS = {
    'worldcoder': ('state-level dynamics (WorldCoder-type)', '纯状态动力学（WorldCoder-type）'),
    'code_as_world': ('program-to-video rendering (Code-as-World-type)', '程序到视频的渲染（Code-as-World-type）'),
    'vibeworlding': ('3D world construction (VibeWorlding-type)', '3D 世界构建（VibeWorlding-type）'),
    'video_wm': ('non-code video and learned world models', '非代码的视频与学习型世界模型'),
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def parse_date(value):
    require(isinstance(value, str) and re.fullmatch(r'\d{4}(?:-\d{2}){0,2}', value), f'Invalid date: {value!r}')
    parts = [int(p) for p in value.split('-')]
    return dt.date(*(parts + [1] * (3 - len(parts))))

def record_date(p):
    return p.get('first_public_date') or p['available_by']

def display_date(p):
    return p['first_public_date'] if p.get('first_public_date') else 'by ' + p['available_by']

def load_data():
    data = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    require(data['schema_version'] == 1, 'Unsupported schema version')
    updated = parse_date(data['updated_on'])
    cutoff = parse_date(data['literature_cutoff'])
    require(cutoff <= updated, 'Literature cutoff is later than catalogue update')
    sections = {s['id']: s for s in data['sections']}
    require(len(sections) == len(data['sections']), 'Duplicate sections')
    require(all(re.fullmatch(r'[a-z][a-z0-9_]*', s) for s in sections), 'Invalid section identifier')
    records = data['papers']
    require(records, 'Empty bibliography')
    for key in ['id', 'citation_key', 'source_url']:
        values = [p[key] for p in records]
        require(len(set(values)) == len(values), f'Duplicate {key}')
    for key in ['arxiv_id', 'doi']:
        values = [p[key] for p in records if key in p]
        require(len(set(values)) == len(values), f'Duplicate {key}')
    ids = {p['id'] for p in records}
    by_id = {p['id']: p for p in records}
    for p in records:
        pid = p['id']
        for field in ['title', 'summary', 'source_url', 'citation_key']:
            require(isinstance(p[field], str) and p[field].strip() == p[field] and p[field], f'{pid}: invalid {field}')
        require(re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', p['citation_key']), f'{pid}: invalid BibTeX key')
        require(p['authors'] and all(isinstance(a, str) and a.strip() == a and a for a in p['authors']), f'{pid}: invalid authors')
        require(p['scope'] in SCOPES, f'{pid}: invalid scope')
        require(p['section'] is None or p['section'] in sections, f'{pid}: unknown section')
        require(p['review_depth'] in DEPTHS, f'{pid}: invalid review depth')
        require(set(p['code_roles']) <= ROLES and len(p['code_roles']) == len(set(p['code_roles'])), f'{pid}: invalid code roles')
        require(p['tags'] and len(p['tags']) == len(set(p['tags'])), f'{pid}: missing or duplicate tags')
        require(all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', t) for t in p['tags']), f'{pid}: invalid tag')
        if not p.get('first_public_date'):
            require(p.get('source_type') == 'project' and p.get('available_by') and p.get('date_basis'),
                    f'{pid}: unknown first date requires project availability evidence')
            require(p.get('evidence_urls'), f'{pid}: missing availability evidence URLs')
        first = parse_date(record_date(p))
        reviewed = parse_date(p['reviewed_on'])
        require(isinstance(p['year'], int) and first.year == p['year'], f'{pid}: year/date mismatch')
        require(first <= cutoff and first <= reviewed <= updated, f'{pid}: inconsistent dates')
        if 'metadata_checked_on' in p:
            require(first <= parse_date(p['metadata_checked_on']) <= updated, f'{pid}: invalid metadata-check date')
        if 'reviewed_version' in p:
            require(re.fullmatch(r'v[1-9]\d*', p['reviewed_version']), f'{pid}: invalid reviewed version')
        url = urlparse(p['source_url'])
        require(url.scheme == 'https' and url.netloc and not url.username and not url.password, f'{pid}: invalid source URL')
        if 'arxiv_id' in p:
            require(re.fullmatch(r'\d{4}\.\d{4,5}', p['arxiv_id']), f'{pid}: invalid arXiv ID')
            require(p['source_url'] == 'https://arxiv.org/abs/' + p['arxiv_id'], f'{pid}: arXiv URL mismatch')
            require(pid == p['arxiv_id'], f'{pid}: arXiv catalogue ID mismatch')
        if 'doi' in p:
            require(re.fullmatch(r'10\.\d{4,9}/\S+', p['doi']), f'{pid}: invalid DOI')
        for related in p.get('related_ids', []):
            require(related in ids and related != pid, f'{pid}: invalid related record')
            require(pid in by_id[related].get('related_ids', []), f'{pid}: asymmetric related_ids')
    require(all(any(p['section'] == sid for p in records) for sid in sections), 'Empty catalogue section')
    classification = json.loads((ROOT / 'data/classification.json').read_text(encoding='utf-8'))
    groups = {r['id']: r['unassigned_group'] for r in classification['records'] if r.get('unassigned_group')}
    for pid, group in groups.items():
        require(group in UNASSIGNED_GROUPS, f'{pid}: unknown unassigned group')
        require(pid in by_id and by_id[pid]['section'] is None, f'{pid}: grouped record must be unassigned')
    for r in classification['records']:
        require((r.get('benchmark_target') in BENCHMARK_TARGETS) == (r.get('unassigned_group') == 'benchmark'),
                f"{r['id']}: benchmark records need exactly one valid benchmark_target")
        if r.get('unassigned_group') == 'survey':
            require(r.get('comparison') and r.get('comparison_zh'), f"{r['id']}: survey needs comparison text")
    require(all(p['section'] or p['id'] in groups for p in records), 'Every record needs a family or an unassigned group')
    data['unassigned_groups'] = groups
    data['benchmark_targets'] = {r['id']: r['benchmark_target'] for r in classification['records'] if r.get('benchmark_target')}
    data['comparisons'] = {r['id']: (r['comparison'], r['comparison_zh']) for r in classification['records'] if r.get('comparison')}
    return data

def md(value):
    return value.replace('|', '\\|').replace('\n', ' ')

def load_localization(data):
    localized = json.loads((ROOT / 'data/readme.zh-CN.json').read_text(encoding='utf-8'))
    require(localized['locale'] == 'zh-CN', 'Unexpected README locale')
    require(set(localized['sections']) == {s['id'] for s in data['sections']}, 'Chinese section translations are out of sync')
    require(set(localized['summaries']) == {p['id'] for p in data['papers']}, 'Chinese paper summaries are out of sync')
    for sid, section in localized['sections'].items():
        require(all(isinstance(section.get(k), str) and section[k].strip() for k in ('title', 'description')), f'{sid}: missing Chinese section text')
    for pid, summary in localized['summaries'].items():
        require(isinstance(summary, str) and summary.strip() and re.search(r'[\u3400-\u9fff]', summary), f'{pid}: missing Chinese summary')
    return localized

def load_survey_links():
    links = json.loads((ROOT / 'data/survey-links.json').read_text(encoding='utf-8'))
    require(set(links) == {'arxiv_url', 'semantic_scholar_url', 'semantic_scholar_citations_badge_url'}, 'Unexpected survey link fields')
    for key, value in links.items():
        if value is None:
            continue
        require(isinstance(value, str), f'{key}: use an HTTPS URL or null')
        parsed = urlparse(value)
        require(parsed.scheme == 'https' and parsed.netloc and not parsed.username and not parsed.password, f'{key}: invalid publication URL')
    require(not links['semantic_scholar_citations_badge_url'] or links['semantic_scholar_url'], 'A live citation badge needs the survey paper link')
    return links

def section_papers(data, section_id):
    return sorted((p for p in data['papers'] if p['section'] == section_id),
                  key=lambda p: (record_date(p), p['id']), reverse=True)

def group_papers(data, group):
    return [p for p in section_papers(data, None) if data['unassigned_groups'].get(p['id']) == group]

def paper_row(p, localized=None):
    label = md(p['title'])
    if p.get('alias') and p['alias'].lower() not in p['title'].lower():
        label += f" ({md(p['alias'])})"
    link_label = 'Project' if p.get('source_type') == 'project' else 'PDF'
    summary = md(localized['summaries'][p['id']] if localized else p['summary'])
    return f"| `{p['year']}` | **{label}** | {summary} | [{link_label}]({p['source_url']}) |"

def paper_table(papers, localized=None):
    header = ('| 年份 | 论文 | 核心机制与简介 | 链接 |' if localized
              else '| Year | Paper | Summary | Link |')
    lines = [header, '|---|---|---|:-:|']
    lines.extend(paper_row(p, localized) for p in papers)
    return lines

def catalogue(data, localized=None):
    if localized:
        lines = [f"**{len(data['papers'])} 条文献来源** · 截止 **{data['literature_cutoff']}** · 按发布日期倒序排列。完整信息见[详细核查表](docs/catalogue.md)与[全量论文总表](docs/paper-master-list.md)。"]
    else:
        lines = [f"**{len(data['papers'])} sources** · updated through **{data['literature_cutoff']}** · ordered by date (newest first). Full metadata in the [annotated catalogue](docs/catalogue.md) and [master list](docs/paper-master-list.md)."]
    for index, section in enumerate(data['sections'], 1):
        title, description, folded = PRESENTATION[section['id']]
        if localized:
            title = localized['sections'][section['id']]['title']
            description = localized['sections'][section['id']]['description']
        subset = section_papers(data, section['id'])
        lines += ['', f'<a id="papers-{section["id"]}"></a>', f'### {index:02d} · {title} ({len(subset)})', '',
                  f'*{description}*', '', *paper_table(subset, localized), '',
                  '[↑ 返回总览](#contents)' if localized else '[↑ Back to overview](#contents)']
    lines += ['', '<a id="papers-other"></a>', '### 其他' if localized else '### Other', '',
              '*不属于三类主线的记录，分为 GUI 世界模型与评测基准两组。*' if localized else
              '*Records outside the three primary families: GUI world models and benchmarks.*']
    for gid, spec in OTHER_GROUPS.items():
        subset = group_papers(data, gid)
        title = spec['title_zh'] if localized else spec['title']
        description = spec['description_zh'] if localized else spec['description']
        lines += ['', f'<a id="papers-other-{gid}"></a>', f'#### {title} ({len(subset)})', '', f'*{description}*', '',
                  '<details>', f'<summary>{len(subset)} {"条记录" if localized else "records"}</summary>', '']
        if gid == 'benchmark':
            for tid, (en, zh) in BENCHMARK_TARGETS.items():
                part = [p for p in subset if data['benchmark_targets'][p['id']] == tid]
                if part:
                    lines += [f"**{'评测' if localized else 'Evaluating'} {zh if localized else en}**", '', *paper_table(part, localized), '']
        else:
            lines += [*paper_table(subset, localized), '']
        lines += ['</details>']
    lines += ['', '[↑ 返回总览](#contents)' if localized else '[↑ Back to overview](#contents)']
    return '\n'.join(lines)

def related_surveys(data, localized=None):
    surveys = group_papers(data, 'survey')
    if localized:
        lines = [
            '相关综述以视频模型或通用世界模型为中心；本综述以**可执行代码作为世界的载体**为纳入标准，按代码承担了世界的多少部分（纯状态 / 白模 + 生成式渲染 / 完整 3D）组织文献，视频模型只作为可选的渲染器出现。',
            '',
            '<details>',
            f'<summary><strong>展开查看与 {len(surveys)} 篇相关综述的逐条对比</strong></summary>',
            '',
            '| 年份 | 相关综述 | 与本综述的区别 | 链接 |',
            '|---|---|---|:-:|',
        ]
    else:
        lines = [
            'Related surveys centre on video models or world models in general. This survey takes **executable code as the substrate of the world** as its inclusion criterion and organises the literature by how much of the world code carries (state only / whitebox + generative rendering / full 3D); video models appear only as optional renderers.',
            '',
            '<details>',
            f'<summary><strong>Compare with {len(surveys)} related surveys</strong></summary>',
            '',
            '| Year | Survey | How We Differ | Link |',
            '|---|---|---|:-:|',
        ]
    for p in surveys:
        label = md(p['title'])
        en, zh = data['comparisons'][p['id']]
        diff = md(zh if localized else en)
        lines.append(f"| `{p['year']}` | **{label}** | {diff} | [PDF]({p['source_url']}) |")
    lines += ['', '</details>']
    return '\n'.join(lines).rstrip()

def navigation(data, localized=None):
    taxonomy_meta = {
        'worldcoder': (
            'State & dynamics only',
            'Does code predict action consequences and support planning?',
            '纯状态与动力学',
            '代码能否预测动作后果并支持规划？',
        ),
        'code_as_world': (
            'Whitebox world + generative rendering',
            'Can executable state & rules drive a generatively rendered world?',
            '白模世界 + 生成式渲染',
            '代码维护的白模状态与规则能否驱动生成式渲染？',
        ),
        'vibeworlding': (
            'Full 3D world',
            'Can an agent write and edit a full 3D world in code?',
            '完整 3D 世界',
            'agent 能否用代码构建并编辑完整 3D 世界？',
        ),
    }
    if localized:
        lines = ['| 分类主线 | 代码承担内容 | 核心问题 | 文献数 |', '|---|---|---|---:|']
    else:
        lines = ['| Family | Code Carries | Core Question | Papers |', '|---|---|---|---:|']
    for index, section in enumerate(data['sections'], 1):
        sid = section['id']
        count = len(section_papers(data, sid))
        title = localized['sections'][sid]['title'] if localized else PRESENTATION[sid][0]
        short_title = title.split(' · ')[0]
        carries_en, q_en, carries_zh, q_zh = taxonomy_meta[sid]
        carries, question = (carries_zh, q_zh) if localized else (carries_en, q_en)
        lines.append(f"| **[{index:02d} · {short_title}](#papers-{sid})** | {carries} | {question} | **{count}** |")
    gui_n = len(group_papers(data, 'gui'))
    bench_n = len(group_papers(data, 'benchmark'))
    survey_n = len(group_papers(data, 'survey'))
    other_total = gui_n + bench_n + survey_n
    if localized:
        lines.append(
            f"| **[其他](#papers-other)** | GUI 世界、评测与综述 | "
            f"[GUI 世界模型](#papers-other-gui) ({gui_n}) · [评测基准](#papers-other-benchmark) ({bench_n}) · [相关综述](#related-surveys) ({survey_n}) | **{other_total}** |"
        )
    else:
        lines.append(
            f"| **[Other](#papers-other)** | GUI worlds, benchmarks & surveys | "
            f"[GUI World Models](#papers-other-gui) ({gui_n}) · [Benchmarks](#papers-other-benchmark) ({bench_n}) · [Related Surveys](#related-surveys) ({survey_n}) | **{other_total}** |"
        )
    return '\n'.join(lines)

def annotated_catalogue(data):
    lines = ['# Annotated catalogue', '', '<!-- Generated from data/papers.json. -->', '',
             '[← Browse the paper collection](../README.md#paper-collection) · [Structured data](../data/papers.json) · [BibTeX](../papers.bib)', '',
             f"**{len(data['papers'])} source records** · literature cutoff **{data['literature_cutoff']}** · metadata snapshot **{data['updated_on']}**.", '',
             'Review: **FT** = targeted full-text sections · **A** = metadata and abstract · **M** = bibliographic metadata.', '',
             'Review depth describes citation and mechanism checking. Dates prefixed **by** are documented availability bounds, not first-release dates. Experimental conditions appear below each table; the [evaluation framework](evaluation.md) explains the shared comparisons.', '',
             '[Three-family taxonomy →](coarse-taxonomy.md) · [Paper master list →](paper-master-list.md)']
    for section in data['sections']:
        subset = section_papers(data, section['id'])
        lines += ['', f"## {section['title']} ({len(subset)})", '',
                  '| Date | Paper | Mechanism / relevance | Scope | Review |',
                  '|---|---|---|---|---|']
        for p in subset:
            label = md(p['title'])
            if p.get('alias') and p['alias'].lower() not in p['title'].lower():
                label += f" **({md(p['alias'])})**"
            paper = f"[{label}]({p['source_url']})"
            lines.append(f"| {display_date(p)} | {paper} | {md(p['summary'])} | {p['scope']} | {DEPTHS[p['review_depth']]} |")
        notes = [p for p in subset if p.get('evidence_notes')]
        if notes:
            lines += ['', '<details>', f'<summary>Evidence notes ({len(notes)})</summary>', '']
            for p in notes:
                lines += [f"- **{md(p.get('alias', p['title']))}:** {p['evidence_notes']}"]
            lines += ['', '</details>']
    blocks = [('Other · GUI world models', 'GUI, web, and computer-use world models kept outside the three families.', group_papers(data, 'gui')),
              ('Other · Benchmarks', 'Benchmarks and diagnostic studies. The README and master list group them by what they evaluate.', group_papers(data, 'benchmark')),
              ('Related surveys', 'Surveys compared against in the README.', group_papers(data, 'survey'))]
    for heading, note, unassigned in blocks:
        if not unassigned:
            continue
        lines += ['', f"## {heading} ({len(unassigned)})", '', note, '',
                  '| Date | Paper | Mechanism / relevance | Scope | Review |',
                  '|---|---|---|---|---|']
        for p in unassigned:
            label = md(p['title'])
            if p.get('alias') and p['alias'].lower() not in p['title'].lower():
                label += f" **({md(p['alias'])})**"
            lines.append(f"| {display_date(p)} | [{label}]({p['source_url']}) | {md(p['summary'])} | {p['scope']} | {DEPTHS[p['review_depth']]} |")
    return '\n'.join(lines) + '\n'

def badge(label, value, color='#6c8ba8', left_color='#4a5568'):
    left = max(42, len(label) * 7 + 16)
    right = max(36, len(value) * 7 + 16) if value else 0
    title = escape(f'{label}: {value}' if value else label)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{left + right}" height="20" role="img" aria-label="{title}">
  <title>{title}</title>
  <rect width="{left + right}" height="20" fill="{color}"/>
  <rect width="{left}" height="20" fill="{left_color if value else color}"/>
  <g fill="#fff" text-anchor="middle" font-family="Verdana, Arial, sans-serif" font-size="11">
    <text x="{left / 2:g}" y="14">{escape(label)}</text>
    <text x="{left + right / 2:g}" y="14">{escape(value)}</text>
  </g>
</svg>
'''

def badges(data, survey_links):
    specs = {'sources': ('Sources', str(len(data['papers']))), 'topics': ('Topics', str(len(data['sections']))),
             'cutoff': ('Literature', data['literature_cutoff']), 'contributions': ('Contributions', 'welcome'),
             'arxiv': ('arXiv', ''), 'paper': ('Paper', ''), 'project': ('Project', '')}
    colors = {'arxiv': '#b47b7b', 'paper': '#7b8a97', 'project': '#7b9a8d'}
    output = {ROOT / f'assets/badges/{name}.svg': badge(label, value, colors.get(name, '#6c8ba8'))
              for name, (label, value) in specs.items()}
    output[ROOT / 'assets/badges/survey-arxiv.svg'] = badge('arXiv', 'Paper' if survey_links['arxiv_url'] else '—', '#8c96a0', '#4a5568')
    output[ROOT / 'assets/badges/survey-citations.svg'] = badge('Semantic Scholar Citations', '—', '#8c96a0', '#4a5568')
    return output

def badge_row(data, survey_links):
    repo = 'https://github.com/FreedomIntelligence/Awesome-Code-World-Model'
    survey_badge = (
        ('https://img.shields.io/badge/Survey-PDF-b47b7b?style=flat-square&labelColor=4a5568',
         'Survey PDF', survey_links['arxiv_url'])
        if survey_links['arxiv_url'] else
        ('https://img.shields.io/badge/Survey%20PDF-coming%20soon-b47b7b?style=flat-square&labelColor=4a5568',
         'Survey PDF coming soon', '#motivation')
    )
    items = [
        (f"https://img.shields.io/badge/Papers-{len(data['papers'])}-6c8ba8?style=flat-square&labelColor=4a5568", 'Papers', '#paper-collection'),
        survey_badge,
        ('https://img.shields.io/github/stars/FreedomIntelligence/Awesome-Code-World-Model?style=flat-square&logo=github&labelColor=4a5568&color=7b9a8d', 'GitHub stars', f'{repo}/stargazers'),
        ('https://img.shields.io/badge/PRs-welcome-8c82a3?style=flat-square&labelColor=4a5568', 'PRs welcome', 'CONTRIBUTING.md'),
    ]
    if survey_links['semantic_scholar_url']:
        scholar_badge = (survey_links['semantic_scholar_citations_badge_url'] or
                         'https://img.shields.io/badge/Semantic%20Scholar-citations-6c8ba8?style=flat-square&logo=semanticscholar&logoColor=white&labelColor=4a5568')
        items.append((scholar_badge, 'Survey Semantic Scholar citations', survey_links['semantic_scholar_url']))
    return ' '.join(f'[![{alt}]({source})]({target})' for source, alt, target in items)

def bib_escape(value):
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#', '$': r'\$', '{': r'\{', '}': r'\}'}
    return ''.join(replacements.get(c, c) for c in value)

def bibliography(data):
    lines = ['% Generated from data/papers.json by scripts/build_catalog.py.',
             '% UTF-8. Years follow source dates or documented availability bounds for undated projects.',
             '% Primary-source citations; unverified conference assignments are omitted.', '']
    for p in sorted(data['papers'], key=lambda p: p['citation_key']):
        authors = ['{' + bib_escape(a) + '}' if a.lower().endswith(' team') else bib_escape(a) for a in p['authors']]
        fields = [('title', '{' + bib_escape(p['title']) + '}'),
                  ('author', ' and '.join(authors)), ('year', str(p['year']))]
        if 'arxiv_id' in p:
            fields += [('eprint', p['arxiv_id']), ('archivePrefix', 'arXiv')]
        if 'doi' in p:
            fields.append(('doi', p['doi']))
        fields.append(('url', p['source_url']))
        if p.get('source_type') == 'project':
            fields.append(('note', 'Project resource; verified available by ' + p['available_by'] + '; first release date unverified' if not p.get('first_public_date') else 'Project resource; date follows the cited author announcement'))
        lines.append('@misc{' + p['citation_key'] + ',')
        lines.extend(f'  {key} = {{{value}}},' for key, value in fields)
        lines += ['}', '']
    return '\n'.join(lines)

class HtmlLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.links.extend(attrs[k] for k in ('href', 'src') if attrs.get(k))
        if attrs.get('id'):
            self.ids.add(attrs['id'])

def markdown_targets(content):
    html = HtmlLinks()
    html.feed(content)
    anchors = set(html.ids)
    counts = {}
    in_code = False
    for line in content.splitlines():
        if line.startswith('```'):
            in_code = not in_code
        if in_code:
            continue
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if match:
            label = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', match[1])
            slug = re.sub(r'[^\w\s-]', '', label.lower()).replace(' ', '-')
            n = counts.get(slug, 0)
            counts[slug] = n + 1
            anchors.add(slug + (f'-{n}' if n else ''))
    links = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content) + html.links
    return links, anchors

def check_links():
    cache = {}
    for path in sorted(ROOT.rglob('*.md')):
        if '.git' in path.parts:
            continue
        content = path.read_text(encoding='utf-8')
        links, _ = markdown_targets(content)
        for target in links:
            parsed = urlparse(target)
            if parsed.scheme:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            require(destination.is_relative_to(ROOT), f'{path.name}: local link escapes repository: {target}')
            require(destination.exists(), f'{path.name}: missing local link: {target}')
            if parsed.fragment and destination.suffix == '.md':
                if destination not in cache:
                    cache[destination] = markdown_targets(destination.read_text(encoding='utf-8'))[1]
                require(unquote(parsed.fragment) in cache[destination], f'{path.name}: missing anchor: {target}')

def replace_region(text, name, content):
    start, end = f'<!-- {name}:BEGIN -->', f'<!-- {name}:END -->'
    require(text.count(start) == 1 and text.count(end) == 1, f'README requires one {name} marker pair')
    require(text.index(start) < text.index(end), f'README {name} markers are reversed')
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    gap = '\n\n'
    return before + start + gap + content + gap + end + after

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate without writing; reject stale generated output')
    args = parser.parse_args()
    data = load_data()
    localized = load_localization(data)
    survey_links = load_survey_links()
    expected = {ROOT / 'papers.bib': bibliography(data), ROOT / 'docs/catalogue.md': annotated_catalogue(data),
                **badges(data, survey_links), **classification_outputs(ROOT, data), **master_list_outputs(ROOT, data)}
    for filename, language in [('README.md', None), ('README.zh-CN.md', localized)]:
        readme_path = ROOT / filename
        readme = readme_path.read_text(encoding='utf-8')
        for name, content in [('BADGES', badge_row(data, survey_links)), ('NAVIGATION', navigation(data, language)),
                              ('CATALOG', catalogue(data, language)), ('RELATED', related_surveys(data, language))]:
            readme = replace_region(readme, name, content)
        expected[readme_path] = readme
    for path, text in expected.items():
        if args.check:
            require(path.exists() and path.read_text(encoding='utf-8') == text, f'{path.name} is stale; run python3 scripts/build_catalog.py')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')
    check_links()
    print(f"{'Validated' if args.check else 'Generated'} bilingual READMEs, {len(data['papers'])} sources/classification rows, {len(data['sections'])} sections, catalogue, coarse CSV, badges, links/anchors, and BibTeX.")

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'Catalogue validation failed: {error}', file=sys.stderr)
        sys.exit(1)
