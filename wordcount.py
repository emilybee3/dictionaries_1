# iterate over the list and seperate out all the words 
# keep track of all unique words 
# print those counts 

#open the file 

#create a dictionary for words

poem_file = open("test.txt")
words_in_poem = []

for line_of_poem in poem_file:
    stripped = line_of_poem.rstrip("\n")
    words_in_poem.extend(stripped.split())
    

words_in_poem_dictionary = {}



#for each word in words in poem
for word in words_in_poem:
    #if its not in dictionary,
    if word not in words_in_poem_dictionary:
        words_in_poem_dictionary[word] = 1
    else:
        words_in_poem_dictionary[word] += 1

print words_in_poem_dictionary
        #and set the value to 1 
    #if it is in the dictionary
    #   up the value by +1 

    

