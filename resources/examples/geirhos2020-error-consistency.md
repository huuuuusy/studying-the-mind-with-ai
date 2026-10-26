**English** · [中文](geirhos2020-error-consistency.zh.md)

# Close scores, different mistakes: error consistency

**Study.** Geirhos, R., Meding, K., & Wichmann, F. A. (2020). Beyond accuracy: Quantifying trial-by-trial behaviour of CNNs and humans by measuring error consistency. *Advances in Neural Information Processing Systems (NeurIPS) 33*. [Proceedings](https://proceedings.neurips.cc/paper/2020/hash/9f6992966d4c363ea0162a056cb45fe5-Abstract.html) · [arXiv](https://arxiv.org/abs/2006.16736)

**In the talk.** Part 1, [One person: people next to the machine](../../docs/part1-people-next-to-machine.md): two systems with similar scores that fail on different items. On one set of images, error consistency was 0.33 between people and only 0.07 between networks and people.

**Question.** Do two decision makers, whether brains or algorithms, use the same strategy? Accuracy alone cannot tell, because two systems can reach the same accuracy with very different strategies. That problem is sharpest when both are near ceiling, as networks and people are on object recognition.

**Method.** *Trial-by-trial error consistency.* For every trial, record whether each decision maker was right or wrong, and ask how often they are wrong on the same trials. Compare that with how often they would coincide by chance given their two accuracies. The index is Cohen's κ applied to right and wrong. It can compare model with model, person with person, and model with person. Making consistent errors trial by trial is a *necessary* condition for a similar strategy.

**Finding.** On object recognition, networks of any architecture are remarkably consistent with one another. Their consistency with human observers is little above chance, so people and networks probably use very different strategies. CORnet-S, a model with loops that feed signals back (recurrent), described as the current best model of the primate brain's object-recognition pathway, behaves essentially like a standard image network in which signals pass only one way (feedforward ResNet-50) in this analysis.

**Why read it.** It turns a vague claim ("the model processes images like people do") into a test that can fail. It also uses a statistic that psychology students already know, Cohen's κ, so the method is easy to transfer to other tasks.

**Limits.** Consistent errors are necessary for a shared strategy but not sufficient. A high κ does not show that the processes are the same, and a low κ alone does not identify which shortcut the model uses. Read κ against the consistency among people, not against an ideal of 1.

**Data and code.** Analysis code: [github.com/wichmann-lab/error-consistency](https://github.com/wichmann-lab/error-consistency); the repository does not state a licence. The human data used in later work are part of [model-vs-human](geirhos2021-partial-success.md).
