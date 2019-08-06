def twosum(nums,target):
    cache = {}
    for i in range(0, len(nums)):
        if target - nums[i] in cache:
            print(cache[target - nums[i]], i)
        else:
            cache[nums[i]] = i

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    twosum(nums,6)