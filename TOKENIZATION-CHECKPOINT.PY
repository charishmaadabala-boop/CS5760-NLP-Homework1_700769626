import spacy
import re

nlp = spacy.load("en_core_web_sm")

text = "I can’t believe it’s already February. NLP is fun, right?"

print("Naive:", text.split())

manual = re.sub(r"([.,!?])", r" \1", text)
manual = manual.replace("can’t", "can n't").replace("it’s", "it 's")
print("Manual:", manual.split())

doc = nlp(text)
print("spaCy:", [t.text for t in doc])
