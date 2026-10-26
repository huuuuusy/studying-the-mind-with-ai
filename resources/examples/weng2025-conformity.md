**English** · [中文](weng2025-conformity.zh.md)

# Asch's experiment with language-model agents

**Study.** Weng, Z., Chen, G., & Wang, W. (2025). Do as we do, not as you think: The conformity of large language models. *International Conference on Learning Representations (ICLR 2025)*, oral. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1da9ca7e9cef4b1af63913f05d1630a4-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2501.13381)

**In the talk.** A backup page for questions, with [Part 3, A society: people we make](../../docs/part3-people-we-make.md): an Asch-style test for AI agents, and Asch's own controls.

**Question.** When language-model agents work together, do they conform to a majority the way people do in Asch's experiments, and what makes them conform more or less?

**Method.** BenchForm is a benchmark of reasoning-intensive tasks with five interaction protocols. In the main setting, the tested agent answers after six other agents. Some protocols follow Asch's design: the other agents give the same answer, and the tested agent is not told whether answers are correct. Two metrics measure the effect: a conformity rate and an independence rate. The authors then varied the length of the earlier interaction and the size of the majority, asked the tested agents to explain themselves, and tried two remedies: an "empowered" persona and a reflection step.

**Finding.**
1. Conformity exists in multi-agent systems built on language models, and it can substantially affect their performance.
2. Its degree depends both on the model and on the setting: with more rounds of earlier discussion, conformity increases, and a larger majority produces more conformity.
3. Both remedies show promise in reducing conformity.

**Why read it.** It takes one of psychology's best-known experiments and runs it, with its logic intact, on artificial agents. It shows how a classic paradigm becomes a test for AI.

**Limits.** That agents conform on reasoning tasks does not show that they conform for the reasons people do. A matching behaviour is not a matching mechanism. Comparing the agents with human data on the same tasks would be the next step.

**Data and code.** [github.com/Zhiyuan-Weng/BenchForm](https://github.com/Zhiyuan-Weng/BenchForm) (MIT).
