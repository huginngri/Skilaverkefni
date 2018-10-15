word = input('Enter a word: ')

vowels = 'aeiou'

while word != '.':
    wordlen = len(word)
    if word[0] in vowels:
        print(word + 'yay')

    else:
        for k, j in enumerate(word) :
            if word[k] in vowels:
                print(word[k:] + word[0:k] + 'ay')
                break
            elif k == (wordlen-1):
                print(word + 'ay')
            
        
    word = input('Enter a word: ')