import csv
import numpy as np 
import matplotlib.pyplot as plt
'''
Author: Cayden Ever
Sources: Mr. Campbell, Shakespeare,  W3schools for read/write, python for everyone
Description: Analyzes data from the plays Hamlet and  A Mid Summer Nights Dream
Date: 2.1.26
'''

def remove_words_from_file(filename, words_to_remove):
    """
    Removes specified words from a file.

    Args:
        filename (str): The path to the file.
        words_to_remove (list of str): A list of words to be removed.
    """
    
    #Read the file content
    with open(filename, 'r') as f:
        file_content = f.read()

    words = file_content.split() #split into list of strings
    filtered_words = []
    
    for word in words:
        clean_word = word.strip('.,;:!?\'"()-—[]{}') #take out punctuation
        if clean_word not in words_to_remove: #remove punctuation from word and add the new word to the dataset
            filtered_words.append(word)
    
    updated_content = ' '.join(filtered_words)
    #Write the updated content back to the file
    with open(filename, 'w') as f:
        f.write(updated_content)


def main():
    file_path = "hamlet.txt"
    # Read the file, convert to lowercase, and write back
    with open(file_path, 'r') as f:
        content = f.read().lower()
    with open(file_path, 'w') as f: #write out the new content into the same file
        f.write(content)
    #specify which words to delete
    words_to_delete = ["man","enter","first","know","go","tis","one","come","then", "there","well", "like","how","now", "let", "you", "me", "here", "o","and","or","nor","but","yet","so","for","though","although","if","unless","while","whilst","whereas","when","whenever","ere","lest","since","because","that","whether","as","than","till","until","which","who","whom","whose","where","wherein","whereof","whereby","whereon","what","whatsoever","whoever","whoso","whomsoever","the","a","an","this","that","these","those","yon","yonder","such","same","i","me","my","mine","myself","thou","thee","thy","thine","thyself","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","we","us","our","ours","ourselves","they","them","their","theirs","themselves","am","is","are","was","were","be","been","being","do","dost","did","doth","have","hast","has","had","shall","shalt","should","will","wilt","would","may","might","must","can","could","of","to","in","on","upon","at","by","with","from","for","against","between","betwixt","through","throughout","into","unto","out","about","around","over","under","beneath","above","before","after","behind","within","without","not","no","ne","never","nay","naught","aught","very","too","so","most","more","less","much","many","few","some","any","all",".",",",";"," :", "!","?","-","—","(",")","[","]","{","}","'","’","\""]
    #call function
    remove_words_from_file(file_path, words_to_delete)

    file_path = "a_mid_summer_nights_dream.txt"
    #Read the file, convert to lowercase, and write back
    with open(file_path, 'r') as f:
        content = f.read().lower()
    with open(file_path, 'w') as f:
        f.write(content)

    remove_words_from_file(file_path, words_to_delete)




    fname = "hamlet.txt" #make the file name hamlet.txt
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            word = word.strip('.,;:!?\'"()-—[]{}')  # Strip punctuation from word edges
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1


    sorted_data = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
    
    #write out data
    

    #get the top 15 most occuring words
    new_dict = dict()
    count = 0 
    limit = 15
    for key, value in sorted_data.items():
        if count < limit:
            print (f'{key}: {value}')
            new_dict[key] = value
            count+= 1
        else:
            break
    #print out the top 15 into hamlet.csv
    with open('hamlet.csv', 'w', newline='') as csvfile:
        csvfile.write("Word,Count\n")
        data = new_dict 
        writer = csv.writer(csvfile)
        for word, count in data.items():#write out data by word and count
            writer.writerow([word, count])
    data = [] 
    labels = []
    for key,value in new_dict.items():
        labels.append(key) 
        data.append(value)
    plt.pie(data,labels = labels) #take the list data and with labels and make a pie chart
    plt.title("Most Occuring Words in Hamlet") #title
    plt.show() #display the graph






    #A mid summer nights dream 
    #getting counts of all words
    fname = "a_mid_summer_nights_dream.txt" #make the file name a_mid_summer_nights_dream.txt
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            word = word.strip('.,;:!?\'"()-—[]{}')  # Strip punctuation from word edges
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1


    #making a pie chart for a mid summer nights dream

    fname = "a_mid_summer_nights_dream.txt" #make the file name a_mid_summer_nights_dream.txt
    try:
        fhand = open(fname) #open mid summer nights
    except:
        print('File cannot be opened:', fname)
        exit()

    counts = dict() #make a dict called counts
    for line in fhand: #for each line 
        words = line.split()  #split into words
        for word in words:   #count the number of times each word shows up
            word = word.strip('.,;:!?\'"()-—[]{}')  # Strip punctuation from word edges
            if word not in counts:  #if its not in the dict create it and give it the value of one
                counts[word] = 1
            else:
                counts[word] += 1  #if it exists add one to its count
    sorted_data = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)} #sort the data in terms of how many counts it has from most to least
    new_dict = dict() #create a dict
    count = 0 
    limit = 15
    for key, value in sorted_data.items():  #for each key and value
        if count < limit:
            print (f'{key}: {value}') #print the key and value
            new_dict[key] = value #make the new value in the dictonary
            count+= 1
        else:
            break
    #writing out the top 15 occuring words to mid_summer_nights_dream.csv
    
    with open('mid_summer_nights_dream.csv', 'w', newline='') as csvfile:
        csvfile.write("Word,Count\n")
        data = new_dict 
        writer = csv.writer(csvfile)
        for word, count in data.items():#write out data by word and count
            writer.writerow([word, count])
    

    # Define the field names (column headers)
    data = [] 
    labels = []
    for key,value in new_dict.items(): #for each key and value in the new dictornary
        labels.append(key)  #add keys
        data.append(value)   #add values
    plt.pie(data,labels = labels) #take the list data and with labels and make a pie chart
    plt.title("Most Occuring Words In A Mid Summer Nights Dream") #make a title
    plt.show() #show the graph



main()


