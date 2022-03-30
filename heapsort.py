# coding:utf-8

def heapsort(nums):
    length = len(nums)
    if length == 0:
        return
    for i,n in enumerate(nums):
        if 2*i + 1 < length:
            if nums[i] < nums[2*i + 1]:
                a = nums[i]
                nums[i] = nums[2*i + 1]
                nums[2 * i + 1] = a

        if 2*i + 2 < length:
            if nums[i] < nums[2*i + 2]:
                b = nums[i]
                nums[i] = nums[2 * i + 2]
                nums[2 * i + 2] = b

    s = nums[0]
    nums[0] = nums[-1]
    nums[-1] = s
    print(s)
    heapsort(nums[:-1])







if __name__ == '__main__':
    lst = [5,9,6,1,8,3,7,5,4]
    heapsort(lst)