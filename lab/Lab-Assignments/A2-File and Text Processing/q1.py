#q1.py
#by Jatin Bhagat, Sep/30/24
#Question 1:
# Write a function named censor() that takes the name of a file (a string) as input. The
# function should:
# o Open the file.
# o Read its contents.
# o Write the contents to a new file, censored.txt, with the following modification:
# Every occurrence of a four-letter word in the file should be replaced with the
# string 'xxxx'.

def censor(file_name):
    """
        takes the name of a file (a string) as input. The o Open the file.
        o Read its contents.
        o Write the contents to a new file, censored.txt, with the following modification:
        Every occurrence of a four-letter word in the file should be replaced with the
        string 'xxxx'.
    """
    file = open(file_name,"r") # Open The file  for reading
    contents_of_file = file.read() # store the data 
    file.close() # close the file 
    new_file_censored = open("censored.txt","w") # Opens the file "censored.txt" for writing, creates the file if it does not exist
    new_file_censored.write(contents_of_file) # write the data store in "contents_of_file" of the file
   
    new_file_censored.close() # close the file "censored.txt"
    new_file_censored = open("censored.txt","r") # Opens a file "censored.txt" for reading
    data_of_censored_as_a_list = new_file_censored.readlines() # store the data of "censored.txt" as a list 
    remvoe_enter = list(map(lambda a:a.strip(),data_of_censored_as_a_list)) # remove enter "/n" if there are any 
    list_into_string = " ".join(remvoe_enter) # Trun the list in string when someting ends with " "
    splits_string_into_list = list_into_string.split() # splits the string "list_into_string" when there is " " and turn into list
    
    """ We truned list into a list in to string "list_into_string" this because we want to look at a individual words and 
        wnat to change them.
    """
    
    for i in range(0,len(splits_string_into_list)):
        """ repeat the code for the length of list "splits_string_into_list"
        """
        if len(splits_string_into_list[i]) == 4:
            splits_string_into_list[i] = "xxxx" # if the word that is in the list "splits_string_into_list" is 4 characters long then replace with "xxxx"
        elif len(splits_string_into_list[i]) == 5:
            if splits_string_into_list[i][4] == ".":
                splits_string_into_list[i] = "xxxx." # if the word that is in the list "splits_string_into_list" is 5 characters long and the 5th characters is "." then replace with "xxxx."
    new_file_censored.close() # close the file
    
    new_file_censored = open("censored.txt","w") # Opens the file "censored.txt" for writing,
    splits_string_into_list = " ".join(splits_string_into_list) # Trun the list in string when someting ends with " "
    new_file_censored.write(splits_string_into_list) # splits the string "list_into_string" when there is " " and turn into list
    new_file_censored.close() # close the file
    
    """ We truned list into a list in to string "list_into_string" this because you can only add string with write()
    """
    
    new_file_censored = open("censored.txt","r") # Opens a file "censored.txt" for reading
    print(new_file_censored.read()) # Prints the data we have changed 
    new_file_censored.close() # close the file
    
    

censor("test.txt")
