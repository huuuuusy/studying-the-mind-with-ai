**English** · [中文](gilardi2023-ai-annotation.zh.md)

# A model as a coder: promising, and in need of validation

**Study.** Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences, 120*(30), e2305016120. [doi:10.1073/pnas.2305016120](https://doi.org/10.1073/pnas.2305016120)
**Read with.** Reiss, M. V. (2023). Testing the reliability of ChatGPT for text annotation and classification: A cautionary remark. [arXiv:2304.11085](https://arxiv.org/abs/2304.11085)

**In the talk.** Part 4, [AI in your own research](../../docs/part4-ai-in-your-research.md), the page "Can AI help with analysis?": a model can help code your data if you treat it as a new coder. Reiss is cited on the next page, for the second of three old traps: the wording moves the answer.

**Question.** Can a chat model replace human coders for labelling text, and how reliable is it when it does?

**Method.** Gilardi and colleagues used four samples of tweets and news articles (n = 6,183) and four kinds of coding: relevance, stance, topics and frame detection. They compared ChatGPT, used without examples ("zero-shot"), with crowd workers and with trained annotators (what psychology calls coders). Reiss took one real classification task, sorting website texts into news and not news. He repeated identical inputs and varied the model settings and the wording of the prompt.

**Finding.**
- **Gilardi et al.** Across the four data sets, ChatGPT's zero-shot accuracy exceeded that of crowd workers by about 25 percentage points on average. Its intercoder agreement exceeded that of both crowd workers and trained annotators on all tasks. It cost less than $0.003 per annotation, about thirty times less than crowd work.
- **Reiss.** The consistency of ChatGPT's classifications can fall short of the usual thresholds for reliability. Even small changes in prompt wording, or simply repeating the same input, can change the output. Pooling several repetitions helps.

**Why read them.** Read together, they show both sides of using a model as a coder: it can be accurate and cheap, and it can be unstable. A model is a new coder whose reliability has to be established, as for any human coder.

**Limits.** Both studies cover particular tasks, languages and model versions at one moment. Results for one coding scheme do not transfer automatically to another.

**Data and code.** See each article for its materials.
