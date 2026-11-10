        # """
        # :type nums1: List[int]
        # :type m: int
        # :type nums2: List[int]
        # :type n: int
        # :rtype: None Do not return anything, modify nums1 in-place instead.
        # """

def merge( nums1, m, nums2, n):
    p1 = m -1
    p2 = n -1
    tail = m+n -1

    while tail >= 0:
        #If p1 is empty
        if p1 == -1:
            nums1[tail] = nums2[p2]
            p2-= 1
        #If p2 is empty
        elif p2 == -1:
            nums1[tail] = nums1[p1]
            p1 -= 1
        #Normal Case
        elif nums1[p1] > nums2[p2]: 
            nums1[tail] = nums1[p1]
            p1-=1
        else:
            nums1[tail] = nums2[p2]
            p2-=1
        tail-=1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))
