def print_rectangle(length,width,filler,end_values):
    for __ in range(width):
        for __ in range(length):
            print(filler ,end = end_values)
        print()

print_rectangle(5,8,"A","ss")