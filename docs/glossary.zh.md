[English](glossary.md) · **中文**

# 词典

讲座和这些导读里用到的术语，用平实的话解释。每个词条说明这个术语是什么意思、它在心理学里对应什么、在哪里出现、一个常见的误读，以及去哪里读更多。术语按讲座的各部分分组，最后附有索引。参考文献保留英文原文。

## 第 1 部分 · 一个人：答对了，理由也对吗？

### 线索（Cue）

**含义。** 输入中任何一个人或模型可以借以得出答案的特征，比如物体的形状、它的纹理、角落里的水印，或者问题的措辞。两个线索在普通题目上可能指向同一个答案，在不寻常的题目上却指向不同的答案。
**在心理学里。** 知觉和判断研究关注线索的使用：观察者依赖哪些信息，以及线索冲突时如何加权。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)。受控比较要问的是，模型的答案建立在哪个线索上。
**容易弄错。** 答案正确，并不能告诉你它来自哪个线索。只有把线索分开的测试才能做到。
**阅读。** [长着大象皮的猫](../resources/examples/geirhos2019-texture-bias.zh.md)。

### 线索冲突（Cue conflict）

**含义。** 一种刻意构造的刺激，让两个线索指向不同的答案，比如一张有猫的形状、大象皮纹理的图片。答案显示了哪个线索胜出。
**在心理学里。** 知觉研究中测量观察者如何给线索加权的标准范式。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)：长着大象皮的猫。
**容易弄错。** 在哪个线索胜出上一致，还不等于在哪些题目难上一致；见[错误一致性](#错误一致性error-consistency)。
**阅读。** Geirhos et al. (2019)，[卡片](../resources/examples/geirhos2019-texture-bias.zh.md)。

### 形状偏好（Shape bias）

**含义。** 在线索冲突图片上，跟着形状而不是纹理做出的判断所占的比例。人有很强的形状偏好；用 ImageNet（一个大型的带标签照片集）训练的网络则偏好纹理。
**在心理学里。** 发展心理学研究描述过幼儿在推广新物体名称时的形状偏好（Landau, Smith & Jones, 1988, *Cognitive Development, 3*(3), 299–321, [doi:10.1016/0885-2014(88)90014-7](https://doi.org/10.1016/0885-2014(88)90014-7)）。在本导读中，这个术语指在线索冲突图片上测得的偏好。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)。
**容易弄错。** 形状偏好既取决于网络结构，也取决于训练数据：同一个网络用风格化图片训练后，就会偏好形状。
**阅读。** Geirhos et al. (2019)，[卡片](../resources/examples/geirhos2019-texture-bias.zh.md)。

### 错误一致性（Error consistency）

**含义。** 两个决策者错在*同样*题目上的频率，超出各自正确率按偶然所能产生的程度。计算方法是逐个试次地对对错计算 Cohen's κ。
**在心理学里。** 一种试次层面的一致性分析，思路与评分者一致性相同，只是用在对错上，而不是用在标签上。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)：分数相近，错误不同。
**容易弄错。** 它是策略相同的*必要*条件，而不是证明。要拿它和人与人之间的一致性比，而不是和 1 比。
**阅读。** Geirhos, Meding & Wichmann (2020)，[卡片](../resources/examples/geirhos2020-error-consistency.zh.md)。

### Cohen's kappa

**含义。** 用于两位评分者把题目分到各个类别时的一致性统计量。它从观察到的一致性中扣除了按偶然预期的一致性。κ = 0 是偶然水平，κ = 1 是完全一致。
**在心理学里。** 用于名义编码的经典评分者信度指标，由 Cohen（1960）提出。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)，作为错误一致性的基础；第 2 部分，作为把模型和人类评分者相比较的一种方法。
**容易弄错。** κ 取决于每个类别出现的频率，所以要拿它和人与人之间在同样题目上的 κ 相比较。
**阅读。** Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37–46. [doi:10.1177/001316446002000104](https://doi.org/10.1177/001316446002000104)

### 聪明的汉斯效应（Clever Hans effect）

**含义。** 由一个非预期的线索产生的正确答案。名字来自聪明的汉斯，一匹看起来会数数和计算的马，实际上它是在对提问者头部极其细微、无意的动作作出反应。Oskar Pfungst 在 1904 年通过去掉这个线索证明了这一点。
**在心理学里。** 实验者效应和控制条件之必要性的奠基性案例。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)，以及用来指称那些因错误理由而成功的模型。
**容易弄错。** 聪明的汉斯确实解决了一个问题，那就是读懂人。关键在于，它解决的任务并不是人们以为它解决的那一个。
**阅读。** Pfungst, O. (1911). *Clever Hans (the horse of Mr. von Osten)*. [Project Gutenberg](https://www.gutenberg.org/ebooks/33936)；Lapuschkin et al. (2019)，[卡片](../resources/examples/lapuschkin2019-clever-hans.zh.md)。

### 捷径学习（Shortcut learning）

**含义。** 学到的决策规则在标准基准（大家共用的测试题集）上表现良好，却无法迁移到更有挑战的测试条件，比如真实世界的场景。这里沿用 Geirhos et al.（2020）的定义。
**在心理学里。** Geirhos 等指出，比较心理学、教育学和语言学里早就有类似的问题。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)。
**容易弄错。** 捷径不只是数据里的一个缺陷。只要训练集里有一个容易的线索能预测答案，任何学习者都可能学到它。
**阅读。** Geirhos, R., et al. (2020). Shortcut learning in deep neural networks. *Nature Machine Intelligence, 2*, 665–673. [doi:10.1038/s42256-020-00257-z](https://doi.org/10.1038/s42256-020-00257-z)

### 人类基线（Human baseline）

**含义。** 人在与模型相同的题目、相同的条件下表现如何。它是判断“人类水平”的参照。
**在心理学里。** 在一项任务上测试的一组人类被试，报告其分布范围，而不只是平均数。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)：人是一个范围，而不是一个完美答案；BLINK 报告的人类正确率为 95.70%。
**容易弄错。** 基线是一个范围，而不是上限。超过普通人的平均水平，并不等于表现得像人。
**阅读。** Fu et al. (2024)，[BLINK 卡片](../resources/examples/fu2024-blink.zh.md)；Geirhos et al. (2021)，[卡片](../resources/examples/geirhos2021-partial-success.zh.md)。

