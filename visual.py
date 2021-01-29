def visual(tul, tur, tdl, tdr, cu, cd):

    blank = (" " * (len(tul) + len(tur) + len(cu) + 2) + "\n") * 2
    result = blank

    for i in range(len(tul)):
        if tul[i] == 1:
            result += "o"
        else:
            result += "-"

    result += " "
    for i in range(len(cu)):
        if cu[i] == 1:
            result += "o"
        else:
            result += "-"

    result += " "
    for i in range(len(tur)):
        if tur[i] == 1:
            result += "o"
        else:
            result += "-"

    result += "\n"
    for i in range(len(tdl)):
        if tdl[i] == 1:
            result += "o"
        else:
            result += "-"

    result += " "
    for i in range(len(cd)):
        if cd[i] == 1:
            result += "o"
        else:
            result += "-"

    result += " "
    for i in range(len(tdr)):
        if tdr[i] == 1:
            result += "o"
        else:
            result += "-"

    result += blank

    return result

# print(visual([1] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 4, [0] * 4))
