[English](fu2024-blink.md) · **中文**

# 看见了，却没有知觉到：BLINK

**研究。** Fu, X., Hu, Y., Li, B., Feng, Y., Wang, H., Lin, X., Roth, D., Smith, N. A., Ma, W.-C., & Krishna, R. (2024). BLINK: Multimodal large language models can see but not perceive. *European Conference on Computer Vision (ECCV 2024)*, Lecture Notes in Computer Science. [doi:10.1007/978-3-031-73337-6_9](https://doi.org/10.1007/978-3-031-73337-6_9) · [arXiv](https://arxiv.org/abs/2404.12390) · [project page](https://zeyofu.github.io/blink/)

**在讲座里。** 讲座里没有展示；配合[第 1 部分，一个人：机器旁边的人](../../docs/part1-people-next-to-machine.zh.md)来读：回答流利的模型，还不是会看的模型。

**问题。** 多模态语言模型是既能看图像、也能读文字的聊天模型，能回答与图像有关的问题。这类模型能否完成人 “within a blink”（一眨眼之间）就能解决的核心知觉任务？

**方法。** 十四项经典计算机视觉任务，例如相对深度、视觉对应、伪造检测和多视角推理，被改写成 3,807 道包含一张或多张图像的多项选择题。人在同样题目上的准确率作为基线。随机猜测提供第二个参照点。

**发现。** 人的平均准确率为 95.70%。当时最好的模型 GPT-4V 和 Gemini 分别为 51.26% 和 45.72%，只比随机猜测高 13.17 和 7.63 个百分点。专门的计算机视觉模型解决这些问题要好得多。作者认为，这类任务难以通过语言来解决。

**为什么值得读。** 它把人类基线从图像分类器扩展到如今大多数人使用的聊天式模型，并表明流利的回答可能掩盖薄弱的知觉。

**局限。** 题目是多项选择，比较也只看准确率。它没有显示人和模型*在哪些*题目上出错（见[错误一致性](geirhos2020-error-consistency.zh.md)）。结果描述的是 2024 年测试的模型；更新的模型应该重新测试。

**数据与代码。** Hugging Face 上的基准：[BLINK-Benchmark/BLINK](https://huggingface.co/datasets/BLINK-Benchmark/BLINK)（据数据集卡片，采用 Apache-2.0 许可证）。
