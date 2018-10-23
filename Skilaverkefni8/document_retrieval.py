import string

def filereader():
    filename = input("Document collection: ")
    filetext =''
    try:    
        with open(filename, 'r') as f:
            for lines in f:
                filetext += lines
        return filetext, 1
    except:
        print("Documents not found.")
        return filetext, 3

def splitter_and_stripper(filetext):
    list_of_documents = filetext.split("<NEW DOCUMENT>\n")
    return list_of_documents

def document_to_dict(document):
    new_dict = {}
    list_of_words = document.split()
    
    for words in list_of_words:
        words = words.strip(string.punctuation).lower()
        words = words.strip()
        words_list = words.split()
        for word in words_list:
            if word not in new_dict.keys():
                new_dict[word] = 1
            else:
                new_dict[word] += 1
    return new_dict


def finder(list_of_documents):

    search_words = input("Enter search words: ")
    search_words = search_words.lower()
    search_words_list = search_words.split()
    set_of_docs = set()
    for number_of_doc, document in enumerate(list_of_documents):
        dict_of_words = document_to_dict(document)
        counter = 0
        for words in search_words_list:
            if words in dict_of_words.keys():
                counter += 1
        if counter == len(search_words_list):
            set_of_docs.add(number_of_doc-1)
    list_of_words = list(set_of_docs)
    if set_of_docs != set():        
        print("Documents that fit search: ", end ='')
        for words in list_of_words:
            print(words, end=' ')
        print()
    else:
        print("No match.")
    

def pick_your_choice():
    print("What would you like to do?\n1. Search Documents\n2. Print Document\n3. Quit Program")
    the_choice = int(input("> "))
    return the_choice

def printer(list_of_documents):
    number_of_doc = int(input("Enter document number: "))
    print("Document #{}".format(number_of_doc))
    print(list_of_documents[number_of_doc+1], end='')



def main():
    the_choice = 1
    the_text, the_choice = filereader()
    list_of_documents = splitter_and_stripper(the_text)
    while the_choice != 3:
        print()
        the_choice = pick_your_choice()
        if the_choice == 1:
            finder(list_of_documents)
        elif the_choice == 2:
            printer(list_of_documents)
        else:
            print("Exiting program.")


main()