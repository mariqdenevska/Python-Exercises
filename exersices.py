#name = input("Enter your name:")
#result = len(name)
#result=name.find('M')
#result=name.rfind('M')
#result=name.capitalize()
#result=name.upper()
#result=name.count('m')
#print(result)
###################################################
#print(help(str))
#************************************#
#validate user input
# username = input("Enter username: ")

# if len(username) > 12 :
#     print("Username is more than 12 char")
# elif username.find(" ") != -1 :
#     print("Username is contains space")
# #elif any(char.isdigit() for char in username)  :
# elif not username.isalpha():
#     print("Username contains digit")
# else :
#     print("Username is ok")   
#********************************************************#

#  while loop 

name = input("enter name: ")

while name == "":
    print("yor name is empty")
    name = input("enter name: ")
print(f"hello {name}")    

#for loop execute a block of code a fixed number of times.
#You can iterate over a range, string, sequence, etc.
# for x in range(1, 11):
#    print(x)

#Collections
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER