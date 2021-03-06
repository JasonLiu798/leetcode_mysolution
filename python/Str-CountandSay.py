#!/bin/env python
#-*- coding:utf-8 -*-

'''
38. Count and Say
easy
https://leetcode.com/problems/count-and-say/
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        curstr='1'
        if n<=0:
            return ''
        if n==1:
            return '1'
        i=0
        while i<n-1:
            curstr=self.genOne(curstr)
            i+=1
        return curstr

    def genOne(self,s):
        res=''
        if s=='':
            return '1'
        idx=0
        while idx<len(s):
            nxt=idx+1
            # print 'idx',idx,'nxt',nxt
            if nxt<len(s):
                dupCnt=1
                while nxt<len(s) and s[nxt]==s[idx]:
                    nxt+=1
                    dupCnt+=1
                if dupCnt>1:
                    res+=str(dupCnt)+s[idx]
                    idx+=dupCnt
                else:
                    res+='1'+str(s[idx])
                    idx+=1
            else:
                res+='1'+s[idx:nxt]
                idx+=1
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.genOne('111221')
    # res = s.countAndSay(4)
    #1 1
    #2 11
    #3 21
    #4 1211
    #5 111221
    #6 312211
    print res




