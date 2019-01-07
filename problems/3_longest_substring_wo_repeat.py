class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n == 1:
            return n
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if unique(s, i, j):
                    ans = max(ans, j - i + 1)
                else:
                    ans = max(ans, 1)
        return ans

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        start = 0
        n = len(s)
        maps = {}

        for i in range(n):

            if maps.get(s[i]) is not None:
                start = max(start, maps.get(s[i]) + 1)
            else:
                start = max(start, 0)
            # print(s[i], maps.get(s[i]), start)
            result = max(result, i - start + 1)
            maps[s[i]] = i
        return result


def unique(s, i, j):
    s_set = set()
    for k in range(i, j + 1):
        if s[k] in s_set:
            return False
        s_set.add(s[k])
    return True


input_value = "abcabcbb"
s1 = Solution()
print(s1.lengthOfLongestSubstring(input_value))
print(s1.lengthOfLongestSubstring2(input_value))
