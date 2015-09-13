# This is a hack to make sure Python 2.x and 3.x behave the same
# You can ignore this bit
try:
    input = raw_input
except NameError:
    pass


# Real program starts here
def ceaser_shift(string, shift):
    new_string = ""
    for char in string:
        new_string = new_string + chr((ord(char) + shift))
    return new_string

password = "swordfish_Sw0rdf1sh"

print("Please enter the password")
password_input = input()

if(password_input == ceaser_shift(password, 1)):
    print("Success, huzzah")
else:
    print("Not success, boo")
