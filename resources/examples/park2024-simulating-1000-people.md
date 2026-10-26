**English** · [中文](park2024-simulating-1000-people.zh.md)

# One agent for each of 1,052 people

**Study.** Park, J. S., Zou, C. Q., Kamphorst, J., Egan, N., Shaw, A., Hill, B. M., Cai, C., Morris, M. R., Liang, P., Willer, R., & Bernstein, M. S. (2024). LLM agents grounded in self-reports enable general-purpose simulation of individuals. *arXiv:2411.10109* (current version v3, 2026; first posted as "Generative agent simulations of 1,000 people"). [arXiv](https://arxiv.org/abs/2411.10109)

**In the talk.** Part 3, [A society: people we make](../../docs/part3-people-we-make.md), the page "From 25 agents to 1,052 people": an agent built from each person's own interview, judged against the same person, measured twice.

**Question.** Can a language model, given what one real person has said about themselves, predict how that person answers surveys and makes choices, across many different tasks?

**Method.** A stratified sample of 1,052 Americans each had a two-hour voice interview with an AI interviewer (the American Voices Project protocol), then completed the core General Social Survey (GSS), the Big Five Inventory, five economic games and five published experiments, twice, two weeks apart. Agents built on GPT-4o were given the interview, the person's survey answers, or both, and compared with agents given only demographics or a short persona. Normalised accuracy divides how often an agent matches its person by how often the person matches their own earlier answers.

**Finding.** On GSS items that were not part of what the agents were given, interview agents gave their person's answer 65.67% of the time; people repeated their own answer 79.53% of the time: a normalised accuracy of 0.83. Survey agents reached 0.82, both sources 0.86, demographics only 0.74. Self-report agents also generally narrowed accuracy gaps across racial and ideological groups. These figures are from the current version (v3, June 2026); the first version, with an earlier analysis, reported 0.85 and 0.71.

**Why read it.** It changes what a simulated person is judged against: not whether it looks human, but whether it matches the same person, measured twice. People's own two-week consistency becomes the ceiling.

**Limits.** Matching individuals is not reproducing how attitudes go together across a sample, as the authors note. In the economic games, no agent type beat demographics alone significantly. In the five experiments, agents' effect sizes were larger than people's, though closely correlated; five studies are too few to say more. One model family, English only, U.S. participants.

**Data and code.** [github.com/joonspk-research/generative_agent](https://github.com/joonspk-research/generative_agent) (MIT): code for interview agents and the AI interviewer, demographic agents built from GSS data, and one example agent of an author. Replication materials: [osf.io/t6g7k](https://osf.io/t6g7k/). The 1,052 agents are not public, to protect participants. The paper offers open access to aggregated responses on the fixed surveys; the repository says researchers can apply for restricted access to individual agents' responses, after a review.
