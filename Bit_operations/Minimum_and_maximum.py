byte_quantity = int (input())

minimum_num= ((2**(byte_quantity*8-1))*(-1))
maximum_num= int((2**(byte_quantity*8)/2))

print(minimum_num, maximum_num-1)