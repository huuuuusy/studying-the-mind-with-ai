[English](argyle2023-silicon-samples.md) · **中文**

# 由一而多：硅样本

**研究。** Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J., Rytting, C., & Wingate, D. (2023). Out of one, many: Using language models to simulate human samples. *Political Analysis, 31*(3), 337–351. [doi:10.1017/pan.2023.2](https://doi.org/10.1017/pan.2023.2) · [arXiv](https://arxiv.org/abs/2209.06899)

**在讲座里。** 第 4 部分[在你自己的研究里用 AI](../../docs/part4-ai-in-your-research.zh.md)里问答用的一张备用页，“AI 能扮演被试吗？”：硅样本能像各个子群体那样作答，所以可以为研究做预测试，但不能取代样本。它的重点必读条目在[第 3 部分，一个社会：我们造出来的人](../../docs/part3-people-we-make.zh.md)。

**问题。** 在社会科学研究中，语言模型能否代表特定人群，例如像具有某种背景的人那样回答一份调查问卷？

**方法。** 作者从美国多项大型调查的真实参与者那里取来数千份社会人口学背景故事，交给 GPT-3，让它以每个人的身份作答（AI 领域叫作给模型设定条件）。由此得到的“硅样本”回答同样的调查问题，答案再和背景相同的真实参与者比。

**发现。** GPT-3 中的偏差并不是一种单一、均匀的属性。它们是细粒度的，并与人口学特征相关，因此给它合适的背景故事，模型就能重现许多人类子群体的回答分布。作者称之为*算法保真度*（*algorithmic fidelity*）。他们认为，具备足够算法保真度的模型可以成为研究人与社会的工具。

**为什么值得读。** 它提出了硅样本这一概念，以及评判它的标准。后来的大部分争论都围绕算法保真度在哪里成立、在哪里失效。

**局限。** 对照的只是美国调查受访者在所研究问题上的回答。后来的研究发现，硅样本可能把某些身份群体描绘错，或抹平群体内部的差异，例如 Wang et al.（2025，*Nature Machine Intelligence*，[doi](https://doi.org/10.1038/s42256-025-00986-z)）；合成的调查数据也可能误导人，例如 Bisbee et al.（2024，*Political Analysis*，[doi](https://doi.org/10.1017/pan.2024.5)）。

**数据与代码。** 人类数据来自美国大型公开调查；复现材料见文章页面。
