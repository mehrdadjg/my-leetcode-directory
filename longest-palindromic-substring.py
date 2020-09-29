""" As of 09/28/2020 16:52 MST
    Runtime: 6476 ms (beats 15.64% of python3 submissions)
    Memory: 19.3 MB (beats 22.92%  of python3 submissions)
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_length = len(s)
        if s_length <= 1:
            return s

        def left(i, d):
            return (i, d-1)

        def below(i, d):
            return(i+1, d-1)

        def isPalindrome(i, d):
            if i >= d:
                return True
            else:
                return s[i] == s[d] and isPalindrome(i+1, d-1)

        def calc_dp(i, d):
            if d == 0:
                return True
            elif d == 1:
                return s[i] == s[i+1]
            else:
                return s[i] == s[i+d] and dp[i+1][d-2]

        max_length = 0
        max_palindrome = s[0]

        dp = [[] for _ in range(s_length)]
        for d in range(s_length):
            for i in range(s_length - d):
                dp[i].append(None)

                dp[i][-1] = calc_dp(i, d)

                if dp[i][-1] == True and max_length < d+1:
                    max_length = d+1
                    max_palindrome = s[i: d+i+1]

        return max_palindrome


s = Solution()
print(s.longestPalindrome("mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd"))
