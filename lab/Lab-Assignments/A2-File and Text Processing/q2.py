s = '''It was the best of
times, it was the worst of times; it was the age of wisdom, it was the age of
foolishness; it was the epoch of belief, it was the epoch of incredulity; it
was ... '''


news = s.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('\n', ' ')

#rint(news)

news = news.split()

news = "".join(news)

news = news.lower()

news = news.split()
print(news)