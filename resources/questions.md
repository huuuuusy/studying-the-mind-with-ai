**English** · [中文](questions.zh.md)

# Questions psychologists bring

Psychologists who hear the talk often arrive with a question from their own work. This page takes
six of them. For each it gives the talk's short answer, the part of the talk that bears on it, and
what to read first. It offers readings and interpretation, not a study design: the design is yours
to make, with your own measures, ethics approval and participants.

The six, in brief:

1. [Can AI help measure well-being, or any construct?](#1-can-ai-help-measure-well-being-or-any-construct)
2. [Will AI add to human contact, or replace it?](#2-will-ai-add-to-human-contact-or-replace-it)
3. [A companion, a tutor or a robot: what makes it work?](#3-a-companion-a-tutor-or-a-robot-what-makes-it-work)
4. [Many signals at once: which model should I use?](#4-many-signals-at-once-which-model-should-i-use)
5. [Gaze, faces and deception: what does a model really read?](#5-gaze-faces-and-deception-what-does-a-model-really-read)
6. [Can an agent take part in a cognitive or emotion task?](#6-can-an-agent-take-part-in-a-cognitive-or-emotion-task)

## 1. Can AI help measure well-being, or any construct?

**The short answer.** It can add evidence, but it cannot settle validity. A model trained on a scale
learns the scale, not the thing behind it.

**In the talk.** [Part 4, evaluation](../docs/part4-ai-in-your-research.md#what-the-talk-showed):
use a group of raters as the reference, and look past the average. The talk's answer to this
question adds that raters' agreement is the ceiling: inter-rater reliability. Test a model's
validity like any new measure. [Part 2](../docs/part2-people-as-the-answer.md) shows why one label hides how much people
differ.

**What to keep in mind.**
- Agreement with a scale is not validity. Language models can score open answers about well-being
  almost as well as the rating scales' own reliability allows (Kjell et al., 2022,
  [doi](https://doi.org/10.1038/s41598-022-07520-w)); that shows the text tracks the scale, and the
  question of what both measure remains.
- A model may have read your items. Well-known questionnaires and their answers are in its training
  text, so a right answer can be recall; compare familiar items with new ones.
- Simulated respondents agree too much: averages close to people's, too little spread
  (Bisbee et al., 2024, [doi](https://doi.org/10.1017/pan.2024.5)).
- A scorer built in one language and used in another raises a question psychology already has a
  name for: measurement invariance.

**Read.** [Psychological text analysis in twelve languages](examples/rathje2024-psychological-text.md);
the field-wide list on [machine-read psychological assessment, with validity critiques](literature.md#behaviour-sensing-and-machine-read-psychological-assessment-with-validity-critiques);
the reading list on [measurement and psychometrics](students.md#measurement-and-psychometrics).

## 2. Will AI add to human contact, or replace it?

**The short answer.** This is a view, not a finding, and the evidence so far is mixed. A better
question than "will it replace us?" is "which designs add to contact, and which take its place?"

**In the talk.** The [closing view](../docs/start-here.md#why-now) gives it as an example of finding
your own crossing: start from a question your field asks best, and bring AI to it.

**What to keep in mind.**
- In a four-week randomised study with 981 people, the assigned chatbot conditions made no clear
  difference, but people who chose to use the chatbot more reported worse outcomes, including more
  loneliness; the design cannot say that the use caused it (Fang et al., 2025,
  [arXiv:2503.17473](https://arxiv.org/abs/2503.17473)).
- What people believe about the source matters. AI-written replies made people feel more heard than
  human ones, until they learned that the reply came from AI (Yin, Jia & Wakslak, 2024,
  [doi](https://doi.org/10.1073/pnas.2319112121)).
- Whether an AI "is a person" is a question for philosophy and ethics; behavioural tests cannot
  settle it.

**Read.** [What language models can and cannot do for psychology](examples/demszky2023-llms-in-psychology.md),
for the concerns that come with each use.

## 3. A companion, a tutor or a robot: what makes it work?

**The short answer.** Take the chain apart: what the agent does, what the person feels, and what
changes. Measure each link, not only the outcome.

**In the talk.** [Part 4, agent modelling](../docs/part4-ai-in-your-research.md#what-the-talk-showed):
fix what the agent decides and let only the words vary, which psychology calls treatment fidelity,
and check it over time, which it calls test–retest. [Part 3](../docs/part3-people-we-make.md) shows how a persona drifts.

**What to keep in mind.**
- The same input can give different outputs, so delivery can differ between participants unless the
  decisions are fixed.
- A persona set in a prompt drifts in a long conversation; one study found clear drift within eight
  rounds (Li et al., 2024, [arXiv:2402.10962](https://arxiv.org/abs/2402.10962)). Consistency is
  tested across sessions: tell the agent something in the first, and ask about it in a later one.
- How responsive the agent is and how responsive it feels are two measures, and beliefs about the
  source change the second (question 2).
- A robot adds sensing, movement and control to everything a virtual agent needs; a virtual agent is
  the simpler place to test the chain first.

**Read.** [Measuring and shaping a model's personality](examples/serapio2025-personality.md); the
field-wide list on [personas and personality in language models](literature.md#personas-and-personality-in-llms).

## 4. Many signals at once: which model should I use?

**The short answer.** Start from the question and the data, not the model. Decide what matters
most: predicting well, running fast, or knowing why. Real-world data often do not need a complex
model at first.

**In the talk.** [Part 4, multimodal learning](../docs/part4-ai-in-your-research.md#what-the-talk-showed):
take one signal away, and test where the data change (new people, new rooms, harder clips).

**What to keep in mind.**
- Put every stream on one clock. Physiological, environmental and self-report data run at
  different rates, and the body responds with a lag.
- Many hours of signal can still be few people. Keep each person on one side of the split, so that
  the model is tested on people it has never seen.
- Signals drop out, and not always at random: a sensor may come off just when someone is
  uncomfortable. Plan for missing data before collecting it.
- If you need to know which factors drive a prediction, say so before choosing the model; a simple
  model you can read may serve better than a strong one you cannot.

**Read.** [Forty-four raters, fourteen films](examples/morgenroth2025-emo-film.md), an open data set
with continuous emotion ratings, brain imaging and physiology; the field-wide list of
[data sets with several human annotators per item](literature.md#datasets-with-several-human-annotators-per-item).

## 5. Gaze, faces and deception: what does a model really read?

**The short answer.** Check the stimuli before the model. A cue that goes with the answer in your
videos can make a model, or a group of people, look accurate.

**In the talk.** [Part 1](../docs/part1-people-next-to-machine.md): Clever Hans read his
questioner's head, and an image model read a tag. [Part 4, multimodal learning](../docs/part4-ai-in-your-research.md#what-the-talk-showed)
asks you to take one signal away and test again.

**What to keep in mind.**
- On one public deception data set, predicting only the person's sex did about as well as leading
  AI lie detectors (Mambreyan et al., 2022,
  [accepted version](https://www.repository.cam.ac.uk/handle/1810/338298)).
- A face reader measures facial movements; calling them emotions is an inference that needs context
  (Barrett et al., 2019; see the [reading list on emotion](students.md#emotion-and-affective-science)).
- Eye tracking records where the centre of gaze lands. Part 1's theory of vision gives the
  periphery the job of noticing where to look, so some of what people use may never become a
  fixation; and what people say they looked at may differ from where their eyes went.
- Faces and hands move, so a fixed area of interest soon points at the wrong place; following a
  region frame by frame is the tracking problem of Part 1.

**Read.** [A right answer found in the wrong place](examples/lapuschkin2019-clever-hans.md);
[Close scores, different mistakes](examples/geirhos2020-error-consistency.md); the field-wide list
on [process and evidence evaluation, including gaze](literature.md#process-and-evidence-evaluation-grounding-gaze-stepwisecausal-reasoning-calibration).

## 6. Can an agent take part in a cognitive or emotion task?

**The short answer.** It can take the task, but a matching choice is not a matching process.
Compare errors and conditions, not only choices.

**In the talk.** [Part 1](../docs/part1-people-next-to-machine.md) compares mistakes, not only
scores; [Part 3](../docs/part3-people-we-make.md) and [Part 4, agent modelling](../docs/part4-ai-in-your-research.md#what-the-talk-showed)
compare the whole range with real people.

**What to keep in mind.**
- Classic tasks and their answers are in the training text. GPT-3 solved a well-known card task but
  failed once the cards were reordered (Binz & Schulz, 2023,
  [doi](https://doi.org/10.1073/pnas.2218523120)); a new variant tests more than the classic.
- Simulated participants are more consistent, and more alike, than people
  ([Aher et al., 2023](literature.md#simulated-participants-and-silicon-samples)); individual
  differences are often what a study is about.
- An agent can name an emotion-regulation strategy and pick one, but it has no body whose state the
  strategy changes. A high score on an emotion test shows it knows the keyed answers, not what it
  responds to (Schlegel et al., 2025, in the [reading list on emotion](students.md#emotion-and-affective-science)).

**Read.** [Out of one, many: silicon samples](examples/argyle2023-silicon-samples.md); the
field-wide lists on [language models on cognitive-psychology tasks](literature.md#llmsvlms-on-cognitive-psychology-tasks-and-batteries-incl-critiques)
and [simulated participants](literature.md#simulated-participants-and-silicon-samples).

---

Ready to talk with an AI researcher about one of these? See [where the two fields meet](working-together.md).
Back to [Start here](../docs/start-here.md).
