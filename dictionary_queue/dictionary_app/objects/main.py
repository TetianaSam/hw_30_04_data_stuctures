
from dictionary import Dictionary


def main():
    dictionary = Dictionary()

    # Initial data input
    initial_data = {
        "hello": ["hola", "salut"],
        "world": ["mundo", "monde"],
        "new": ["nuevo"],
        "old": ["viejo"],
        "happy": ["feliz", "contento"],
        "sad": ["triste"],
        "fast": ["rápido", "veloz"],
        "slow": ["lento", "despacio"],
        "big": ["grande"],
        "small": ["pequeño"]
    }
    dictionary.initialize_data(initial_data)

    # Display all words and their translations
    print("All words and their translations:")
    dictionary.display()

    # Add a new word and its translation
    dictionary.add_word("good", "bueno")

    # Add translation to an existing word
    dictionary.add_translation("good", "bien")

    # Replace translations for a word
    dictionary.replace_translations("happy", ["alegre", "contento", "feliz"])

    # Delete a translation for a word
    dictionary.delete_translation("slow", "despacio")

    # Delete a word
    dictionary.delete_word("sad")

    # Display all words and their translations
    print("\nUpdated words and their translations:")
    dictionary.display()

    # Simulate some usage to update popularity
    for _ in range(5):
        dictionary.add_translation("hello", "hi")
    for _ in range(2):
        dictionary.add_translation("new", "nuevo")
    dictionary.add_translation("old", "ancien")

    # Display popular words
    print("\nTop 10 Most Popular Words:")
    dictionary.display_popular_words()


if __name__ == "__main__":
    main()
