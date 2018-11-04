

def create_name_dict():
    f = open("ticker_name.txt", "r")
    message = f.read()
    dict = {}
    is_name = False
    key = ""
    name = ""
    for index in range(0, len(message)):
        if not is_name:
            if message[index] == ",":
                is_name = True
            else:
                key += str(message[index])
        else:
            if message[index] == "\n":
                dict[key] = name
                is_name = False
                name = ""
                key = ""
            else:
                name += str(message[index])
    return dict

    f.close()


def create_desc_dict():
    f = open("ticker_desc.txt", "r")
    message = f.read()
    dict = {}
    is_name = False
    key = ""
    name = ""
    is_sector = True
    for index in range(0, len(message)):
        if not is_name:
            if message[index] == ",":
                is_name = True
            else:
                key += str(message[index])
        else:
            if message[index] == "\n":
                dict[key] = name
                is_name = False
                name = ""
                key = ""
                is_sector = True
            else:
                if message[index] == ",":
                    if is_sector:
                        name += ": "
                        is_sector = False
                    else:
                        name += str(message[index])
                else:
                    name += str(message[index])
    return dict

    f.close()
