[English](gilardi2023-ai-annotation.md) · **中文**

# 让模型当编码者：有前景，但需要验证

**研究。** Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences, 120*(30), e2305016120. [doi:10.1073/pnas.2305016120](https://doi.org/10.1073/pnas.2305016120)
**一起读。** Reiss, M. V. (2023). Testing the reliability of ChatGPT for text annotation and classification: A cautionary remark. [arXiv:2304.11085](https://arxiv.org/abs/2304.11085)

**在讲座里。** 第 4 部分，[在你自己的研究里用 AI](../../docs/part4-ai-in-your-research.zh.md)，“AI 能帮忙做分析吗？”这一页：如果把模型当作一名新的编码者，它可以帮你编码数据。Reiss 在下一页被引用，用来说明三个老陷阱中的第二个：措辞会改变答案。

**问题。** 聊天模型能否代替人类编码者给文本打标签？它这样做时，可靠性如何？

**方法。** Gilardi 及其同事使用了四个推文和新闻文章样本（n = 6,183），以及四类编码：相关性、立场、主题和框架识别。他们把不给示例（“zero-shot”，零样本）的 ChatGPT 与众包工作者和受过训练的标注者（心理学里叫编码者）相比较。Reiss 选了一个真实的分类任务：把网站文本分为新闻和非新闻。他重复输入完全相同的内容，并改变模型设置和提示词的措辞。

**发现。**
- **Gilardi et al.** 在四个数据集上，ChatGPT 的零样本准确率平均比众包工作者高约 25 个百分点。在所有任务上，它的编码者间一致性都高于众包工作者和受过训练的标注者。每条标注的成本低于 $0.003，约为众包的三十分之一。
- **Reiss.** ChatGPT 分类结果的一致性可能达不到通常的信度阈值。即使提示词措辞有微小变化，或者只是重复同样的输入，输出也可能改变。把多次重复的结果合并起来会有帮助。

**为什么值得读。** 两篇合起来读，能看到把模型当编码者的两面：它可以准确又便宜，也可能不稳定。模型是一名新的编码者，它的信度必须先确立，和任何人类编码者一样。

**局限。** 两项研究都只涵盖某一时刻的特定任务、语言和模型版本。一种编码方案上的结果不会自动迁移到另一种方案。

**数据与代码。** 材料见各篇文章。
