class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

if __name__ == '__main__':
    solution = Solution()
    print (solution.toLowerCase("Hello"))
    print (solution.toLowerCase("here"))
    print (solution.toLowerCase("LOVELY"))