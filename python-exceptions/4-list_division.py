#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for i in range(list_length):
        try:
            answer = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            answer = 0
            print("wrong type")
        except ZeroDivisionError:
            answer = 0
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list[i] = answer
    return new_list
