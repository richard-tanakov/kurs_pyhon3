nums = [int(i) for i in input().split()]
if len(nums) % 2 == 1:
    nums.sort()
    print(nums[1])
elif len(nums) % 2 == 0:
    nums.sort()
    out = (nums[2] + nums[1]) / 2
if out % 1 == 0:
    print(int(out))
else:
    print(out)