### 分布外数据（Out-of-distribution data）

**含义。** 与训练数据有系统差异的测试题目，比如对一个用照片训练的模型来说，加了噪声的、风格化的或只有边缘的图片。常简称为 OOD。
**在心理学里。** 接近迁移问题，以及在学习条件之外的泛化问题。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)：对失真的稳健性，模型过去在这方面远远落后于人。
**容易弄错。** 在分布外数据上表现好，说的是正确率；它完全不能说明错误是否和人相似。
**阅读。** Geirhos et al. (2021)，[卡片](../resources/examples/geirhos2021-partial-success.zh.md)。

### 心理物理学（Psychophysics）

**含义。** 测量刺激的物理属性如何与知觉相联系的方法，使用受控的刺激、大量的试次和严格的呈现条件。
**在心理学里。** 实验心理学最古老的方法之一。第 1 部分中的人机比较把它同时用在网络和人身上。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)：Tübingen 系列研究中的人类数据来自实验室心理物理学。
**容易弄错。** 实验室条件，比如短暂呈现，决定了测的是人的哪一种能力；比较结论只在这些条件下成立。
**阅读。** Lu, Z.-L., & Dosher, B. (2013). *Visual Psychophysics: From Laboratory to Theory*. MIT Press. [doi:10.7551/mitpress/9780262019453.001.0001](https://doi.org/10.7551/mitpress/9780262019453.001.0001)

### 解释方法（Explanation method）

**含义。** 显示模型做决策时依赖了输入的哪些部分的技术，常常是叠在图像上的一张热图。也叫相关性方法或归因方法。
**在心理学里。** 思路上类似眼动追踪这类过程测量：提供关于答案是怎么得出来的证据，而不只是答案是什么。
**在哪里出现。** [第 1 部分](part1-people-next-to-machine.zh.md)：靠来源标签认出来的马。
**容易弄错。** 热图显示模型看了哪里，而不是为什么。要用操纵来确认：去掉那块区域，看答案会不会变。
**阅读。** Lapuschkin et al. (2019)，[卡片](../resources/examples/lapuschkin2019-clever-hans.zh.md)。

## 第 2 部分 · 一群人：它遵循谁的标准？

### 参照（Reference）

**含义。** 模型拿来比较的人类数据：每题一个标签、一次多数投票、几位评分者，或者人们回答的完整分布。
**在心理学里。** 效度研究中的效标，以及评分者是谁、如何抽样的问题。AI 论文常把评分者叫作标注员或标注者，把在网上付费招募的评分者叫作众包工作者；在心理学里，他们就是评分者或编码者。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：以一群人为参照。
**容易弄错。** “与人类标签一致”掩盖了这是谁的标签，以及人们之间有多大分歧。
**阅读。** [第 2 部分的重点必读](part2-people-as-the-answer.zh.md#重点必读)。

### 评分者信度（Inter-rater reliability）

**含义。** 独立的评分者评判同样的题目时，彼此一致的程度。
**在心理学里。** 对任何编码或评分方案的标准检验，用 κ、α 或组内相关系数报告。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：把模型当作又一位评分者，拿它的一致程度和人与人之间的一致程度相比较。
**容易弄错。** 信度低，可能是编码方案不好，也可能是题目本身确实有歧义。下结论之前，先看人们在哪些题目上有分歧。
**阅读。** Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures, 1*(1), 77–89. [doi:10.1080/19312450709336664](https://doi.org/10.1080/19312450709336664)

### Krippendorff's alpha

**含义。** 一个适用于任意多位评分者、适用于名义、顺序、等距或等比数据、也适用于有缺失评分的数据的一致性系数。α = 1 是完全一致，α = 0 是偶然水平。
**在心理学里。** 在内容分析和有两位以上编码者的编码研究中被广泛使用。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：人与人之间的 α，以及把模型作为又一位评分者加进去之后的 α。
**容易弄错。** 加入模型后 α 上升，并不意味着模型表现得像人。一个总是给出多数答案的模型会提高 α，而它自己毫无分布可言。
**阅读。** Hayes & Krippendorff (2007), [doi:10.1080/19312450709336664](https://doi.org/10.1080/19312450709336664)。

### 金标准标签与多数投票（Gold label and majority vote）

**含义。** 金标准标签是给一道题指定的唯一“正确”答案。多数投票是几位评分者中最常见的答案。AI 里的大多数数据集存的是这两者之一。
**在心理学里。** 就像用一份标准答案给测验评分，或者把一个小组的评分简化为它们的众数。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：一个标签或一次多数投票，会掩盖人们之间有多大分歧。
**容易弄错。** 与多数一致，等于奖励模型比人更确定。
**阅读。** Uma et al. (2021)，[卡片](../resources/examples/uma2021-learning-from-disagreement.zh.md)。

### 标签分布（Label distribution）

**含义。** 一道题上选择每个答案的人所占的比例，比如 70% 选猫、30% 选狗。*软标签*是把这个分布当作训练目标，而不是只用一个答案。
**在心理学里。** 一个样本的完整反应分布，而不是它的众数。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：CIFAR-10H 每张图约有 50 个人类标签。
**容易弄错。** 只有几位评分者的分布噪声很大。CIFAR-10H 每张图用约 50 人，是有原因的。
**阅读。** Peterson et al. (2019)，[卡片](../resources/examples/peterson2019-cifar10h.zh.md)。

### 人类标注差异（Human label variation）

**含义。** 人们对同一道题会给出不同而又合理的答案这一事实，以及把它当作研究对象、而不是当作误差的研究。
**在心理学里。** 判断中的个体差异，以及评分者误差与真正的歧义之间的区分。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)。
**容易弄错。** 并非所有分歧都有意义，有些只是不专心。把两者分开是分析的一部分。
**阅读。** Plank, B. (2022). The "problem" of human label variation: On ground truth in data, modeling and evaluation. *EMNLP 2022.* [doi:10.18653/v1/2022.emnlp-main.731](https://doi.org/10.18653/v1/2022.emnlp-main.731)

### 视角主义（Perspectivism）

**含义。** 一种观点：对许多任务来说，并不存在唯一的真实答案，不同评分者群体的视角应当被保留下来并加以建模。
**在心理学里。** 接近“一个测量反映的是谁的规范”这一问题，以及判断中的跨文化差异。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：训练聊天模型的，是谁的比较判断。
**容易弄错。** 要保留视角，就得知道评分者是谁；匿名的众包标签事后无法按群体拆分。
**阅读。** Cabitza, F., et al. (2023). Toward a perspectivist turn in ground truthing for predictive computing. *AAAI 2023.* [doi:10.1609/aaai.v37i6.25840](https://doi.org/10.1609/aaai.v37i6.25840)

### 看到的与推断的（Seen and inferred）

**含义。** 输入中可以观察到的东西（比如一个动作或一件事）与被解读进去的东西（比如一种意图或一种感受）之间的区分。人们通常在前者上比在后者上更一致。
**在心理学里。** 观察与归因之间的界线，自 Heider 和 Simmel（1944）以来一直有人研究。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：五位观察者对发生了什么意见一致，对这意味着什么却各有说法。
**容易弄错。** 模型的描述把两者混在一起。在把模型和人比较之前，先把它们分开编码。
**阅读。** Heider & Simmel (1944)，[卡片](../resources/examples/heider1944-moving-shapes.zh.md)。

### 评分者模型（Rater model）

**含义。** 描述每位评分者如何产生标签的统计模型，比如每位评分者的错误率，用来合并许多不完美的评分。
**在心理学里。** 与把题目、评分者和误差分开的测量模型相关。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：从许多评分者那里学习，而不是只看多数。
**容易弄错。** 评分者模型假定存在一个可以还原的真实标签；对主观题目来说，这个假定可能不成立。
**阅读。** Dawid, A. P., & Skene, A. M. (1979). Maximum likelihood estimation of observer error-rates using the EM algorithm. *Applied Statistics, 28*(1), 20–28. [doi:10.2307/2346806](https://doi.org/10.2307/2346806)

### 基于人类反馈的学习（Learning from human feedback）

**含义。** 用人对模型输出的判断来训练模型，通常的做法是让人比较或排序答案，用这些比较训练一个奖励模型，再调整模型使它在奖励模型上得分高。
**在心理学里。** 成对比较，最古老的量表方法之一，在这里被用作训练信号。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)：ChatGPT 的训练建立在人的成对比较之上。
**容易弄错。** 模型学到的，是给出反馈的那些特定的人、在他们所收到的指示下的偏好。
**阅读。** Ouyang et al. (2022)，[卡片](../resources/examples/ouyang2022-human-feedback.zh.md)；Christiano, P., et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS.* [Proceedings](https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html)

### 大语言模型当评判者（LLM as a judge）

**含义。** 用大语言模型代替人类评判者来给答案打分或比较答案。
**在心理学里。** 一位新的评分者，在使用它的评分之前，要先确定它的信度和偏差。
**在哪里出现。** [第 2 部分](part2-people-as-the-answer.zh.md)；第 4 部分，当模型给你的数据编码时。
**容易弄错。** 总体一致性高，可能掩盖系统性的偏差。Zheng et al.（2023）报告了位置偏差、冗长偏差和偏向自己的偏差。
**阅读。** Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *NeurIPS 2023.* [doi:10.52202/075280-2020](https://doi.org/10.52202/075280-2020)

## 第 3 部分 · 一个社会：像到能研究我们吗？

### 机器演人（Machine playing people）

**含义。** 让模型扮演人：一个虚拟学生、一个模拟的班级或小镇、一群智能体，或者一项研究里的被试。有时它扮演某个人身边的人，比如受训老师面对的那个班级；有时它代替被试作答。无论哪种情况，得出的结论都是关于真实的人如何行为的。
**在心理学里。** 接近模拟或实验同谋，只不过它的行为是生成的，而不是照剧本演的。
**在哪里出现。** [第 3 部分](part3-people-we-make.zh.md)：它像我们，像到能研究我们吗？另见[第 4 部分](part4-ai-in-your-research.zh.md)，模拟被试用来预测试一项研究。
**容易弄错。** 演人的模型，表现部分是由设置决定的。它表现得像某一类人，还不是关于这类人的证据。
**阅读。** [第 3 部分的重点必读](part3-people-we-make.zh.md#重点必读)。

### 人设（Persona）

**含义。** 在指令中给模型的一段描述，说明它应该是谁：特质、背景、观点或角色。
**在心理学里。** 一种实验操纵：由研究者设定的条件，它的效果需要检验。
**在哪里出现。** 讲座开场：图灵测试中的人设提示。[第 3 部分](part3-people-we-make.zh.md)：虚拟学生。
**容易弄错。** 同一个人设的不同等价措辞，可能给出不同的结果；要全部报告。
**阅读。** Serapio-García et al. (2025)，[卡片](../resources/examples/serapio2025-personality.zh.md)；Jones & Bergen (2026)，[卡片](../resources/examples/jones2026-turing-test.zh.md)。

### 操纵检验（Manipulation check）

**含义。** 检验一项操纵是否起到了应有的作用。对人设来说，讲座里的检验是：它有没有改变它点名的那个特质，而且主要只改变这个特质？意思相同的措辞，也应该给出相同的结果。
**在心理学里。** 实验社会心理学中，在解释一项操纵的效应之前的标准做法。
**在哪里出现。** [第 3 部分](part3-people-we-make.zh.md)：人设是一种操纵。
**容易弄错。** 用测这个特质的问卷来检验，是第一步检验，讲座里就是这样做的，而且它可以通过。看人设没有点名的行为，是更强的检验。
**阅读。** Serapio-García et al. (2025)，[卡片](../resources/examples/serapio2025-personality.zh.md)。

### 硅样本（Silicon sample）

**含义。** 以真实调查受访者的背景为条件，让语言模型生成的一组回答，用来代替人类样本。这个术语来自 Argyle et al.（2023）。
**在心理学里。** 一种模拟样本；它会引出任何方便样本都有的问题，还有新的问题。
**在哪里出现。** [第 3 部分](part3-people-we-make.zh.md)和[第 4 部分](part4-ai-in-your-research.zh.md)。
**容易弄错。** 匹配一个群体的平均回答，不等于匹配它的分布；硅样本可能抹平群体内部的差异。
**阅读。** Argyle et al. (2023)，[卡片](../resources/examples/argyle2023-silicon-samples.zh.md)。

### 算法保真度（Algorithmic fidelity）

**含义。** 一个经过适当条件设定的模型，在多大程度上能复现特定人类子群体的回答分布。这个术语来自 Argyle et al.（2023）。
**在心理学里。** 一种针对模拟样本的效标效度。
**在哪里出现。** [第 3 部分](part3-people-we-make.zh.md)。
**容易弄错。** 在一组问题和一个总体上证明的保真度，不会自动推广到其他问题和总体。
**阅读。** Argyle et al. (2023)，[卡片](../resources/examples/argyle2023-silicon-samples.zh.md)。

### 图灵测试（Turing test）

**含义。** 图灵的模仿游戏：一位评判者用文字同一台机器和一个人交谈，说出哪个是哪个。在标准的三方版本中，评判者同时和两者交谈。
**在心理学里。** 一种盲评，也是对人如何区分人与机器的一种测量。
**在哪里出现。** 讲座开场（[从这里开始](start-here.zh.md)）：图灵的测试，2026 年重做了一次（Jones & Bergen）。[第 3 部分](part3-people-we-make.zh.md)：哪条回复出自真实的人？
**容易弄错。** 通过测试说明的是，在这些评判者看来对话像人，而不是背后有一个像人的心智。
**阅读。** Turing, A. M. (1950). Computing machinery and intelligence. *Mind.* [doi:10.1093/mind/lix.236.433](https://doi.org/10.1093/mind/lix.236.433)；Jones & Bergen (2026)，[卡片](../resources/examples/jones2026-turing-test.zh.md)。

### 生成式智能体（Generative agent）

**含义。** 一个建立在语言模型之上、带有记忆、反思和规划能力的软件智能体，能随时间产生可信的行为，并与其他智能体互动。
**在心理学里。** 一个模拟的人，它的行为是生成的，而不是事先由规则规定的。
**在哪里出现。** [第 3 部分](part3-people-we-make.zh.md)：Smallville。
**容易弄错。** 生成式智能体通常以可信度（像不像真人）来评判，这和与真实的人的行为一致并不是一回事。
**阅读。** Park et al. (2023)，[卡片](../resources/examples/park2023-generative-agents.zh.md)。

### 从众（Conformity）

**含义。** 改变自己的答案去和群体保持一致。Asch 证明，当前面每个人都给出明显错误的答案时，许多人也会跟着给出错误答案。
**在心理学里。** 社会影响的经典范式，有一些广为人知的控制条件，比如安排一位持异议者。
**在哪里出现。** [第 3 部分](part3-people-we-make.zh.md)：给 AI 智能体做的 Asch 式测试。
**容易弄错。** 会从众的智能体在这一点上表现得像人；但不能由此推出它们从众的理由和人相同。
**阅读。** Asch, S. E. (1955). Opinions and social pressure. *Scientific American.* [doi:10.1038/scientificamerican1155-31](https://doi.org/10.1038/scientificamerican1155-31)；Weng et al. (2025)，[卡片](../resources/examples/weng2025-conformity.zh.md)。

### 基于智能体的模型（Agent-based model）

**含义。** 一种模拟：许多个体智能体遵循行为规则并相互作用，群体层面的模式从个体行为中涌现出来。
**在心理学里。** 在社会心理学和社会学中，用来探究哪些个体层面的机制能够产生观察到的社会模式。
**在哪里出现。** [第 3 部分](part3-people-we-make.zh.md)：从简单的基于规则的智能体，到建立在语言模型之上的智能体。
**容易弄错。** 一个能复现某种模式的模型，展示的是这种模式可能如何产生，而不是它在人群中就是这样产生的。
**阅读。** Schelling, T. C. (1971). Dynamic models of segregation. *Journal of Mathematical Sociology.* [doi:10.1080/0022250x.1971.9989794](https://doi.org/10.1080/0022250x.1971.9989794)

## 第 4 部分 · 在你自己的研究里用 AI

### AI 编码者（AI coder）

**含义。** 用来为研究给材料打标签或编码的语言模型，比如把文本分类、评定情感，或者给开放式回答编码。
**在心理学里。** 内容分析中的一位新编码者，在使用它的编码之前，要先对照人类编码者检验它的信度。
**在哪里出现。** [第 4 部分](part4-ai-in-your-research.zh.md)：如果把模型当作一位新的编码者来对待，它可以帮你给数据编码。
**容易弄错。** 同一个模型的重复运行不是相互独立的编码者；它们之间的一致性几乎说明不了效度。
**阅读。** Gilardi et al. (2023)，[卡片](../resources/examples/gilardi2023-ai-annotation.zh.md)。

### 提示词敏感性（Prompt sensitivity）

**含义。** 指令的措辞以本不该有影响的方式改变时，或者同样的输入只是再运行一次时，模型输出发生的变化。
**在心理学里。** 类似一个测量对题目措辞的敏感性，测验编制正是要消除这一点。
**在哪里出现。** [第 4 部分](part4-ai-in-your-research.zh.md)，以及[第 3 部分](part3-people-we-make.zh.md)中人设的等价措辞。
**容易弄错。** 只报告一个提示词，会掩盖结果在多大程度上依赖于它；至少换一种措辞，两者都报告。
**阅读。** Reiss (2023)，与 [Gilardi 卡片](../resources/examples/gilardi2023-ai-annotation.zh.md)一起读。

### 预测驱动推断（Prediction-powered inference）

**含义。** 一种统计框架，把一大批模型预测和一小批人工标签结合起来，给出有效的置信区间，而不假定模型是正确的。
**在心理学里。** 当大部分测量由一个不完美的工具完成、并在一个随机子样本上校准时，保持推断有效的一种方法。
**在哪里出现。** [第 4 部分](part4-ai-in-your-research.zh.md)：当模型给你的大部分数据编码时，你还能得出什么结论。
**容易弄错。** 人工标注的题目必须是同一批材料的随机样本。
**阅读。** Angelopoulos et al. (2023)，[卡片](../resources/examples/angelopoulos2023-prediction-powered-inference.zh.md)。

### 模拟被试（Simulated participant）

**含义。** 被提示像研究被试那样作答的语言模型，用来预测试材料、预测结果，或者（有争议地）取代样本。
**在心理学里。** 一位回答由生成而来的预试被试；适合用来检查材料，不适合用来估计人会如何反应。
**在哪里出现。** [第 4 部分](part4-ai-in-your-research.zh.md)：模拟被试可以用来预测试一项研究，但不能取代样本。
**容易弄错。** 方向预测对了，大小却可能是错的：模拟出的效应可能过大。
**阅读。** Ashokkumar et al. (2026)，[卡片](../resources/examples/ashokkumar2026-predicting-experiments.zh.md)；Argyle et al. (2023)，[卡片](../resources/examples/argyle2023-silicon-samples.zh.md)。

## 索引

按英文名的字母顺序排列。

[基于智能体的模型](#基于智能体的模型agent-based-model) · [AI 编码者](#ai-编码者ai-coder) · [算法保真度](#算法保真度algorithmic-fidelity) · [聪明的汉斯效应](#聪明的汉斯效应clever-hans-effect) · [Cohen's kappa](#cohens-kappa) · [从众](#从众conformity) · [线索](#线索cue) · [线索冲突](#线索冲突cue-conflict) · [错误一致性](#错误一致性error-consistency) · [解释方法](#解释方法explanation-method) · [生成式智能体](#生成式智能体generative-agent) · [金标准标签与多数投票](#金标准标签与多数投票gold-label-and-majority-vote) · [人类基线](#人类基线human-baseline) · [人类标注差异](#人类标注差异human-label-variation) · [评分者信度](#评分者信度inter-rater-reliability) · [Krippendorff's alpha](#krippendorffs-alpha) · [标签分布](#标签分布label-distribution) · [基于人类反馈的学习](#基于人类反馈的学习learning-from-human-feedback) · [大语言模型当评判者](#大语言模型当评判者llm-as-a-judge) · [机器演人](#机器演人machine-playing-people) · [操纵检验](#操纵检验manipulation-check) · [分布外数据](#分布外数据out-of-distribution-data) · [人设](#人设persona) · [视角主义](#视角主义perspectivism) · [预测驱动推断](#预测驱动推断prediction-powered-inference) · [提示词敏感性](#提示词敏感性prompt-sensitivity) · [心理物理学](#心理物理学psychophysics) · [评分者模型](#评分者模型rater-model) · [参照](#参照reference) · [看到的与推断的](#看到的与推断的seen-and-inferred) · [形状偏好](#形状偏好shape-bias) · [捷径学习](#捷径学习shortcut-learning) · [硅样本](#硅样本silicon-sample) · [模拟被试](#模拟被试simulated-participant) · [图灵测试](#图灵测试turing-test)
