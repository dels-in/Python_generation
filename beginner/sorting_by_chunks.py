def chunked(str, num_chunks):
    str = str.split()
    chunked_list = []

    for i in range(0, len(str), num_chunks):
        chunked_list.append(str[i:i + num_chunks])
    return chunked_list


s, n = input(), int(input())
chunked_string = chunked(s, n)

print(chunked_string)
