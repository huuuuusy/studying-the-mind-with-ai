**English** · [中文](fu2024-blink.zh.md)

# Seeing but not perceiving: BLINK

**Study.** Fu, X., Hu, Y., Li, B., Feng, Y., Wang, H., Lin, X., Roth, D., Smith, N. A., Ma, W.-C., & Krishna, R. (2024). BLINK: Multimodal large language models can see but not perceive. *European Conference on Computer Vision (ECCV 2024)*, Lecture Notes in Computer Science. [doi:10.1007/978-3-031-73337-6_9](https://doi.org/10.1007/978-3-031-73337-6_9) · [arXiv](https://arxiv.org/abs/2404.12390) · [project page](https://zeyofu.github.io/blink/)

**In the talk.** Not shown; read it with [Part 1, One person: people next to the machine](../../docs/part1-people-next-to-machine.md): a model that answers fluently is not yet a model that sees.

**Question.** Can multimodal language models, chat models that take images as well as text and answer questions about them, do the core perception tasks that people solve "within a blink"?

**Method.** Fourteen classic computer vision tasks, such as relative depth, visual correspondence, forensics detection and multi-view reasoning, are reformatted into 3,807 multiple-choice questions with one or more images. Human accuracy on the same questions serves as the baseline. Random guessing gives a second reference point.

**Finding.** People reach 95.70% accuracy on average. The best models at the time, GPT-4V and Gemini, reach 51.26% and 45.72%, only 13.17 and 7.63 percentage points above random guessing. Specialist computer vision models solve these problems much better. The authors argue that such tasks resist being solved through language.

**Why read it.** It extends the human baseline from image classifiers to the chat-style models that most people now use, and it shows that fluent answers can hide weak perception.

**Limits.** The questions are multiple choice, and the comparison is on accuracy only. It does not show *which* items people and models fail on (see [error consistency](geirhos2020-error-consistency.md)). The results describe the models tested in 2024; newer models should be tested again.

**Data and code.** Benchmark on Hugging Face: [BLINK-Benchmark/BLINK](https://huggingface.co/datasets/BLINK-Benchmark/BLINK) (Apache-2.0 according to the data set card).
