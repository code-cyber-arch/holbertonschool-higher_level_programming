#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    to_print = dir(hidden_4)
    for i in to_print:
        if i[:2] != "__":
            print(i)
