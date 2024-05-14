class Word:
    def __init__(self, word, translation):
        self.word = word
        self.translations = [translation]

    def add_translation(self, translation):
        if translation not in self.translations:
            self.translations.append(translation)

    def replace_translations(self, translations):
        self.translations = translations

    def delete_translation(self, translation):
        if translation in self.translations:
            self.translations.remove(translation)

    def __str__(self):
        return f"{self.word}: {', '.join(self.translations)}"
