class Solution:

    def __init__(self):
        pass

    def canMakePaliQueries(self, s, queries):
        ans = []
        for query in queries:
            left = query[0]
            right = query[1] + 1
            change = query[2]
            subs_string = s[left:right]
            is_palindrome_able = self.is_palindrome(subs_string, change)
            print(is_palindrome_able)
            print("-----------------")
            ans.append(is_palindrome_able)
        return ans

    def is_palindrome(self, string, change):
        print(string)
        if change >= 13:
            return True
        set_data = set()
        for c in string:
            if set_data.__contains__(c):
                set_data.remove(c)
            else:
                set_data.add(c)
        print(set_data)
        if change >= len(set_data) / 2:
            return True
        return False


if __name__ == '__main__':
    q = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    sol = Solution()
    result = sol.canMakePaliQueries("abcda", q)
    print(result)
