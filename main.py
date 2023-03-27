import tkinter as tk
import nltk
from textblob import TextBlob

from newspaper import Article

#nltk.download('punkt')
# url ='https://edition.cnn.com/2023/03/25/middleeast/israel-judiciary-netanyahu-explainer-intl/index.html'
#
#
#
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()
# print(f'Title:{article.title}')
# print(f'Author:{article.authors}')
# print(f'Publisher:{article.publish_date}')
# print(f'Summary:{article.summary}')
#
# analysis = TextBlob(article.text)
# print(analysis.polarity)
# print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negitive" if analysis.polarity < 0 else "neutral"}')
def summarize():
    url = utext.get('1.0', "end").strip()
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentimental.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0','end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentimental.delete('1.0', 'end')
    sentimental.insert('1.0',
                       f'Polarity:{analysis.polarity} , Sentiment:{"positive" if analysis.polarity > 0 else "negitive" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentimental.config(state='disabled')


root = tk.Tk()
root.title("News Summary")
root.geometry('1200x600')

tlable = tk.Label(root, text="Title")
tlable.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentimental Analysis")
selabel.pack()

sentimental = tk.Text(root, height=1, width=140)
sentimental.config(state='disabled', bg='#dddddd')
sentimental.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
