[English](geirhos2021-partial-success.md) · **中文**

# 部分成功：稳健性差距在缩小，一致性差距没有

**研究。** Geirhos, R., Narayanappa, K., Mitzkus, B., Thieringer, T., Bethge, M., Wichmann, F. A., & Brendel, W. (2021). Partial success in closing the gap between human and machine vision. *Advances in Neural Information Processing Systems (NeurIPS) 34*, oral. [Proceedings](https://proceedings.neurips.cc/paper/2021/hash/c8877cff22082a16395a57e97232bb6f-Abstract.html) · [arXiv](https://arxiv.org/abs/2106.07411)

**在讲座里。** 第 1 部分，[一个人：机器旁边的人](../../docs/part1-people-next-to-machine.zh.md)：后来，最好的模型在准确率上赶上了人，错误却仍然和人不同。

**问题。** 第一个网络在 ImageNet 上超过人类准确率几年之后，模型在更难的测试样例上是否更接近人类视觉了？

**方法。** 人类观察者接受了一大批分布外数据集的测试，也就是和模型训练时见过的图像不一样的图像，例如加噪、风格化或只保留边缘的图像：90 名被试，共 85,120 个心理物理学试次。所选模型在三个方面不同于用带标签照片训练的标准网络。一是训练它们去做的事：从没有标签的图像中学（自监督），抵御为骗过模型而改动的图像（对抗训练），或者把图像和它的文字说明配对（CLIP 式训练）。二是结构，例如视觉 Transformer。三是学过的图像数量（从 100 万到 10 亿张）。每个模型都在准确率和图像层面的错误一致性上与人比较。

**发现。**
1. 长期存在的抗失真稳健性差距正在缩小。在大多数数据集上，最好的模型现在已超过人在短暂呈现条件下的表现（用论文的话说，是人的 “feedforward”（前馈）表现）。
2. 图像层面仍有相当大的一致性差距：人犯的错误与模型不同。大多数模型在错误上彼此一致，即使它们差别很大，比如对比式自监督模型和标准监督模型。
3. 在许多情况下，当训练集扩大到原来的 10 到 1,000 倍时，与人的一致性会提高。

**为什么值得读。** 它说明为什么准确率和错误一致性必须分开报告：一个可以达到人类水平，另一个却仍然相距很远。它还附带一个人人可用的基准。

**局限。** 人类数据来自对单张图像的短暂、受控呈现，因此描述的是快速识别，而不是人类视觉的全部。结果描述的是 2021 年测试的模型。

**数据与代码。** 17 个数据集的人类试次数据和评测代码：[github.com/bethgelab/model-vs-human](https://github.com/bethgelab/model-vs-human)。代码采用 MIT 许可证；刺激材料的许可证因数据集而异；人类试次数据的许可证没有注明。
