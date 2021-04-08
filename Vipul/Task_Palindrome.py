from collections import Counter

def check_palindrome(str):
    if str==str[::-1]:
        print("Minimum character required more : 0")
    else:
        to_form_palindrome(str)
        
def to_form_palindrome(str):
    var_count = Counter(str)
    count = 0
    for i in var_count.values():
        if i % 2 != 0:
            count +=1
    print("Minimum character required more :{}".format(count-1))
    
n = int(input("enter no of testcases : "))
for i in range(n):
    str = input("enter the string: ")
    str = str.replace(" ","")
    str = str.lower()
    check_palindrome(str)
