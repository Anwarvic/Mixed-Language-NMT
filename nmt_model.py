import string
from language_detector import LanguageDetector
from translator import ArabicEnglishTranslator, FrenchEnglishTranslator
from aligner import LanguageAligner


class MixedLanguageNMT:
    def __init__(self):
        self._lang_detector = LanguageDetector()
        self._ar_en_translator = ArabicEnglishTranslator()
        self._fr_en_translator = FrenchEnglishTranslator()
        self._aligner = LanguageAligner()
    
    def _clean(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def translate(self, text):
        # first clean text from punctuations
        text = self._clean(text)
        print(text)
        # detect languages
        segments, langs = self._lang_detector.detect_languages(text)
        # translate languages
        trans = []
        for segment, lang in zip(segments, langs):
            if lang == "ar":
                trans.append(self._ar_en_translator.translate(segment))
            elif lang == "fr":
                trans.append(self._fr_en_translator.translate(segment))
            elif lang == "en":
                trans.append(segment)
        # align results
        text = self._aligner.align(trans)
        # return result
        return text



if __name__ == "__main__":
    nmt = MixedLanguageNMT()
    text = "الطقس اليوم very nice"
    text = "ذهبت إلى school مع أصدقائي the geeks"
    print( nmt.translate(text) )
