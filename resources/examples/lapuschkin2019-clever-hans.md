**English** · [中文](lapuschkin2019-clever-hans.zh.md)

# A right answer found in the wrong place: Clever Hans predictors

**Study.** Lapuschkin, S., Wäldchen, S., Binder, A., Montavon, G., Samek, W., & Müller, K.-R. (2019). Unmasking Clever Hans predictors and assessing what machines really learn. *Nature Communications, 10*, 1096. [doi:10.1038/s41467-019-08987-4](https://doi.org/10.1038/s41467-019-08987-4) (open access) · [arXiv](https://arxiv.org/abs/1902.10178)

**In the talk.** Part 1, [One person: people next to the machine](../../docs/part1-people-next-to-machine.md): Clever Hans, the horse that seemed to count but was reading tiny, unintended movements of its questioner's head, and AI's own Clever Hans, a model that recognised horses by a source tag on the photos.

**Question.** When a learning machine reaches high accuracy, has it solved the task it was built for, or found an easier cue in the data?

**Method.** Explanation methods show which parts of an input a model relied on for each decision. Spectral Relevance Analysis (SpRAy), proposed in the paper, groups these explanations across many inputs, so that whole strategies become visible rather than single cases. The decisive test is the same one Oskar Pfungst used on Clever Hans in 1904 (his report appeared in English in 1911): remove the suspected cue and see whether the answer survives, then add the cue where it does not belong and see whether the answer follows it.

**Finding.** An image classifier (a Fisher vector classifier, an older, pre-deep-learning kind) trained on PASCAL VOC 2007, a public photo collection, recognised horses by a source tag that appears in about one-fifth of the horse images. Removing the tag removed the ability to classify the picture as a horse, and adding the tag to a car image changed its classification. Across tasks from computer vision and arcade games, the paper finds strategies ranging from naive and short-sighted to well-informed and strategic. Standard performance metrics can be blind to these differences.

**Why read it.** It is the modern Clever Hans case, and it shows the experimental logic that psychology already has: a manipulation that removes the cue is a control condition.

**Limits.** Explanation maps are themselves measurements and need their own validation. A map that points to a region shows where the model looked, not why. The removal and insertion test is what makes the conclusion convincing.

**Data and code.** The article is open access (CC BY 4.0). It uses public data sets (PASCAL VOC 2007 and arcade games).
