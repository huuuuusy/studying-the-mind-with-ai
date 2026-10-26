**English** · [中文](uma2021-learning-from-disagreement.zh.md)

# When people disagree, learn from the disagreement

**Study.** Uma, A. N., Fornaciari, T., Hovy, D., Paun, S., Plank, B., & Poesio, M. (2021). Learning from disagreement: A survey. *Journal of Artificial Intelligence Research, 72*, 1385–1470. [doi:10.1613/jair.1.12752](https://doi.org/10.1613/jair.1.12752) (open access)

**In the talk.** Not shown; read it with Part 2, [A group: people as the answer](../../docs/part2-people-as-the-answer.md): one label, or a majority vote, hides how much people disagree.

**Question.** Most of AI still assumes one correct ("gold") answer for every item. What happens if we take seriously that people disagree, and train and evaluate models on all their judgements?

**Method.** A survey that also runs its own experiments. It reviews the evidence for disagreement in language and vision tasks, from objective ones such as part-of-speech tagging (marking each word as a noun, verb and so on) to subjective ones. It then trains the most common approaches on every available data set with multiple judgements per item, and evaluates the resulting models in several ways.

**Finding.**
1. Even without a single gold standard, the field must agree on how to evaluate models, because the ranking of training methods depends on the evaluation chosen.
2. Results depend strongly on the data set. Soft labels keep the share of people who chose each answer; a gold label keeps one answer. With substantial data sets, which give many judgements by high-quality coders for each item, training directly on soft labels did better than training on combined or even gold labels. This held both when models were scored against one answer (hard evaluation) and against the spread of answers (soft evaluation).
3. When those conditions do not hold, combining gold and soft labels generally did best in hard evaluation.

**Why read it.** It is the entry point to a whole research area that treats the spread among people as information. It is also a map of the data sets that make this possible.

**Limits.** The survey covers language and vision tasks up to 2021; large language models as raters came later (see the [wider landscape](../../docs/part2-people-as-the-answer.md#the-wider-landscape)).

**Data and code.** All data sets and models used in the paper are freely available as supplementary materials.
