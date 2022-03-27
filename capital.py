def cap_func(inputter):
    inputdata = inputter
    newword = ''
    out = ''
    for eachwords in inputdata:
        if eachwords.isalpha():
            newword += eachwords
        else:
            newword += ' '

    newdata = newword.split()
    for words in newdata:
        out += words.title()

    return out

print(cap_func(input()))

#by distyoh. trying python 2022
#input = CATS and AND*DOGS are%awesome
#output= CatsAndAndDogsAreAwesome
