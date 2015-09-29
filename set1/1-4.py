# This is a hack to make sure Python 2.x and 3.x behave the same
# You can ignore this bit
try:
    input = raw_input
except NameError:
    pass


# Real program starts here
def hash_password(string):
    return str(len(string) % 10)


hashed_password = "6"

print("Please enter the password")
password_input = input()

if(hash_password(password_input) == hashed_password):
    print("Success, huzzah")
else:
    print("Not success, boo")

print("")
print("Press enter to continue")
input()
