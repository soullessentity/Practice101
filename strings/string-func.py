def reverse_str(string1):
    str1 = ""
    for ch in string1:
        str1 = ch + str1
        print(ch, str1)
    print(str1)

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
    reverse_str("hello")
    substring_p("hello", "lo")
    substring_p("hello", "ho")
