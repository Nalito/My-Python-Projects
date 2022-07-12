def switch(word, num):
    # A-Z = 65-90; a-z = 97-122
    new_word = []
    newword = ""
    for i in word:
        chrnum = ord(i)
        chrnum2 = chrnum + num

        if chrnum2 > 122:
            num1 = chrnum2 - 122
            num2 = 96 + num1
            chrword = chr(num2)
        elif chrnum2 < 97:
            num1 = 97 - chrnum2
            num2 = 123 - num1
            chrword = chr(num2)
        elif chrnum2 < 65:
            num1 = 65 - chrnum2
            num2 = 91 - num1
            chrword = chr(num2)
        elif (chrnum2 > 64 and chrnum2 < 91) or (chrnum2 > 96 or chrnum2 < 123):
            chrword = chr(chrnum2)
        else:
            num1 = chrnum2 - 90
            num2 = 64 + num1
            chrword = chr(num2)

        new_word.append(chrword)
    print(newword.join(new_word))


word = input("Type in the word you wish to decode")
num = int(input("By how many digits?"))
switch(word, num)
