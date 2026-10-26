**English** · [中文](peterson2019-cifar10h.zh.md)

# About fifty people per image: CIFAR-10H

**Study.** Peterson, J. C., Battleday, R. M., Griffiths, T. L., & Russakovsky, O. (2019). Human uncertainty makes classification more robust. *IEEE/CVF International Conference on Computer Vision (ICCV)*, 9616–9625. [doi:10.1109/ICCV.2019.00971](https://doi.org/10.1109/ICCV.2019.00971) · [arXiv](https://arxiv.org/abs/1908.07086)

**In the talk.** Not shown; read it with Part 2, [A group: people as the answer](../../docs/part2-people-as-the-answer.md): score a model against the group, not one label.

**Question.** Image classifiers are trained and scored against one correct label per image. What do they miss about how people see the same images, and does it matter?

**Method.** People categorised every image in the CIFAR-10 test set, which has 10,000 small images in ten classes:
- 2,571 participants on Amazon Mechanical Turk each categorised 200 images, with an obvious image as an attention check every 20 trials;
- this gave 511,400 human decisions, about 50 per image;
- the result is a full *distribution* of human labels for each image, not one answer.

Classifiers were then compared with these distributions and also trained on them.

**Finding.** Classifiers trained in the usual way do not show human-like uncertainty. Explicit training on the human label distributions closes this gap. The models then do better on test sets increasingly unlike the training data, and are harder to fool with adversarial attacks (images changed slightly on purpose to make a model err).

**Why read it.** It turns human disagreement from noise into data. The same image can be a cat to most people and a dog to some, and a model that knows this behaves better.

**Limits.** CIFAR-10 images are tiny, and the ten categories are simple. Crowd workers on one platform are one particular human reference.

**Data and code.** CIFAR-10H: [github.com/jcpeterson/cifar-10h](https://github.com/jcpeterson/cifar-10h) (CC BY-NC-SA 4.0).
