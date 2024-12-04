def most_frequent_word(filename, stop_words):
    file = open("test.txt","r")
    sent = file.readline()
    sent.lower()
    for i in sent:
        if i == ".":
            sent = sent.replace(i,"")
        elif i == ",":
            sent = sent.replace(i,"")

    sent = sent.split()
    for q in range(len(sent)):
        for w in range(len(stop_words)):
            print(q)
            if sent[q] == stop_words[w]:
                sent = sent.pop(0)
    print(sent)

stop_words = ["a", "the", "an", "in", "of", "to", "and", "is"]
filename = "sample.txt"
most_frequent_word(filename, stop_words)