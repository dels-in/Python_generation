def boxing(str):
    str=str.split()
    boxed_list = [[str[0]]]

    for i in range(1, len(str)):
        if str[i] in boxed_list[-1]:
            boxed_list[-1].extend(str[i])
        else:
            boxed_list.append([str[i]])
    return boxed_list


a = input()
boxed_string = boxing(a)

print(boxed_string)
