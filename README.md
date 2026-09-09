# Book Passage Analyzer

A modular Python tool that analyzes book excerpts to compute word counts, infer dominant emotional tone, match candidate book titles using thematic keyword sets, and generate a concise extractive summary.

Built entirely using Python standard libraries (`os`, `re`) with zero external dependencies.

## Features

- **Word Count:** Accurately counts tokens using regular expression word boundaries.
- **Emotion Detection:** Analyzes text against categorized emotion lexicons (Joy, Sadness, Anger, Fear) with a neutral fallback state.
- **Candidate Book Matching:** Compares thematic vocabulary against profiles from notable works (e.g., *The Alchemist*, *Man's Search for Meaning*, *To Kill a Mockingbird*).
- **Extractive Summarization:** Ranks sentences based on key content-word frequencies while ignoring common stopwords, selecting the top 2 sentences in chronological order.
- **Flexible Input:** Accepts direct text, a local `.txt` file path, or defaults to an embedded sample passage if Enter is pressed without typing.

## How to Run

1. Clone or download this repository.
2. Run the script using Python 3:

```bash
python passage_analyzer.py
# book-passage-analyzer
