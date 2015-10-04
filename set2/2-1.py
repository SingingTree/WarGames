# This is a hack to make sure Python 2.x and 3.x behave the same
# You can ignore this bit
try:
    input = raw_input
except NameError:
    pass

# Real program starts here
def hash(number):
    return number % 23


password_hash = 17

print("Please enter the password")
password_input = int(input())

if(hash(password_input) == password_hash):
    print("Success, huzzah")
else:
    print("Not success, boo")

print("")
print("Press enter to continue")
input()
