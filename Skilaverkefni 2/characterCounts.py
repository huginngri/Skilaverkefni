sentence = input('Enter a sentence: ')


upper = 0
lower = 0
digit = 0
punct = 0

for k, j in enumerate(sentence):
    if sentence[k].isdigit() == True:
        digit += 1
    elif sentence[k].islower() == True:
        lower +=1
    elif sentence[k].isupper() == True:
        upper +=1
    elif sentence[k] == ' ':
        white = 0
    else:
        punct +=1
print('{:>15s} {:>5d}'.format(" Upper case", upper))
print('{:>15s} {:>5d}'.format(" Lower case", lower))
print('{:>15s} {:>5d}'.format(" Digits", digit))
print('{:>15s} {:>5d}'.format(" Punctuation", punct))