<div align="center">

# Code World Models

<p>
  代码世界模型开放研究主页 —<br>
  精选文献、即将发布的综述、评测基准与后训练模型。<br>
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

<!-- BADGES:BEGIN -->

[![Papers](https://img.shields.io/badge/Papers-200-6c8ba8?style=flat-square&labelColor=4a5568)](#paper-collection) [![Survey PDF coming soon](https://img.shields.io/badge/Survey%20PDF-coming%20soon-b47b7b?style=flat-square&labelColor=4a5568)](#motivation) [![GitHub stars](https://img.shields.io/github/stars/FreedomIntelligence/Awesome-Code-World-Model?style=flat-square&logo=github&labelColor=4a5568&color=7b9a8d)](https://github.com/FreedomIntelligence/Awesome-Code-World-Model/stargazers) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-8c82a3?style=flat-square&labelColor=4a5568)](CONTRIBUTING.md)

<!-- BADGES:END -->

<p><img src="./assets/banner.png" alt="以程序构建可执行世界：代码、持久状态与渲染观测" width="960"></p>

</div>

<a id="motivation"></a>
## 概述

随着编码智能体在生成、执行和迭代改进复杂程序方面的能力不断增强，**代码**正成为世界建模的一种严谨而有前景的表示基底。除了预测像素，代码世界模型还提供**显式动力学、持久状态与可编程交互**，为构建可控、可编辑、可验证的世界提供了一条互补路径。

<a id="upcoming-releases"></a>
作为我们持续研究工作的一部分，我们将陆续开源一系列围绕代码世界模型的研究成果，包括系统**综述（Survey）**、面向可执行动力学与可渲染世界的**评测基准（Benchmarks）**，以及**后训练方法与开源模型（Post-Training & Models）**。

> **欢迎贡献与合作：** 非常欢迎提交 PR、推荐论文以及开展研究合作。欢迎联系 [@YihDu](https://github.com/YihDu) 和 [@MichaelCao0](https://github.com/MichaelCao0)，或在 [GitHub](https://github.com/FreedomIntelligence/Awesome-Code-World-Model/issues) 提交 Issue 参与讨论。

<a id="contents"></a>
<a id="taxonomy"></a>
## 分类与导航

<!-- NAVIGATION:BEGIN -->

| 分类主线 | 代码承担内容 | 核心问题 | 文献数 |
|---|---|---|---:|
| **[01 · WorldCoder-type](#papers-worldcoder)** | 纯状态与动力学 | 代码能否预测动作后果并支持规划？ | **50** |
| **[02 · Code-as-World-type](#papers-code_as_world)** | 白模世界 + 生成式渲染 | 代码维护的白模状态与规则能否驱动生成式渲染？ | **30** |
| **[03 · VibeWorlding-type](#papers-vibeworlding)** | 完整 3D 世界 | agent 能否用代码构建并编辑完整 3D 世界？ | **45** |
| **[其他](#papers-other)** | GUI 世界、评测与综述 | [GUI 世界模型](#papers-other-gui) (25) · [评测基准](#papers-other-benchmark) (37) · [相关综述](#related-surveys) (13) | **75** |

<!-- NAVIGATION:END -->

<a id="paper-collection"></a>
## 文献目录

<!-- CATALOG:BEGIN -->

**200 条文献来源** · 截止 **2026-11-26** · 按发布日期倒序排列。完整信息见[详细核查表](docs/catalogue.md)与[全量论文总表](docs/paper-master-list.md)。

<a id="papers-worldcoder"></a>
### 01 · WorldCoder-type · 程序化动力学 (50)

*纯状态层面的可执行动力学：转移机制、世界程序归纳、规划与模型修复，不生成外观。*

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **CodeWAM: A Code World Action Model for End-to-End Autonomous Driving** | CodeWAM 用可执行代码推演候选规划下的自车运动状态，并与学习式视觉场景模型联合评估端到端驾驶未来后果。 | [PDF](https://arxiv.org/abs/2611.32483) |
| `2026` | **Creating Hybrid Interactive Narrative Systems with LLM: From Formal Description to Evaluation** | 叙事事件写成带前置条件与效果的操作。三种叙事管理器在同一组事实和目标上行动，生成的故事轨迹可以按规划序列比较。 | [PDF](https://arxiv.org/abs/2611.02807) |
| `2026` | **Algebraic World Model: From Exploration to Proofs** | 通过可执行 Python 假设、类型化规则和 Lean 证明探索未知游戏中的可达性与不可达性。 | [PDF](https://arxiv.org/abs/2610.40503) |
| `2026` | **PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds** | 由 VLM 提出可执行物理世界，确定性物理引擎验证反事实分支并生成可验证的训练任务。 | [PDF](https://arxiv.org/abs/2610.34921) |
| `2026` | **Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players (AutoTavern)** | 自我改进的研究 agent 构建并验证 Hearthstone Battlegrounds 模拟器，再训练对手和游戏 agent；作为相邻可执行环境工作保留。 | [PDF](https://arxiv.org/abs/2610.33845) |
| `2026` | **LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica** | 研究编码智能体根据描述与数据组合、校准可执行 Modelica 物理系统模型，并以行为拟合、物理不变量与可解释性进行验收。 | [PDF](https://arxiv.org/abs/2610.25019) |
| `2026` | **Neurosymbolic Learning of Interpretable World Models (CGWM)** | 学习视觉概念落地，而无可学习参数的预测器执行给定时序逻辑转移规则；通过符号想象轨迹进行可微规划。 | [PDF](https://arxiv.org/abs/2610.19955) |
| `2026` | **A Declared World Model: Language Models Write the Rules of the Scene They are Shown** | 语言模型根据带标签场景图编写世界规则，由确定性引擎检查动作并计算下一状态；实验检验规则能否迁移到未见布局。 | [PDF](https://www.preprints.org/manuscript/202610.1139) |
| `2026` | **Write Once, Plan Many: Building Reusable Visual Planning Systems from One Scene** | 由给定领域规则和单个练习场景生成可复用渲染、动力学、感知与规划程序，以执行和重建反馈改进，随后冻结复用。 | [PDF](https://arxiv.org/abs/2610.19234) |
| `2026` | **RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions** | 提取可复用角色原型与可执行转移规则，在新环境中更新角色分配和参数估计，保持已获得的转移规则不变。 | [PDF](https://arxiv.org/abs/2610.13172) |
| `2026` | **Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** | Memento 3 结合轨迹判断与精确回放，修订反思式规则手册和可执行模型。 | [PDF](https://arxiv.org/abs/2610.11794) |
| `2026` | **LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** | LLM-IDEA 通过考虑可辨识性的实验设计，区分不同机制解释。 | [PDF](https://arxiv.org/abs/2610.11253) |
| `2026` | **Kepler: Auditable World Models for ARC-AGI-3** | Kepler 通过回溯与条件转移检查以及成本统计，研究可审计的 ARC-AGI-3 世界模型。 | [PDF](https://arxiv.org/abs/2610.00834) |
| `2026` | **Schema: Discovering Unknown Environments via Agentic Program Induction** | agent 在持久的程序工作区中以可执行程序表达对未知环境的理解，对照交互历史检验程序，并在逐步验证下基于程序规划（ARC-AGI-3 等游戏）。 | [PDF](https://arxiv.org/abs/2609.39140) |
| `2026` | **EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning** | EMPIRIC 学习残差代码，为物理引擎补充缺失的力、约束与隐藏状态。 | [PDF](https://arxiv.org/abs/2609.35047) |
| `2026` | **Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning** | Code as Worlds 通过提出、实例化、执行、渲染和验证的循环，发现可执行物理表示。 | [PDF](https://arxiv.org/abs/2608.27549) |
| `2026` | **PDDLCoder: Agentic PDDL Generation for LLM-Assisted Symbolic Planning** | agent 循环从自然语言生成、分析并修正 PDDL 域与问题，并提供可自动验证计划可执行性的 gym 环境基准。 | [PDF](https://arxiv.org/abs/2608.16637) |
| `2026` | **Twin: Playing an Unknown Game with a Test-Time Digital Twin** | Twin 在测试时构建数字孪生，并在未知游戏中选择动作前检查历史转移。 | [PDF](https://arxiv.org/abs/2608.14490) |
| `2026` | **Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3** | Tycho 在求解 ARC-AGI-3 游戏时，主动修订抽象与程序化假设。 | [PDF](https://arxiv.org/abs/2607.28287) |
| `2026` | **VisualPatchWorld: Code World Models as Latent Structured Representations for Planning** | VisualPatchWorld 从结构化状态—动作轨迹拟合动力学，并利用视觉场景图重新规划。 | [PDF](https://arxiv.org/abs/2607.25236) |
| `2026` | **Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation** | 将 LLM 生成的仿真器族与神经仿真推断结合，用于机制选择和参数估计。 | [PDF](https://arxiv.org/abs/2607.17540) |
| `2026` | **Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?** | 在 ARC-AGI-3 编码 agent 中，检验维护可执行模型、简化和回放验证的作用。 | [PDF](https://arxiv.org/abs/2607.15439) |
| `2026` | **When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models** | 说明 LLM 合成的代码世界模型即使通过转移准确率检验，仍可能因少数关键动力学出错而在博弈中失败；主张以对规划是否够用、而非预测准确率作为验收标准。 | [PDF](https://arxiv.org/abs/2607.14169) |
| `2026` | **World-Time Compute with Verified Code World Models** | World-Time Compute 利用经验证的符号代码世界，生成具有精确标签的训练轨迹。 | [PDF](https://arxiv.org/abs/2609.09163) |
| `2026` | **OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3** | OPINE-World 通过错误优先探索，联合修订符号本体、转移假设与目标。 | [PDF](https://arxiv.org/abs/2607.01531) |
| `2026` | **Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** | Mind-Studio 为部分可观测游戏构建可执行模型，并评价同状态起点的多步前瞻保真度。 | [PDF](https://arxiv.org/abs/2606.16070) |
| `2026` | **PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty** | PO-PDDL 从机器人演示视频中重建潜在符号状态轨迹，学习随机转移与观测规则以支持不确定性下的信念空间规划。 | [PDF](https://arxiv.org/abs/2606.15654) |
| `2026` | **PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments** | PatchWorld 通过反例引导的补丁优化可执行信念状态模型，并用于动作前瞻。 | [PDF](https://arxiv.org/abs/2605.30880) |
| `2026` | **Distilling Game Code World Model Generation into Lightweight Large Language Models (GameCWM distillation)** | 通过后训练，将前沿 LLM 生成游戏代码世界模型（规则、合法动作、转移、观测与奖励）的能力蒸馏到小模型中。 | [PDF](https://arxiv.org/abs/2605.24375) |
| `2026` | **Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models (Alice / Baba in Wonderland)** | Alice 在词汇先验错配下学习可执行动力学，以旧行为保持冲突指导假设修订与探索。 | [PDF](https://arxiv.org/abs/2605.16725) |
| `2026` | **Learning POMDP World Models from Observations with Language-Model Priors (Pinductor)** | LLM 根据少量观测—动作轨迹提出候选 POMDP 世界模型，并以基于信念的似然迭代修正，无需访问隐藏状态。 | [PDF](https://arxiv.org/abs/2605.13740) |
| `2026` | **Executable World Models for ARC-AGI-3 in the Era of Coding Agents** | 通过历史回放、简化与规划，构建 ARC-AGI-3 的可执行世界模型。 | [PDF](https://arxiv.org/abs/2605.05138) |
| `2026` | **Neuro-Symbolic Synergy for World Modeling (NeSyS)** | 在对方解释不好的转移上交替训练 LLM 世界模型与可执行符号规则，并通过对数线性重排序将两者结合。 | [PDF](https://arxiv.org/abs/2602.10480) |
| `2026` | **Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents (TheoryCoder-2)** | TheoryCoder-2 在程序合成 agent 中学习和复用规划抽象。 | [PDF](https://arxiv.org/abs/2602.00929) |
| `2026` | **CASSANDRA: Programmatic and Probabilistic Learning and Inference for Stochastic World Modeling** | 面向商业类规划领域，用 LLM 编写的代码建模确定性部分，并以 LLM 引导概率图模型的结构学习来刻画随机变量，组合成转移模型。 | [PDF](https://arxiv.org/abs/2601.18620) |
| `2025` | **Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback** | Agent2World 通过研究、开发和自适应测试 agent，生成符号世界模型与训练轨迹。 | [PDF](https://arxiv.org/abs/2512.22336) |
| `2025` | **One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration (OneLife)** | OneLife 从 Crafter-OO 中的无引导探索学习按条件激活的概率法则。 | [PDF](https://arxiv.org/abs/2510.12088) |
| `2025` | **Code World Models for General Game Playing** | 为棋盘和纸牌游戏合成 Python 转移、合法动作、终止检查、价值启发式及隐藏状态推断函数。 | [PDF](https://arxiv.org/abs/2510.04542) |
| `2025` | **Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video (FAE)** | FAE 利用受约束的响应式 DSL，从游戏视频的精灵网格表示中提取行为程序。 | [PDF](https://arxiv.org/abs/2508.11836) |
| `2025` | **PoE-World: Compositional World Modeling with Products of Programmatic Experts** | PoE-World 将多个程序化专家组合为随机世界模型，支持预测与规划。 | [PDF](https://arxiv.org/abs/2505.10819) |
| `2025` | **LLM-Guided Probabilistic Program Induction for POMDP Model Estimation** | 以 LLM 作为先验生成 POMDP 各组成部分（转移、观测、奖励、初始状态）的短概率程序，并依据经验分布修正，实验包括机器人搜索任务。 | [PDF](https://arxiv.org/abs/2505.02216) |
| `2025` | **WALL-E 2.0: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents** | 从探索轨迹中提取动作规则、知识图与场景图，编码为可执行代码以校准 LLM 世界模型，并用模型预测控制进行规划。 | [PDF](https://arxiv.org/abs/2504.15785) |
| `2025` | **Synthesizing world models for bilevel planning (TheoryCoder)** | TheoryCoder 将合成的低层 Python 动力学与给定的高层 PDDL 抽象结合，进行双层规划。 | [PDF](https://arxiv.org/abs/2503.20124) |
| `2025` | **Generating Symbolic World Models via Test-time Scaling of Large Language Models** | 通过 Best-of-N 搜索与细粒度语言化反馈，生成和修正 PDDL 世界模型。 | [PDF](https://arxiv.org/abs/2502.04728) |
| `2024` | **Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search (GIF-MCTS)** | GIF-MCTS 根据描述、离线转移数据和执行反馈，搜索可执行的 Python 世界模型。 | [PDF](https://arxiv.org/abs/2405.15383) |
| `2024` | **WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** | WorldCoder 从交互中合成 Python 转移与奖励模型，将模型一致性与乐观规划结合。 | [PDF](https://arxiv.org/abs/2402.12275) |
| `2023` | **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** | 利用 LLM 构建和修正 PDDL 域模型，再通过可靠的外部规划器进行任务规划。 | [PDF](https://arxiv.org/abs/2305.14909) |
| `2023` | **Combining Functional and Automata Synthesis to Discover Causal Reactive Programs (AutumnSynth)** | AutumnSynth 交替合成转移函数与自动机，恢复包含潜在状态的响应式程序。 | [PDF](https://doi.org/10.1145/3571249) |
| `2021` | **Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning (EMPA)** | EMPA 学习概率游戏引擎程序，并通过内部仿真支持探索与规划。 | [PDF](https://arxiv.org/abs/2107.12544) |
| `2017` | **Game Engine Learning from Video** | 从视频中学习可执行的游戏引擎规则，以未来状态预测和 agent 训练进行评价。 | [PDF](https://www.ijcai.org/proceedings/2017/518) |

[↑ 返回总览](#contents)

<a id="papers-code_as_world"></a>
### 02 · Code-as-World-type · 白模世界 + 生成式渲染 (30)

*代码维护白模/proxy 世界的持久状态与规则，由生成式渲染器补全外观。*

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds** | ContextRenderer 面向游戏引擎多样化动态代理提出动态上下文学习与循环历史压缩，在长程交互中保持条件跟随与视觉连续性。 | [PDF](https://arxiv.org/abs/2611.25838) |
| `2026` | **WorldRuler: Interactive World Modeling under Configurable Rules** | WorldRuler 用可执行三维规则图组织用户自定义规则、依赖与跨存取档物体状态，并与视频生成及感知反馈构成闭环。 | [PDF](https://arxiv.org/abs/2611.24869) |
| `2026` | **Code World Model 2.0: Towards Infinite Controllable Video Generation (Invoker-Render)** | Invoker-Render（Code World Model 2.0）通过 ProForcing 在多粒度结构代理、外观参考与文本条件下统一双向创作与四步因果流式渲染，由上游引擎锁定状态与运动。 | [PDF](https://arxiv.org/abs/2611.22925) |
| `2026` | **GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models** | 游戏引擎决定事件何时发生、结果如何以及相机状态，视频模型绘制交互细节。同一套游戏机制可以呈现出多种视觉效果。 | [PDF](https://arxiv.org/abs/2611.19247) |
| `2026` | **Streaming Code World Model (Streaming CWM)** | 在 Code World Model 与 CARLA 导出的深度和语义代理上实现四步因果分块流式视频渲染。 | [Project](https://github.com/TingtingLiao/streaming-code-world-model) |
| `2026` | **CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models** | 从共享的可编程 3D 代理和 RGB 参考图联合渲染双人视角，以同步的 GTA V 观测检验同一角色跨视角的外观一致性。 | [PDF](https://arxiv.org/abs/2611.15602) |
| `2026` | **Fight World Model: Customizable Combat through Visual Interaction Proxies** | 将可执行的战斗状态和规则解析与视频渲染分开，用绑定身份和时间的交互代理保持攻击、受击与生命状态一致。 | [PDF](https://arxiv.org/abs/2610.40607) |
| `2026` | **Wizard: Manipulate Any World in Real Time via Agentic Control** | 用骨架和几何代理结合显式游戏状态，支持实时、可泛化的视频世界控制；摘要未证明代码是世界表示。 | [PDF](https://arxiv.org/abs/2610.40339) |
| `2026` | **EdenLive: Real-Time Generative Rendering from Any Visual Reference** | 生成式渲染器把上游参考视频、目标首帧和提示转换为增强视频；状态和规则由上游程序维护。官方还提供从提示生成可玩游戏的 skill 与工作台。 | [Project](https://github.com/VAST-AI-Research/EdenLive) |
| `2026` | **BoxWorld: Let World Engines Control and Video Generators Render** | 编码智能体把用户规则写成 Box World Engine，由持久属性和状态变量驱动神经视频渲染，并提出成对状态控制评测。 | [PDF](https://arxiv.org/abs/2610.36371) |
| `2026` | **Mundo: Customized World Model** | 从图像重建可编辑的三维代理场景；场景程序指定对象和物理参数，脚本及通常采用的 MuJoCo 推进状态，代理帧与参考视图共同控制视频渲染。 | [Project](https://mundo-world-model.github.io/) |
| `2026` | **AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark** | 把编码智能体生成的游戏 blockout 渲染成保持实体、布局和时序一致的高质量视频；属于 renderer 相邻工作。 | [PDF](https://arxiv.org/abs/2610.31466) |
| `2026` | **SolarRenderer: Few-Step Generative Reference Rendering** | 通过控制与加速 LoRA 适配冻结视频骨干，将对齐的结构视频转成细节视频，并支持流式生成。 | [PDF](https://arxiv.org/abs/2610.28630) |
| `2026` | **Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds** | 编码智能体把玩家要求写成游戏代码与规则；引擎维护持久状态，因果视频模型根据低模画面生成细节视图。 | [PDF](https://arxiv.org/abs/2610.27999) |
| `2026` | **State World Models: Execute the Rules, Generate the Pixels** | 编码智能体生成有类型的游戏定义；运行时先执行语义与空间状态规则，再调用冻结视频渲染器，之后接收与规则兼容的视觉反馈。 | [PDF](https://arxiv.org/abs/2610.26811) |
| `2026` | **Mallea: Building, Steering, and Memorizing Worlds with Coding Agent** | 编码智能体联合构建对象结构与规则，支持保留未受影响状态的运行时编辑，并结合执行状态与对象纹理记忆进行渲染。 | [PDF](https://arxiv.org/abs/2610.21283) |
| `2026` | **Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation (ATAS)** | 将剧本编译为带空间和事件时间引用的镜头请求，检索配准场景与事件记忆，并在检查通过后将生成观测写入记忆。 | [PDF](https://arxiv.org/abs/2610.20571) |
| `2026` | **Generative World Simulation with DAO and JING (DAO + JING)** | DAO 在交互规则和世界时间下维护共享角色、物体与空间状态，JING 为不同观察者生成视听体验。 | [PDF](https://arxiv.org/abs/2610.19726) |
| `2026` | **From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction (DR-WM)** | 结合 RGB 场景重建、真实动作响应校准的地形接触先验与物理仿真，以模拟运动和几何指导视频世界模型。 | [PDF](https://arxiv.org/abs/2610.17630) |
| `2026` | **StreamRender-H3: Interactive Coding Worlds with Real-time Streaming Diffusion Render** | three.js 游戏引擎维护地图、规则和状态，并根据玩家输入推进；语义帧连接引擎和流式 MiniMax-H3 渲染器，构成执行式模拟与生成外观分离的系统。 | [Project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/) |
| `2026` | **AgentGarten: Code Worlds for Evolving Agents** | AgentGarten 将程序定义的仿真后端连接到共享实时渲染器，并复用 agent 的文字技能手册。 | [PDF](https://arxiv.org/abs/2610.12374) |
| `2026` | **Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models** | 编码智能体与轻量引擎维护可扩展世界状态表，生成粗粒度视觉条件，并纳入新出现的对象以支持持续交互。 | [PDF](https://arxiv.org/abs/2610.01614) |
| `2026` | **WorldWeave: Growing Persistent Geometric Worlds for Video Generation** | WorldWeave 通过智能体引导的场景组织与确定性几何编译维护可扩展持久三维结构，并以只读深度查询驱动跨重访一致的视频生成。 | [PDF](https://arxiv.org/abs/2609.34221) |
| `2026` | **Code Plans, Diffusion Renders: Open-Ended Generative World Modeling (CoDeR)** | CoDeR 协调可执行白盒世界的构建与生成式 Artist，创建开放式视觉世界。 | [PDF](https://arxiv.org/abs/2609.26458) |
| `2026` | **GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models** | GameDirector 利用视觉情境估计和显式玩法规则，控制游戏视频生成。 | [PDF](https://arxiv.org/abs/2609.25652) |
| `2026` | **Programmable World Model** | Programmable World Model 将包含非视觉事实的持久引擎状态，编译为视频生成控制信号。 | [PDF](https://arxiv.org/abs/2609.10540) |
| `2026` | **Magpie: Real-Time World Renderer for Interactive Games** | Magpie 将持久的游戏引擎状态与规则，连接到由白盒观测驱动的交互式神经渲染器。 | [PDF](https://arxiv.org/abs/2608.27168) |
| `2026` | **Code World Model: Coding Agent as World Brain** | Code World Model 通过可执行代理表示，连接编码世界大脑与视觉世界引擎。 | [PDF](https://arxiv.org/abs/2608.25927) |
| `2026` | **Generative World Renderer at the Speed of Play (AlayaRenderer-Flash)** | AlayaRenderer-Flash 将接收物理引擎结构化状态与 G-buffer 的生成式世界渲染器蒸馏为逾 30 FPS 的少步因果流式模型，支持实时可玩交互。 | [PDF](https://arxiv.org/abs/2607.18703) |
| `2025` | **Web World Models** | Web World Models 以类型化 Web 状态和代码定义的规则，支撑持久的生成式世界。 | [PDF](https://arxiv.org/abs/2512.23676) |

[↑ 返回总览](#contents)

<a id="papers-vibeworlding"></a>
### 03 · VibeWorlding-type · agentic 3D 世界构建 (45)

*代码写出完整 3D 世界（几何、材质、布局，可含物理），由常规渲染器或仿真器执行；包含静态场景。*

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **TelePhysica: Agentic Reconstruction of Physically Interactive Scenes** | 从单张照片重建可视网格与可执行物理模型，检验重力平衡后可反转外力并重新仿真。仿真轨迹还可用于引导视频生成。 | [PDF](https://arxiv.org/abs/2611.18078) |
| `2026` | **SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation (SceneAgent (portable game scenes))** | 用持久化的 SceneContext 保存构建中的游戏场景。构建 agent 可跨引擎复用布局技能，由适配器转换坐标、绑定资产并导出场景。 | [PDF](https://arxiv.org/abs/2611.17821) |
| `2026` | **BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs** | BlenderFORGE 基于隔离的确定性 Blender 沙箱导出结构化状态并计算多轮强化学习奖励，训练开源多模态模型编写 bpy 代码精确编辑三维场景。 | [PDF](https://arxiv.org/abs/2611.10768) |
| `2026` | **Gym-Anything for Robotics: Scaling physical simulations with digital agents** | 把仿真创建视为编码智能体任务，构建并审计 RoboWorld 物理仿真环境；作为 3D/模拟器构建支撑工作收录。 | [PDF](https://arxiv.org/abs/2610.40565) |
| `2026` | **Cinematize from Unreal: Agentic Choreography for Controllable World Simulation (CineU)** | 把 Unreal 工程作为可检查的持久世界，利用智能体生成代码执行并验证操作，通过几何约束、时间线和局部修复完成世界编排。 | [PDF](https://arxiv.org/abs/2610.38468) |
| `2026` | **Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction (SceneEvolve)** | 用可执行代码表示组合式 3D 场景，并在固定模型和执行后端的条件下演化重建 harness。 | [PDF](https://arxiv.org/abs/2610.37046) |
| `2026` | **SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments** | 通过重建、物理建模、仿真检查和修复，把 3D/4D 采集转换为可交互仿真环境；作为相邻 real-to-sim 工作保留。 | [PDF](https://arxiv.org/abs/2610.34745) |
| `2026` | **SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning** | 用视觉布局采样、契约引导的 3D 编译和物理稳定性检查生成具身学习环境；作为相邻场景构建工作保留。 | [PDF](https://arxiv.org/abs/2610.32978) |
| `2026` | **WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations** | 从真实机器人演示构建交互式数字孪生，通过编码智能体迭代修复可执行世界程序并验证物理一致性。 | [PDF](https://arxiv.org/abs/2610.31834) |
| `2026` | **WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State** | 分层规划预测区域与地块的类型化规格，固定过程生成器将其编译成场景；持久记录保留对象身份、边界约束和编辑，以支持流式加载与重访。 | [PDF](https://arxiv.org/abs/2610.28827) |
| `2026` | **SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images** | 从单张图像重建物体与布局，通过场景代码编辑、受限位姿搜索和仿真验证，保留物理稳定且与图像对齐的场景配置。 | [PDF](https://arxiv.org/abs/2610.28585) |
| `2026` | **NeoWorld-3: From Pixels to Code-Defined Physical Worlds** | 通过分层编码智能体、可微参数拟合以及关节与物理检查，从视觉证据重建可编辑几何程序。 | [PDF](https://arxiv.org/abs/2610.27690) |
| `2026` | **InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation** | 用 VLM 驱动符号约束的程序化生成和确定性布局，构建可编辑、可动画化的开放式 3D 世界。 | [PDF](https://arxiv.org/abs/2610.26853) |
| `2026` | **Self-Building Labs** | 智能体从科学目标、照片和设备信息构建实验室数字孪生、机器人技能与工作流，并通过观测和物理反馈改进场景模型。 | [PDF](https://arxiv.org/abs/2610.23826) |
| `2026` | **3DCodeVerse: Exploring 3D Worlds as Code** | 将可执行 3D 程序、资产与验证记录组成数据资源，并通过执行检查、几何测量及视觉反馈迭代生成和修正程序。 | [PDF](https://arxiv.org/abs/2610.22341) |
| `2026` | **RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks** | 基于 Newton 的交互式工具包，将求解器、接触模型与物理参数显式开放给人类和编码智能体，依据观测行为迭代调整操作仿真。 | [PDF](https://arxiv.org/abs/2610.18835) |
| `2026` | **CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations** | 从每个区域一张航拍图构建可供 agent 操作的参数化 3D 城市，以带实体身份、版本化校验更新的代码状态持久保存。 | [PDF](https://arxiv.org/abs/2610.18342) |
| `2026` | **Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation** | 将生成的视觉场景编译为具有物理属性的 MuJoCo 世界，通过仿真器反馈修正可执行动力学与场景设置。 | [PDF](https://arxiv.org/abs/2610.17651) |
| `2026` | **USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation** | USDCraft 将输入几何转为可执行建模程序，导出具有关节结构的 USD 仿真资产。 | [PDF](https://arxiv.org/abs/2610.11322) |
| `2026` | **Code2Games: Enabling Coding Agents for Gaming World Generation** | 根据游戏意图，在生成的 Blender 世界上规划玩法，迁移到 Unreal Engine 5，并依据编译与运行时反馈修复，得到可玩的游戏世界。 | [PDF](https://arxiv.org/abs/2610.05033) |
| `2026` | **LEGO-Anything: Coding Agents for 3D Scene Reconstruction** | LEGO-Anything 将三维场景重建为可执行程序，并分别评价产物有效性、几何和外观。 | [PDF](https://arxiv.org/abs/2609.36380) |
| `2026` | **Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** | Recursive Code World Models 通过递归程序、全局—局部修订和共享参考视图重建复杂场景。 | [PDF](https://arxiv.org/abs/2609.11499) |
| `2026` | **FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation** | FuncRoom-Agent 通过递归 DSL、顺序专家模型和执行依据的过程奖励，生成功能性室内场景。 | [PDF](https://arxiv.org/abs/2608.29519) |
| `2026` | **aDSL: Agentic 3D Creation via Joint Agent-Program Design** | aDSL 协同设计关系型三维领域特定语言与规划—执行—审阅多智能体闭环，利用执行反馈修复几何与空间约束违规。 | [PDF](https://arxiv.org/abs/2608.17975) |
| `2026` | **VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?** | VibeWorlding 研究多模态 coding agent 如何在 Blender 沙盒中通过资产检索、程序化编辑、渲染反馈与物理可行性检查端到端构建和修改开放式 3D 世界。它的核心任务是世界构建与编辑，不应直接计作时间动力学发现。 | [PDF](https://arxiv.org/abs/2608.15265) |
| `2026` | **WorldClaw: Agentic 3D Open-World Generation at Scale** | WorldClaw 通过区域规划、地形生成和渲染反馈，构建大规模可编辑三维场景。 | [PDF](https://arxiv.org/abs/2608.05248) |
| `2026` | **SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation** | 由规划、编码、审查多智能体编写 Blender 程序，生成含流体、粒子、刚体和关节机构的动态 4D 场景，并依据渲染视频检查运动。 | [PDF](https://arxiv.org/abs/2607.01766) |
| `2026` | **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** | SceneCode 构建可编辑的室内世界程序，包含关节物体、仿真导出与持久场景组织。 | [PDF](https://arxiv.org/abs/2605.19587) |
| `2026` | **Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code Synthesis** | Code-as-Room 解析俯视房间图像并通过带跨阶段记忆的结构化执行框架多阶段合成三维室内几何、材质与光照 Blender 代码。 | [PDF](https://arxiv.org/abs/2605.18451) |
| `2026` | **SR-Platform: An Agentic Pipeline for Natural Language-Driven Robot Simulation Environment Synthesis** | 经场景规划、CadQuery 资产合成、受约束布局和 MJCF 组装，将自然语言描述转为可执行的 MuJoCo 环境。 | [PDF](https://arxiv.org/abs/2605.14700) |
| `2026` | **ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** | ChronoAgentic 结合规划、编码、视觉审阅与轨迹检查，构建 PyChrono 仿真程序。 | [PDF](https://arxiv.org/abs/2605.14398) |
| `2026` | **SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning** | 自我演化的 coding agent 编写并运行 Unreal Engine 代码，根据语言或图像指令构建带可验证任务的物理具身环境。 | [PDF](https://arxiv.org/abs/2605.09423) |
| `2026` | **Code2Worlds: Empowering Coding LLMs for 4D World Generation** | Code2Worlds 生成用于四维仿真的物体与场景程序，并结合 Blender 动力学与视觉运动反馈。 | [PDF](https://arxiv.org/abs/2602.11757) |
| `2026` | **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** | agent 将布局与物体生成器和语义、真实感、物理稳定性评估器结合，大规模生成面向具身任务的可仿真场景。 | [PDF](https://arxiv.org/abs/2602.10116) |
| `2026` | **Imagine a City: CityGenAgent for Procedural 3D City Generation** | 从语言出发，以街区程序和建筑程序分层生成 3D 城市，并用监督微调与强化学习保证程序有效且语义一致。 | [PDF](https://arxiv.org/abs/2602.05362) |
| `2025` | **Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search** | 研究程序化场景表示，以及通过程序搜索进行错误修正的方法。 | [PDF](https://arxiv.org/abs/2510.16147) |
| `2025` | **Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation** | 研究命令式与声明式场景程序的表示差异，以及基于程序的错误修正。 | [PDF](https://arxiv.org/abs/2504.05482) |
| `2024` | **SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements** | SceneMotifCoder 从少量视觉示例中学习可编辑的物体排列程序。 | [PDF](https://arxiv.org/abs/2408.02211) |
| `2024` | **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code** | SceneCraft 将场景蓝图转为 Blender 代码，并利用渲染反馈迭代修正。 | [PDF](https://arxiv.org/abs/2403.01248) |
| `2024` | **Open-Universe Indoor Scene Generation using LLM Program Synthesis and Uncurated Object Databases** | 基于未精选的物体数据库，合成可执行的室内场景布局约束。 | [PDF](https://arxiv.org/abs/2403.09675) |
| `2023` | **Holodeck: Language Guided Generation of 3D Embodied AI Environments** | Holodeck 通过空间约束与优化构建语言驱动的三维具身环境。 | [PDF](https://arxiv.org/abs/2312.09067) |
| `2023` | **Infinite Photorealistic Worlds Using Procedural Generation (Infinigen)** | Infinigen 通过程序化规则生成世界尺度的逼真几何与材质。 | [PDF](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html) |
| `2020` | **ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis** | ShapeAssembly 以层次化参数装配程序表示三维部件结构。 | [PDF](https://arxiv.org/abs/2009.08026) |
| `2018` | **CSGNet: Neural Shape Parser for Constructive Solid Geometry** | CSGNet 将视觉形状解析为可执行的构造实体几何程序。 | [PDF](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html) |
| `2013` | **Procedural content generation for games** | 游戏程序化内容生成的历史参考文献；本轮核查书目信息。 | [PDF](https://doi.org/10.1145/2422956.2422957) |

[↑ 返回总览](#contents)

<a id="papers-other"></a>
### 其他

*不属于三类主线的记录，分为 GUI 世界模型与评测基准两组。*

<a id="papers-other-gui"></a>
#### GUI 世界模型 (25)

*GUI、网页与 computer-use 世界模型，包括以可渲染代码预测下一屏的工作；不纳入三类主线。*

<details>
<summary>25 条记录</summary>

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **Interactive Neural Computers** | 将桌面环境建模为带惊奇门控槽位记忆与残差潜渲染的端到端交互式世界模型，从键鼠动作预测下一屏并保持屏外文件内容。 | [PDF](https://arxiv.org/abs/2611.32811) |
| `2026` | **MKD2World: A Typed Spatial MarkDown World Model For Web Agents** | MKD2World 将桌面网页序列化为编码元素类型、坐标框与控件状态的 Typed Spatial Markdown，用于动作条件下一状态预测以辅助网页智能体决策。 | [PDF](https://arxiv.org/abs/2611.06544) |
| `2026` | **WebHarbor: Docking Real Websites for Evolving GUI Agent Environments** | 编码 agent 根据新任务扩展容器化的网站副本，由人工核对界面与业务流程。共提供 153 个可执行网站环境。 | [PDF](https://arxiv.org/abs/2611.03634) |
| `2026` | **Agent World Model in the Wild: Computer-Use Agent Environment Synthesis (WildAWM)** | 合成贯通 GUI、MCP 和 CLI 的可执行计算机环境，以可重放状态构建程序和基于执行的任务、验证器质量门控支持智能体训练。 | [PDF](https://arxiv.org/abs/2610.26828) |
| `2026` | **Beyond Next-Screen Prediction: The Decision Value of GUI World Models** | 控制预测呈现方式和监督条件，对比 GUI 前瞻预测与直接动作排序器，检验预测画面对决策的增量价值。 | [PDF](https://arxiv.org/abs/2610.24372) |
| `2026` | **Latent World Action Model for GUI Agents** | 将 GUI 世界模型的预测目标从全屏像素重建转向动作感知对比学习的潜空间转移预测，并与动作选择头共享多模态表征。 | [PDF](https://arxiv.org/abs/2610.14228) |
| `2026` | **Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents** | 研究以 GUI 世界模型验证状态转移，并区分界面相似度与转移正确性。 | [PDF](https://arxiv.org/abs/2610.11942) |
| `2026` | **AutoGUIWorld: Image Generators as Visual World Models for GUI Agent** | AutoGUIWorld 通过规划视觉后果并迭代编辑截图，合成 GUI 交互轨迹。 | [PDF](https://arxiv.org/abs/2610.01215) |
| `2026` | **The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models (StateAliasBench)** | StateAliasBench 配对可见 GUI 条件相同、未来却不同的案例，诊断隐藏转移状态。 | [PDF](https://arxiv.org/abs/2609.32679) |
| `2026` | **WebWorld: The Browser as a World Model for Self-Improving Web Code** | 通过浏览器执行与验证自改进 Web 代码，检查交互合同及已有行为的保持。 | [PDF](https://arxiv.org/abs/2608.30530) |
| `2026` | **GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments** | GUI-CC 结合离线参考动作与在线 agent 闭环，评价多步上下文一致性。 | [PDF](https://arxiv.org/abs/2609.00048) |
| `2026` | **AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** | AppDeltaWorld 结合检索结构、视觉资产与闭环修订，预测由动作转移约束的 HTML 更新。 | [PDF](https://arxiv.org/abs/2608.05891) |
| `2026` | **SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction** | 利用预测语义下一状态的安全增强 GUI 世界模型，在移动 agent 执行前筛查指令并评估动作风险。 | [PDF](https://arxiv.org/abs/2607.15550) |
| `2026` | **OpenComputer: Verifiable Software Worlds for Computer-Use Agents** | OpenComputer 提供真实软件环境、结构化状态验证与可审计的任务奖励。 | [PDF](https://arxiv.org/abs/2605.19769) |
| `2026` | **How Mobile World Model Guides GUI Agents?** | 比较文本、图像和可渲染代码表示，分析重建、在线使用及 agent 消费预测的不同方式。 | [PDF](https://arxiv.org/abs/2605.10347) |
| `2026` | **Computer-Using World Model** | Computer-Using World Model 先预测文本变化，再生成桌面软件交互后的截图。 | [PDF](https://arxiv.org/abs/2602.17365) |
| `2026` | **World-Model-Augmented Web Agents with Action Correction (WAC)** | WAC 让网页智能体在执行前调用状态转移世界模型模拟动作后果，并由裁判模型审查风险以触发动作纠偏。 | [PDF](https://arxiv.org/abs/2602.15384) |
| `2026` | **WebWorld: A Large-Scale World Model for Web Agent Training** | WebWorld 学习大规模网页仿真器，用于 agent 训练。 | [PDF](https://arxiv.org/abs/2602.14721) |
| `2026` | **Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning** | 合成约 1000 个由代码驱动、数据库支撑的工具环境用于 agent 强化学习，其状态转移比 LLM 模拟的环境更一致。 | [PDF](https://arxiv.org/abs/2602.10090) |
| `2026` | **Code2World: A GUI World Model via Renderable Code Generation** | Code2World 结合 AndroidCode、视觉修订与渲染感知学习，生成下一屏 GUI 代码。 | [PDF](https://arxiv.org/abs/2602.09856) |
| `2026` | **Generative Visual Code Mobile World Models (gWorld)** | gWorld 使用单一视觉语言模型，将移动 GUI 的未来观测预测为可渲染 Web 代码。 | [PDF](https://arxiv.org/abs/2602.01576) |
| `2026` | **InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training** | 大规模生成带可验证任务评估器的多页面功能性网站环境，用于训练 GUI agent。 | [PDF](https://arxiv.org/abs/2601.04126) |
| `2026` | **MobileDreamer: Generative Sketch World Model for GUI Agent** | 以文本草图世界模型预测移动 GUI 动作后的状态，供 GUI agent 进行前瞻推演。 | [PDF](https://arxiv.org/abs/2601.04035) |
| `2025` | **MobileWorldBench: Towards Semantic World Modeling For Mobile Agents** | MobileWorldBench 评价移动环境的语义状态转移及其对 GUI agent 的使用价值。 | [PDF](https://arxiv.org/abs/2512.14014) |
| `2025` | **ViMo: A Generative Visual GUI World Model for App Agents** | ViMo 通过图形与文本分解建模移动 GUI 的未来观测。 | [PDF](https://arxiv.org/abs/2504.13936) |

</details>

<a id="papers-other-benchmark"></a>
#### 评测基准 (37)

*评测基准与诊断研究，按评测对象分组。*

<details>
<summary>37 条记录</summary>

**评测 纯状态动力学（WorldCoder-type）**

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning** | 在 44 个情境中评估生成的部分可观测随机博弈模型，分别检验模型能否合法执行、结构与参考模型是否吻合，以及语义是否忠实。 | [PDF](https://arxiv.org/abs/2611.14419) |
| `2026` | **GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations** | 以实际执行得到的结果为参照，结合确定性检查与语义评判，测试文本模型对动作后环境响应的预测。 | [PDF](https://arxiv.org/abs/2610.22708) |
| `2026` | **GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions** | GameLogicBench 在多种可复现情景下，以逐仿真 tick 的状态检查验证 Godot 游戏规则。 | [PDF](https://arxiv.org/abs/2609.21562) |
| `2026` | **ScratchWorld: Evaluating If World Models Compute Executable Consequences** | ScratchWorld 利用可回放验证的 Scratch 转移与变化字段指标，评价可执行后果。 | [PDF](https://arxiv.org/abs/2606.31689) |
| `2025` | **Benchmarking World-Model Learning with Environment-Level Queries (WorldTest)** | 提出在无奖励探索后用环境层面的查询（可达性、反事实效果等）评估世界模型，并实例化为含 43 个交互式网格环境的 AutumnBench。 | [PDF](https://arxiv.org/abs/2510.19788) |
| `2025` | **Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** | Text2World 以多样化域和执行指标评价文本到 PDDL 世界模型的生成。 | [PDF](https://arxiv.org/abs/2502.13092) |

**评测 程序到视频的渲染（Code-as-World-type）**

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **WorldDraft: If Code Builds the World, Can Video Models Just Render It?** | 由 48 组可执行 4D 世界构造 432 个配对案例。固定动力学，改变代理精细度与外观提示，分别测运动和相机轨迹的保持程度、目标外观的实现程度。 | [PDF](https://arxiv.org/abs/2611.16217) |
| `2026` | **VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation** | VibeVideoBench 在无生成视频模型的沙箱中评测多模态智能体纯靠编写代码渲染音视频的 239 个任务，结合程序规格检查与细粒度准则打分。 | [PDF](https://arxiv.org/abs/2610.35864) |
| `2026` | **Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V** | 以文本、图像和视频为输入，评估可执行程序生成完整视频的能力，并测量执行、质量、指令对齐与参考保真。 | [PDF](https://arxiv.org/abs/2610.28416) |
| `2026` | **RenderBench: Benchmarking Render-to-Real Video Transfer with Reconstructed Digital Twins** | RenderBench 将可编辑三维数字孪生与代理渲染同真实目标视频配对，按物体、可见性、关节与运动定位代理到真实视频迁移的失真。 | [PDF](https://arxiv.org/abs/2610.08684) |
| `2026` | **PROWBench: Do Video Models Render What the Program Specifies?** | PROWBench 将渲染视频中的事件与可执行程序规格及事件日志进行对齐比较。 | [PDF](https://arxiv.org/abs/2610.02205) |
| `2026` | **Proxy2World: Learning to Generate Worlds From Lightweight Proxies without Seeing Them** | Proxy2World 通过跨模态流匹配从带位姿 RGBD 视频学习轻量代理条件生成，并提出 ProxyBench 评测不同场景与运动下的结构遵循度。 | [PDF](https://arxiv.org/abs/2609.35023) |

**评测 3D 世界构建（VibeWorlding-type）**

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **VeriWorld: A Verifiable Visual SWE-Bench for Spatial Reasoning in 3D Environments** | VeriWorld 在具备可执行动作与确定性验证器的交互式三维环境中对比视觉、结构化与联合输入，揭示感知到结构的推理鸿沟与协议敏感性。 | [PDF](https://arxiv.org/abs/2611.30226) |
| `2026` | **3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest extreme Long-Horizon Browser Games** | 3D GameDev Arena 包含 14 类共 108 个超长程从零构建三维网页游戏任务，联合代码功能验收、智能体试玩与人类盲测偏好评估编码智能体。 | [PDF](https://arxiv.org/abs/2611.24073) |
| `2026` | **OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation** | 针对 180 个 HTML5 游戏任务设置 1,800 条要求，通过静态源代码评判显式功能以及游戏系统间的深层关联。 | [PDF](https://arxiv.org/abs/2611.17681) |
| `2026` | **VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender** | 用 242 个任务评估可执行 Blender 场景。Scene Check 重跑代码核对隐藏的 4D 场景事实，Screen Check 再检查这些事实能否在预览视频中看出来。 | [PDF](https://arxiv.org/abs/2611.15789) |
| `2026` | **Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds** | 用 145 个任务评估编码 agent 构建物体、场景和交互世界的能力。开放世界任务区分局部机关是否可用，以及依赖通行空间和持久状态的完整活动能否完成。 | [PDF](https://arxiv.org/abs/2611.09017) |
| `2026` | **3DCodeEdit: Benchmarking Instruction-Guided 3D Program Editing** | 评测对 Blender 程序的指令驱动编辑，用渲染检查暴露“代码可运行但几何结果错误”的问题。 | [PDF](https://arxiv.org/abs/2610.38231) |
| `2026` | **UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity** | 用 Unity 项目和确定性的里程碑测试评测编码智能体对场景结构、组件配置和运行时行为的处理。 | [PDF](https://arxiv.org/abs/2610.35980) |
| `2026` | **BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References** | 通过多模态任务要求、渲染视图和任务评分细则，评估智能体创建的可编辑 Blender 场景。 | [PDF](https://arxiv.org/abs/2610.23986) |
| `2026` | **ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling** | 评估单个机制、多阶段组合机械系统以及意图驱动的可执行三维世界合成。 | [PDF](https://arxiv.org/abs/2610.15166) |
| `2026` | **WorldBench: Evaluating LLMs on Three.js Voxel World Generation** | 评测 LLM 编写的 Three.js 体素世界；评判器既探索运行中的世界、又阅读代码，只有两者一致时才计为证据。 | [PDF](https://arxiv.org/abs/2610.10622) |
| `2026` | **Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos** | Video2World 从几何、动力学和功能三个方面，评价具身视频到交互世界的重建。 | [PDF](https://arxiv.org/abs/2610.04432) |
| `2026` | **Spec2Game: Can LLMs Generate Complete Playable Games from Detailed Specifications?** | 评测根据详细游戏规格（含受控规则变体）生成完整 Pygame 项目的能力，区分可执行性与规则是否被忠实实现。 | [PDF](https://arxiv.org/abs/2610.04253) |
| `2026` | **Code4Scene: Benchmarking Coding Agents for Constructing and Editing 3D Scenes** | Code4Scene 基于 170 个 Unreal Engine 任务直接检查引擎原生场景的任务完成度、物理合法性与非编辑区保持度，评测三维构建与精确编辑。 | [PDF](https://arxiv.org/abs/2609.36777) |
| `2026` | **WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis** | WorldCoder-Bench 通过隐藏的运行时行为合同，评价具有物理依据的三维世界构建。 | [PDF](https://arxiv.org/abs/2606.01869) |
| `2026` | **VoxelCodeBench: Benchmarking 3D World Modeling Through Code Generation** | VoxelCodeBench 在 Unreal Engine 中执行体素世界生成代码，从符号理解、几何构建与多物体组合评测超越语法可执行性的三维空间正确性。 | [PDF](https://arxiv.org/abs/2604.02580) |

**评测 非代码的视频与学习型世界模型**

| 年份 | 论文 | 核心机制与简介 | 链接 |
|---|---|---|:-:|
| `2026` | **StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model** | StrideWorld 以运动前固定的真实初始几何和单步动作步幅为参照，揭示交互视频世界模型在相机漫游与组合路径下的场景形变与失速。 | [PDF](https://arxiv.org/abs/2611.24408) |
| `2026` | **The Flip Test: Video World Models Fail to Learn the World State (FlipTest)** | 用近乎相同的初始帧、配对对照及密集参数扫描，测试视频预测能否在物理结果刚好翻转的边界上随之改变。 | [PDF](https://arxiv.org/abs/2611.19822) |
| `2026` | **WorldProbe: When Video World Models Fall Apart under Long-Horizon Spatial Exploration** | 用目标条件多模态 agent 在线调整相机动作，探测视频世界模型的长时空间一致性。 | [PDF](https://arxiv.org/abs/2610.39721) |
| `2026` | **WMEval: Evaluating Interactive World Models Grounded on Physical Simulations** | 以 Unity 物理仿真为真值，对交互式世界模型进行感知、状态和物理因果层面的对齐评测。 | [PDF](https://arxiv.org/abs/2610.33894) |
| `2026` | **Events, Not Pixels: Where World Models Get the Return Wrong** | 在匹配预算下用真实转移替换部分想象转移诊断回报误差；对所测模型，奖励或终止事件比视觉误差大的帧更影响回报。 | [PDF](https://arxiv.org/abs/2610.29435) |
| `2026` | **Execution Before Memory: Diagnosing Memory Failures in Video World Models** | 提出 MIST 评测将“指令要求的隐藏状态改变是否实际发生”与“后续帧是否记住该结果”解耦，指出视频世界模型的许多记忆失败实为执行缺失。 | [PDF](https://arxiv.org/abs/2610.23542) |
| `2026` | **WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions** | 以配对真实执行评估动作条件机器人世界模型，覆盖状态正确性、交互空间对齐、局部交互保真及多视角动作一致性。 | [PDF](https://arxiv.org/abs/2610.18826) |
| `2026` | **Can Video World Models Track Unobserved World States? (Visual Shell Game)** | 通过动作条件“三杯猜球”视频测试与置换群状态追踪分析，检验视频世界模型能否在长交换序列与视野外演化中维护可修订的隐藏世界状态。 | [PDF](https://arxiv.org/abs/2608.30692) |
| `2026` | **Current World Models Lack a Persistent State Core (WRBench)** | WRBench 将移开镜头作为可观测性干预，在 23 个模型的 9,600 段视频上检验视野外物理事件是否随时间持续演化而非停滞在离开瞬间。 | [PDF](https://arxiv.org/abs/2606.20545) |
| `2025` | **WorldModelBench: Judging Video Generation Models As World Models** | WorldModelBench 从指令遵从、物理合理性和人类偏好评价视频世界模型。 | [PDF](https://arxiv.org/abs/2502.20694) |

</details>

[↑ 返回总览](#contents)

<!-- CATALOG:END -->

<a id="related-surveys"></a>
## 相关综述：我们的不同之处

<!-- RELATED:BEGIN -->

相关综述以视频模型或通用世界模型为中心；本综述以**可执行代码作为世界的载体**为纳入标准，按代码承担了世界的多少部分（纯状态 / 白模 + 生成式渲染 / 完整 3D）组织文献，视频模型只作为可选的渲染器出现。

<details>
<summary><strong>展开查看与 13 篇相关综述的逐条对比</strong></summary>

| 年份 | 相关综述 | 与本综述的区别 | 链接 |
|---|---|---|:-:|
| `2026` | **Video Models as Generative Renderers: Foundations, Interfaces, Systems, and Beyond** | 该综述以视频渲染器为中心，按上游规格阶梯（T0–T3b）组织条件视频生成，代码引擎只是其中一种上游代理源。本综述以可执行代码世界本身为中心，覆盖纯状态动力学（01）、白模加生成式渲染（02）与完整三维世界构建（03），并用 L0–L4 拆解上游状态决定权。 | [Project](https://genrender-hub.github.io/) |
| `2026` | **Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement** | 该综述以视频生成模型为中心，梳理围绕它构建的 agent harness（视频制作、交互式世界建模、递归自我改进），代码只是 harness 的组件之一。本综述以代码为世界的载体：代码承担状态与规则、白模世界或完整 3D 世界，视频模型只是可选的渲染器之一。 | [PDF](https://arxiv.org/abs/2610.40191) |
| `2026` | **Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence** | 该文从自进化具身编码智能体视角结合 Code as Policy 与 Code as World；本综述专门系统展开 Code as World 在状态动力学、代理生成渲染与三维世界构建上的完整谱系。 | [PDF](https://arxiv.org/abs/2609.35432) |
| `2026` | **AI for Games in the Foundation Model Era** | 该综述覆盖游戏领域的方方面面，包括学习型游戏世界模型与 AI 辅助开发。本综述中游戏只是若干领域之一，重点是以可执行代码写成的游戏规则与世界。 | [PDF](https://arxiv.org/abs/2609.16679) |
| `2026` | **Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence** | 该综述聚焦具身预测世界模型与直接 VLA 策略的评测对比；本综述将机器人视为验证载体之一，重点考察可执行世界程序、持久状态与反事实可验证性。 | [PDF](https://arxiv.org/abs/2609.29669) |
| `2026` | **From Generation to Simulation: How Far Are World Models from Being True Simulators?** | 该综述考察潜变量、视频和联合嵌入世界模型距离模拟器还有多远。代码世界模型走的是相反路线：从带显式状态的可执行基底出发；本综述研究这一基底如何被归纳、构建和渲染。 | [PDF](https://arxiv.org/abs/2608.23070) |
| `2026` | **From Pixels to States: Rethinking Interactive World Models as Game Engines** | 该综述主张视频世界模型应恢复游戏引擎中的显式状态循环。Code-as-World 方法把这一循环保留在可执行代码中，视频模型只负责渲染；本综述比较的是代码承担了这一循环的多少部分。 | [PDF](https://arxiv.org/abs/2607.14076) |
| `2026` | **Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application** | 该综述把环境视为 agent 的训练基础设施。本综述只关注其代码充当世界模型、预测或模拟世界演化的情形，基准和合成任务环境居于次要位置。 | [PDF](https://arxiv.org/abs/2606.12191) |
| `2026` | **Bridging the Agent-World Gap: Text World Models for LLM-based Agents** | 该综述聚焦文本环境，把"代码作为世界模型"视为一种构建范式。本综述以代码世界本身为主题，并从文本与符号状态扩展到白模加生成式渲染以及完整 3D 世界。 | [PDF](https://arxiv.org/abs/2606.09032) |
| `2026` | **Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends** | 该综述以动作条件视频与三维生成式世界模型为中心；本综述以可执行代码为世界基底，视频生成模型仅作为可选的条件渲染器出现。 | [PDF](https://arxiv.org/abs/2606.01164) |
| `2026` | **World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications** | 该综述按架构、方法族、推理策略与应用领域梳理广义学习型世界模型；本综述专门聚焦以可执行代码承载状态、规则或三维结构的世界模型。 | [PDF](https://arxiv.org/abs/2606.00133) |
| `2026` | **Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond** | 该综述按能力层级与规律类型梳理 400 余项工作，代码化模型只是众多实现方式之一。本综述的组织问题是代码在世界中承担什么，只收录以代码为世界载体的方法。 | [PDF](https://arxiv.org/abs/2604.22748) |
| `2025` | **LLMs as Planning Formalizers: A Survey for Leveraging Large Language Models to Construct Automated Planning Models** | 该综述覆盖 WorldCoder-type 的一个分支：由语言写出的符号规划模型。本综述将其与 Python 转移程序、物理残差、生成式渲染的代码世界和 3D 世界程序放在同一框架下。 | [PDF](https://arxiv.org/abs/2503.18971) |

</details>

<!-- RELATED:END -->

<a id="contributing"></a>
## 参与贡献与联系

欢迎推荐论文、修正元数据、补充评测基准以及探讨研究合作。

- **补充或更新文献：** 请遵循[贡献指南](CONTRIBUTING.md)或直接[提交 Issue](https://github.com/FreedomIntelligence/Awesome-Code-World-Model/issues/new)。
- **研究合作与交流：** 欢迎联系 [@YihDu](https://github.com/YihDu) 和 [@MichaelCao0](https://github.com/MichaelCao0)。

<details>
<summary><strong>维护说明：本地构建与来源约定</strong></summary>

两份 README 共享 [data/papers.json](data/papers.json) 中的论文数据，中文摘要保存在 [data/readme.zh-CN.json](data/readme.zh-CN.json)。本地重新生成与校验：

```bash
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

文献记录链接到 arXiv、DOI 或正式会议页面。论文标题与方法别名分别保存；日期遵循原始来源元数据，可能与会议年份不同。核查深度与影响结论的实验条件见[详细核查表](docs/catalogue.md)和[核查协议](docs/review-protocol.md)。

| 相似名称 | 对应区别 |
|---|---|
| Code2World / Code2Worlds | GUI 观测预测 / 四维仿真生成 |
| Web World Models / WebWorld | 代码定义的持久世界 / 学习型网页仿真 / 基于浏览器的代码验证，分别对应三项工作 |
| WorldCoder / WorldCoder-Bench | 基于模型的 agent / 三维世界构建基准 |
| TheoryCoder / TheoryCoder-2 | 方法别名；文献库保留各自的正式论文标题 |
| OneLife / General Game Playing | 从探索中学习随机动力学 / 根据游戏规则和轨迹构建可执行模型 |
| FAIR CWM | 计算执行与代码生成的神经建模 |

相关预印本在结构化数据中互相链接。数量表示文献来源记录，详细核查表分别标注核心方法、历史来源、支撑表示、基准和对照方法。

</details>

<a id="about-this-initiative"></a>
## 关于本研究计划

本仓库是持续推进中的代码世界模型（Code World Models）研究计划的一部分，汇聚关注可执行世界表示、可编程动力学与交互式世界生成的研究者。

我们致力于贡献一系列开放研究成果，涵盖综述、评测基准与新的建模方法，欢迎与更广泛的研究社区开展讨论与合作。

<a id="acknowledgements"></a>
## 致谢

衷心感谢 [Yankai Chen](https://yankai-chen.github.io/) 对本研究计划的指导与支持。

<p align="center"><a href="#code-world-models">返回顶部 ↑</a></p>
