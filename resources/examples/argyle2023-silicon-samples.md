**English** · [中文](argyle2023-silicon-samples.zh.md)

# Out of one, many: silicon samples

**Study.** Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J., Rytting, C., & Wingate, D. (2023). Out of one, many: Using language models to simulate human samples. *Political Analysis, 31*(3), 337–351. [doi:10.1017/pan.2023.2](https://doi.org/10.1017/pan.2023.2) · [arXiv](https://arxiv.org/abs/2209.06899)

**In the talk.** A backup page for questions in Part 4, [AI in your own research](../../docs/part4-ai-in-your-research.md), "Can AI play the participant?": silicon samples answer like each subgroup, so they can pretest a study but not replace the sample. Its key-reading entry is in [Part 3, A society: people we make](../../docs/part3-people-we-make.md).

**Question.** Can a language model take the place of specific groups of people in social science research, for example by answering a survey as a person with a given background would?

**Method.** The authors gave GPT-3 thousands of sociodemographic backstories taken from real participants in several large surveys conducted in the United States, and asked it to answer as each person would (*conditioning* the model, in AI terms). The resulting "silicon samples" answered the same survey questions, and their answers were compared with those of the real participants who had the same backgrounds.

**Finding.** The biases in GPT-3 are not one uniform property. They are fine-grained and correlated with demographics, so that suitable backstories make the model reproduce the response distributions of many human subgroups. The authors call this *algorithmic fidelity*. They argue that a model with enough of it can be a tool for studying people and society.

**Why read it.** It introduced the idea of the silicon sample and a criterion for it. Much of the later debate is about where algorithmic fidelity holds and where it fails.

**Limits.** The comparison is with American survey respondents on the questions studied. Later work finds that silicon samples can misrepresent and flatten identity groups, for example Wang et al. (2025, *Nature Machine Intelligence*, [doi](https://doi.org/10.1038/s42256-025-00986-z)), and that synthetic survey data can mislead, for example Bisbee et al. (2024, *Political Analysis*, [doi](https://doi.org/10.1017/pan.2024.5)).

**Data and code.** The human data come from large public U.S. surveys; see the article page for replication materials.
