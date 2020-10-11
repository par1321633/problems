"""
https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        output = []
        start = 0
        end = len(s)
        while start < end:
            if s[start] in output:
                start = start + 1
                continue
            output.append(s[start])
            sl = 0
            el = len(output)
            while sl < el-1 and sl >= 0:
                if output[sl] > output[sl+1]:
                    if output[sl] in s[start:]:
                        output.pop(sl)
                        el = el-1
                        sl = sl-1
                        continue
                sl = sl + 1
            start = start + 1
        return ''.join(output)

if __name__ == '__main__':
    s = 'bcabc'
    print ("Case : String : {}".format(s))
    sol = Solution().removeDuplicateLetters(s)
    print ("Solution : {}".format(sol))

    s = 'cbacdcbc'
    print("Case : String : {}".format(s))
    sol = Solution().removeDuplicateLetters(s)
    print("Solution : {}".format(sol))

