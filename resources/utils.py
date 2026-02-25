def check_that_lists_are_equal(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    if set_1 == set_2:
        return True
    else:
        difference = set_1 ^ set_2
        print(f"Lists are not equal. List_1: {list_1}, List_2: {list_2}, Difference: {difference}")
        return False
