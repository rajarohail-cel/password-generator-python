
import string
import random

l_letters = list(string.ascii_lowercase)
u_letters = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

print("This program generates a random password based on given criteria from user.\n ")
c = 'y'

while c != 'n' and c != 'no':

    while True:
        try:
            str_len = input("How long do you want the password to be?: ")
            pass_len = int(str_len)
            if pass_len <= 0:
                print("Please enter a number greater than 0 for password length. ")
                continue
            break
        except ValueError:
            print("Invalid Input. Please enter a valid number. (e.g 8). ")
            continue
    
    while True:
        password = ""
        u_case = input("Do you want any uppercase letters? (y/n): ").lower()
        num = input("Do you want any numbers in the password? (y/n): ").lower()
        sym = input("Do you want any symbols in the password? (y/n): ").lower()
        invalid = False

        if u_case == 'y' or u_case == "yes":
            pass_l = l_letters + u_letters
        elif u_case == 'n' or u_case == "no":
            pass_l = l_letters
        else:
            print("The input for if uppercase letters be in the password is invalid. Re-enter.")
            invalid = True

        if num == 'y' or num == "yes":
            pass_l += digits
        elif num == 'n' or num == "no":
            pass_l = pass_l
        else:
            print("The input for if digits be in the password is invalid. Re-enter.")
            invalid = True

        if sym == 'y' or sym == "yes":
            pass_l += symbols
        elif sym == 'n' or sym == "no":
            pass_l = pass_l
        else:
            print("The input for if symbols be in the password is invalid. Re-enter.")
            invalid = True
        
        if invalid:
            print("Please re-enter all invalid criteria choices.\n")
            continue

        break

    for i in range(pass_len):
        password += random.choice(pass_l)
    
    print("\nYour random generated password is: ",password)
    s = input("Do you want to save this password? (y/n): ").lower()
    if s=='y' or s=="yes":
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
        print("Password saved to passwords.txt!")
    else:
        print("Password was not saved.")
    c = input("\n\nDo you want to Continue? (y/n): ").lower()
print("Thank you for using the random password generator!")