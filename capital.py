def cap_func(lempar):
    inputdata = lempar
    newword = ''
    data = ''
    for eachwords in inputdata:
        if eachwords.isalpha():
            newword += eachwords
        else:
            newword += ' '

    newdata = newword.split()
    for words in newdata:
        data += words.title()

    return data

print(cap_func(input()))

#by distyoh. trying python 2022