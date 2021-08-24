import nltk
import string
from heapq import nlargest

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
if text.count(". ") > 20:
    length = int(round(text.count(". ")/10, 0))
else:
    length = 1

nopuch =[char for char in text if char not in string.punctuation]
nopuch = "".join(nopuch)

processed_text = [word for word in nopuch.split() if word.lower() not in nltk.corpus.stopwords.words('english')]

word_freq = {}
for word in processed_text:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] = word_freq[word] + 1

max_freq = max(word_freq.values())
for word in word_freq.keys():
    word_freq[word] = (word_freq[word]/max_freq)

sent_list = nltk.sent_tokenize(text)
sent_score = {}
for sent in sent_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_freq.keys():
            if sent not in sent_score.keys():
                sent_score[sent] = word_freq[word]
            else:
                sent_score[sent] = sent_score[sent] + word_freq[word]

summary_sents = nlargest(length, sent_score, key=sent_score.get)
summary = " ".join(summary_sents)
print(summary)