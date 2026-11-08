# PingBot — Table Tennis Rules Assistant 🏓

PingBot is a Python-based NLP FAQ chatbot designed to answer questions related to the official Laws of Table Tennis. It provides users with information about table tennis rules through a simple, interactive conversational interface.

The chatbot uses keyword-based text matching and a predefined knowledge base to identify user questions and generate relevant responses. Its purpose is to make understanding table tennis rules easier and more accessible.

## Features

- **Rule-Based Question Answering:** Answers questions using a predefined table tennis rules knowledge base.
- **Keyword Matching:** Identifies relevant questions using keyword-based scoring.
- **Question Normalization:** Processes user input by converting text to lowercase and removing unnecessary characters.
- **Multiple Rule Categories:** Covers scoring, serving, doubles, equipment, penalties, and other table tennis regulations.
- **Conversational Interface:** Provides an interactive chat experience using Gradio.
- **Fallback Responses:** Handles unrelated or unmatched questions without generating unsupported answers.
- **Official References:** Includes links to the official ITTF rules for further information.

## Topics Covered

PingBot's knowledge base includes:

- Scoring and Game Rules
- Match Format
- Service Rotation
- Legal Service Requirements
- Net Services and Let Rules
- Singles and Doubles Playing Order
- Points and Obstruction
- Racket Requirements
- Ball Specifications
- Table and Net Dimensions
- Expedite System
- Intervals and Breaks
- Coaching and Advice
- Conduct and Penalties
- Wheelchair and Para Table Tennis
- Umpire Decisions

## Technologies Used

- **Python 3:** Core programming language.
- **Regular Expressions (re):** Text normalization and processing.
- **Gradio:** Interactive chatbot frontend and user interface.

## How It Works

1. The user enters a table tennis-related question.
2. PingBot normalizes the input text.
3. The keyword-matching system compares the question against predefined keywords in its knowledge base.
4. A scoring mechanism identifies the most relevant rule category.
5. The corresponding answer is displayed in the chatbot interface.
6. If no relevant match is found, PingBot provides a fallback response.

## Project Structure

```text
PingBot/
│
├── maincode.py
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd PingBot
```

**3. Install the required dependency**

```bash
pip install gradio
```

**4. Run the application**

```bash
python maincode.py
```

The chatbot will launch in your default web browser.

## Learning Objectives

- Understand basic Natural Language Processing (NLP) concepts.
- Practice text preprocessing and normalization.
- Learn keyword-based question matching.
- Work with Python lists, dictionaries, and functions.
- Understand how to build an interactive chatbot.
- Gain practical experience with the Gradio library.
- Apply programming concepts to a real-world conversational application.

## Limitations

- The chatbot uses predefined rules rather than a trained machine learning model.
- Its answers depend on the keywords available in its knowledge base.
- It does not automatically retrieve or update information from the ITTF website.
- It may fail to recognize questions that do not match its predefined keywords.

## Future Improvements

- Implement more advanced NLP techniques.
- Improve semantic understanding of user questions.
- Expand the knowledge base with additional ITTF regulations.
- Introduce machine learning-based intent classification.
- Improve conversational context and follow-up question handling.

## Reference

**Official Source:** [ITTF — International Table Tennis Federation](https://www.ittf.com/statutes/)

## Author

**Muhammad Saim**

GitHub: https://github.com/saimkabirdev-svg

---

*PingBot is an educational AI Lab mini project developed to demonstrate basic NLP concepts, rule-based chatbot development, and interactive application development using Python.*
