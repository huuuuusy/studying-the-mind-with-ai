**English** · [中文](rathje2024-psychological-text.zh.md)

# Psychological text analysis in twelve languages

**Study.** Rathje, S., Mirea, D.-M., Sucholutsky, I., Marjieh, R., Robertson, C. E., & Van Bavel, J. J. (2024). GPT is an effective tool for multilingual psychological text analysis. *Proceedings of the National Academy of Sciences, 121*(34), e2308950121. [doi:10.1073/pnas.2308950121](https://doi.org/10.1073/pnas.2308950121)

**In the talk.** Not shown; read it with [Part 4, AI in your own research](../../docs/part4-ai-in-your-research.md): a model can help measure psychological constructs in text, checked against human raters and existing methods.

**Question.** Psychology often measures constructs in text: sentiment, emotion, morality. Can a general-purpose language model, asked with simple prompts, measure them as well as existing methods, and in several languages?

**Method.** Fifteen data sets were used: 47,925 tweets and news headlines that people had already annotated, in 12 languages. Three versions of GPT (3.5 Turbo, 4 and 4 Turbo) were asked to detect sentiment, discrete emotions, offensiveness and moral foundations, using simple prompts such as "is this text negative?". Their answers were compared with the human annotations (the annotators are what psychology calls raters), and with dictionary methods and fine-tuned machine-learning models (models trained further for one task).

**Finding.** GPT's agreement with the human annotators (r = 0.59 to 0.77) was much higher than that of English-language dictionary analysis (r = 0.20 to 0.30). It came close to, and sometimes beat, several top fine-tuned models. Performance improved with successive versions, especially for lesser-spoken languages, and became cheaper.

**Why read it.** It is the most direct evidence for the everyday use psychologists are most likely to make of a language model, measuring constructs in text, and it compares the model with the methods psychologists already use.

**Limits.** "Accurate" here means agreement with the existing human annotations, so the model is only as valid as those annotations. Correlations of 0.6 to 0.8 leave room for systematic differences on particular kinds of text, and model versions change.

**Data and code.** The article provides sample code and a video tutorial for analysing text with the GPT application programming interface.
