import re


def count_specific_word(text, search_word):
    """
    Count occurrences of a specific word using substring matching.
    """
    if not text or not search_word:
        return 0

    text_lower = text.lower()
    search_lower = search_word.lower()
    count = 0
    position = 0

    while True:
        position = text_lower.find(search_lower, position)
        if position == -1:
            break
        count += 1
        position += len(search_lower)

    return count


def identify_most_common_word(text):
    """
    Identify the most common word using regex to extract words.
    """
    if not text.strip():
        return None

    words = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())

    if not words:
        return None

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_word = words[0]
    highest_count = word_counts[most_common_word]

    for word in words:
        if word_counts[word] > highest_count:
            most_common_word = word
            highest_count = word_counts[word]

    return most_common_word


def calculate_average_word_length(text):
    """
    Calculate the average length of words.
    Punctuation and special characters are excluded.
    """
    if not text.strip():
        return 0

    words = re.findall(r"[a-zA-Z0-9]+", text)

    total_length = 0

    for word in words:
        total_length += len(word)

    if len(words) == 0:
        return 0
    else:
        return float(total_length / len(words))


def count_paragraphs(text):
    """
    Count paragraphs separated by empty lines.
    """
    if not text.strip():
        return 1

    paragraphs = text.strip().split("\n\n")

    return len(paragraphs)


def count_sentences(text):
    """
    Count sentences based on periods, exclamation marks,
    and question marks.
    """
    if not text.strip():
        return 1

    sentences = re.findall(r"[^.!?]+[.!?]", text)

    return len(sentences)


def main():
    """
    Read the news article and display the analysis results.
    """

    try:
        with open("news_article.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: news_article.txt was not found.")
        return

    search_word = input("Enter the word you want to count: ").strip()

    specific_word_count = count_specific_word(text, search_word)
    most_common_word = identify_most_common_word(text)
    average_word_length = calculate_average_word_length(text)
    paragraph_count = count_paragraphs(text)
    sentence_count = count_sentences(text)

    print()
    print("--------------- RESULTS ---------------")
    print(
        f"Occurrences of '{search_word}': "
        f"{specific_word_count}"
    )
    print(f"Most common word: {most_common_word}")
    print(f"Average word length: {average_word_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")
    print("---------------------------------------")


if __name__ == "__main__":
    main()
