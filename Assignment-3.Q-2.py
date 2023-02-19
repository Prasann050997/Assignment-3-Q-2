#Write a Python program to reverse a string.

def reverse(str):   
    str = str[::-1]   
    return str   
    
x = "1234abcd"   
print ("The reversed string is : ",reverse(x))  