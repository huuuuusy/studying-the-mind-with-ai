**English** · [中文](ouyang2022-human-feedback.zh.md)

# A chat model's training rests on people's comparisons

**Study.** Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., et al. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems (NeurIPS) 35*. [doi:10.52202/068431-2011](https://doi.org/10.52202/068431-2011) · [arXiv](https://arxiv.org/abs/2203.02155)

**In the talk.** Part 2, [A group: people as the answer](../../docs/part2-people-as-the-answer.md): ChatGPT's training and its rankings rest on people's paired comparisons.

**Question.** Can a language model be made to follow what users intend by training it on human judgements, rather than by making it bigger?

**Method.** Labellers (raters, in psychology's terms) wrote demonstrations of the desired behaviour for a set of prompts, and GPT-3 was fine-tuned on them, that is, trained a little further on these examples. Labellers then ranked several model outputs for the same prompt. These rankings trained a reward model, a scoring model that gives each answer one score. The language model was then trained to raise that score, a method called reinforcement learning from human feedback (RLHF). The resulting models are called InstructGPT. They were evaluated by asking people which outputs they prefer.

**Finding.** On the authors' prompt distribution, people preferred the outputs of a 1.3-billion-parameter InstructGPT model to those of the 175-billion-parameter GPT-3, a model with over 100 times more parameters (the numbers a model adjusts as it learns). InstructGPT also improved on truthfulness and produced less toxic output. The paper also reports how much the labellers agreed with each other: training labellers agreed with each other about 73% of the time (72.6 ± 1.5%).

**Why read it.** It shows that the "reference" for today's chat models is a group of people making comparisons, and that this group disagrees about a quarter of the time. Whose judgements are used, and how their disagreement is handled, is a measurement question.

**Limits.** The authors note that the model is aligned to, that is, made to follow, the preferences of a particular group: their labellers, who were mostly English-speaking people living in the United States or Southeast Asia, and to the researchers' own instructions. It is not aligned to people in general.

**Data and code.** The labellers' demonstrations and rankings were not released with the paper.
