def xyz_there(str):
    if len(str) < 3:
        return False
    elif len(str) == 3:
        return str == "xyz"
    else:
        for i in range(len(str) - 2):
            if str[i:i + 3] == "xyz":
                if i == 0:
                    return True
                else:
                    if str[i - 1] == "." and i != len(str) - 2:
                        continue
                    else:
                        return True
    return False
