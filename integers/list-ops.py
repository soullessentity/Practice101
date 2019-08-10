def list_sort(l1):
    print(l1)
    l1.sort()
    print(l1)

def list_reverse(l2):
    print(l2)
    l2.reverse()
    print(l2)

def list_append(l1,l2):
    l1.extend(l2)
    print(l1)

    print(l1+l2)

    l1.append(l2)
    print(l1)

def list_max_sum_of_two(l1):
    l1.sort()
    print(l1)
    leng = len(l1)

    value = l1[leng-1] + l1[leng-2]
    print(value)

import itertools
def list_of_sublists(nums):
    for i in range (0, len(nums)+1):
        list_new = list(itertools.combinations(nums,i))
        print(list_new)

if __name__ == '__main__':
    list1 = [1,6,2,5]
    list2 = [7,3,4,9]
    list3 = [1,2,3]

    list_sort(list1.copy())
    list_reverse(list1)
    list_append(list1.copy(),list2)
    list_max_sum_of_two(list2)
    list_of_sublists(list3)