#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    a = dir(hidden_4)
    for i in range(0, len(a)):
        if a[i].startswith('_'):
            continue
        else:
            print("{}".format(a[i]))
