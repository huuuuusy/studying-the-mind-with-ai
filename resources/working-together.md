**English** · [中文](working-together.zh.md)

# Working together: psychology and AI research

This page is written by an AI researcher for psychology researchers and students who would like to work with AI researchers on the question of the talk: **it looks capable; how would we know it really is?** Neither side can answer it alone. AI research has the models, the benchmarks (standard test sets) and the engineering to run them on many items. Psychology has the methods that tell a capable-looking performance from a capable one: controlled designs, measurement and validity, samples of real people, reliability and ethics.

The page sets out what each side brings, four ways to work together (one for each of the first three parts of the talk, plus one for your own research), what to agree on before you start, and the misunderstandings that come up most often in both directions. Each way of working comes with readings and a published study to learn from.

A backup page of the talk, on starting a study with an AI researcher, suggests four kinds of first study: comparing errors (Part 1), building a human reference (Part 2), checking a persona and running a blind rating (both Part 3). Here, the first two are ways 1 and 2, and the persona check and the blind rating both belong to way 3; way 4, a model in your own study, has no counterpart on that page.

## What each side brings

| Area | Psychology brings | AI research brings |
|---|---|---|
| The question | a construct, and what would count as evidence for it | a model, and the task it is said to do well |
| Design | paradigms, control conditions, counterbalancing, pre-registration | access to models, prompts and settings; running thousands of items, many times |
| People | samples, recruitment, consent and ethics approval | benchmarks and data sets, often with one label per item |
| Measurement | reliability, validity, psychometrics | metrics such as accuracy, and item-level outputs |
| Analysis | effect sizes, comparison with the spread among people | explanation methods, training and fine-tuning (further training of an existing model), simulations of many agents |

## Four ways to work together

### 1. Design a controlled comparison together

*Part 1 · One person: right answer, right reason? The check: compare the mistakes, not only the scores.*

- **The question.** A model scores close to people on a task. Does it get there for the same reasons?
- **Psychology brings.** The task and its items; the cue you suspect the model uses; a control condition that separates that cue from the one you meant to test; a sample of people tested under the same conditions.
- **AI research brings.** One or several models run on the same items, with item-level output; for image models, explanation maps that show where a model looked.
- **Agree on.** The same items and conditions for people and model; right and wrong recorded per item on both sides; the range among people as the reference, not 100%.
- **Read first.** Geirhos, Meding & Wichmann (2020) on error consistency; Pfungst (1911) on Clever Hans.
- **Model study.** [Close scores, different mistakes](examples/geirhos2020-error-consistency.md).

### 2. Build a human reference together

*Part 2 · A group: whose standard does it follow? The check: compare with a group, not one person.*

- **The question.** A model is said to agree with "the human label". Whose label is it, and how much do people agree with each other?
- **Psychology brings.** A rating design; how raters are sampled; inter-rater reliability; keeping what is seen (an action) apart from what is inferred (a feeling).
- **AI research brings.** Model outputs on many items and repeated runs; evaluation, or training, against the distribution of people's answers rather than a single label.
- **Agree on.** Several raters per item; every rater's answers kept, not only the majority; the model's agreement reported against the agreement among people, and whether it keeps their spread.
- **Read first.** Heider & Simmel (1944); Morgenroth et al. (2025), Emo-FilM, *Scientific Data*, [doi](https://doi.org/10.1038/s41597-025-04803-5). In Emo-FilM, raters agreed only moderately on emotion moment by moment.
- **Model studies.** [About fifty people per image](examples/peterson2019-cifar10h.md) and [Forty-four raters, fourteen films](examples/morgenroth2025-emo-film.md).

### 3. Test a simulation together

*Part 3 · A society: is it like us enough to study us? The check: compare it with real people.*

- **The question.** A simulated participant, or a group of agents, acts like a kind of person. Does the persona do what it says, and does the simulation match real people?
- **AI research brings.** Personas, agents and multi-agent simulations; running them many times, under several wordings of the same instruction.
- **Psychology brings.** The manipulation check; validated questionnaires and behavioural measures; data from real people to compare with; the blind rating.
- **Agree on.** What counts as a pass, written down before anyone looks at the results; several equivalent wordings of every persona; a comparison with real people at the level the claim is about, whether one person, a group or a whole class.
- **Read first.** Serapio-García et al. (2025); Turing (1950); Jones & Bergen (2026); Park et al. (2023).
- **Model studies.** [Measuring and shaping a model's personality](examples/serapio2025-personality.md) and [A three-party Turing test, with a persona](examples/jones2026-turing-test.md).

### 4. Bring a model into your own study

*Part 4 · AI in your own research.*

- **The question.** A model codes your data, or answers your materials as a pretest. What can you still conclude about people?
- **AI research brings.** Choosing a model and setting it up; running it the same way every time; keeping the outputs of every run.
- **Psychology brings.** The coding scheme and the human coders the model is checked against; the real sample, of which a simulated pretest is no replacement; the validation.
- **Agree on.** The model, version, date, full prompt, settings and number of runs, recorded; at least one rewording; agreement with two people checked before the model's codes are used.
- **Model studies.** [A model as a coder](examples/gilardi2023-ai-annotation.md) and [Predicting the results of experiments](examples/ashokkumar2026-predicting-experiments.md).

## Before you start: what to agree on

- **The claim**, in one sentence, and the level it is about: one person, a group or a society.
- **The data.** Who provides which data; public data where possible; ethics approval and consent before anything is collected from people.
- **The model record.** The model, version, date, full prompt, settings and number of runs, kept for every condition.
- **What counts as a pass**, decided before anyone looks.
- **Who does what**, and how authorship will be decided.

## Common misunderstandings, in both directions

- **"A higher score means more human-like."** Close scores can hide different mistakes; compare which items each gets wrong ([Part 1](../docs/part1-people-next-to-machine.md)).
- **"The human label is the answer."** It is one reading of the item, and people often disagree; compare the model with the spread among people ([Part 2](../docs/part2-people-as-the-answer.md)).
- **"If people cannot tell it apart, it is like people."** A blind rating shows that the output looks human, not what lies behind it ([Part 3](../docs/part3-people-we-make.md)).
- **"One prompt is one experiment."** A model's output can change with the wording of the prompt, or simply on a second run; reword, repeat and report every run ([Part 4](../docs/part4-ai-in-your-research.md)).
- **"A model is a black box, so its behaviour cannot be studied."** Its behaviour can be studied with the designs psychology already uses for people: controlled items, item-level data and manipulation checks.
- **"A simulated sample can replace the participants."** Simulated samples have predicted the direction of real effects but overestimated their size; use them as a pretest, not as the sample ([Part 4](../docs/part4-ai-in-your-research.md)).

**Start where psychology is strongest: measurement and design.**
