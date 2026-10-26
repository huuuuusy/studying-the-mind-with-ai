**English** · [中文](geirhos2021-partial-success.zh.md)

# Partial success: the robustness gap closes, the consistency gap does not

**Study.** Geirhos, R., Narayanappa, K., Mitzkus, B., Thieringer, T., Bethge, M., Wichmann, F. A., & Brendel, W. (2021). Partial success in closing the gap between human and machine vision. *Advances in Neural Information Processing Systems (NeurIPS) 34*, oral. [Proceedings](https://proceedings.neurips.cc/paper/2021/hash/c8877cff22082a16395a57e97232bb6f-Abstract.html) · [arXiv](https://arxiv.org/abs/2106.07411)

**In the talk.** Part 1, [One person: people next to the machine](../../docs/part1-people-next-to-machine.md): later, the best models matched people's accuracy, but not their errors.

**Question.** A few years after the first network surpassed human accuracy on ImageNet, are models getting closer to human vision on harder test cases?

**Method.** Human observers were tested on a broad set of out-of-distribution data sets, images unlike those the models were trained on, such as noisy, stylised or edge-only images: 85,120 psychophysical trials across 90 participants. Models were chosen to differ from standard networks trained on labelled photos in three ways. One is what they were trained to do: learn from unlabelled images (self-supervised), resist images altered to fool them (adversarially trained), or match images with their captions (CLIP-style). Another is their design, for example vision transformers. The third is how many images they learned from (from 1 million to 1 billion). Each model was compared with people on accuracy and on image-level error consistency.

**Finding.**
1. The long-standing gap in robustness to distortion is closing. The best models now exceed human performance under brief presentation (human "feedforward" performance, in the paper's words) on most of the data sets.
2. A substantial image-level consistency gap remains: people make different errors from models. Most models agree with one another in their errors, even when they differ a lot, such as contrastive self-supervised and standard supervised models.
3. In many cases, consistency with people improves when the training set grows 10 to 1,000 times larger.

**Why read it.** It shows why accuracy and error consistency must be reported separately: one can reach the human level while the other stays far away. It also comes with a benchmark that anyone can use.

**Limits.** The human data come from brief, controlled presentation of single images, so they describe fast recognition, not everything human vision does. Results describe the models tested in 2021.

**Data and code.** Human trial data for 17 data sets and evaluation code: [github.com/bethgelab/model-vs-human](https://github.com/bethgelab/model-vs-human). Code under MIT; stimulus licences differ by data set; the licence of the human trial data is not stated.
