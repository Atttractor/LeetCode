package main

import "fmt"

func moveZeroes(nums []int)  {
    count := 0
	for _, elem := range nums {
		if elem != 0 {
			nums[count] = elem
			count++
		}
	}
	for i := count; i < len(nums); i ++ {
		nums[i] = 0
	}
	fmt.Println(nums)
}
/*
Runtime: 19ms, beats 72.22%
Memory: 6.83MB, beats 65.79%
Task: 
	Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
	Note that you must do this in-place without making a copy of the array.
*/