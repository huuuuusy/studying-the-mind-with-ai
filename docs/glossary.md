**English** · [中文](glossary.zh.md)

# Glossary

The terms used in the talk and in these guides, in plain language. Each entry gives what the
term means, its counterpart in psychology, where it comes up, a common misreading, and where
to read more. Terms are grouped by the parts of the talk; an index follows at the end.

## Part 1 · One person: right answer, right reason?

### Cue

**What it means.** Any feature of an input that a person or a model can use to reach an answer, such as an object's shape, its texture, a watermark in the corner or the wording of a question. Two cues can lead to the same answer on ordinary items and to different answers on unusual ones.
**In psychology.** Cue use is studied in perception and judgement: which information an observer relies on, and how cues are weighted when they conflict.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md). A controlled comparison asks which cue a model's answer rests on.
**Easy to get wrong.** A correct answer does not tell you which cue produced it. Only a test that separates the cues can.
**Read.** [A cat with elephant skin](../resources/examples/geirhos2019-texture-bias.md).

### Cue conflict

**What it means.** A stimulus built so that two cues point to different answers, for example an image with the shape of a cat and the texture of elephant skin. The answer shows which cue won.
**In psychology.** A standard paradigm in perception research for measuring how observers weight cues.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md): the cat with elephant skin.
**Easy to get wrong.** Agreement on which cue wins is not yet agreement on which items are hard; see [error consistency](#error-consistency).
**Read.** Geirhos et al. (2019), [card](../resources/examples/geirhos2019-texture-bias.md).

### Shape bias

**What it means.** On cue-conflict images, the share of decisions that follow the shape rather than the texture. People are strongly shape-biased; networks trained on ImageNet (a large set of labelled photographs) are texture-biased.
**In psychology.** Developmental research describes a shape bias in how young children extend new object names (Landau, Smith & Jones, 1988, *Cognitive Development, 3*(3), 299–321, [doi:10.1016/0885-2014(88)90014-7](https://doi.org/10.1016/0885-2014(88)90014-7)). In this guide the term means the measured preference on cue-conflict images.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md).
**Easy to get wrong.** Shape bias depends on the training data as well as the architecture: the same network becomes shape-biased when trained on stylised images.
**Read.** Geirhos et al. (2019), [card](../resources/examples/geirhos2019-texture-bias.md).

### Error consistency

**What it means.** How often two decision makers are wrong on the *same* items, beyond what their accuracies would produce by chance. It is computed as Cohen's κ on right and wrong, trial by trial.
**In psychology.** A trial-level analysis of agreement, in the spirit of inter-rater agreement, applied to correctness rather than to labels.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md): close scores, different mistakes.
**Easy to get wrong.** It is a *necessary* condition for a shared strategy, not proof of one. Read it against the consistency among people, not against 1.
**Read.** Geirhos, Meding & Wichmann (2020), [card](../resources/examples/geirhos2020-error-consistency.md).

### Cohen's kappa

**What it means.** An agreement statistic for two raters who sort items into categories. It corrects the observed agreement for the agreement expected by chance. κ = 0 is chance level and κ = 1 is perfect agreement.
**In psychology.** Classic inter-rater reliability for nominal codes, introduced by Cohen (1960).
**Where it comes up.** [Part 1](part1-people-next-to-machine.md), as the basis of error consistency; in Part 2, as one way to compare a model with human raters.
**Easy to get wrong.** κ depends on how often each category occurs, so compare it with the κ between people on the same items.
**Read.** Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37–46. [doi:10.1177/001316446002000104](https://doi.org/10.1177/001316446002000104)

### Clever Hans effect

**What it means.** A right answer produced by an unintended cue. The name comes from Clever Hans, a horse who seemed to count and calculate but was responding to tiny, unintended movements of the questioner's head. Oskar Pfungst showed this in 1904 by removing the cue.
**In psychology.** A founding case of experimenter effects and of the need for control conditions.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md), and as the name for models that succeed for the wrong reason.
**Easy to get wrong.** Clever Hans did solve something, namely reading people. The point is that the task he solved was not the one he was credited with.
**Read.** Pfungst, O. (1911). *Clever Hans (the horse of Mr. von Osten)*. [Project Gutenberg](https://www.gutenberg.org/ebooks/33936); Lapuschkin et al. (2019), [card](../resources/examples/lapuschkin2019-clever-hans.md).

### Shortcut learning

**What it means.** Learning decision rules that perform well on standard benchmarks (shared test sets) but fail to transfer to more challenging test conditions, such as real-world scenarios. This follows the definition of Geirhos et al. (2020).
**In psychology.** Geirhos et al. note that related problems are known in comparative psychology, education and linguistics.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md).
**Easy to get wrong.** A shortcut is not a bug in the data alone. It is what any learner may pick up when an easy cue predicts the answer in the training set.
**Read.** Geirhos, R., et al. (2020). Shortcut learning in deep neural networks. *Nature Machine Intelligence, 2*, 665–673. [doi:10.1038/s42256-020-00257-z](https://doi.org/10.1038/s42256-020-00257-z)

### Human baseline

**What it means.** How people perform on the same items under the same conditions as the model. It is the reference against which "human-level" is judged.
**In psychology.** A sample of human participants tested on a task, with its spread reported, not only its mean.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md): people as a range, not a perfect answer; BLINK's 95.70% human accuracy.
**Easy to get wrong.** A baseline is a range, not a ceiling. Exceeding the average person is not the same as behaving like people.
**Read.** Fu et al. (2024), [BLINK card](../resources/examples/fu2024-blink.md); Geirhos et al. (2021), [card](../resources/examples/geirhos2021-partial-success.md).

### Out-of-distribution data

**What it means.** Test items that differ systematically from the training data, such as noisy, stylised or edge-only images for a model trained on photographs. The term is often shortened to OOD.
**In psychology.** Close to the question of transfer and of generalisation beyond the conditions of learning.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md): robustness to distortions, where models used to fall far behind people.
**Easy to get wrong.** Doing well on OOD data is about accuracy; it says nothing about whether the errors resemble people's.
**Read.** Geirhos et al. (2021), [card](../resources/examples/geirhos2021-partial-success.md).

### Psychophysics

**What it means.** The measurement of how physical properties of a stimulus relate to perception, using controlled stimuli, many trials and careful presentation conditions.
**In psychology.** One of the oldest methods of experimental psychology. The human–machine comparisons in Part 1 apply it to networks and people at once.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md): the human data in the Tübingen studies come from laboratory psychophysics.
**Easy to get wrong.** Laboratory conditions, such as brief presentation, define which human ability is being measured; the comparison holds for those conditions.
**Read.** Lu, Z.-L., & Dosher, B. (2013). *Visual Psychophysics: From Laboratory to Theory*. MIT Press. [doi:10.7551/mitpress/9780262019453.001.0001](https://doi.org/10.7551/mitpress/9780262019453.001.0001)

### Explanation method

**What it means.** A technique that shows which parts of an input a model relied on for a decision, often as a heat map over an image. It is also called a relevance or attribution method.
**In psychology.** Similar in spirit to process measures such as eye tracking: evidence about how an answer was reached, not only what it was.
**Where it comes up.** [Part 1](part1-people-next-to-machine.md): the horse recognised by its source tag.
**Easy to get wrong.** A map shows where the model looked, not why. Confirm it with a manipulation: remove the region and see whether the answer changes.
**Read.** Lapuschkin et al. (2019), [card](../resources/examples/lapuschkin2019-clever-hans.md).

## Part 2 · A group: whose standard does it follow?

### Reference

**What it means.** The human data a model is compared with: one label per item, a majority vote, several raters, or the full distribution of people's answers.
**In psychology.** The criterion in a validation study, and the question of who the raters are and how they were sampled. AI papers often call the raters labellers or annotators, and paid online raters crowd workers; in psychology they are raters or coders.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): a group of people as the reference.
**Easy to get wrong.** "Agrees with the human label" hides whose label it is and how much people disagree.
**Read.** [Key readings for Part 2](part2-people-as-the-answer.md#key-readings).

### Inter-rater reliability

**What it means.** How far independent raters agree when they judge the same items.
**In psychology.** The standard check on any coding or rating scheme, reported with κ, α or intraclass correlation.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): treat the model as one more rater and compare its agreement with people's agreement with each other.
**Easy to get wrong.** Low reliability can mean a poor coding scheme or a genuinely ambiguous item. Look at which items people disagree on before you conclude.
**Read.** Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures, 1*(1), 77–89. [doi:10.1080/19312450709336664](https://doi.org/10.1080/19312450709336664)

### Krippendorff's alpha

**What it means.** An agreement coefficient for any number of raters, for nominal, ordinal, interval or ratio data, and for data with missing ratings. α = 1 is perfect agreement and α = 0 is chance level.
**In psychology.** Widely used in content analysis and in coding studies with more than two coders.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): α among people, and α with the model added as one more rater.
**Easy to get wrong.** α going up when the model is added does not mean the model behaves like a person. A model that always gives the majority answer raises α while having no spread of its own.
**Read.** Hayes & Krippendorff (2007), [doi:10.1080/19312450709336664](https://doi.org/10.1080/19312450709336664).

### Gold label and majority vote

**What it means.** A gold label is the single "correct" answer assigned to an item. A majority vote is the most common answer among several raters. Most data sets in AI store one of the two.
**In psychology.** Like scoring a test against one answer key, or reducing a panel's ratings to their mode.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): one label, or a majority vote, hides how much people disagree.
**Easy to get wrong.** Agreement with the majority rewards a model for being more certain than people are.
**Read.** Uma et al. (2021), [card](../resources/examples/uma2021-learning-from-disagreement.md).

### Label distribution

**What it means.** The share of people who chose each answer for an item, for example 70% cat and 30% dog. A *soft label* is this distribution used as the training target, instead of one answer.
**In psychology.** The full response distribution of a sample, rather than its mode.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): CIFAR-10H gives about 50 human labels per image.
**Easy to get wrong.** A distribution from a few raters is noisy. CIFAR-10H uses about 50 per image for a reason.
**Read.** Peterson et al. (2019), [card](../resources/examples/peterson2019-cifar10h.md).

