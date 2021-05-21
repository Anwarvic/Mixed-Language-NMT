# Mixed-Language-NMT
It's a poc (proof-of-concept) idea of creating an NMT (Neural Machine Translation) Model that is able to translate a mixed-language sentence written in up to three different languages (Arabic, English, and French) into a unified Language (English).

## Dependencies
To install the dependencies needed for running this module, all you need to 
do is to run the following code to install all needed dependencies:
```
pip install -r requirements.txt
```

## How to use it
You can use translate any sentence that is written in any combiniation of these
three language (Arabic, English and French) using the Mixed-Language NMT model
by running the following code:
```
>>> from nmt_model import MixedLanguageNMT
>>> nmt = MixedLanguageNMT()
>>> text = "الطقس اليوم very nice"
>>> nmt.translate(text)
The weather today very nice
>>> text = "ذهبت إلى school مع أصدقائي the geeks"
>>> nmt.translate(text)
I went to school with my friends the geeks
>>> text = "ذهبت إلىI going to the restaurant français"
>>> nmt.translate(text)
I going to the restaurant French
```

As you can see, it's not perfect yet. I lacks a language model for English and
an understanding of how to handle similar words that are common between French 
and English.


