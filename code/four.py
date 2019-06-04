x=input()
y=ord(x)
if((y>=97 and y<=122) or (y>=65 and y<=90)):
    if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
