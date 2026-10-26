[English](peterson2019-cifar10h.md) · **中文**

# 每张图约五十人：CIFAR-10H

**研究。** Peterson, J. C., Battleday, R. M., Griffiths, T. L., & Russakovsky, O. (2019). Human uncertainty makes classification more robust. *IEEE/CVF International Conference on Computer Vision (ICCV)*, 9616–9625. [doi:10.1109/ICCV.2019.00971](https://doi.org/10.1109/ICCV.2019.00971) · [arXiv](https://arxiv.org/abs/1908.07086)

**在讲座里。** 讲座里没有展示；配合[第 2 部分，一群人：人作为答案](../../docs/part2-people-as-the-answer.zh.md)来读：拿一群人而不是一个标签给模型打分。

**问题。** 图像分类器的训练和打分都以每张图像的一个正确标签为准。关于人如何看待同样的图像，它们漏掉了什么？这重要吗？

**方法。** CIFAR-10 测试集有十个类别的 10,000 张小图像，每一张都由人做了分类：
- 2,571 名 Amazon Mechanical Turk 上的被试各自分类 200 张图像，每 20 个试次插入一张明显的图像作为注意力检查；
- 共得到 511,400 个人类判断，每张图像约 50 个；
- 结果是每张图像的一个完整的人类标签*分布*，而不是一个答案。

随后拿分类器和这些分布比较，也用这些分布来训练分类器。

**发现。** 用常规方式训练的分类器没有表现出类似人的不确定性。专门用人类标签分布来训练，可以缩小这一差距。这样训练出的模型，在越来越不像训练数据的测试集上表现更好，也更不容易被对抗攻击（故意对图像做细微改动，让模型出错）骗过。

**为什么值得读。** 它把人与人之间的分歧从噪声变成了数据。同一张图像，在大多数人看来是猫，在一些人看来是狗；知道这一点的模型表现更好。

**局限。** CIFAR-10 的图像很小，十个类别也很简单。单一平台上的众包工作者只是一种特定的人类参照。

**数据与代码。** CIFAR-10H：[github.com/jcpeterson/cifar-10h](https://github.com/jcpeterson/cifar-10h)（CC BY-NC-SA 4.0）。
