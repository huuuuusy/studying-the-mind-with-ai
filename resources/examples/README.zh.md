[English](README.md) · **中文**

# 重点必读，每篇一张卡片

每张卡片用一页介绍一项已发表的研究：问题、用心理学术语描述的方法、发现、为什么值得读、局限，以及数据和代码是否公开。讲座的每个部分各有五张，另有两张分别配合开场和一张备用页。卡片上的数字都来自论文本身；可以顺着链接去核对。有七张卡片介绍的研究讲座里没有展示（Peterson、Morgenroth、Uma、Rathje、Demszky、Angelopoulos 和 Ashokkumar）；这几张卡片都说明了该配合讲座的哪一部分来读。

| 部分 | 卡片 | 研究 | 方法 | 数据公开 |
|---|---|---|---|---|
| 1 · 一个人 | [长着大象皮的猫](geirhos2019-texture-bias.zh.md) | Geirhos et al., 2019, *ICLR* | 线索冲突刺激，实验室心理物理学 | 是 |
| 1 · 一个人 | [分数相近，错误不同](geirhos2020-error-consistency.zh.md) | Geirhos, Meding & Wichmann, 2020, *NeurIPS* | 逐试次的错误一致性（Cohen's κ） | 代码公开 |
| 1 · 一个人 | [在错误的地方找到正确答案](lapuschkin2019-clever-hans.zh.md) | Lapuschkin et al., 2019, *Nature Communications* | 解释图；去掉和加入线索 | 公开数据集 |
| 1 · 一个人 | [部分成功](geirhos2021-partial-success.zh.md) | Geirhos et al., 2021, *NeurIPS* | 17 个数据集，85,120 个人类试次；正确率和一致性 | 是 |
| 1 · 一个人 | [看见了，却没有知觉到](fu2024-blink.zh.md) | Fu et al., 2024, *ECCV* | 3,807 道知觉题上的人类基线 | 是 |
| 2 · 一群人 | [人会从移动的图形里读出意图](heider1944-moving-shapes.zh.md) | Heider & Simmel, 1944, *American Journal of Psychology* | 对一段动画的自由描述；三组，114 名被试 | 否（文章在 JSTOR 上） |
| 2 · 一群人 | [聊天模型的训练建立在人的比较之上](ouyang2022-human-feedback.zh.md) | Ouyang et al., 2022, *NeurIPS* | 标注员（心理学里叫评分者）的排序作为训练信号；标注员之间的一致性 | 否 |
| 2 · 一群人 | [每张图约五十人](peterson2019-cifar10h.zh.md) | Peterson et al., 2019, *ICCV* | 10,000 张图的 511,400 个人类标签；标签分布 | 是 |
| 2 · 一群人 | [四十四位评分者，十四部影片](morgenroth2025-emo-film.zh.md) | Morgenroth et al., 2025, *Scientific Data* | 44 位评分者的连续情绪评分，附 fMRI | 是 |
| 2 · 一群人 | [人们意见不一时，就从分歧中学习](uma2021-learning-from-disagreement.zh.md) | Uma et al., 2021, *JAIR* | 综述，附在多评分者数据集上的实验 | 是 |
| 3 · 一个社会 | [社会拟像：开张之前就住满人的社区](park2022-social-simulacra.zh.md) | Park et al., 2022, *UIST* | 由目标、规则和人设生成社区；真实与生成讨论的辨别，200 位评判者 | 只有演示页 |
| 3 · 一个社会 | [二十五个生成式智能体组成的小镇](park2023-generative-agents.zh.md) | Park et al., 2023, *UIST* | 记忆、反思和计划；可信度，以及消融实验（拿掉某些部分，看每一部分起什么作用） | 代码公开 |
| 3 · 一个社会 | [为 1,052 个人各造一个智能体](park2024-simulating-1000-people.zh.md) | Park et al., arXiv:2411.10109 | 由两小时访谈造出智能体，拿每个人两周后的自己的回答来检验 | 代码公开；智能体需申请 |
| 3 · 一个社会 | [由一而多：硅样本](argyle2023-silicon-samples.zh.md) | Argyle et al., 2023, *Political Analysis* | 以真实受访者的背景为条件的模型，与他们的回答比较 | 调查数据公开 |
| 3 · 一个社会 | [测量和塑造模型的人格](serapio2025-personality.zh.md) | Serapio-García et al., 2025, *Nature Machine Intelligence* | 心理测量的信度和效度；用指令塑造特质 | 见原文 |
| 开场 | [借助人设的三方图灵测试](jones2026-turing-test.zh.md) | Jones & Bergen, 2026, *PNAS* | 预注册、随机化的图灵测试；有人设和无人设 | 见原文 |
| 3 · 备用页 | [用语言模型智能体重做 Asch 实验](weng2025-conformity.zh.md) | Weng, Chen & Wang, 2025, *ICLR* | Asch 式的实验程序；从众率和独立率 | 代码公开 |
| 4 · 你的研究 | [让模型当编码者](gilardi2023-ai-annotation.zh.md) | Gilardi et al., 2023, *PNAS*，以及 Reiss, 2023 | 模型与众包工作者和受过训练的标注者对比；重复的和改写过的提示词 | 见原文 |
| 4 · 你的研究 | [用十二种语言做心理学文本分析](rathje2024-psychological-text.zh.md) | Rathje et al., 2024, *PNAS* | 47,925 篇标注过的文本，12 种语言；模型与词典和微调过的模型（在这项任务上额外训练过的模型）对比 | 示例代码 |
| 4 · 你的研究 | [语言模型能为心理学做什么，不能做什么](demszky2023-llms-in-psychology.zh.md) | Demszky et al., 2023, *Nature Reviews Psychology* | Perspective：用途、顾虑、建议 | 不适用 |
| 4 · 你的研究 | [用 AI 标签加少量人工标签得出有效结论](angelopoulos2023-prediction-powered-inference.zh.md) | Angelopoulos et al., 2023, *Science* | 预测驱动推断 | 代码公开 |
| 4 · 你的研究 | [预测实验的结果](ashokkumar2026-predicting-experiments.zh.md) | Ashokkumar et al., 2026, *Nature* | 为 70 项实验、469 个效应生成模拟样本 | 见原文 |

**怎么读卡片。** 先读*问题*和*发现*，再读*方法*：它通常是你在心理学里已经熟悉的设计。*局限*说明这项研究没有表明什么。
