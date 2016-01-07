import sys
def print_lol(the_list, indent=False, depth=0, fileTo=sys.stdout):
    for item in the_list:
        if isinstance(item,list):
            print_lol(item, indent, depth+1, fileTo)
        else:
            if indent:
                for tabs in range(depth):
                    print("\t", end='', file=fileTo)
            print(item, file=fileTo)