### Human label variation

**What it means.** The fact that people give different, plausible answers to the same item, and the research that studies it instead of treating it as error.
**In psychology.** Individual differences in judgement, and the distinction between rater error and genuine ambiguity.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md).
**Easy to get wrong.** Not all disagreement is meaningful; some is inattention. Separating the two is part of the analysis.
**Read.** Plank, B. (2022). The "problem" of human label variation: On ground truth in data, modeling and evaluation. *EMNLP 2022.* [doi:10.18653/v1/2022.emnlp-main.731](https://doi.org/10.18653/v1/2022.emnlp-main.731)

### Perspectivism

**What it means.** The view that, for many tasks, there is no single ground truth, and that the perspectives of different groups of raters should be kept and modelled.
**In psychology.** Close to the question of whose norms a measure reflects, and to cross-cultural differences in judgement.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): whose comparisons train a chat model.
**Easy to get wrong.** Keeping perspectives requires knowing who the raters are; anonymous crowd labels cannot be split by group afterwards.
**Read.** Cabitza, F., et al. (2023). Toward a perspectivist turn in ground truthing for predictive computing. *AAAI 2023.* [doi:10.1609/aaai.v37i6.25840](https://doi.org/10.1609/aaai.v37i6.25840)

### Seen and inferred

**What it means.** The distinction between what is observable in an input, such as an action or an event, and what is read into it, such as an intention or a feeling. People usually agree more on the first than on the second.
**In psychology.** The line between observation and attribution, which has been studied since Heider and Simmel (1944).
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): five observers agree on what happened, not on what it means.
**Easy to get wrong.** A model's description mixes the two. Code them separately before you compare a model with people.
**Read.** Heider & Simmel (1944), [card](../resources/examples/heider1944-moving-shapes.md).

