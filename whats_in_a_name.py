'''
Author: Cayden Ever
Sources: Google, Mr. Campbell, ASCII Keys Table
Description: Set of functions that do different things to a string (name)
Date: 9/30/25
Bugs: My encryption function doesn't work on numbers only on letters. first name does not remove titles like Dr.
'''
from collections import Counter 
import re 
#importing the counter library for only my personal choice function

import random   #import random library
def reverse_reverse_display(name):
    '''
    Reverses name and displays it
    
    Args:
        name(str): inputed text
    Returns:
        name starting at the end going to beginning
    ''' 

    return (name[::-1]) #return the input in reversed order because it goes start:end:direction

def vowel_count (name): 
    '''
    counts the number of vowels in a string
    
    Args:
        name(str): inputed text
    Returns:
        number of vowels in name (int)
    ''' 
    vowels = 0   #set vowels to 0 
    for i in name:  #for every character in the text
        if i in "aeiouAEIOU": #If there is a vowel in the text
            vowels +=1  #add one to vowel count
    return (vowels)   #return the number of vowels in the text
def consonant_count (name): 
    '''
    counts the amount of consonants in a string
    
    Args:
        name(str): inputed text
    Returns:
        number of consants in the name (int)
    ''' 
    consonants = 0 #set the consonants to 0
    for i in name:  #for ever character in name
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": # if there is a consonant in the text
            consonants += 1  #add one to cosonant count
    return (consonants) #return number of consonants
def get_last_name(name): 
    """
    Returns the last name in a string

    Args:
        name (str): inputed text
    Returns:
        name starting at the end and stopping at the last space
    """
    finalspace = len(name) #set the var finalspace to the legnth of name
    for i in range (len(name)-1,0,-1): #for each character in name starting at the end of the text, ending at the beggning, going backward
        if name [i] == " ": #if there is a space
            break #break the loop
        else: 
            finalspace -= 1 #subtract 1 from finalspace var
    return name[finalspace :]  #return the text starting at the last space and ending at the end therefore returning the last word.

def get_first_name(name): 
    '''
    Extracts first name
    
    Args:
        name(str): inputed text
    Returns:
        text until the first space in the str
    '''  
    first_space = 0  #set the first space to 0
    for i in range (0,len(name)-1):             #go from the begginning
        if name [i] == " ":            #if you hit a space
            break               #break loop
        else: 
            first_space += 1 #add one to the first space var
    return name[: first_space] #return the text but stop at the first space

def get_middle_names(name):
    '''
    Extracts middle names
    
    Args:
        name(str): inputed text
    Returns:
        name excluding the first and last element that is seperated by spaces
    ''' 
    beg = 1                     #set beginning to 1 
    for i in range (0,len(name)-1):   #find first space
        if name [i] == " ":   #if there is a space
            break
        else:  
            beg+=1 
    
    end = len(name)   
    for i in range (len(name)-1,-1, -1):  #find the last space
        if name [i] == " ":
            break
        else:
            end -= 1
    return name [beg:end]  # return the middle name/names using start at first space and end at last space
def boolean_for_hyphen(name): 
    '''
    checks if there is a hyphen in text
    
    Args:
        name(str): inputed text
    Returns:
        A boolean based on if there is a hyphen in text
    ''' 
    hyphen = 0
    for i in name: 
        if i in "-":
            hyphen +=1
    if hyphen == 0:
        return False
    if hyphen>0:
        return True

def convert_lower(name):
    '''
    converts text to lowercase letters
    
    Args:
        name(str): inputed text
    Returns:
        a list of text converted to lower
    ''' 
    name_list = list(name)
    new_list_name = []
    for c in name_list:
        int_value = ord(c) #convert to ASCII
        if int_value < 90 and int_value > 65:  #checking if it is uppercase
            int_value +=32       #convert to lowercase
        lowercase_letter = chr(int_value)         #make lowercase letter turn from ASCII to letter
        new_list_name.append (lowercase_letter)    #add the lowercase letter to the new_name variable
    return ("".join(new_list_name))                # return the full list
        
        

def convert_upper(name): 
    '''
    converts text to uppercase letters
    
    Args:
        name(str): inputed text
    Returns:
        a list of text converted to upper
    ''' 
    name_list = list(name)
    new_list_name = []
    for c in name_list:
        int_value = ord(c)
        if int_value < 122 and int_value > 97:
            int_value -= 32
        uppercase_letter = chr(int_value)
        new_list_name.append (uppercase_letter)
    return ("".join(new_list_name))
        
def shuffle_list(name):
    '''
    randomly shuffles a list.
    Args:
        name(str): inputed text
    Returns:
        shuffled list
    '''
    name = list(name)
    shuffled_name = ""
    while (len(name)) > 0:
        num = random.randint(0,len(name)-1)
        shuffled_name = shuffled_name + name[num]
        del name[num]
    return shuffled_name 

def is_palindrome(name):
    '''
    detects if str reads the same forward or backward

    Args:
        name(str): inputed text
    Returns:
        Boolean based on if name is a palindrome
    '''
    if name == name [::-1]:
        return True
    else:
        return False
def my_split(name):
    '''
    Manually splits a str without str class.

    Args:
        name(str): inputed text
    Returns:
        a list of elements that were formerly seperated by spaces
    '''
    parts = []
    current = ""
    for char in name:
        if char == " ":
            if len(current) > 0:
                parts.append(current)
                current = ""
        else:
            current += char
    if len(current) > 0:
        parts.append(current)
    print(parts)
    return parts     

