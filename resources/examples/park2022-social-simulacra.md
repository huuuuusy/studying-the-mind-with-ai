**English** · [中文](park2022-social-simulacra.zh.md)

# Social simulacra: a community populated before it opens

**Study.** Park, J. S., Popowski, L., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2022). Social simulacra: Creating populated prototypes for social computing systems. *Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology (UIST '22)*, 1–18. [doi:10.1145/3526113.3545616](https://doi.org/10.1145/3526113.3545616) · [arXiv](https://arxiv.org/abs/2208.04024)

**In the talk.** Part 3, [A society: people we make](../../docs/part3-people-we-make.md), the page "Where Smallville came from": before Smallville, the same team let a language model play the users of an online community that did not exist yet.

**Question.** A new online community is tried out with a small group, but many problems, such as trolling, appear only at a larger scale. Can a designer see how a community might behave when populated, and change the design before it opens?

**Method.** The designer describes the community in plain language: its goal, its rules and a few member personas. A chain of prompts to GPT-3, each building on the answer to the last, expands these into thousands of members and generate their posts and replies, including anti-social behaviour. The tool, SimReddit, also answers "what if?" questions, such as how a thread goes on if a moderator steps in. The authors regenerated 50 subreddits (discussion groups on Reddit) created after GPT-3's release from their goals and rules alone, and asked 200 participants (50 per condition) to pick the real conversation from pairs of one real and one generated. Other conditions used conversations written by crowd workers or reduced versions of the system. Separately, 16 social computing designers used the tool to design a new community.

**Finding.** Participants misidentified on average 41% (SD = 10) of the pairs; guessing at random gives 50%. Crowd workers' conversations were easier to spot (32%, SD = 13), as were generations without the community description or the personas. The designers met uses and harms they had not anticipated, and revised their rules.

**Why read it.** It is where Smallville came from: a design need for many different test users, on demand. It also set an early criterion for simulated people: can people tell generated behaviour from real behaviour?

**Limits.** Telling real from generated tests plausibility, not accuracy. A thread can look real without matching how that community would develop, and the authors say social simulacra cannot predict this; they show a range of possible outcomes. The evaluation used Reddit, English, participants in the United States, and the 2020 GPT-3 model, before it was trained to follow instructions.

**Data and code.** The project page shows generated example communities: [social-simulacra.herokuapp.com](https://social-simulacra.herokuapp.com/). No code repository is linked; the paper describes the prompts.
