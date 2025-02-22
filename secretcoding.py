def encode(string):

    coding = True
    codedstr =[]
    while(coding):
        for word in words:
            if(len(word)>=3):
                rn1 = "dvt"
                rn2 = "gjy"
                newl = rn1 + word[1:] + word[0] + rn2
                codedstr.append(newl)

            else:
                newl = word[::-1]
                codedstr.append(newl)

        print(f" coding is{codedstr}")

        coding = False
def decode(codedstr):

    decoding = True
    decodedstr =[]
    while(decoding):
        for word in codedstr:
            if(len(word) < 3):
                newl = word[::-1]
                decodedstr.append(newl)

            else:
                word2 = word[3:-3]
                newl = word2[-1] + word2[:-1]
                decodedstr.append(newl)

        print(decodedstr)
        decoding = False


stmt = input("enter message you want to encode or decode :")
words = stmt.split(" ")
docon = 'y'
while(docon != 'n'):
    encoding =[]
   # docon = input("if you want to continue?[y/n]:")
    print("enter 1 if you want to encode")
    print("enter 2 if you want to decode")
    choice = int(input("enter your choice:"))
    if(choice ==1):
        encoding.append(encode(words))

    else:
         decode(encoding)

    docon = input("if you want to continue?[y/n]:")










        

        


