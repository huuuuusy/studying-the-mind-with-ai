[English](geirhos2020-error-consistency.md) · **中文**

# 分数相近，错误不同：错误一致性

**研究。** Geirhos, R., Meding, K., & Wichmann, F. A. (2020). Beyond accuracy: Quantifying trial-by-trial behaviour of CNNs and humans by measuring error consistency. *Advances in Neural Information Processing Systems (NeurIPS) 33*. [Proceedings](https://proceedings.neurips.cc/paper/2020/hash/9f6992966d4c363ea0162a056cb45fe5-Abstract.html) · [arXiv](https://arxiv.org/abs/2006.16736)

**在讲座里。** 第 1 部分，[一个人：机器旁边的人](../../docs/part1-people-next-to-machine.zh.md)：分数相近、却错在不同题目上的两个系统。在一批图片上，人与人之间的错误一致性是 0.33，网络与人之间只有 0.07。

**问题。** 两个决策者，无论是大脑还是算法，用的是同一种策略吗？仅凭准确率无法判断，因为两个系统可以用截然不同的策略达到相同的准确率。当两者都接近上限时，这个问题最突出，网络和人在物体识别上正是如此。

**方法。** *逐试次错误一致性。* 对每个试次，记录每个决策者是对还是错，再看他们在同一批试次上一起出错的频率。再和偶然水平比较：按两者各自的准确率，纯属偶然时会有多少次一起出错。这个指标就是用在对错上的 Cohen's κ。它可以比较模型与模型、人与人，以及模型与人。逐试次地犯一致的错误，是策略相似的*必要*条件。

**发现。** 在物体识别上，任何架构的网络彼此之间都高度一致。它们与人类观察者的一致性只略高于偶然水平，因此人和网络很可能使用非常不同的策略。CORnet-S 内部有把信号送回去的回路（循环模型），被描述为当前最好的灵长类大脑物体识别通路模型；在这项分析中，它的表现与信号只朝一个方向传的标准图像网络（前馈的 ResNet-50）基本相同。

**为什么值得读。** 它把一个含糊的说法（“模型像人一样处理图像”）变成一个可能失败的检验。它还使用心理学学生已经熟悉的统计量 Cohen's κ，因此这一方法很容易迁移到其他任务。

**局限。** 一致的错误是共享策略的必要条件，但不是充分条件。κ 高并不说明加工过程相同，仅凭 κ 低也无法确定模型用的是哪条捷径。解读 κ 时要以人与人之间的一致性为参照，而不是以理想值 1 为参照。

**数据与代码。** 分析代码：[github.com/wichmann-lab/error-consistency](https://github.com/wichmann-lab/error-consistency)；该仓库没有注明许可证。后续研究使用的人类数据收录在 [model-vs-human](geirhos2021-partial-success.zh.md) 中。
