class Solution:
    # Solved this again, seemed more intuitive to go through in order instead
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = 0
        while m > 0 and n > 0:
            if nums1[ptr] > nums2[0]:
                num = nums2.pop(0)
                nums1.insert(ptr, num)
                nums1.pop()
                n -= 1
            else:
                m -= 1
            ptr += 1
        
        while nums2:
            num = nums2.pop(0)
            nums1[ptr] = num
            ptr += 1

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index of nums 1
        last = m + n - 1

        # while both lists, merge in reverse
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # while nums2: insert values into nums1
        while n > 0 :
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1

        # don't need to worry about nums1 values remaining as that is the list
        # we're sorting into