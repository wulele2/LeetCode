# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they
 add up to a specific target.
You may assume that each input would have exactly one solution, and you may 
not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# =============================================================================
# 以下是第一种思路：暴力循环
# 1.由于题目中要求不能出现在同一个位置。--应该考虑添加 i！=j 这行代码
# =============================================================================
def twosum1(num,target):
    '''
    num--int array
    target--int
    '''
    length=len(num)
    for i in range(length):
        for j in range(length-1):
            if num[i]+num[j+1]==target and i!=j:
                return i,j+1
# =============================================================================
# 第二种利用做差。
# 1.关于字典的用法
#2.以下其实 借助了哈希表的思路。即记录下每个元素出现的位置。
# =============================================================================
def twosum2(num,target):
    '''
    num--int array
    target--int
    '''
    h={}
    length=len(num)
    for i in range(length):
        sub=target-num[i]
        if sub not in h:
            h[sub]=i      #h[3]=0;{3:0} ;h[2]=1;{3:0,2,1}
        else:
            return h[sub],i
# =============================================================================
# 以下同样python哈希表。
# 注意学会利用 enumerate的用法
# =============================================================================
def twosum3(num,target):
    '''
    num--int array
    target--int
    '''
    h={}
    for index,n in enumerate(num):
        sub=target-n
        if sub in h:
            return h[sub],index
        else:
            h[sub]=index
a=[1,2,2,7]
b=4
print(twosum3(a,b))
            
    
    
    
    
    
    