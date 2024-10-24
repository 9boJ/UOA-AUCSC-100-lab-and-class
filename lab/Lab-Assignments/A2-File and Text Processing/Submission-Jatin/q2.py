#q1.py
#by Jatin Bhagat, Sep/30/24
#Question 2:
"""
    Given the following text assigned to variable s: s = '''It was the best of 
    times, it was the worst of times; it was the age of wisdom, it was the age of 
    foolishness; it was the epoch of belief, it was the epoch of incredulity; it 
    was ... '''
"""

s = '''It was the best of
times, it was the worst of times; it was the age of wisdom, it was the age of
foolishness; it was the epoch of belief, it was the epoch of incredulity; it
was ... '''

#a
news = s.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('\n', ' ') #., ,, ;, and \n are replaced by spaces.

#b
news = news.split() #splits the list into list

news = " ".join(news) # join the list into a string with " " 

#c
news = news.lower() # all characters in "newS" are Converted to lowercase.

#d
Count_it_was = news.count("it was") # Counts the number of occurrences of the string 'it was' in newS and returns the value

#e
news = news.replace("it was","is") #replaces every occurrence of 'was' with 'is' in "newS"

#f
lists = news.split() #Split newS into a list of words and assign this list to "listS"

print(lists) # prints the list "lists"

