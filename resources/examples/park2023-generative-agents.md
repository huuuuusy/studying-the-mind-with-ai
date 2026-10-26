**English** · [中文](park2023-generative-agents.zh.md)

# A town of twenty-five generative agents

**Study.** Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)*, 1–22. [doi:10.1145/3586183.3606763](https://doi.org/10.1145/3586183.3606763) · [arXiv](https://arxiv.org/abs/2304.03442)

**In the talk.** Part 3, [A society: people we make](../../docs/part3-people-we-make.md), the page "Smallville: a town of language-model agents": a simulated town of agents built on a language model, and how believable each part of their minds made them.

**Question.** Can a large language model, given memory and the ability to plan, produce believable everyday human behaviour, alone and in a group?

**Method.** Each generative agent stores a complete record of its experiences in natural language. Over time it condenses these memories into higher-level reflections, and it retrieves them to plan what to do next. Twenty-five agents live in a small simulated town, like a game world, inspired by *The Sims*, and users can talk to them. A hundred people rated how believable the agents were. The authors also built reduced versions, taking the parts away one after another: first reflection, then planning as well, then memory (observation) too. People playing the same roles were a further comparison.

**Finding.** The agents produced believable individual and emergent social behaviour. In one run, a single user-specified idea, that one agent wants to throw a Valentine's Day party, led the agents over the next two days to spread invitations, make new acquaintances, ask each other out to the party, and arrive together at the right time. Each part made the agents more believable. The full agents scored 29.9; without reflection, 26.9; without reflection or planning, 25.6; with no memory, reflection or planning, 21.2. People playing the same roles scored 23, below the full agents.

**Why read it.** It is the study that made simulated people with language models a field. It also shows the criterion such simulations are usually judged by: believability.

**Limits.** Believable is not the same as accurate. The study shows that the behaviour looks human to observers; it does not compare the agents with how real people in a real town behave. Comparing simulated people with the real people they are meant to resemble would close this gap; the same team took that step next, with [1,052 people](park2024-simulating-1000-people.md).

**Data and code.** [github.com/joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) (Apache-2.0).
