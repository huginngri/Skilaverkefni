import random
import string

def get_word_string(file):
    words = ''
    try:
        thefile = open(file, "r")
        for word in thefile:
            words += word
    except:
        print("File {} not found".format(filename))
    return words

def scramble_strings(string_normal):
    '''Takes normal words and scrambles it'''
    word_list = string_normal.split()
    words = ''
    for word in word_list:
        k = 1
        if len(word) > 3:
            flottur = []
            for letters in word:
                flottur.append(letters)
            if flottur[-1] in string.punctuation:
                breyting = flottur[1:len(flottur)-2]
                therange = list(range(0,len(flottur)-3))
            else:
                breyting = flottur[1:len(flottur)-1]
                therange = list(range(0,len(flottur)-2))
            random.shuffle(therange)
            for i in therange:
                flottur.pop(k)
                flottur.insert(k,breyting[i])
                k +=1
            words += ''.join(flottur) + ' '
        else:
            words += ''.join(word) + ' '
    return words

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_strings(word_string)
print(scrambled_string)