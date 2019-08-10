def count_character(str):
    print("Length of string is ", len(str))

def is_substr(str1,str2, sub):
    if str.find(str1,sub) == -1:
        print("sub string doesnt exists")
    else:
        print("sub string exists")

    if str2.find(sub) == -1:
        print("sub string doesnt exists")
    else:
        print("sub string exists")
from collections import Counter
def count_char(str1):
    cache = {}
    for ch in str1:
        if ch in cache:
            cache[ch] += 1
        else:
            cache[ch] = 1
    print(cache)

    for elm in cache:
        if cache[elm] > 1:
            print(elm, "has duplicate and counter is ", cache[elm])
        else:
            print(elm, "is unique")


    str2 = "hello howdy"
    cache1 = Counter(str2)
    print(cache1)

    cache2 = {}
    for ch in str2:
        cache2[ch] = str2.count(ch)
    print("cache2",cache2)

    for key in cache2:
        if cache2[key] > 1:
            print(key, "has duplicate")
        else:
            print(key, " is unique")


def reverse_str(str1):
    str2 = ""
    for ch in str1:
        str2 = ch + str2
    print(str2)

    list1 = []
    list1 = str1.split()
    print(list1)

    for ind in list1:
        
if __name__ == '__main__':
    count_character("hello")
    is_substr("hello hi", "how are you", "hi")
    count_char("how are you woman how")
    reverse_str("hello there")
