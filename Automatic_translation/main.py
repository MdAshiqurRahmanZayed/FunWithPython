#using goslate pip install goslate
from textblob import TextBlob
import goslate

text = "python is a powerful language"
new_translate = goslate.Goslate()
translations =new_translate.translate(text, 'fr')
print(translations)

#using from textblob import TextBlob | pip install textblob
text = TextBlob("Python is a strong language")
translations = text.translate(to = 'ar')
print(translations)
