class Words:
    
    def __init__(self, the_text=""):
        self.the_text = the_text
        if the_text:
            self.words = self.text_to_words()
        else:
            self.words = []
            
    def setText(self, the_text):
        self.the_text = the_text
        self.words = self.text_to_words()
        
    def getWords(self):
        return self.words
    
    def text_to_words(self):
        """ return a list of words with all punctuation and numbers removed,
            and all in lowercase based on the given text string.
        """

        my_substitutions = str.maketrans(
          # If you find any of these
          "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
          # Replace them by these
          "abcdefghijklmnopqrstuvwxyz                                          ")

        # Translate the text now.
        cleaned_text = self.the_text.translate(my_substitutions)
        wds = cleaned_text.split()
        return wds

    def remove_dups(self):
        """ Remove duplicate words from the list of words.
        Returns:
            list: A new list with duplicate words removed.
        """
        unique_words = []
        for word in self.words:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

# Example usage:
words_obj = Words("Hello hello world world world")
unique_words = words_obj.remove_dups()

