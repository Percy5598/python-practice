# text_analyzer.py

import re
from collections import Counter


def clean_text(text):
    """Convert text to lowercase and remove punctuation."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def tokenize(text):
    """Split text into individual words."""
    return text.split()


def analyze_text(text):
    # Basic statistics
    character_count = len(text)

    words = tokenize(clean_text(text))
    word_count = len(words)

    sentences = re.split(r"[.!?]+", text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    sentence_count = len(sentences)

    # Word frequency
    word_frequency = Counter(words)

    # Average word length
    if words:
        average_word_length = sum(len(word) for word in words) / len(words)
    else:
        average_word_length = 0

    return {
        "characters": character_count,
        "words": word_count,
        "sentences": sentence_count,
        "word_frequency": word_frequency,
        "average_word_length": average_word_length,
    }


def main():
    print("=== NLP Text Analyzer ===")

    text = input("\nEnter your text:\n")

    if not text.strip():
        print("You didn't enter any text.")
        return

    results = analyze_text(text)

    print("\n=== Results ===")
    print(f"Characters: {results['characters']}")
    print(f"Words: {results['words']}")
    print(f"Sentences: {results['sentences']}")
    print(f"Average word length: {results['average_word_length']:.2f}")

    print("\n=== Most Common Words ===")

    for word, count in results["word_frequency"].most_common(10):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()