#!/usr/bin/python3
def uppercase(str):
    upp_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upp_str += chr(ord(i) - 32)
        else:
            upp_str += i
    print("{}".format(upp_str))
