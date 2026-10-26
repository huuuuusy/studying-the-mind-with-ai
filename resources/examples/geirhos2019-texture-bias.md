**English** · [中文](geirhos2019-texture-bias.zh.md)

# A cat with elephant skin: ImageNet-trained networks see texture, people see shape

**Study.** Geirhos, R., Rubisch, P., Michaelis, C., Bethge, M., Wichmann, F. A., & Brendel, W. (2019). ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness. *International Conference on Learning Representations (ICLR)*, oral. [OpenReview](https://openreview.net/forum?id=Bygh9j09KX) · [arXiv](https://arxiv.org/abs/1811.12231)

**In the talk.** Part 1, [One person: people next to the machine](../../docs/part1-people-next-to-machine.md): the network that calls a cat with elephant skin an elephant.

**Question.** Do convolutional networks recognise objects by their shape, as people do, or by their texture?

**Method.** A cue-conflict design, the standard way perception research asks which of two cues an observer uses. Style transfer, a method that redraws one image in the texture of another, gives one image the shape of one category and the texture of another. People and networks then classify the same images, and the analysis counts which cue each one follows. The human data come from controlled laboratory psychophysics: nine experiments, 48,560 trials, 97 observers.

**Finding.** Networks trained on ImageNet, a large collection of labelled photos, are strongly biased towards texture, while people decide by shape. The same network design (ResNet-50, a standard image network) learns a shape-based representation instead when it is trained on *Stylized-ImageNet*, a version of ImageNet whose textures have been replaced. That network fits human behaviour better, detects objects better and is more robust to a wide range of image distortions.

**Why read it.** It is the clearest example of this part's question, *same task, close scores: the same reasons?* Put two cues in conflict and see which one wins, for people and machines alike. It also shows that the answer depends on training data, not only on the architecture.

**Limits.** Shape versus texture is one cue dimension among many. People and a model can agree on which cue wins and still fail on different images, which is what [error consistency](geirhos2020-error-consistency.md) measures.

**Data and code.** Stimuli, human data, trained models and code: [github.com/rgeirhos/texture-vs-shape](https://github.com/rgeirhos/texture-vs-shape). The repository does not state a single licence; check each component before you reuse it.
