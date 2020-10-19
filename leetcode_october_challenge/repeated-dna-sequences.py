"""
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = len(s)
        if l <=10 :
            return []
        out = []
        for i in range(0, l-10):
            if s[i:i+10] in s[i+1:]:
                if s[i:i+10] in out:
                    continue
                out.append(s[i:i+10])
        return out


class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = len(s)
        hash_d = {}
        #print (l, s)
        if l <=10 :
            return []
        for i in range(0, l-10+1):
            #print (i)
            #print (s[i:i+10], s[i:])
            hash_d[s[i:i+10]] = hash_d.get(s[i:i+10], 0) + 1

        return [k for k, v in hash_d.items() if v > 1]


if __name__ == '__main__':
    s = "CAAAAAAAAAC"
    print ("Case 1 : S {}".format(s))
    sol = Solution().findRepeatedDnaSequences(s)
    print ("Solution : {}".format(sol))

    s = "GAGAGAGAGAGAG"
    print("Case 2 : S {}".format(s))
    sol = Solution().findRepeatedDnaSequences(s)
    print("Solution : {}".format(sol))

    s = "AAAAAAAAAA"
    print("Case 3 : S {}".format(s))
    sol = Solution().findRepeatedDnaSequences(s)
    print("Solution : {}".format(sol))

