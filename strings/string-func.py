def reverse_str(string1):
    temp = string1.split(' ')
    print(type(temp))
    str1 = ""

    list2 = []
    for i in range(0, len(temp)):
        str1 = temp[i]
        str2 = ""
        for ch in str1:
            str2 = ch + str2
        list2.append(str2)

    print(' '.join(list2))

def substring_p(str1, sub1):
    if str.find(str1,sub1) == -1:
        print(sub1, " not a substring")
    else:
        print(sub1, " is sub string of ", str1)
    if str1.find(sub1) == -1:
        print("not substring")
    else:
        print("is a substring")


if __name__ == '__main__':
    reverse_str("hello i am divya")
    # substring_p("hello", "lo")
    # substring_p("hello", "ho")
