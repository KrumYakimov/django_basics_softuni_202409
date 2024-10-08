from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BadLanguageValidator:
    def __init__(self, bad_words=None):
        if bad_words is None:
            self.bad_words = ["bad_word_1", "bad_word_2", "bad_word_3"]
        else:
            self.bad_words = bad_words

    def __call__(self, value):
        for bad_word in self.bad_words:
            if bad_word.lower() in value.lower():
                raise ValidationError("The text contains bad language")

