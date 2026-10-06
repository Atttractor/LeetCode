package main

import "fmt"


func merge(nums1 []int, m int, nums2 []int, n int)  {
    ind1 := m - 1
	ind2 := n - 1
	ind := n + m - 1

	for ind >= 0 && ind2 >= 0 {
		if ind1 >= 0 && nums1[ind1] > nums2[ind2] {
			nums1[ind] = nums1[ind1]
			ind1--
		} else {
			nums1[ind] = nums2[ind2]
			ind2--
		}
		ind--
	}
	fmt.Println(nums1)
}
/*
Runtime: 0ms, beats 100.00%
Memory: 2.35MB, beats 15.73%. Это из-за трёх переменных,зато по скорости пушечка
Task: 
	You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
	Merge nums1 and nums2 into a single array sorted in non-decreasing order.
	The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
	To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
	and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
*/