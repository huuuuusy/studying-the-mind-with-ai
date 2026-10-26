**English** · [中文](ashokkumar2026-predicting-experiments.zh.md)

# Predicting the results of experiments before running them

**Study.** Ashokkumar, A., Hewitt, L., Ghezae, I., & Willer, R. (2026). Large language models can predict the results of social science experiments. *Nature.* [doi:10.1038/s41586-026-10742-x](https://doi.org/10.1038/s41586-026-10742-x)

**In the talk.** Not shown; read it with [Part 4, AI in your own research](../../docs/part4-ai-in-your-research.md): a simulated participant can pretest a study; it does not replace the sample.

**Question.** Can a language model, asked to simulate how representative samples of people respond, predict the results of real experiments, including experiments it cannot have seen in training?

**Method.** The authors built an archive of 70 preregistered, nationally representative survey experiments in the United States, with 469 experimental effects and 119,330 participants. They prompted a model to simulate how representative American samples would respond to each experiment's stimuli, and estimated treatment effects by comparing the simulated responses across conditions. A second archive of 15 megastudies with 606 effects served as a further test. They also surveyed 460 social scientists about likely uses and risks.

**Finding.**
- Predictions from GPT-4 were strongly correlated with the actual treatment effects, with accuracy similar to pooled forecasts by people. The correlations stayed high for studies not published or posted before the model's training data were collected (its training cutoff), and for prominent open-weight models (models whose trained parameters are public).
- **The predictions systematically overestimated effect sizes.**
- In the megastudy archive, correlations were lower but comparable to those of pooled expert forecasters.

**Why read it.** It is the strongest evidence for one specific, careful use of simulated participants: predicting the direction of effects to choose, pilot or prioritise studies. It also shows the limit: predicted effects are too large.

**Limits.** The experiments are American survey experiments. A good correlation across many effects does not make any single prediction reliable, and overestimated effect sizes would mislead power calculations if used in place of a pilot with people.

**Data and code.** See the article for the archive and materials.
