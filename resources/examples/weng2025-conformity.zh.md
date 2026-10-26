[English](weng2025-conformity.md) · **中文**

# 用语言模型智能体重做 Asch 实验

**研究。** Weng, Z., Chen, G., & Wang, W. (2025). Do as we do, not as you think: The conformity of large language models. *International Conference on Learning Representations (ICLR 2025)*, oral. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1da9ca7e9cef4b1af63913f05d1630a4-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2501.13381)

**在讲座里。** 问答用的备用页，配合[第 3 部分，一个社会：我们造出来的人](../../docs/part3-people-we-make.zh.md)：针对 AI 智能体的 Asch 式检验，以及 Asch 自己的控制条件。

**问题。** 语言模型智能体协同工作时，会不会像 Asch 实验中的人那样向多数从众？是什么让它们更多或更少地从众？

**方法。** BenchForm 是一个由推理密集型任务构成的基准，包含五种交互协议。在基本设定中，受测的智能体在另外六个智能体之后作答。一些协议沿用 Asch 的设计：其他智能体给出相同的答案，且不告诉受测的智能体答案是否正确。效应用两个指标衡量：从众率和独立率。作者随后改变了先前互动的长度和多数的规模，要求受测的智能体解释自己的选择，并尝试了两种补救办法：一个“被赋权”（“empowered”）的人设，以及一个反思步骤。

**发现。**
1. 基于语言模型的多智能体系统中存在从众，而且它会显著影响系统的表现。
2. 从众的程度既取决于模型，也取决于设定：先前讨论的轮次越多，从众越强；多数的规模越大，从众也越多。
3. 两种补救办法在减少从众方面都显示出希望。

**为什么值得读。** 它拿来心理学最著名的实验之一，保持其逻辑不变，在人工智能体上运行。它展示了一个经典范式如何变成针对 AI 的检验。

**局限。** 智能体在推理任务上从众，并不表明它们从众的原因与人相同。行为相符不等于机制相符。下一步应把这些智能体与人类在同样任务上的数据相比较。

**数据与代码。** [github.com/Zhiyuan-Weng/BenchForm](https://github.com/Zhiyuan-Weng/BenchForm)（MIT）。
