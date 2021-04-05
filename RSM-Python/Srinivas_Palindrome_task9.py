# ------------------ Steps   -------------------
# 1 Check if input string is palindrome
# 2    if palindrome -- Output 0
# 3    else send to function check_if_it_can_form_palindrome()
# 4        if it can be rearranged into palindrome -- Output 0 
# 5        else add the number of characters to be appended
# 6            Output -- no. of characters added to make it a palindrome

from collections import Counter

def is_palindrome(s):  #  1
    return s==s[::-1]

def check_palindrome(st):             
    if(is_palindrome(st)):  #  2
        print('0')                      
    else:
        check_if_it_can_form_palindrome(st)   #  3

def check_if_it_can_form_palindrome(st):  #  3
    count=0
    res=Counter(st)
    for c in res.values():
        if(int(c)%2!=0):
            count=count+1
    print(count-1)                          # 4, 5 (-1 becuase we can have one odd character in the palindrome)

repeat=int(input("No. of strings"))
for i in range (0,repeat):
    string=input("Enter String ")
    check_palindrome(string)

