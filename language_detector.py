from googletrans import Translator


class LanguageDetector:
    def __init__(self):
        self._detector = Translator()

    def _detect(self, word):
        return str(self._detector.detect(word).lang)
    
    def detect_languages(self, text):
        """
        Returns
        -------
        segments: list
            A list of different segments of the input text where consecutive
            words are from the same language.
        langs: list
            A list of all detected languages of the input in order.
        
        Raises
        ------
        AssertionError: WHen the number of segments doesn't equal to the number
        of languages detected.
        """
        segments = []
        langs = []
        prev_lang = None
        for token in text.split():
            curr_lang = self._detect(token)
            if curr_lang == prev_lang:
                segments[-1].append(token)
            else:
                langs.append(curr_lang)
                segments.append([token])
            prev_lang = curr_lang
        assert len(segments) == len(langs)
        return [" ".join(seg) for seg in segments], langs


if __name__ == "__main__":
    detector = LanguageDetector()
    segments, langs = detector.detect_languages("الطقس اليوم very nice")
    print(segments)
    print(langs)