def selection_sort(name):
    '''
    Sorts a list using the Selection Sort algorithm and returns a new sorted list.
    Does not modify the original list.

    Args:
        name(str): inputed text
    Returns:
        text sorted by ordinal starting with special characters then the alphabet.
            
    '''
    if not name:
        return []

    # Create a copy to avoid modifying the original list
    temp_list = list(name)
    sorted_list = []

    while temp_list:
        min_value = temp_list[0]
        min_index = 0
        for i in range(1, len(temp_list)):
            if temp_list[i] < min_value:
                min_value = temp_list[i]
                min_index = i
        
        sorted_list.append(temp_list.pop(min_index))
    
    return sorted_list

def extract_initials(name):
    '''
    Extracts the first initials of each word
    Args:
        name (str): input
    Returns:
        each initials seperated by periods.
    '''

    elements = my_split(name)

    if len(elements) < 2 :
        fi = get_first_name(name)
        fi = fi[0]

        output = fi
    elif len(elements) < 3 :
        fi = get_first_name(name)
        fi = fi[0]
        li = get_last_name(name)
        li = li[0]

        output = fi + "." + li
    else:
        fi = get_first_name(name)
        fi = fi[0]
        mi = get_middle_names(name)
        mi = mi[0]
        li = get_last_name(name)
        li = li[0]

        output = fi + "." + mi  + "." + li + "."
    return output

def has_description(name):
  '''
  Checks for description titles

  Args:
        name(str): inputed text

  Returns:
        Boolean based on if name has a title.
          

  
  '''
  piece = get_first_name(name)
  titles = ["Dr.", "Mrs.", "Ms.", "Mr.", "Sir", "Ma'm", "Ph.d", "Esq"]
  for i in titles:
    if piece in titles :
        return True
    else:
        return False

def encrypt(name, shift):
    '''
    Encrypts a string.

    Args:
        name (str): inputed text
        shift: amount of letters over text is to be shifted

    Returns:
        encrypted text as a str.
    
    '''
    result = ""
    for char in name:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) #
            result += shifted_char
        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def decrypt(name, shift):
    '''
    Decrypts a string.
    
    Args:
        text (str): The ciphertext to decrypt.
        shift (int): The same shift value used for encryption.

    Returns:
        str: The decrypted string.
    '''
    return encrypt(name, -shift) #just doing the encrypt in the opposite order therefroe decrypting.

def count_word_frequency(name):
    '''
    Counts the frequency of each word in a given text.

    Args:
        name (str): The input string of text.

    Returns:
        frequency: A dictionary where keys are words and values are their frequencies.
    '''
    # Convert name to lower and remove punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', name).lower()

    # Split the text into words using .split
    words = cleaned_text.split()

    # Use Counter that I imported to count word frequencies
    word_counts = Counter(words)

    return word_counts #return the word counts properly formated

def main():
    """
    Main Function
    """
    while True:
        name = input("Welcome to the bank of functions! Please enter your name or a word: ")
        choice = input('''Which function would you like to perform: 
                       q. quit the program
                       1. Reverse your word/name 
                       2. Count the vowels in your word/name 
                       3. Count the consonants in your word/name 
                       4. Find the last element in your input 
                       5. Find the first element in your name
                       6. Find the middle names of your text.
                       7. Detect if there is hyphens in your text:
                       8. Convert to lowercase
                       9. Convert to uppercase
                       10. randomly shuffle your name
                       11. Check if your name is a palindrome
                       12. Sort your list by all characters
                       13. Extract initials
                       14. Check for titles like Dr., Mrs., etc...
                       15. Encrypt and decrypt your text to keep it seceret.
                       16. Count the frequency of each word in your text
                       '''
                       )
        if choice == "q":
            break
        if choice == "1":
            print(f"your word/name reversed is: {reverse_reverse_display(name)}")
        elif choice == "2":
            print(f"the amount of vowels in your word/name is: {vowel_count(name)}")
        elif choice == "3":
            print (f"the amount of consonants in your name is: {consonant_count(name)}")
        elif choice == "4": 
            print (f"the last element of your input is: {get_last_name(name)}")
        elif choice == "5": 
            print (f"the first element of your input is: {get_first_name(name)}")
        elif choice == "6":
            print (f"the middle names of your words is: {get_middle_names(name)}")
        elif choice == "7":
            if boolean_for_hyphen(name) == True:
                print ("you do have hyphens in your text.")
            if boolean_for_hyphen(name) == False: 
                print ("you have no hyphens in your text")
        elif choice == "8":
            print (f"your text in all lowercase is {convert_lower(name)}")
        elif choice == "9":
            print (f"your text converted to uppercase is: {convert_upper(name)}")
        elif choice == "10":
            print (f"your text shuffled up is:{shuffle_list(name)}")
        elif choice == "11":
            print (f"Your true/false for if your text is a palindrome is: {is_palindrome(name)}")
        elif choice == "12":
            print (f"Your text sorted by the computer is: {selection_sort(name)}")
        elif choice == "13":
            print (f"the initials of: {name} are {extract_initials(name)}")
        elif choice == "14": 
            print (f"A true or false on if you have a title before your name is:{has_description(name)}")
        elif choice == "15":
            number_shift = input("How many letters would you like to shift your text over?:")
            shift = int(number_shift)
            print (f"your text encrypted is: {encrypt(name, shift)}")
            decrypt_choice = input ("would you like to decrypt your text using your decrypt function? type y/n: ")
            if decrypt_choice.lower() == "y":
                encrypted_text = encrypt(name, shift)
                print (f"your text decrypted is {decrypt(encrypted_text, shift)}")
            else:
                break
        elif choice == "16":
            frequency = count_word_frequency(name)
            print(f"the frequency of each word in your text is {frequency}")
        else:
            print("not a valid input. Please try again.")
                
        

main()