### Rater model

**What it means.** A statistical model of how each rater produces labels, for example each rater's error rates, used to combine many imperfect ratings.
**In psychology.** Related to measurement models that separate the item, the rater and error.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): learning from many raters instead of a majority.
**Easy to get wrong.** A rater model assumes there is a true label to recover; for subjective items that assumption may not hold.
**Read.** Dawid, A. P., & Skene, A. M. (1979). Maximum likelihood estimation of observer error-rates using the EM algorithm. *Applied Statistics, 28*(1), 20–28. [doi:10.2307/2346806](https://doi.org/10.2307/2346806)

### Learning from human feedback

**What it means.** Training a model on people's judgements of its outputs, typically by having people compare or rank answers, training a reward model on those comparisons, and tuning the model to score well on it.
**In psychology.** Paired comparison, one of the oldest scaling methods, used here as a training signal.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md): ChatGPT's training rests on people's paired comparisons.
**Easy to get wrong.** The model learns the preferences of the particular people who gave the feedback, under the instructions they were given.
**Read.** Ouyang et al. (2022), [card](../resources/examples/ouyang2022-human-feedback.md); Christiano, P., et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS.* [Proceedings](https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html)

### LLM as a judge

**What it means.** Using a large language model to grade or compare answers, in place of human judges.
**In psychology.** A new rater whose reliability and biases have to be established before its ratings are used.
**Where it comes up.** [Part 2](part2-people-as-the-answer.md); in Part 4, when a model codes your data.
**Easy to get wrong.** High overall agreement can hide systematic biases. Zheng et al. (2023) report position, verbosity and self-enhancement biases.
**Read.** Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *NeurIPS 2023.* [doi:10.52202/075280-2020](https://doi.org/10.52202/075280-2020)

## Part 3 · A society: like us enough to study us?

### Machine playing people

**What it means.** A model set up to play people: a virtual student, a simulated class or town, a group of agents, or a participant in a study. Sometimes it plays the people around someone, such as the class a trainee teacher faces; sometimes it answers in a participant's place. Either way, the conclusion drawn is about how real people behave.
**In psychology.** Close to a simulation or a confederate, but one whose behaviour is generated, not scripted.
**Where it comes up.** [Part 3](part3-people-we-make.md): is it like us enough to study us? Also [Part 4](part4-ai-in-your-research.md), where a simulated participant pretests a study.
**Easy to get wrong.** A model that plays people behaves partly as the setup tells it to. That it acts like a kind of person is not yet evidence about such people.
**Read.** [Key readings for Part 3](part3-people-we-make.md#key-readings).

### Persona

**What it means.** A description given to a model, in its instructions, of who it should be: traits, background, opinions or a role.
**In psychology.** An experimental manipulation: a condition the researcher sets, whose effect has to be checked.
**Where it comes up.** The opening of the talk: the persona prompt in the Turing test. [Part 3](part3-people-we-make.md): virtual students.
**Easy to get wrong.** Equivalent wordings of the same persona can give different results; report all of them.
**Read.** Serapio-García et al. (2025), [card](../resources/examples/serapio2025-personality.md); Jones & Bergen (2026), [card](../resources/examples/jones2026-turing-test.md).

### Manipulation check

**What it means.** A test of whether a manipulation did what it was meant to do. For a persona, the talk's check: did it move the trait it names, and mainly that trait? Wordings that should mean the same should also give the same result.
**In psychology.** Standard practice in experimental social psychology before interpreting an effect of a manipulation.
**Where it comes up.** [Part 3](part3-people-we-make.md): a persona is a manipulation.
**Easy to get wrong.** A questionnaire on the trait is the first check, as in the talk, and it can pass. Behaviour the persona did not name is a stronger check.
**Read.** Serapio-García et al. (2025), [card](../resources/examples/serapio2025-personality.md).

### Silicon sample

**What it means.** A set of model responses produced by conditioning a language model on the backgrounds of real survey respondents, used in place of a human sample. The term comes from Argyle et al. (2023).
**In psychology.** A simulated sample; it raises the same questions as any convenience sample, in addition to new ones.
**Where it comes up.** [Part 3](part3-people-we-make.md) and [Part 4](part4-ai-in-your-research.md).
**Easy to get wrong.** Matching a group's average answer is not matching its spread; silicon samples can flatten differences within groups.
**Read.** Argyle et al. (2023), [card](../resources/examples/argyle2023-silicon-samples.md).

### Algorithmic fidelity

**What it means.** The degree to which a model, suitably conditioned, reproduces the response distributions of particular human subgroups. The term comes from Argyle et al. (2023).
**In psychology.** A kind of criterion validity for a simulated sample.
**Where it comes up.** [Part 3](part3-people-we-make.md).
**Easy to get wrong.** Fidelity shown on one set of questions and one population does not carry over automatically to others.
**Read.** Argyle et al. (2023), [card](../resources/examples/argyle2023-silicon-samples.md).

### Turing test

**What it means.** Turing's imitation game: a judge chats by text with a machine and a human and says which is which. In the standard three-party version, the judge talks to both at once.
**In psychology.** A blind rating, and also a measure of how people tell humans from machines.
**Where it comes up.** The opening of the talk ([start here](start-here.md)): Turing's test, run again in 2026 (Jones & Bergen). [Part 3](part3-people-we-make.md): which reply is the real person?
**Easy to get wrong.** Passing shows that the conversation looks human to these judges, not that a human-like mind lies behind it.
**Read.** Turing, A. M. (1950). Computing machinery and intelligence. *Mind.* [doi:10.1093/mind/lix.236.433](https://doi.org/10.1093/mind/lix.236.433); Jones & Bergen (2026), [card](../resources/examples/jones2026-turing-test.md).

### Generative agent

**What it means.** A software agent built on a language model, with memory, reflection and planning, that produces believable behaviour over time and interacts with other agents.
**In psychology.** A simulated person whose behaviour is generated, not specified by rules in advance.
**Where it comes up.** [Part 3](part3-people-we-make.md): Smallville.
**Easy to get wrong.** Generative agents are usually judged by believability, which is not the same as agreement with how real people behave.
**Read.** Park et al. (2023), [card](../resources/examples/park2023-generative-agents.md).

### Conformity

**What it means.** Changing one's answer to match a group. Asch showed that many people give a clearly wrong answer when everyone before them does.
**In psychology.** A classic paradigm of social influence, with well-known controls such as a single dissenter.
**Where it comes up.** [Part 3](part3-people-we-make.md): an Asch-style test for AI agents.
**Easy to get wrong.** Agents that conform behave like people in that respect; it does not follow that they conform for the same reasons.
**Read.** Asch, S. E. (1955). Opinions and social pressure. *Scientific American.* [doi:10.1038/scientificamerican1155-31](https://doi.org/10.1038/scientificamerican1155-31); Weng et al. (2025), [card](../resources/examples/weng2025-conformity.md).

### Agent-based model

**What it means.** A simulation in which many individual agents follow behavioural rules and interact, so that group-level patterns emerge from individual behaviour.
**In psychology.** Used in social psychology and sociology to ask which individual-level mechanisms can produce an observed social pattern.
**Where it comes up.** [Part 3](part3-people-we-make.md): from simple rule-based agents to agents built on language models.
**Easy to get wrong.** A model that reproduces a pattern shows one way it could arise, not that it arises that way among people.
**Read.** Schelling, T. C. (1971). Dynamic models of segregation. *Journal of Mathematical Sociology.* [doi:10.1080/0022250x.1971.9989794](https://doi.org/10.1080/0022250x.1971.9989794)

## Part 4 · AI in your own research

### AI coder

**What it means.** A language model used to label or code material for research, such as sorting texts into categories, rating sentiment or coding open-ended answers.
**In psychology.** A new coder in a content analysis, whose reliability must be checked against human coders before its codes are used.
**Where it comes up.** [Part 4](part4-ai-in-your-research.md): a model can help code your data if you treat it as a new coder.
**Easy to get wrong.** Repeated runs of one model are not independent coders; agreement between them says little about validity.
**Read.** Gilardi et al. (2023), [card](../resources/examples/gilardi2023-ai-annotation.md).

### Prompt sensitivity

**What it means.** The change in a model's output when the wording of the instruction changes in ways that should not matter, or when the same input is simply run again.
**In psychology.** Like sensitivity of a measure to the wording of an item, which test construction tries to remove.
**Where it comes up.** [Part 4](part4-ai-in-your-research.md), and in [Part 3](part3-people-we-make.md) as equivalent wordings of a persona.
**Easy to get wrong.** Reporting one prompt hides how much the result depends on it; reword at least once and report both.
**Read.** Reiss (2023), with the [Gilardi card](../resources/examples/gilardi2023-ai-annotation.md).

### Prediction-powered inference

**What it means.** A statistical framework that combines a large set of model predictions with a smaller set of human labels to give valid confidence intervals, without assuming the model is correct.
**In psychology.** A way to keep inference valid when most of the measurement is done by an imperfect tool, calibrated on a random subsample.
**Where it comes up.** [Part 4](part4-ai-in-your-research.md): what you can still conclude when a model codes most of your data.
**Easy to get wrong.** The human-labelled items must be a random sample of the same material.
**Read.** Angelopoulos et al. (2023), [card](../resources/examples/angelopoulos2023-prediction-powered-inference.md).

### Simulated participant

**What it means.** A language model prompted to respond as a research participant would, used to pretest materials, predict results or, controversially, replace a sample.
**In psychology.** A pilot participant whose responses are generated; useful for checking materials, not for estimating how people respond.
**Where it comes up.** [Part 4](part4-ai-in-your-research.md): a simulated participant can pretest a study; it does not replace the sample.
**Easy to get wrong.** Correct predictions of direction can come with wrong sizes: simulated effects can be too large.
**Read.** Ashokkumar et al. (2026), [card](../resources/examples/ashokkumar2026-predicting-experiments.md); Argyle et al. (2023), [card](../resources/examples/argyle2023-silicon-samples.md).

## Index

[Agent-based model](#agent-based-model) · [AI coder](#ai-coder) · [Algorithmic fidelity](#algorithmic-fidelity) · [Clever Hans effect](#clever-hans-effect) · [Cohen's kappa](#cohens-kappa) · [Conformity](#conformity) · [Cue](#cue) · [Cue conflict](#cue-conflict) · [Error consistency](#error-consistency) · [Explanation method](#explanation-method) · [Generative agent](#generative-agent) · [Gold label and majority vote](#gold-label-and-majority-vote) · [Human baseline](#human-baseline) · [Human label variation](#human-label-variation) · [Inter-rater reliability](#inter-rater-reliability) · [Krippendorff's alpha](#krippendorffs-alpha) · [Label distribution](#label-distribution) · [Learning from human feedback](#learning-from-human-feedback) · [LLM as a judge](#llm-as-a-judge) · [Machine playing people](#machine-playing-people) · [Manipulation check](#manipulation-check) · [Out-of-distribution data](#out-of-distribution-data) · [Persona](#persona) · [Perspectivism](#perspectivism) · [Prediction-powered inference](#prediction-powered-inference) · [Prompt sensitivity](#prompt-sensitivity) · [Psychophysics](#psychophysics) · [Rater model](#rater-model) · [Reference](#reference) · [Seen and inferred](#seen-and-inferred) · [Shape bias](#shape-bias) · [Shortcut learning](#shortcut-learning) · [Silicon sample](#silicon-sample) · [Simulated participant](#simulated-participant) · [Turing test](#turing-test)
