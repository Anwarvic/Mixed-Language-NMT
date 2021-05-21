class LanguageAligner:
    def __init__(self):
        self._lang_model = None

    def align(self, segments):
        """
        Aligns different English segments into one comprehensible English
        sentence. And it should fill the gaps between these segments when
        needed.
        """
        return " ".join(segments)
