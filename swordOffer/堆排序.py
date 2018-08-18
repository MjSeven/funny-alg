# !/usr/bin/python3


def heap_sort(nums):
	if not nums:
		return
	size = len(nums)
	build_heap(nums, size)
	for i in range(size)[::-1]:
		nums[0], nums[i] = nums[i], nums[0]
		adjust_heap(nums, 0, i)

def build_heap(nums, size):
	for i in range(size//2)[::-1]:
		adjust_heap(nums, i, size)

def adjust_heap(nums, i, size):
	lchild = 2*i+1
	rchild = 2*i+2
	m = i
	if i < size//2:
		if lchild < size and nums[lchild] > nums[m]:
			m = lchild
		if rchild < size and nums[rchild] > nums[m]:
			m = rchild

		if m!= i:
			nums[m], nums[i] = nums[i], nums[m]
			adjust_heap(nums, m, size)


if __name__ == '__main__':
    nums = [1, 9, 38, 65, 97, 76, 13, 27, 49, 100]
    heap_sort(nums)
    print(nums)