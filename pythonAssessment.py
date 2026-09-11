from typing import Optional
from pathlib import Path
from collections import Counter
import re


def count_specific_word(text: str, search_word: str) -> int:
    """
    Count how many times a specific word appears in the text.
    The comparison is case-insensitive.
    """
    if not text or not search_word:
        return 0

    words = re.findall(
        r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*",
        text.lower()
    )

    count = 0
    index = 0
    while index < len(words):
        if words[index] == search_word.lower():
            count += 1
        index += 1

    return count


def identify_most_common_word(text: str) -> Optional[str]:
    """
    Identify the word that appears most frequently in the text.
    Return None if the text is empty.
    """
    if not text.strip():
        return None

    words = re.findall(
        r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*",
        text.lower()
    )

    if not words:
        return None

    return Counter(words).most_common(1)[0][0]


def calculate_average_word_length(text: str) -> float:
    """
    Calculate the average length of words in the text.
    Punctuation and special characters are excluded.
    """
    if not text.strip():
        return 0

    words = re.findall(
        r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*",
        text
    )

    if not words:
        return 0

    lengths = [
        len(word.replace("-", "").replace("'", ""))
        for word in words
    ]

    return sum(lengths) / len(lengths)


def count_paragraphs(text: str) -> int:
    """
    Count the number of paragraphs.
    Paragraphs are separated by empty lines.
    """
    if not text.strip():
        return 1

    paragraphs = re.split(
        r"\n\s*\n",
        text.strip()
    )

    return len(paragraphs)


def count_sentences(text: str) -> int:
    """
    Count the number of sentences.
    Sentences end with '.', '!' or '?'.
    """
    if not text.strip():
        return 1

    sentences = re.findall(
        r"[^.!?]+(?:[.!?]+|$)",
        text.strip()
    )

    return sum(
        1
        for sentence in sentences
        if sentence.strip()
    )


def main() -> None:
    """
    Main program that reads the article and displays
    all text analysis results.
    """

    article_file = Path("news_article.txt")

    try:
        text = article_file.read_text(
            encoding="utf-8"
        )

    except FileNotFoundError:
        print(f"Error: Could not find '{article_file}'.")
        print(
            "Place news_article.txt in the same folder "
            "as pythonAssessment.py."
        )
        return

    print("======================================")
    print("      NEWS ARTICLE TEXT ANALYSIS")
    print("======================================")

    search_word = input(
        "Enter the word you want to count: "
    ).strip()

    specific_word_count = count_specific_word(
        text,
        search_word
    )

    most_common_word = identify_most_common_word(
        text
    )

    average_word_length = calculate_average_word_length(
        text
    )

    paragraph_count = count_paragraphs(text)

    sentence_count = count_sentences(text)

    print()
    print("--------------- RESULTS ---------------")

    print(
        f"Occurrences of '{search_word}': "
        f"{specific_word_count}"
    )

    print(
        f"Most common word: "
        f"{most_common_word}"
    )

    print(
        f"Average word length: "
        f"{average_word_length:.2f}"
    )

    print(
        f"Number of paragraphs: "
        f"{paragraph_count}"
    )

    print(
        f"Number of sentences: "
        f"{sentence_count}"
    )

    print("---------------------------------------")


if __name__ == "__main__":
    main()