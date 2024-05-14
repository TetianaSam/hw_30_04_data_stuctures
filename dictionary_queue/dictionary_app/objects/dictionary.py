from collections import defaultdict
from word import Word
from queue import PriorityQueue


class Dictionary:
    def __init__(self):
        self.words = {}
        self.word_usage = defaultdict(int)
        self.popularity_queue = PriorityQueue()

    def initialize_data(self, data):
        for word, translations in data.items():
            self.words[word] = Word(word, translations[0])
            for translation in translations[1:]:
                self.words[word].add_translation(translation)

    def add_word(self, word, translation):
        if word not in self.words:
            self.words[word] = Word(word, translation)
        else:
            print(f"'{word}' already exists. Use add_translation to add more translations.")
        self._update_popularity(word)

    def add_translation(self, word, translation):
        if word in self.words:
            self.words[word].add_translation(translation)
            self._update_popularity(word)
        else:
            print(f"'{word}' does not exist. Use add_word to add the word first.")

    def replace_translations(self, word, translations):
        if word in self.words:
            self.words[word].replace_translations(translations)
            self._update_popularity(word)
        else:
            print(f"'{word}' does not exist in the dictionary.")

    def delete_word(self, word):
        if word in self.words:
            del self.words[word]
            del self.word_usage[word]
            self.popularity_queue = PriorityQueue()  # Rebuild priority queue
            for w, count in self.word_usage.items():
                self.popularity_queue.add_word(w, count)
        else:
            print(f"'{word}' does not exist in the dictionary.")

    def delete_translation(self, word, translation):
        if word in self.words:
            self.words[word].delete_translation(translation)
            self._update_popularity(word)
            if not self.words[word].translations:  # Remove word if no translations left
                self.delete_word(word)
        else:
            print(f"'{word}' does not exist in the dictionary.")

    def display(self):
        for word in self.words.values():
            print(word)

    def _update_popularity(self, word):
        self.word_usage[word] += 1
        self.popularity_queue.add_word(word, self.word_usage[word])

    def display_popular_words(self):
        print("10 Most Popular Words:")
        for count, word in self.popularity_queue.get_top_n(10):
            print(f"{word}: {count} uses")

        print("\n10 Least Popular Words:")
        for count, word in self.popularity_queue.get_bottom_n(10):
            print(f"{word}: {count} uses")


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
