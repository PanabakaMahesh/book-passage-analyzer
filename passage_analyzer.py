import os
import re

# Sample passage for testing
DEFAULT_PASSAGE = (
    "When a person really desires something, all the universe conspires to help that "
    "person realize his dream. The boy could see that the desert was vast and full of treasure, "
    "but the greatest peace came from knowing his heart was finally quiet and hopeful."
)


def get_passage():
    user_input = input("Enter passage, file path, or press Enter for sample: ").strip()

    if not user_input:
        return DEFAULT_PASSAGE

    if os.path.isfile(user_input):
        with open(user_input, "r", encoding="utf-8") as f:
            return f.read().strip()

    return user_input


def count_words(text):
    return len(re.findall(r'\b\w+\b', text))


def find_predominant_emotion(text):
    emotions = {
        "Joy": {"happy", "joy", "smile", "love", "peace", "hope", "delight"},
        "Sadness": {"sad", "tears", "cry", "pain", "loss", "grief", "sorrow", "lonely"},
        "Anger": {"angry", "rage", "furious", "hate", "mad", "bitter"},
        "Fear": {"fear", "afraid", "scared", "terror", "danger", "panic"}
    }

    words = re.findall(r'\b\w+\b', text.lower())
    scores = {e: 0 for e in emotions}

    for word in words:
        for emotion, keywords in emotions.items():
            if word in keywords:
                scores[emotion] += 1

    if max(scores.values()) == 0:
        return "Neutral / Undetermined"

    return max(scores, key=scores.get)


def suggest_books(text):
    books = {
        "The Alchemist by Paulo Coelho":
            {"dream", "journey", "destiny", "treasure", "desert", "heart"},
        "Man's Search for Meaning by Viktor Frankl":
            {"meaning", "suffering", "life", "purpose", "hope", "camp"},
        "To Kill a Mockingbird by Harper Lee":
            {"justice", "racism", "court", "atticus", "scout", "prejudice"}
    }

    words = set(re.findall(r'\b\w+\b', text.lower()))
    scores = {}

    for book, keywords in books.items():
        scores[book] = len(words.intersection(keywords))

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    matches = [book for book, score in ranked if score > 0]

    return matches[:3] if matches else ["No strong keyword matches found."]


def summarize_passage(text, n=2):
    sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text) if s.strip()]

    if len(sentences) <= n:
        return " ".join(sentences)

    stopwords = {
        "the", "a", "an", "and", "or", "in", "on", "at",
        "to", "is", "was", "it", "of", "for", "with"
    }

    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = {}

    for word in words:
        if word not in stopwords:
            word_freq[word] = word_freq.get(word, 0) + 1

    scores = []

    for i, sentence in enumerate(sentences):
        sentence_words = re.findall(r'\b\w+\b', sentence.lower())
        score = sum(word_freq.get(word, 0) for word in sentence_words)
        scores.append((score, i))

    best = sorted(scores, reverse=True)[:n]
    best = sorted(best, key=lambda x: x[1])

    return " ".join(sentences[i] for _, i in best)


def main():
    passage = get_passage()

    if not passage:
        print("No input provided.")
        return

    print("\n--- Book Passage Analysis ---")
    print("Total Words:", count_words(passage))
    print("Predominant Emotion:", find_predominant_emotion(passage))

    print("\nPossible Books:")
    for book in suggest_books(passage):
        print("-", book)

    print("\nSummary:")
    print(summarize_passage(passage))


if __name__ == "__main__":
    main()