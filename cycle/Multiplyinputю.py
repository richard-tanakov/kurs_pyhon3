nums_out = 1
while nums_out != 0:
    nums = int(input())
    if nums == 0:
        print(nums_out)
        break
    elif nums != 0:
        nums_out *= nums
