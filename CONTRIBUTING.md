# Contributing

Thank you for helping. Corrections, broken links, clearer explanations and suggested readings
are all welcome.

## Small fixes

A typo, a broken link or a clearer sentence: open a pull request directly.

## Suggesting a reading

Open an issue or a pull request with:

- the full reference and a link to the publisher, DOI, arXiv or OpenReview page;
- where it belongs (which part of the talk, and which group in the field-wide list);
- one sentence on why it is worth reading.

## Rules

- **Links, not files.** No PDFs or copied text from papers.
- **Check before you add.** Give the published title and venue, and check the link opens.
- **Numbers from the source.** Every number on a key-reading card must appear in the paper it describes.
- **Published or public work only.** No unpublished data, no participant responses, no private logs.
- **Data sets with their terms.** When you list a data set, say how it is accessed and under which licence.

## Checks

`python3 .github/scripts/check_links.py` checks that every relative link and heading in the
Markdown files exists. The same check runs on every pull request.

## Licence of contributions

By contributing you agree that your text and figures are released under
[CC BY-NC 4.0](LICENSE) and any code under the [MIT licence](LICENSE-code.txt), as for the rest
of the repository. Do not add or modify the talk's drawings in `docs/figures/talk/`.
