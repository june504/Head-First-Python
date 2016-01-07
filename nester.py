def print_lol(the_list, indent=False, depth=0):
    for item in the_list:
        if isinstance(item,list):
            print_lol(item, indent, depth+1)
        else:
            for tabs in range(depth):
                print("\t", end='')
            print(item)
