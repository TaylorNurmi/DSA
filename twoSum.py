
#about 10 minutes
def twoSum(nums, target):
    checked = {}
    for i in range(len(nums)):
        if nums[i] + nums[i+1] == target:
            return [i, i+1]
        if target - nums[i] in checked:
            print(checked[target - nums[i]])
            return [checked[target - nums[i]], i]
        if nums[i] not in checked:
            checked[nums[i]] = i
