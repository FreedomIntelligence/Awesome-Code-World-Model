<div align="center">

# Code World Models

<p>
  An open research hub for Code World Models —<br>
  curated literature, forthcoming survey, benchmarks, and post-trained models.<br>
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a>
</p>

<!-- BADGES:BEGIN -->

[![Papers](https://img.shields.io/badge/Papers-201-6c8ba8?style=flat-square&labelColor=4a5568)](#paper-collection) [![Survey PDF coming soon](https://img.shields.io/badge/Survey%20PDF-coming%20soon-b47b7b?style=flat-square&labelColor=4a5568)](#motivation) [![GitHub stars](https://img.shields.io/github/stars/FreedomIntelligence/Awesome-Code-World-Model?style=flat-square&logo=github&labelColor=4a5568&color=7b9a8d)](https://github.com/FreedomIntelligence/Awesome-Code-World-Model/stargazers) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-8c82a3?style=flat-square&labelColor=4a5568)](CONTRIBUTING.md)

<!-- BADGES:END -->

<p><img src="./assets/banner.png" alt="Worlds, made executable: code, persistent state, and rendered observations" width="960"></p>

</div>

<a id="motivation"></a>
## Overview

As coding agents become increasingly capable of generating, executing, and refining complex programs, **code** is emerging as a principled substrate for world modeling. Beyond predicting pixels, code world models provide **explicit dynamics, persistent state, and programmable interaction**—offering a complementary path toward controllable, editable, and verifiable worlds.

<a id="upcoming-releases"></a>
As part of our ongoing research effort, we plan to release a series of open resources on Code World Models—including a comprehensive **survey**, **benchmarks** for executable dynamics and renderable worlds, and **post-training recipes and open models**.

> **Contribute & Collaborate:** PRs, paper suggestions, and research collaborations are warmly welcome. Contact [@YihDu](https://github.com/YihDu) and [@MichaelCao0](https://github.com/MichaelCao0), or open an issue on [GitHub](https://github.com/FreedomIntelligence/Awesome-Code-World-Model/issues).

<a id="contents"></a>
<a id="taxonomy"></a>
## Taxonomy & Navigation

<!-- NAVIGATION:BEGIN -->

| Family | Code Carries | Core Question | Papers |
|---|---|---|---:|
| **[01 · WorldCoder-type](#papers-worldcoder)** | State & dynamics only | Does code predict action consequences and support planning? | **50** |
| **[02 · Code-as-World-type](#papers-code_as_world)** | Whitebox world + generative rendering | Can executable state & rules drive a generatively rendered world? | **31** |
| **[03 · VibeWorlding-type](#papers-vibeworlding)** | Full 3D world | Can an agent write and edit a full 3D world in code? | **45** |
| **[Other](#papers-other)** | GUI worlds, benchmarks & surveys | [GUI World Models](#papers-other-gui) (25) · [Benchmarks](#papers-other-benchmark) (37) · [Related Surveys](#related-surveys) (13) | **75** |

<!-- NAVIGATION:END -->

<a id="paper-collection"></a>
## Paper Collection

<!-- CATALOG:BEGIN -->

**201 sources** · updated through **2026-11-26** · ordered by date (newest first). Full metadata in the [annotated catalogue](docs/catalogue.md) and [master list](docs/paper-master-list.md).

<a id="papers-worldcoder"></a>
### 01 · WorldCoder-type · Programmatic Dynamics (50)

*State-level executable dynamics: transition mechanisms, world-program induction, planning, and model repair, without generated appearance.*

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **CodeWAM: A Code World Action Model for End-to-End Autonomous Driving** | Represents ego-vehicle motion under candidate plans with executable dynamics code paired with a learned visual scene model to evaluate future consequences in end-to-end driving. | [PDF](https://arxiv.org/abs/2611.32483) |
| `2026` | **Creating Hybrid Interactive Narrative Systems with LLM: From Formal Description to Evaluation** | Encodes narrative events as operations with explicit preconditions and effects. Three experience managers act on the same facts and goals, making their story trajectories comparable as plans. | [PDF](https://arxiv.org/abs/2611.02807) |
| `2026` | **Algebraic World Model: From Exploration to Proofs** | Explores unknown games with executable Python hypotheses, typed rules, and Lean formalization for reachability and impossibility proofs. | [PDF](https://arxiv.org/abs/2610.40503) |
| `2026` | **PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds** | Has a shared VLM propose executable physical worlds while a deterministic engine verifies counterfactual branches and produces answer-bound training tasks. | [PDF](https://arxiv.org/abs/2610.34921) |
| `2026` | **Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players (AutoTavern)** | A self-improving research-agent system builds and verifies a faithful Hearthstone Battlegrounds simulator, then trains agents against calibrated opponents. | [PDF](https://arxiv.org/abs/2610.33845) |
| `2026` | **LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica** | Studies LLM coding agents that assemble and calibrate executable Modelica physical-system models from descriptions and data, with acceptance based on behavioral fit, invariants and interpretability. | [PDF](https://arxiv.org/abs/2610.25019) |
| `2026` | **Neurosymbolic Learning of Interpretable World Models (CGWM)** | Learns visual concept grounding while a parameter-free predictor applies supplied temporal-logic transition rules; planning differentiates through symbolic imagined trajectories. | [PDF](https://arxiv.org/abs/2610.19955) |
| `2026` | **A Declared World Model: Language Models Write the Rules of the Scene They are Shown** | A language model writes world rules from a labelled scene graph. A deterministic engine checks proposed actions and computes next states. Experiments test whether generated rules transfer beyond the observed layout. | [PDF](https://www.preprints.org/manuscript/202610.1139) |
| `2026` | **Write Once, Plan Many: Building Reusable Visual Planning Systems from One Scene** | Builds reusable executable renderers, dynamics, perception and planning programs from supplied domain rules and one practice scene; execution and reconstruction checks refine programs before reuse. | [PDF](https://arxiv.org/abs/2610.19234) |
| `2026` | **RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions** | Extracts reusable role prototypes and executable transition rules, then adapts role assignments and parameter estimates in new environments while keeping transition rules fixed. | [PDF](https://arxiv.org/abs/2610.13172) |
| `2026` | **Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** | Memento 3 revises reflective rulebooks and executable models using trajectory judgments and exact replay. | [PDF](https://arxiv.org/abs/2610.11794) |
| `2026` | **LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** | LLM-IDEA uses identifiability-aware experimental design to distinguish mechanistic explanations. | [PDF](https://arxiv.org/abs/2610.11253) |
| `2026` | **Kepler: Auditable World Models for ARC-AGI-3** | Kepler studies auditable ARC-AGI-3 world models through retrospective and conditional transition checks and cost accounting. | [PDF](https://arxiv.org/abs/2610.00834) |
| `2026` | **Schema: Discovering Unknown Environments via Agentic Program Induction** | An agent harness keeps its understanding of an unknown environment as executable programs in a persistent workspace, checks them against interaction history, and plans with them under step-wise verification (ARC-AGI-3 and other games). | [PDF](https://arxiv.org/abs/2609.39140) |
| `2026` | **EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning** | EMPIRIC learns residual code that extends a physics engine with missing forces, constraints, and hidden state. | [PDF](https://arxiv.org/abs/2609.35047) |
| `2026` | **Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning** | Code as Worlds discovers executable physical representations through propose, instantiate, execute, render, and verify loops. | [PDF](https://arxiv.org/abs/2608.27549) |
| `2026` | **PDDLCoder: Agentic PDDL Generation for LLM-Assisted Symbolic Planning** | An agentic loop generates, analyzes and refines PDDL domains and problems from natural language, with a benchmark of gym environments that verify plan applicability automatically. | [PDF](https://arxiv.org/abs/2608.16637) |
| `2026` | **Twin: Playing an Unknown Game with a Test-Time Digital Twin** | Twin builds a test-time digital twin and checks historical transitions before choosing actions in unknown games. | [PDF](https://arxiv.org/abs/2608.14490) |
| `2026` | **Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3** | Tycho actively revises abstractions and programmatic hypotheses while solving ARC-AGI-3 games. | [PDF](https://arxiv.org/abs/2607.28287) |
| `2026` | **VisualPatchWorld: Code World Models as Latent Structured Representations for Planning** | VisualPatchWorld fits dynamics from structured state-action traces and uses visual scene graphs for replanning. | [PDF](https://arxiv.org/abs/2607.25236) |
| `2026` | **Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation** | Combines LLM-generated simulator families with neural simulation-based inference to select mechanisms and estimate parameters. | [PDF](https://arxiv.org/abs/2607.17540) |
| `2026` | **Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?** | Tests executable-model discipline, simplification, and replay verification in coding agents for ARC-AGI-3. | [PDF](https://arxiv.org/abs/2607.15439) |
| `2026` | **When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models** | Shows that an LLM-synthesized code world model can pass transition-accuracy checks yet lose at play because its rare errors sit on pivotal dynamics, and proposes play-adequacy rather than prediction accuracy as the acceptance criterion. | [PDF](https://arxiv.org/abs/2607.14169) |
| `2026` | **World-Time Compute with Verified Code World Models** | World-Time Compute uses verified symbolic code worlds to generate exactly labeled trajectories for model training. | [PDF](https://arxiv.org/abs/2609.09163) |
| `2026` | **OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3** | OPINE-World jointly revises symbolic ontology, transition hypotheses, and goals through error-prioritized exploration. | [PDF](https://arxiv.org/abs/2607.01531) |
| `2026` | **Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** | Mind-Studio constructs executable models for partially observable games and evaluates same-state multi-step lookahead fidelity. | [PDF](https://arxiv.org/abs/2606.16070) |
| `2026` | **PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty** | Learns symbolic POMDP domains in PO-PDDL from robot demonstration videos by inferring latent state trajectories and stochastic transition and observation rules for belief-space planning. | [PDF](https://arxiv.org/abs/2606.15654) |
| `2026` | **PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments** | PatchWorld optimizes executable belief-state models through counterexample-guided patches and uses them for action lookahead. | [PDF](https://arxiv.org/abs/2605.30880) |
| `2026` | **Distilling Game Code World Model Generation into Lightweight Large Language Models (GameCWM distillation)** | Distills the generation of game code world models (rules, legal actions, transitions, observations, rewards) from frontier LLMs into smaller models through post-training. | [PDF](https://arxiv.org/abs/2605.24375) |
| `2026` | **Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models (Alice / Baba in Wonderland)** | Alice learns executable dynamics under misaligned lexical priors, using preservation conflicts to revise hypotheses and guide exploration. | [PDF](https://arxiv.org/abs/2605.16725) |
| `2026` | **Learning POMDP World Models from Observations with Language-Model Priors (Pinductor)** | An LLM proposes candidate POMDP world models from a few observation-action trajectories and refines them against a belief-based likelihood, without access to hidden state. | [PDF](https://arxiv.org/abs/2605.13740) |
| `2026` | **Executable World Models for ARC-AGI-3 in the Era of Coding Agents** | Builds executable ARC-AGI-3 models with history replay, simplification, and planning. | [PDF](https://arxiv.org/abs/2605.05138) |
| `2026` | **Neuro-Symbolic Synergy for World Modeling (NeSyS)** | Alternately trains an LLM world model and executable symbolic rules on transitions the other explains poorly, combining them through log-linear reranking. | [PDF](https://arxiv.org/abs/2602.10480) |
| `2026` | **Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents (TheoryCoder-2)** | TheoryCoder-2 learns and reuses planning abstractions in program-synthesis agents. | [PDF](https://arxiv.org/abs/2602.00929) |
| `2026` | **CASSANDRA: Programmatic and Probabilistic Learning and Inference for Stochastic World Modeling** | Builds transition models for business-style planning domains from LLM-written code for deterministic features plus LLM-guided structure learning of a probabilistic graphical model for stochastic ones. | [PDF](https://arxiv.org/abs/2601.18620) |
| `2025` | **Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback** | Agent2World uses research, development, and adaptive testing agents to generate symbolic world models and training trajectories. | [PDF](https://arxiv.org/abs/2512.22336) |
| `2025` | **One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration (OneLife)** | OneLife learns conditionally activated probabilistic laws from unguided exploration in Crafter-OO. | [PDF](https://arxiv.org/abs/2510.12088) |
| `2025` | **Code World Models for General Game Playing** | Synthesizes Python transitions, legal moves, termination, value heuristics, and hidden-state inference for board and card games. | [PDF](https://arxiv.org/abs/2510.04542) |
| `2025` | **Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video (FAE)** | FAE extracts sprite-grid behavior programs from gameplay video through a constrained reactive DSL. | [PDF](https://arxiv.org/abs/2508.11836) |
| `2025` | **PoE-World: Compositional World Modeling with Products of Programmatic Experts** | PoE-World composes programmatic experts into a stochastic world model for prediction and planning. | [PDF](https://arxiv.org/abs/2505.10819) |
| `2025` | **LLM-Guided Probabilistic Program Induction for POMDP Model Estimation** | Uses an LLM as a prior over short probabilistic programs for POMDP components (transition, observation, reward, initial state) and refines them against empirical data, including robot search domains. | [PDF](https://arxiv.org/abs/2505.02216) |
| `2025` | **WALL-E 2.0: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents** | Extracts action rules, knowledge graphs and scene graphs from exploration trajectories, encodes them as executable code that aligns an LLM world model, and plans with model-predictive control. | [PDF](https://arxiv.org/abs/2504.15785) |
| `2025` | **Synthesizing world models for bilevel planning (TheoryCoder)** | TheoryCoder combines synthesized low-level Python dynamics with supplied high-level PDDL abstractions for bilevel planning. | [PDF](https://arxiv.org/abs/2503.20124) |
| `2025` | **Generating Symbolic World Models via Test-time Scaling of Large Language Models** | Generates and corrects PDDL world models with Best-of-N search and fine-grained verbalized feedback. | [PDF](https://arxiv.org/abs/2502.04728) |
| `2024` | **Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search (GIF-MCTS)** | GIF-MCTS searches executable Python world models using descriptions, offline transitions, and execution feedback. | [PDF](https://arxiv.org/abs/2405.15383) |
| `2024` | **WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** | WorldCoder synthesizes Python transition and reward models from interaction, coupling model consistency with optimistic planning. | [PDF](https://arxiv.org/abs/2402.12275) |
| `2023` | **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** | Uses LLMs to construct and correct PDDL domain models for sound model-based task planning. | [PDF](https://arxiv.org/abs/2305.14909) |
| `2023` | **Combining Functional and Automata Synthesis to Discover Causal Reactive Programs (AutumnSynth)** | AutumnSynth alternates transition-function synthesis and automata synthesis to recover reactive programs with latent state. | [PDF](https://doi.org/10.1145/3571249) |
| `2021` | **Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning (EMPA)** | EMPA learns probabilistic game-engine programs and runs internal simulations for exploration and planning. | [PDF](https://arxiv.org/abs/2107.12544) |
| `2017` | **Game Engine Learning from Video** | Learns executable game-engine rules from video and evaluates future-state prediction and agent training. | [PDF](https://www.ijcai.org/proceedings/2017/518) |

[↑ Back to overview](#contents)

<a id="papers-code_as_world"></a>
### 02 · Code-as-World-type · Whitebox Worlds + Generative Rendering (31)

*Code keeps persistent state and rules over a whitebox/proxy world; a generative renderer supplies appearance.*

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **Zing-1.0: A Playable World System Built on Controllable Rendering** | An executable engine resolves player actions under world rules and emits proxy video to a block-causal streaming renderer synchronized with simulation updates. | [PDF](https://arxiv.org/abs/2611.27336) |
| `2026` | **ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds** | Autoregressive video diffusion renderer with dynamic-context learning, recurrent history compression and cross-representation flow alignment for sustained rendering from game-engine proxies. | [PDF](https://arxiv.org/abs/2611.25838) |
| `2026` | **WorldRuler: Interactive World Modeling under Configurable Rules** | Organizes user-defined rules, dependencies and object states in an executable 3D rule graph coupled in a closed loop with video generation and perceptual feedback across save-and-load. | [PDF](https://arxiv.org/abs/2611.24869) |
| `2026` | **Code World Model 2.0: Towards Infinite Controllable Video Generation (Invoker-Render)** | Pairs bidirectional creation and four-step causal streaming via ProForcing over multi-granularity structural proxies, an appearance reference and language, while the upstream engine supplies state and motion. | [PDF](https://arxiv.org/abs/2611.22925) |
| `2026` | **GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models** | A game engine computes event timing, outcomes and camera state. A video model renders the interaction, allowing the same mechanic to take different visual forms. | [PDF](https://arxiv.org/abs/2611.19247) |
| `2026` | **Streaming Code World Model (Streaming CWM)** | Implements causal four-step chunked streaming video generation over depth and semantic proxies exported from Code World Model and CARLA driving state. | [Project](https://github.com/TingtingLiao/streaming-code-world-model) |
| `2026` | **CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models** | Renders two players’ views jointly from a shared programmable 3D proxy and RGB references. Synchronized GTA V observations test whether characters retain their appearance across viewpoints. | [PDF](https://arxiv.org/abs/2611.15602) |
| `2026` | **Fight World Model: Customizable Combat through Visual Interaction Proxies** | Separates executable combat state and rule resolution from video rendering with identity- and timing-aligned interaction proxies; tests rule changes and customization. | [PDF](https://arxiv.org/abs/2610.40607) |
| `2026` | **Wizard: Manipulate Any World in Real Time via Agentic Control** | Combines structured skeleton/geometry proxies with an agentic framework that maintains game state for real-time, generalizable video-world control. | [PDF](https://arxiv.org/abs/2610.40339) |
| `2026` | **EdenLive: Real-Time Generative Rendering from Any Visual Reference** | A generative renderer maps upstream reference video, a target first frame and a prompt to enhanced video. The upstream program maintains state and rules. Released tooling also includes a prompt-to-playable-game skill and workbench. | [Project](https://github.com/VAST-AI-Research/EdenLive) |
| `2026` | **BoxWorld: Let World Engines Control and Video Generators Render** | A coding agent turns user rules into a Box World Engine exposing persistent attributes and status variables; a state renderer converts the stream into interactive video. | [PDF](https://arxiv.org/abs/2610.36371) |
| `2026` | **Mundo: Customized World Model** | Images are reconstructed into an editable 3D proxy. A scene program specifies objects and physical parameters; scripts and usually MuJoCo evolve state. Proxy frames condition a video renderer together with context views. | [Project](https://mundo-world-model.github.io/) |
| `2026` | **AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark** | Renders agent-built game blockouts into entity-consistent video while preserving layout, camera, entity timing, and count changes. | [PDF](https://arxiv.org/abs/2610.31466) |
| `2026` | **SolarRenderer: Few-Step Generative Reference Rendering** | Adapts a frozen video backbone with control and acceleration LoRAs to turn aligned structural video into detailed video, including streaming generation. | [PDF](https://arxiv.org/abs/2610.28630) |
| `2026` | **Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds** | A coding agent turns player requests into executable game rules; an engine owns persistent state, while a causal video model renders detailed views from low-poly proxies. | [PDF](https://arxiv.org/abs/2610.27999) |
| `2026` | **State World Models: Execute the Rules, Generate the Pixels** | A coding agent writes a typed game definition; a runtime executes rules over semantic and spatial state before a frozen video renderer, then admits rule-compatible visual feedback. | [PDF](https://arxiv.org/abs/2610.26811) |
| `2026` | **Mallea: Building, Steering, and Memorizing Worlds with Coding Agent** | A coding agent jointly builds object structures and rules, supports runtime edits preserving unaffected state, and combines executed state with object texture memory for rendering. | [PDF](https://arxiv.org/abs/2610.21283) |
| `2026` | **Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation (ATAS)** | Compiles screenplay shots with spatial and event-time references, retrieves registered scene and event memories, and admits generated observations into memory only after checks. | [PDF](https://arxiv.org/abs/2610.20571) |
| `2026` | **Generative World Simulation with DAO and JING (DAO + JING)** | DAO maintains shared character, object, and space states under world time and interaction rules, while JING renders observer-specific audiovisual experiences. | [PDF](https://arxiv.org/abs/2610.19726) |
| `2026` | **From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction (DR-WM)** | Combines RGB scene reconstruction and behavior-calibrated terrain contact priors with physics simulation, using simulated motion and geometry to guide a video world model. | [PDF](https://arxiv.org/abs/2610.17630) |
| `2026` | **StreamRender-H3: Interactive Coding Worlds with Real-time Streaming Diffusion Render** | A three.js game engine maintains maps, rules and state, advancing on player inputs. Semantic frames connect it to a streaming MiniMax-H3 renderer. The demonstrated system separates executable simulation from generated appearance. | [Project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/) |
| `2026` | **AgentGarten: Code Worlds for Evolving Agents** | AgentGarten connects program-defined simulation backends to a shared real-time renderer and reusable agent playbooks. | [PDF](https://arxiv.org/abs/2610.12374) |
| `2026` | **Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models** | A coding agent and lightweight engine maintain an extensible world-state table, compile coarse visual conditions, and incorporate newly observed objects for persistent interaction. | [PDF](https://arxiv.org/abs/2610.01614) |
| `2026` | **WorldWeave: Growing Persistent Geometric Worlds for Video Generation** | Decouples expandable world-state maintenance from video synthesis via agent-guided scene organization, deterministic geometry compilation and read-only depth queries across revisits. | [PDF](https://arxiv.org/abs/2609.34221) |
| `2026` | **Code Plans, Diffusion Renders: Open-Ended Generative World Modeling (CoDeR)** | CoDeR coordinates executable whitebox world construction with a generative Artist for open-ended visual worlds. | [PDF](https://arxiv.org/abs/2609.26458) |
| `2026` | **GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models** | GameDirector uses visual situation estimates and explicit gameplay rules to control game-video generation. | [PDF](https://arxiv.org/abs/2609.25652) |
| `2026` | **Programmable World Model** | Programmable World Model compiles persistent engine state, including nonvisual facts, into controls for video generation. | [PDF](https://arxiv.org/abs/2609.10540) |
| `2026` | **Magpie: Real-Time World Renderer for Interactive Games** | Magpie combines persistent game-engine state and rules with a whitebox-conditioned interactive neural renderer. | [PDF](https://arxiv.org/abs/2608.27168) |
| `2026` | **Code World Model: Coding Agent as World Brain** | Code World Model separates a coding world brain from a visual world engine through executable proxy representations. | [PDF](https://arxiv.org/abs/2608.25927) |
| `2026` | **Generative World Renderer at the Speed of Play (AlayaRenderer-Flash)** | Distills a G-buffer and prompt-conditioned generative world renderer into a few-step autoregressive streaming model running at over 30 FPS when paired with a physics engine. | [PDF](https://arxiv.org/abs/2607.18703) |
| `2025` | **Web World Models** | Web World Models uses typed web state and code-defined rules as the substrate for persistent, generative worlds. | [PDF](https://arxiv.org/abs/2512.23676) |

[↑ Back to overview](#contents)

<a id="papers-vibeworlding"></a>
### 03 · VibeWorlding-type · Agentic 3D World Construction (45)

*Code specifies the full 3D world (geometry, materials, layout, and optionally physics) for conventional rendering or simulation; static scenes included.*

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **TelePhysica: Agentic Reconstruction of Physically Interactive Scenes** | Reconstructs visual meshes and executable physical models from a photograph, checks equilibrium, then simulates interventions such as reversing an applied force. Simulated trajectories can also guide video synthesis. | [PDF](https://arxiv.org/abs/2611.18078) |
| `2026` | **SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation (SceneAgent (portable game scenes))** | Stores the evolving game scene in a persistent SceneContext. Builder agents reuse layout skills across engines while adapters translate coordinates, bind assets and export scenes. | [PDF](https://arxiv.org/abs/2611.17821) |
| `2026` | **BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs** | Trains open-weight MLLM agents to edit explicit 3D scenes via Blender Python code inside an isolated deterministic sandbox with structured state export and multi-turn RL rewards. | [PDF](https://arxiv.org/abs/2611.10768) |
| `2026` | **Gym-Anything for Robotics: Scaling physical simulations with digital agents** | Treats simulation creation as a coding-agent task and releases RoboWorld environments plus an adversarial creation-audit loop for physical simulation construction. | [PDF](https://arxiv.org/abs/2610.40565) |
| `2026` | **Cinematize from Unreal: Agentic Choreography for Controllable World Simulation (CineU)** | Uses an Unreal project as a persistent inspectable world; agent-generated code performs geometry- and capability-constrained operations with verification and localized repair. | [PDF](https://arxiv.org/abs/2610.38468) |
| `2026` | **Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction (SceneEvolve)** | Represents compositional 3D scenes as executable code and evolves the reconstruction harness while fixing model parameters, action semantics, and execution backend. | [PDF](https://arxiv.org/abs/2610.37046) |
| `2026` | **SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments** | Coordinates reconstruction, physical modeling, simulation inspection, and repair to turn 3D/4D captures into interactive simulation environments. | [PDF](https://arxiv.org/abs/2610.34745) |
| `2026` | **SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning** | Combines visual layout sampling with contract-guided 3D compilation and physical-stability checks for embodied-learning environments. | [PDF](https://arxiv.org/abs/2610.32978) |
| `2026` | **WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations** | Constructs interactive digital twins from in-the-wild robot demonstrations by iteratively refining an executable world program with verification feedback. | [PDF](https://arxiv.org/abs/2610.31834) |
| `2026` | **WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State** | Hierarchical planning predicts typed regional and tile specifications; fixed procedural generators compile them, while persistent records retain identities, boundary contracts and edits across streaming revisits. | [PDF](https://arxiv.org/abs/2610.28827) |
| `2026` | **SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images** | Reconstructs objects and scene layout from one image, then edits scene code and uses bounded pose search plus simulation validation to retain physically stable, visually aligned configurations. | [PDF](https://arxiv.org/abs/2610.28585) |
| `2026` | **NeoWorld-3: From Pixels to Code-Defined Physical Worlds** | Reconstructs editable geometry programs from visual evidence through hierarchical coding agents, differentiable parameter fitting and articulation/physics checks. | [PDF](https://arxiv.org/abs/2610.27690) |
| `2026` | **InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation** | Uses a VLM-driven procedural pipeline with symbolic constraints and deterministic placement to build editable, animated, photorealistic 3D worlds. | [PDF](https://arxiv.org/abs/2610.26853) |
| `2026` | **Self-Building Labs** | Agents construct laboratory digital twins, reusable robot skills and workflows from objectives, photographs and device information, refining scene models using observations and physical feedback. | [PDF](https://arxiv.org/abs/2610.23826) |
| `2026` | **3DCodeVerse: Exploring 3D Worlds as Code** | Packages executable 3D programs with assets and verification records; a generation-and-repair harness uses execution, geometry measurements and visual feedback. | [PDF](https://arxiv.org/abs/2610.22341) |
| `2026` | **RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks** | Interactive Newton-based toolkit exposes solver, contact-model and physical-parameter choices so humans and coding agents can refine manipulation simulations against observed behavior. | [PDF](https://arxiv.org/abs/2610.18835) |
| `2026` | **CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations** | Builds agent-operable, parameterized 3D cities from one aerial image per region, kept as persistent code-based state with entity identities and versioned, validated updates. | [PDF](https://arxiv.org/abs/2610.18342) |
| `2026` | **Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation** | Compiles generated visual scenes into MuJoCo-compatible worlds with physical attributes and refines executable dynamics using simulator feedback. | [PDF](https://arxiv.org/abs/2610.17651) |
| `2026` | **USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation** | USDCraft converts source geometry into executable modeling programs that export articulated USD simulation assets. | [PDF](https://arxiv.org/abs/2610.11322) |
| `2026` | **Code2Games: Enabling Coding Agents for Gaming World Generation** | Builds playable gaming worlds from a game intent by planning gameplay over a generated Blender world, porting it to Unreal Engine 5, and repairing it with compilation and runtime feedback. | [PDF](https://arxiv.org/abs/2610.05033) |
| `2026` | **LEGO-Anything: Coding Agents for 3D Scene Reconstruction** | LEGO-Anything reconstructs 3D scenes as executable programs and separates artifact, geometry, and appearance evaluation. | [PDF](https://arxiv.org/abs/2609.36380) |
| `2026` | **Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** | Recursive Code World Models reconstruct complex scenes using recursive programs, global-local refinement, and shared reference views. | [PDF](https://arxiv.org/abs/2609.11499) |
| `2026` | **FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation** | FuncRoom-Agent generates functional indoor scenes with a recursive DSL, sequential expert, and execution-grounded process reward. | [PDF](https://arxiv.org/abs/2608.29519) |
| `2026` | **aDSL: Agentic 3D Creation via Joint Agent-Program Design** | Co-designs a relational 3D domain-specific language with a Plan-Execute-Critic multi-agent loop that repairs geometry and constraint violations from execution feedback. | [PDF](https://arxiv.org/abs/2608.17975) |
| `2026` | **VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?** | VibeWorlding studies an end-to-end multimodal coding agent that constructs and edits open 3D worlds in a Blender sandbox through asset retrieval, procedural editing, rendered-view feedback, and physical-feasibility checks. | [PDF](https://arxiv.org/abs/2608.15265) |
| `2026` | **WorldClaw: Agentic 3D Open-World Generation at Scale** | WorldClaw builds large editable 3D scenes through region planning, terrain generation, and render-guided refinement. | [PDF](https://arxiv.org/abs/2608.05248) |
| `2026` | **SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation** | A planner-coder-reviewer multi-agent system writes Blender programs for dynamic 4D scenes with fluids, particles, rigid bodies and articulated mechanisms, and checks motion from rendered video. | [PDF](https://arxiv.org/abs/2607.01766) |
| `2026` | **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** | SceneCode builds editable indoor world programs with articulated objects, simulation exports, and persistent scene organization. | [PDF](https://arxiv.org/abs/2605.19587) |
| `2026` | **Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code Synthesis** | Parses top-down room views and synthesizes executable Blender code for 3D indoor geometry, materials and lighting with a structured execution harness and cross-stage memory. | [PDF](https://arxiv.org/abs/2605.18451) |
| `2026` | **SR-Platform: An Agentic Pipeline for Natural Language-Driven Robot Simulation Environment Synthesis** | Turns natural-language descriptions into executable MuJoCo environments through scene planning, CadQuery asset synthesis, constrained layout and MJCF assembly. | [PDF](https://arxiv.org/abs/2605.14700) |
| `2026` | **ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** | ChronoAgentic constructs PyChrono simulation programs using planning, coding, visual review, and trajectory checks. | [PDF](https://arxiv.org/abs/2605.14398) |
| `2026` | **SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning** | A self-evolving coding agent writes and runs Unreal Engine code to build physically grounded embodied environments with verifiable tasks from language or image instructions. | [PDF](https://arxiv.org/abs/2605.09423) |
| `2026` | **Code2Worlds: Empowering Coding LLMs for 4D World Generation** | Code2Worlds generates object and scene programs for 4D simulation, using Blender dynamics and visual motion feedback. | [PDF](https://arxiv.org/abs/2602.11757) |
| `2026` | **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** | An agent couples layout and object generators with critics for semantics, realism and physical stability to produce simulation-ready scenes for embodied tasks at scale. | [PDF](https://arxiv.org/abs/2602.10116) |
| `2026` | **Imagine a City: CityGenAgent for Procedural 3D City Generation** | Generates 3D cities hierarchically as block and building programs from language, trained with supervised fine-tuning and reinforcement learning for valid, aligned programs. | [PDF](https://arxiv.org/abs/2602.05362) |
| `2025` | **Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search** | Studies procedural scene programs and error correction through program search. | [PDF](https://arxiv.org/abs/2510.16147) |
| `2025` | **Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation** | Studies imperative and declarative scene-program representations and program-based error correction. | [PDF](https://arxiv.org/abs/2504.05482) |
| `2024` | **SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements** | SceneMotifCoder learns editable object-arrangement programs from a few visual examples. | [PDF](https://arxiv.org/abs/2408.02211) |
| `2024` | **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code** | SceneCraft translates scene blueprints into Blender code and refines them with rendered visual feedback. | [PDF](https://arxiv.org/abs/2403.01248) |
| `2024` | **Open-Universe Indoor Scene Generation using LLM Program Synthesis and Uncurated Object Databases** | Open-Universe Indoor Scene Generation synthesizes executable layout constraints over uncurated object databases. | [PDF](https://arxiv.org/abs/2403.09675) |
| `2023` | **Holodeck: Language Guided Generation of 3D Embodied AI Environments** | Holodeck builds language-guided 3D embodied environments through spatial constraints and optimization. | [PDF](https://arxiv.org/abs/2312.09067) |
| `2023` | **Infinite Photorealistic Worlds Using Procedural Generation (Infinigen)** | Infinigen provides procedural rules for generating photorealistic geometry and materials at world scale. | [PDF](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html) |
| `2020` | **ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis** | ShapeAssembly represents 3D part structure with hierarchical parametric assembly programs. | [PDF](https://arxiv.org/abs/2009.08026) |
| `2018` | **CSGNet: Neural Shape Parser for Constructive Solid Geometry** | CSGNet parses visual shapes into executable constructive-solid-geometry programs. | [PDF](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html) |
| `2013` | **Procedural content generation for games** | Historical reference on procedural content generation for games; bibliographic metadata reviewed. | [PDF](https://doi.org/10.1145/2422956.2422957) |

[↑ Back to overview](#contents)

<a id="papers-other"></a>
### Other

*Records outside the three primary families: GUI world models and benchmarks.*

<a id="papers-other-gui"></a>
#### GUI World Models (25)

*GUI, web, and computer-use world models, including renderable-code screen predictors. Kept outside the three families.*

<details>
<summary>25 records</summary>

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **Interactive Neural Computers** | Trains an end-to-end desktop world model with surprise-gated slot memory and residual latent rendering to predict post-action screens and recall off-screen files. | [PDF](https://arxiv.org/abs/2611.32811) |
| `2026` | **MKD2World: A Typed Spatial MarkDown World Model For Web Agents** | Serializes desktop web interfaces into Typed Spatial Markdown encoding element types, bounding boxes and control states for action-conditioned next-state prediction in web agents. | [PDF](https://arxiv.org/abs/2611.06544) |
| `2026` | **WebHarbor: Docking Real Websites for Evolving GUI Agent Environments** | Coding agents extend Dockerized replicas of real websites as new tasks arrive. Human contributors check visual fidelity and workflow behavior across 153 environments. | [PDF](https://arxiv.org/abs/2611.03634) |
| `2026` | **Agent World Model in the Wild: Computer-Use Agent Environment Synthesis (WildAWM)** | Synthesizes executable computer-use worlds spanning GUI, MCP and CLI interfaces, with replayable state-building programs and execution-based task/verifier quality gates for agent training. | [PDF](https://arxiv.org/abs/2610.26828) |
| `2026` | **Beyond Next-Screen Prediction: The Decision Value of GUI World Models** | Controls prediction presentation and supervision when comparing GUI lookahead with a directly learned action ranker, testing the incremental decision value of predicted screens. | [PDF](https://arxiv.org/abs/2610.24372) |
| `2026` | **Latent World Action Model for GUI Agents** | Replaces full-screen pixel reconstruction with action-aware contrastive latent transition prediction and joint action selection for GUI agents. | [PDF](https://arxiv.org/abs/2610.14228) |
| `2026` | **Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents** | Studies GUI world models as transition verifiers and separates screen similarity from transition correctness. | [PDF](https://arxiv.org/abs/2610.11942) |
| `2026` | **AutoGUIWorld: Image Generators as Visual World Models for GUI Agent** | AutoGUIWorld synthesizes GUI trajectories by planning visual consequences and iteratively editing screenshots. | [PDF](https://arxiv.org/abs/2610.01215) |
| `2026` | **The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models (StateAliasBench)** | StateAliasBench pairs identical visible GUI conditions with different futures to diagnose hidden transition state. | [PDF](https://arxiv.org/abs/2609.32679) |
| `2026` | **WebWorld: The Browser as a World Model for Self-Improving Web Code** | Uses the browser to execute and verify self-improving web code against interaction contracts and preserved behaviors. | [PDF](https://arxiv.org/abs/2608.30530) |
| `2026` | **GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments** | GUI-CC evaluates multi-step contextual consistency through offline reference actions and online agent loops. | [PDF](https://arxiv.org/abs/2609.00048) |
| `2026` | **AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** | AppDeltaWorld predicts transition-grounded HTML updates with retrieved structure, visual assets, and closed-loop refinement. | [PDF](https://arxiv.org/abs/2608.05891) |
| `2026` | **SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction** | Uses a safety-augmented GUI world model that predicts semantic next states to screen instructions and assess action risk before a mobile agent acts. | [PDF](https://arxiv.org/abs/2607.15550) |
| `2026` | **OpenComputer: Verifiable Software Worlds for Computer-Use Agents** | OpenComputer provides real software environments with structured state verification and auditable task rewards. | [PDF](https://arxiv.org/abs/2605.19769) |
| `2026` | **How Mobile World Model Guides GUI Agents?** | Compares text, image, and renderable-code mobile predictions across reconstruction, online use, and agent-consumption strategies. | [PDF](https://arxiv.org/abs/2605.10347) |
| `2026` | **Computer-Using World Model** | Computer-Using World Model predicts textual changes and then screenshots for desktop software interactions. | [PDF](https://arxiv.org/abs/2602.17365) |
| `2026` | **World-Model-Augmented Web Agents with Action Correction (WAC)** | Couples a web action model with a transition world model and judge to simulate candidate action outcomes and trigger corrective feedback before risky browser execution. | [PDF](https://arxiv.org/abs/2602.15384) |
| `2026` | **WebWorld: A Large-Scale World Model for Web Agent Training** | WebWorld learns a large-scale web simulator for agent training. | [PDF](https://arxiv.org/abs/2602.14721) |
| `2026` | **Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning** | Synthesizes about 1,000 code-driven, database-backed tool environments for agentic reinforcement learning, with more consistent state transitions than LLM-simulated environments. | [PDF](https://arxiv.org/abs/2602.10090) |
| `2026` | **Code2World: A GUI World Model via Renderable Code Generation** | Code2World learns next-GUI code generation with AndroidCode, visual revision, and render-aware learning. | [PDF](https://arxiv.org/abs/2602.09856) |
| `2026` | **Generative Visual Code Mobile World Models (gWorld)** | gWorld predicts mobile GUI observations as renderable web code with a single vision-language model. | [PDF](https://arxiv.org/abs/2602.01576) |
| `2026` | **InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training** | Generates functional multi-page web environments with verifiable task evaluators at scale for training GUI agents. | [PDF](https://arxiv.org/abs/2601.04126) |
| `2026` | **MobileDreamer: Generative Sketch World Model for GUI Agent** | A textual sketch world model forecasts post-action mobile GUI states for lookahead rollouts by a GUI agent. | [PDF](https://arxiv.org/abs/2601.04035) |
| `2025` | **MobileWorldBench: Towards Semantic World Modeling For Mobile Agents** | MobileWorldBench evaluates semantic mobile state transitions and their usefulness for GUI agents. | [PDF](https://arxiv.org/abs/2512.14014) |
| `2025` | **ViMo: A Generative Visual GUI World Model for App Agents** | ViMo models mobile GUI futures through graphic and textual decomposition. | [PDF](https://arxiv.org/abs/2504.13936) |

</details>

<a id="papers-other-benchmark"></a>
#### Benchmarks (37)

*Benchmarks and diagnostic studies, grouped by what they evaluate.*

<details>
<summary>37 records</summary>

**Evaluating state-level dynamics (WorldCoder-type)**

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning** | Evaluates formal models generated as partially observable stochastic games on 44 scenarios. Mechanical checks, structural agreement and semantic judgments test different aspects of fidelity. | [PDF](https://arxiv.org/abs/2611.14419) |
| `2026` | **GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations** | Tests textual action-conditioned successor predictions against execution-derived references, combining deterministic checks with semantic judging. | [PDF](https://arxiv.org/abs/2610.22708) |
| `2026` | **GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions** | GameLogicBench checks Godot game rules at every simulation tick across varied reproducible scenarios. | [PDF](https://arxiv.org/abs/2609.21562) |
| `2026` | **ScratchWorld: Evaluating If World Models Compute Executable Consequences** | ScratchWorld uses replay-verified Scratch transitions and changed-field metrics to evaluate executable consequences. | [PDF](https://arxiv.org/abs/2606.31689) |
| `2025` | **Benchmarking World-Model Learning with Environment-Level Queries (WorldTest)** | Proposes evaluating learned world models with environment-level queries (reachability, counterfactual effects) after reward-free exploration, instantiated as AutumnBench with 43 interactive grid-world environments. | [PDF](https://arxiv.org/abs/2510.19788) |
| `2025` | **Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** | Text2World evaluates text-to-PDDL world-model generation with diverse domains and execution-based criteria. | [PDF](https://arxiv.org/abs/2502.13092) |

**Evaluating program-to-video rendering (Code-as-World-type)**

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **WorldDraft: If Code Builds the World, Can Video Models Just Render It?** | Across 432 paired cases from 48 executable 4D world families, varies proxy detail and appearance cues while holding dynamics fixed. Scores motion and camera preservation separately from target appearance. | [PDF](https://arxiv.org/abs/2611.16217) |
| `2026` | **VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation** | Evaluates multimodal coding agents on 239 sandbox tasks that synthesize complete videos and audio purely in code, scored via specification checks and ~13k requirement rubrics. | [PDF](https://arxiv.org/abs/2610.35864) |
| `2026` | **Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V** | Benchmarks executable-program video creation from text, images and videos with objective and model-judged measures of execution, quality and alignment. | [PDF](https://arxiv.org/abs/2610.28416) |
| `2026` | **RenderBench: Benchmarking Render-to-Real Video Transfer with Reconstructed Digital Twins** | Pairs reconstructed editable 3D digital twins and proxy renders with real target videos across static and dynamic scenes to benchmark render-to-real structural and appearance fidelity. | [PDF](https://arxiv.org/abs/2610.08684) |
| `2026` | **PROWBench: Do Video Models Render What the Program Specifies?** | PROWBench compares rendered video events with executable program specifications and event logs. | [PDF](https://arxiv.org/abs/2610.02205) |
| `2026` | **Proxy2World: Learning to Generate Worlds From Lightweight Proxies without Seeing Them** | Learns proxy-conditioned world generation from posed RGBD videos via cross-modal flow matching and introduces ProxyBench to evaluate structural adherence across scenes and motions. | [PDF](https://arxiv.org/abs/2609.35023) |

**Evaluating 3D world construction (VibeWorlding-type)**

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **VeriWorld: A Verifiable Visual SWE-Bench for Spatial Reasoning in 3D Environments** | Evaluates spatial reasoning in interactive 3D environments with executable actions and deterministic verification across matched visual, structured and combined input channels. | [PDF](https://arxiv.org/abs/2611.30226) |
| `2026` | **3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest extreme Long-Horizon Browser Games** | Benchmarks coding agents on 108 long-horizon from-scratch 3D browser game tasks across 14 genres using functional code acceptance, agent playtesting and blind human preference. | [PDF](https://arxiv.org/abs/2611.24073) |
| `2026` | **OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation** | Evaluates generated HTML5 games against 1,800 requirements across 180 tasks. Static source inspection scores specified features and deeper relationships among game systems. | [PDF](https://arxiv.org/abs/2611.17681) |
| `2026` | **VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender** | Tests executable Blender scenes on 242 briefs. Scene Check reruns code against hidden 4D facts, and Screen Check judges whether the verified facts are visible in the rendered preview. | [PDF](https://arxiv.org/abs/2611.15789) |
| `2026` | **Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds** | Evaluates coding agents on 145 object, scene and interactive-world tasks. Open-world tests distinguish working local mechanisms from activities requiring clearance and persistent state. | [PDF](https://arxiv.org/abs/2611.09017) |
| `2026` | **3DCodeEdit: Benchmarking Instruction-Guided 3D Program Editing** | Benchmarks instruction-guided edits to Blender programs and uses render-based checklists to expose geometric-foresight failures. | [PDF](https://arxiv.org/abs/2610.38231) |
| `2026` | **UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity** | Evaluates coding agents on Unity projects with deterministic milestone tests over scene structure, component configuration, and runtime behavior. | [PDF](https://arxiv.org/abs/2610.35980) |
| `2026` | **BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References** | Evaluates agent-created Blender projects against multimodal briefs using rendered views, task rubrics and visual-quality judgments. | [PDF](https://arxiv.org/abs/2610.23986) |
| `2026` | **ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling** | Evaluates individual mechanisms, compositional mechanical systems, and intent-driven executable 3D world synthesis. | [PDF](https://arxiv.org/abs/2610.15166) |
| `2026` | **WorldBench: Evaluating LLMs on Three.js Voxel World Generation** | Benchmarks LLM-written Three.js voxel worlds with a judge that both explores the running world and reads the code, counting evidence only when the two agree. | [PDF](https://arxiv.org/abs/2610.10622) |
| `2026` | **Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos** | Video2World evaluates video-to-interactive-world reconstruction through geometry, dynamics, and function. | [PDF](https://arxiv.org/abs/2610.04432) |
| `2026` | **Spec2Game: Can LLMs Generate Complete Playable Games from Detailed Specifications?** | Benchmarks generating complete Pygame projects from detailed game specifications with controlled rule variants, separating executability from faithful rule realization. | [PDF](https://arxiv.org/abs/2610.04253) |
| `2026` | **Code4Scene: Benchmarking Coding Agents for Constructing and Editing 3D Scenes** | Evaluates coding agents on 170 Unreal Engine 3D scene construction and state-preserving editing tasks by inspecting engine-native scene fulfillment, integrity and static physical validity. | [PDF](https://arxiv.org/abs/2609.36777) |
| `2026` | **WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis** | WorldCoder-Bench tests physically grounded 3D world synthesis using hidden runtime behavior contracts. | [PDF](https://arxiv.org/abs/2606.01869) |
| `2026` | **VoxelCodeBench: Benchmarking 3D World Modeling Through Code Generation** | Executes generated voxel-manipulation code in Unreal Engine to benchmark symbolic interpretation, geometric construction and multi-object spatial composition beyond syntax validity. | [PDF](https://arxiv.org/abs/2604.02580) |

**Evaluating non-code video and learned world models**

| Year | Paper | Summary | Link |
|---|---|---|:-:|
| `2026` | **StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model** | Evaluates interactive video world models against pre-motion ground-truth start geometry and calibrated per-action camera strides, exposing severe scene deformation under free-scale baselines. | [PDF](https://arxiv.org/abs/2611.24408) |
| `2026` | **The Flip Test: Video World Models Fail to Learn the World State (FlipTest)** | Uses near-identical initial frames, matched controls and dense parameter sweeps to test whether video predictions change at the physical boundary where an outcome flips. | [PDF](https://arxiv.org/abs/2611.19822) |
| `2026` | **WorldProbe: When Video World Models Fall Apart under Long-Horizon Spatial Exploration** | Uses a goal-conditioned agent to adapt camera actions online and probe long-horizon spatial consistency in video world models. | [PDF](https://arxiv.org/abs/2610.39721) |
| `2026` | **WMEval: Evaluating Interactive World Models Grounded on Physical Simulations** | Uses Unity physical simulations as ground-truth oracles to compare interactive world-model trajectories at perceptual and state/causal levels. | [PDF](https://arxiv.org/abs/2610.33894) |
| `2026` | **Events, Not Pixels: Where World Models Get the Return Wrong** | Diagnoses return errors by replacing selected imagined transitions with real ones under matched budgets; reward/terminal events matter more than visually poor frames for the tested models. | [PDF](https://arxiv.org/abs/2610.29435) |
| `2026` | **Execution Before Memory: Diagnosing Memory Failures in Video World Models** | Introduces MIST to separate whether an instructed hidden change was executed from whether a video world model remembers it later, showing execution failure often masquerades as forgetting. | [PDF](https://arxiv.org/abs/2610.23542) |
| `2026` | **WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions** | Evaluates action-conditioned robot world-model rollouts against paired physical executions across state correctness, spatial alignment, local interaction fidelity and multiview coherence. | [PDF](https://arxiv.org/abs/2610.18826) |
| `2026` | **Can Video World Models Track Unobserved World States? (Visual Shell Game)** | Uses an action-conditioned video Shell Game and S_5 swap-tracking analysis to test whether video world models maintain revisable unobserved world states across long swap chains. | [PDF](https://arxiv.org/abs/2608.30692) |
| `2026` | **Current World Models Lack a Persistent State Core (WRBench)** | Treats camera lookaway as an observability intervention across 9,600 videos from 23 models to test whether unobserved events keep evolving rather than freezing until revisited. | [PDF](https://arxiv.org/abs/2606.20545) |
| `2025` | **WorldModelBench: Judging Video Generation Models As World Models** | WorldModelBench evaluates video world models using instruction adherence, physical plausibility, and human preferences. | [PDF](https://arxiv.org/abs/2502.20694) |

</details>

[↑ Back to overview](#contents)

<!-- CATALOG:END -->

<a id="related-surveys"></a>
## Related surveys & how we differ

<!-- RELATED:BEGIN -->

Related surveys centre on video models or world models in general. This survey takes **executable code as the substrate of the world** as its inclusion criterion and organises the literature by how much of the world code carries (state only / whitebox + generative rendering / full 3D); video models appear only as optional renderers.

<details>
<summary><strong>Compare with 13 related surveys</strong></summary>

| Year | Survey | How We Differ | Link |
|---|---|---|:-:|
| `2026` | **Video Models as Generative Renderers: Foundations, Interfaces, Systems, and Beyond** | It centers on the video renderer along a T0–T3b conditioning specification ladder, where code engines are one upstream proxy source among traditional G-buffers and neural states. Our survey centers on executable code as the world substrate—spanning state-only dynamics (01), proxy+renderer worlds (02) and full 3D engine code (03)—and uses L0–L4 to separate upstream state ownership. | [Project](https://genrender-hub.github.io/) |
| `2026` | **Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement** | It surveys agent harnesses built around video generation models, covering video production, interactive world modeling and recursive self-improvement, so the video model is the centre and code is one harness component. Here code is the world substrate: it carries state and rules, a whitebox world, or the full 3D world, and a video model is only one possible renderer. | [PDF](https://arxiv.org/abs/2610.40191) |
| `2026` | **Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence** | It studies self-evolving physical coding agents that pair Code as Policy with Code as World for robotic execution. Our survey systematically develops Code as World itself across state induction, generative proxy rendering and 3D world construction. | [PDF](https://arxiv.org/abs/2609.35432) |
| `2026` | **AI for Games in the Foundation Model Era** | It covers games broadly, including learned game-world models and AI-assisted development. Here games are one domain among several, and the focus is on game rules and worlds written as executable code. | [PDF](https://arxiv.org/abs/2609.16679) |
| `2026` | **Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence** | It maps evaluation benchmarks for predictive embodied world models versus direct VLA policies. Here robotics is one validation domain, and the focus is on executable world programs, persistent state and counterfactual verifiability. | [PDF](https://arxiv.org/abs/2609.29669) |
| `2026` | **From Generation to Simulation: How Far Are World Models from Being True Simulators?** | It asks how far latent, video and joint-embedding world models are from simulators. Code world models take the opposite route: they start from an executable simulator-like substrate with explicit state, and this survey studies how that substrate is induced, built and rendered. | [PDF](https://arxiv.org/abs/2608.23070) |
| `2026` | **From Pixels to States: Rethinking Interactive World Models as Game Engines** | It argues that video world models should recover the explicit state loop of game engines. Code-as-World methods keep that loop in executable code and use video models only to render it; this survey compares how much of the loop code owns. | [PDF](https://arxiv.org/abs/2607.14076) |
| `2026` | **Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application** | It treats environments as training infrastructure for agents. Here an environment matters only when its code acts as a world model, predicting or simulating how the world evolves; benchmarks and synthetic task environments are secondary. | [PDF](https://arxiv.org/abs/2606.12191) |
| `2026` | **Bridging the Agent-World Gap: Text World Models for LLM-based Agents** | It covers textual environments and treats code-as-world-model as one construction paradigm. Here code-as-world is the subject itself, extended from text and symbolic states to whitebox worlds with generative rendering and full 3D worlds. | [PDF](https://arxiv.org/abs/2606.09032) |
| `2026` | **Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends** | It centers on action-conditioned video and 3D generative world models. Here executable code is the world substrate, and video generators appear as optional state-conditioned renderers. | [PDF](https://arxiv.org/abs/2606.01164) |
| `2026` | **World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications** | It surveys broad learned world models along architecture, method family, reasoning strategy and domain. Our survey focuses specifically on world models where executable code carries world state, rules or 3D structure. | [PDF](https://arxiv.org/abs/2606.00133) |
| `2026` | **Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond** | It organizes world models by capability level and law regime across 400+ works, with code-based models as one implementation among many. Here the organizing question is what executable code carries in the world, and only methods where code is the world substrate are included. | [PDF](https://arxiv.org/abs/2604.22748) |
| `2025` | **LLMs as Planning Formalizers: A Survey for Leveraging Large Language Models to Construct Automated Planning Models** | It covers one corner of the WorldCoder-type line: symbolic planning models written from language. Here such models sit alongside Python transition programs, physical residuals, generatively rendered code worlds and 3D world programs. | [PDF](https://arxiv.org/abs/2503.18971) |

</details>

<!-- RELATED:END -->

<a id="contributing"></a>
## Contributing & Contact

We welcome paper suggestions, metadata corrections, benchmark additions, and research collaborations.

- **Add or update papers:** Follow the [contribution guide](CONTRIBUTING.md) or [open an issue](https://github.com/FreedomIntelligence/Awesome-Code-World-Model/issues/new).
- **Collaborations & inquiries:** Feel free to reach out to [@YihDu](https://github.com/YihDu) and [@MichaelCao0](https://github.com/MichaelCao0).

<details>
<summary><strong>Maintainer notes: local build &amp; source policy</strong></summary>

The collection is generated from [data/papers.json](data/papers.json). To regenerate and validate locally:

```bash
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

Records link to primary arXiv, DOI, or official proceedings pages. Paper titles and method aliases are stored separately. Dates follow the source metadata; conference years may differ. Review depth and paper-specific experimental conditions are available in the [annotated catalogue](docs/catalogue.md) and [review protocol](docs/review-protocol.md).

| Similar names | Distinction |
|---|---|
| Code2World / Code2Worlds | GUI observation prediction / 4D simulation generation |
| Web World Models / WebWorld | Code-defined persistent worlds / learned web simulation / browser-based code verification; three separate sources |
| WorldCoder / WorldCoder-Bench | Model-based agent / 3D world-synthesis benchmark |
| TheoryCoder / TheoryCoder-2 | Method aliases; their exact publication titles are retained in the bibliography |
| OneLife / General Game Playing | Stochastic dynamics from exploration / executable models from game rules and trajectories |
| FAIR CWM | Neural modeling of computational execution and code generation |

Related preprints are linked in the structured data. Counts describe bibliographic source records, with core methods, historical lineage, enabling representations, benchmarks, and comparators labeled in the annotated catalogue.

</details>

<a id="about-this-initiative"></a>
## About This Initiative

This repository is part of an ongoing research initiative on Code World Models, bringing together researchers interested in executable world representations, programmable dynamics, and interactive world generation.

We aim to contribute a series of open research efforts, including surveys, benchmarks, and new modeling approaches, and welcome discussions and collaborations with the broader research community.

<a id="acknowledgements"></a>
## Acknowledgements

We gratefully acknowledge [Yankai Chen](https://yankai-chen.github.io/) for guidance and support of this research initiative.

<p align="center"><a href="#code-world-models">Back to top ↑</a></p>
