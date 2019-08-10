def twosum(nums,target):
    cache = {}
    for i in range(0, len(nums)):
        if target - nums[i] in cache:
            print(cache[target - nums[i]], i)
        else:
            cache[nums[i]] = i
def two_sum(nums,target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print([{i}], [{j}])

def threesum(nums,target):
    cache = {}
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (target - nums[i] - nums [j]) in cache:
                print(cache[target - nums[i] - nums [j]], i, j)
            else:
                cache[nums[i]] = i
                cache[nums[j]] = j

def three_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    print(nums[i], "+", nums[j], "+", nums[k], "=", target, [i], [j], [k])

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    nums1 = [1,2,3,4,5,6,7,8,9,10,11,12]
    twosum(nums,6)
    two_sum(nums,6)
    threesum(nums1,13)
    three_sum(nums1,13)