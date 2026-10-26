**English** · [中文](serapio2025-personality.zh.md)

# Measuring and shaping a model's personality, psychometrically

**Study.** Serapio-García, G., Safdari, M., Crepy, C., Sun, L., Fitz, S., Romero, P., Abdulhai, M., Faust, A., & Matarić, M. (2025). A psychometric framework for evaluating and shaping personality traits in large language models. *Nature Machine Intelligence, 7*(12), 1954–1968. [doi:10.1038/s42256-025-01115-6](https://doi.org/10.1038/s42256-025-01115-6) · [arXiv](https://arxiv.org/abs/2307.00184) (earlier arXiv version, 2023: *Personality traits in large language models*)

**In the talk.** Part 3, [A society: people we make](../../docs/part3-people-we-make.md), the page "A persona is a manipulation" sets out the check, and a backup page, "A persona check that passed", shows this study's result: each Big Five trait prompted on its own, from low to high; mainly the trait that was prompted moved, so the check can pass.

**Question.** When a language model answers a personality test, are the scores reliable and valid in the sense psychology requires of human tests? And can a model's personality be shaped deliberately?

**Method.** Established personality inventories were given to 18 language models under many prompt set-ups (different wordings and framings of the instructions). The scores were then examined with the standard psychometric criteria used for human tests: reliability, and validity against other measures. The method was also used in reverse: instructions set traits to target levels, and the authors checked whether text generated afterwards expressed those levels.

**Finding.**
1. For some models, under specific prompt set-ups, personality measurements are reliable and valid.
2. The evidence for reliability and validity is stronger for larger models and for models further trained to follow instructions.
3. Personality in a model's output can be shaped along desired dimensions to mimic specific human personality profiles.

**Why read it.** It brings the full toolkit of psychometrics to model personas: a persona is treated as something to be measured and validated, not taken at face value. It is a model of what a manipulation check on a persona looks like.

**Limits.** The questionnaire is the first check, and it is the one the talk showed. A model that scores as extraverted after being told to be extraverted may be following the instruction rather than having a trait, so behaviour that the persona did not name is a stronger test. The authors also discuss the ethical risks of shaping personality.

**Data and code.** See the article for code and data availability.
