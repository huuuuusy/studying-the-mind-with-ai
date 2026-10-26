[English](geirhos2019-texture-bias.md) · **中文**

# 长着大象皮的猫：用 ImageNet 训练的网络看纹理，人看形状

**研究。** Geirhos, R., Rubisch, P., Michaelis, C., Bethge, M., Wichmann, F. A., & Brendel, W. (2019). ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness. *International Conference on Learning Representations (ICLR)*, oral. [OpenReview](https://openreview.net/forum?id=Bygh9j09KX) · [arXiv](https://arxiv.org/abs/1811.12231)

**在讲座里。** 第 1 部分，[一个人：机器旁边的人](../../docs/part1-people-next-to-machine.zh.md)：把长着大象皮的猫叫作大象的网络。

**问题。** 卷积网络识别物体时，是像人一样依靠形状，还是依靠纹理？

**方法。** 采用线索冲突设计，这是知觉研究判断观察者使用两种线索中哪一种的标准做法。风格迁移是一种用另一张图像的纹理重画一张图像的方法，它让一张图像具有某一类别的形状和另一类别的纹理。随后人和网络对同一批图像分类，分析统计各自跟随的是哪一种线索。人类数据来自受控的实验室心理物理学研究：九项实验，48,560 个试次，97 名观察者。

**发现。** 用 ImageNet（一个大型的带标签照片集）训练的网络强烈偏好纹理，而人依据形状做判断。同一种网络结构（ResNet-50，一种常用的图像网络）如果在 *Stylized-ImageNet* 上训练，就会转而学到基于形状的表征；*Stylized-ImageNet* 是把纹理替换掉的 ImageNet 版本。这个网络与人类行为更吻合，物体检测更好，对多种图像失真也更稳健。

**为什么值得读。** 这是本部分问题最清楚的例子：*同样的任务，相近的分数，理由也相同吗？* 让两种线索相互冲突，看哪一种胜出，对人和机器都是如此。它还表明，答案取决于训练数据，而不只取决于架构。

**局限。** 形状与纹理只是众多线索维度中的一个。人和模型可能在哪种线索胜出上一致，却仍然错在不同的图像上，这正是[错误一致性](geirhos2020-error-consistency.zh.md)所衡量的。

**数据与代码。** 刺激材料、人类数据、训练好的模型和代码：[github.com/rgeirhos/texture-vs-shape](https://github.com/rgeirhos/texture-vs-shape)。该仓库没有注明统一的许可证；复用前请逐项核对各个部分。
