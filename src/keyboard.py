from src.item import Item


class MixinLang:
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        available_languages = ['EN', 'RU']
        if language in available_languages:
            self.__language = language
        else:
            raise AttributeError

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLang, Item):
    pass
