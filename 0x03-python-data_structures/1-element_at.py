#!/usr/bin/python3
def element_at(my_list, idx):
    _len = len(my_list)
    if idx < 0:
        return None
    elif idx > _len:
        return None
    elif idx == 0 and _len == 0:
        return None
    else:
        return my_list[idx]
