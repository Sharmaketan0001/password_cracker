from random import *
user_pwd = input("Enter a password:-  ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9','!','`','@','#','$','%','^','&','*','()','(',')']

pw = ""
while(pw!= user_pwd):
    pw = ""
    for letter in range(len(user_pwd)):
        guess_pwd = pwd[randint(0,25)]
        pw += guess_pwd
    print(pw)
    

        
print("Your password is:- ",pw)
