from googletrans import Translator


class GoogleTranslator:
    def __init__(self, src, dst):
        self._translator = Translator()
        self._src = src
        self._dst = dst
    
    def translate(self, text):
        return self._translator.translate(
            text, src=self._src, dest=self._dst).text

class ArabicEnglishTranslator(GoogleTranslator):
    def __init__(self):
        super().__init__("ar", "en")

class FrenchEnglishTranslator(GoogleTranslator):
    def __init__(self):
        super().__init__("fr", "en")
    


if __name__ =="__main__":
    ar_en_tran = ArabicEnglishTranslator()
    print(ar_en_tran.translate("الطقس جميل هذه الساعة"))

    fr_en_tran = FrenchEnglishTranslator()
    print(fr_en_tran.translate("il fait beau cette heure"))

