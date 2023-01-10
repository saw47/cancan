from var import DOWN



def list_printer(item: list):
    len = item.__len__()
    for i in item:
        if i.index != len - 1:
            print(f"{i[0]} -> {i[1]};")
        else:
            print(f"{i[0]} -> {i[1]}.")
    print(DOWN)



