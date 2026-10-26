# Studying the Human Mind with AI: reading list by part of the talk

*用 AI 研究人的心智：按讲座部分的阅读清单。本页的文献条目保留英文；中文导读从[这里](../docs/start-here.zh.md)开始。*

This is the reading list of this repository, the companion to the talk *Studying the Human Mind with AI*. The talk asks one question: **it looks capable; how would we know it really is?** Its first three parts each ask a narrower question, with a check borrowed from psychology, from one person to a group to a society; Part 4 brings the checks into your own research:

- **One person, people next to the machine:** right answer, right reason? Compare the mistakes, not only the scores.
- **A group, people as the answer:** whose standard does it follow? Compare with a group, not one person.
- **A society, people we make:** is it like us enough to study us? Compare it with real people.

The frame underneath, the three places in a test, is on the [start page](../docs/start-here.md#behind-the-four-questions-three-places-in-a-test).

This page is a curated start; the full field-wide list (about 300 entries, by part of the talk and subtopic, with datasets and simulation frameworks) is [literature.md](literature.md). The list is growing. Entries are links only, and every link was checked before it was added (last check 2026-10-15; additions checked 2026-10-20). For a version organised by area of psychology, see [students.md](students.md); for working with AI researchers, see [working-together.md](working-together.md).

## Start here: using large models in your research

*从这里开始：在你的研究里使用大模型*

For psychology students and researchers who want to try a large model in a study.

- **Read.**
  - Demszky et al. (2023), Using large language models in psychology, *Nat. Rev. Psychol.* [doi](https://doi.org/10.1038/s44159-023-00241-5)
  - Binz & Schulz (2023), Using cognitive psychology to understand GPT-3, *PNAS*. [doi](https://doi.org/10.1073/pnas.2218523120)
  - Gilardi, Alizadeh & Kubli (2023), ChatGPT outperforms crowd workers for text-annotation tasks, *PNAS*. [doi](https://doi.org/10.1073/pnas.2305016120)
- **Open data.**
  - VideoCube, tracking through shot cuts and scene changes; the human eye-tracking comparison is reported on the site but not released as data. [site](http://videocube.aitestunion.com)
- **Always record** the model, version, date, full prompt, settings and number of runs, and ask about ethics approval before collecting anything from people.
- **Working with AI researchers:** [working-together.md](working-together.md).

## Background: from the imitation game to validity

*背景：从模仿游戏到效度*

- Turing (1950), Computing machinery and intelligence, *Mind*. [doi](https://doi.org/10.1093/mind/lix.236.433)
- Pfungst (1911), *Clever Hans (the horse of Mr. von Osten)*. [Project Gutenberg](https://www.gutenberg.org/ebooks/33936)
- Jones & Bergen (2026), Large language models pass a standard three-party Turing test, *PNAS*. [doi](https://doi.org/10.1073/pnas.2524472123)
- Demszky et al. (2023), Using large language models in psychology, *Nat. Rev. Psychol.* [doi](https://doi.org/10.1038/s44159-023-00241-5)
- **Background in psychology:** construct validity, and what can and cannot be inferred from a measurement.
  - Cronbach & Meehl (1955), Construct validity in psychological tests, *Psychol. Bull.* [doi](https://doi.org/10.1037/h0040957)
  - Poldrack (2006), Can cognitive processes be inferred from neuroimaging data? *Trends Cogn. Sci.* [doi](https://doi.org/10.1016/j.tics.2005.12.004)
- **Psychology inside AI:**
  - Hubel & Wiesel (1959) [doi](https://doi.org/10.1113/jphysiol.1959.sp006308) and (1962) [doi](https://doi.org/10.1113/jphysiol.1962.sp006837)
  - Fukushima (1980), Neocognitron [doi](https://doi.org/10.1007/bf00344251)
  - Thorndike (1898) [doi](https://doi.org/10.1037/h0092987)
  - Sutton & Barto (2018) [book page](http://incompleteideas.net/book/the-book-2nd.html)
  - Mnih et al. (2015) [doi](https://doi.org/10.1038/nature14236)
  - Christiano et al. (2017) [proceedings](https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html)
  - Ouyang et al. (2022) [doi](https://doi.org/10.52202/068431-2011)

## Part 1 · One person: people next to the machine

*第 1 部分 · 一个人：机器旁边的人*

**Scores and errors**
- Geirhos et al. (2019), ImageNet-trained CNNs are biased towards texture, *ICLR*. [OpenReview](https://openreview.net/forum?id=Bygh9j09KX)
- Geirhos, Meding & Wichmann (2020), error consistency, *NeurIPS*. [proceedings](https://proceedings.neurips.cc/paper/2020/hash/9f6992966d4c363ea0162a056cb45fe5-Abstract.html)
- Geirhos et al. (2021), Partial success in closing the gap between human and machine vision, *NeurIPS*. [proceedings](https://proceedings.neurips.cc/paper/2021/hash/c8877cff22082a16395a57e97232bb6f-Abstract.html). Data and code: [model-vs-human](https://github.com/bethgelab/model-vs-human)
- Hu, Zhao, Huang & Huang (2023), Global instance tracking: Locating target more like humans, *IEEE TPAMI*. [doi](https://doi.org/10.1109/tpami.2022.3153312)
- Hu, Zhao & Huang (2024), SOTVerse, *IJCV*. [doi](https://doi.org/10.1007/s11263-023-01908-5)
- Zhang, Hu et al. (2024), Beyond accuracy: Tracking more like human via visual search, *NeurIPS*. [doi](https://doi.org/10.52202/079017-0086)

**Cues and evidence**
- Lapuschkin et al. (2019), Unmasking Clever Hans predictors, *Nat. Commun.* [doi](https://doi.org/10.1038/s41467-019-08987-4)
- Geirhos et al. (2020), Shortcut learning in deep neural networks, *Nat. Mach. Intell.* [doi](https://doi.org/10.1038/s42256-020-00257-z)
- Li, Li, Hu, Huang & Zhang (2026), CausalStep, *AAAI*. [doi](https://doi.org/10.1609/aaai.v40i8.37582)
- Li, Li, Hu & Huang (2026), Select less, reason more, *CVPR*. [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Select_Less_Reason_More_Prioritizing_Evidence_Purity_for_Video_Reasoning_CVPR_2026_paper.html)
- Center for AI Safety, Scale AI & HLE Contributors Consortium (2026), *Nature*. [doi](https://doi.org/10.1038/s41586-025-09962-4)

**Models of the mind and theory-guided design**
- Yamins et al. (2014), *PNAS*. [doi](https://doi.org/10.1073/pnas.1403112111)
- Binz & Schulz (2023), Using cognitive psychology to understand GPT-3, *PNAS*. [doi](https://doi.org/10.1073/pnas.2218523120)
- Binz et al. (2025), A foundation model to predict and capture human cognition, *Nature*. [doi](https://doi.org/10.1038/s41586-025-09215-4)
- Orr et al. (2025), Not even wrong: On the limits of prediction as explanation in cognitive science. [arXiv:2510.03311](https://arxiv.org/abs/2510.03311)
- Zhaoping (2023), Peripheral and central sensation, *Trends Cogn. Sci.* [doi](https://doi.org/10.1016/j.tics.2023.03.001)

## Part 2 · A group: people as the answer

*第 2 部分 · 一群人：人作为答案*

**Sensing behaviour**
- Mathis et al. (2018), DeepLabCut, *Nat. Neurosci.* [doi](https://doi.org/10.1038/s41593-018-0209-y)

**Raters, describers and judges**
- Thurstone, L. L. (1927), A law of comparative judgment, *Psychol. Rev.* [doi](https://doi.org/10.1037/h0070288)
- Bradley, R. A., & Terry, M. E. (1952), Rank analysis of incomplete block designs: I. The method of paired comparisons, *Biometrika*. [doi](https://doi.org/10.1093/biomet/39.3-4.324) The paired-comparison model behind reward models and Chatbot Arena.
- Ouyang et al. (2022), Training language models to follow instructions with human feedback, *NeurIPS*. [doi](https://doi.org/10.52202/068431-2011)
- Chiang, W.-L., et al. (2024), Chatbot Arena: An open platform for evaluating LLMs by human preference, *ICML*. [PMLR](https://proceedings.mlr.press/v235/chiang24b.html)
- Loftus & Palmer (1974), *J. Verbal Learn. Verbal Behav.* [doi](https://doi.org/10.1016/s0022-5371(74)80011-3)
- Heider & Simmel (1944), An experimental study of apparent behavior, *Am. J. Psychol.* [doi](https://doi.org/10.2307/1416950)
- Gilardi, Alizadeh & Kubli (2023), ChatGPT outperforms crowd workers for text-annotation tasks, *PNAS*. [doi](https://doi.org/10.1073/pnas.2305016120)
- Wang, Morgenstern & Dickerson (2025), LLMs that replace human participants can misportray and flatten identity groups, *Nat. Mach. Intell.* [doi](https://doi.org/10.1038/s42256-025-00986-z)
- Li, Li, Hu, Guo & Zhang (2026), VerifyBench, *AAAI*. [doi](https://doi.org/10.1609/aaai.v40i38.40448)

## Part 3 · A society: people we make

*第 3 部分 · 一个社会：我们造出来的人*

**One person: personas and simulated participants**
- Park et al. (2023), Generative agents, *UIST*. [doi](https://doi.org/10.1145/3586183.3606763)
- Park et al., LLM agents grounded in self-reports enable general-purpose simulation of individuals. [arXiv:2411.10109](https://arxiv.org/abs/2411.10109)
- Argyle et al. (2023), Out of one, many, *Political Analysis*. [doi](https://doi.org/10.1017/pan.2023.2)
- Aher, Arriaga & Kalai (2023), Simulating multiple humans, *ICML*. [PMLR](https://proceedings.mlr.press/v202/aher23a.html)
- Atari et al. (2023), Which humans? *PsyArXiv*. [doi](https://doi.org/10.31234/osf.io/5b26t)
- Serapio-García et al. (2025), A psychometric framework for personality traits in LLMs, *Nat. Mach. Intell.* [doi](https://doi.org/10.1038/s42256-025-01115-6)
- Costello, Pennycook & Rand (2024), Durably reducing conspiracy beliefs through dialogues with AI, *Science*. [doi](https://doi.org/10.1126/science.adq1814). Erratum: *Science* 394 (2026), [doi](https://doi.org/10.1126/science.aem1178)

**A group and a society**
- Asch (1955), Opinions and social pressure, *Sci. Am.* [doi](https://doi.org/10.1038/scientificamerican1155-31)
- Weng, Chen & Wang (2025), The conformity of large language models, *ICLR*. [proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1da9ca7e9cef4b1af63913f05d1630a4-Abstract-Conference.html)
- Hirashima, S., Hu, S., & Cheong, K. H. (2026), Beyond hyper-rationality: Persona-driven heterogeneity in networked agent-based systems, *IEEE TNSE*. [doi](https://doi.org/10.1109/TNSE.2026.3742449)

## Data and tools

*数据与工具*

| Resource | What it offers | Link |
|---|---|---|
| model-vs-human | Trial-level human psychophysics on 17 image distortions, plus a model benchmark toolbox | [GitHub](https://github.com/bethgelab/model-vs-human) |
| IPIP Big-Five markers | Public-domain personality items, used for persona manipulation checks | [ipip.ori.org](https://ipip.ori.org/newBigFive5broadKey.htm) |
