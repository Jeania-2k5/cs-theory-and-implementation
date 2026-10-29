# 10) Longest Common Subsequence (Dynamic Programming)

s1 = "AGGTAB"
s2 = "GXTXAYB"

n = len(s1)
m = len(s2)

# DP table
dp = []
for i in range(n + 1):
    row = [0] * (m + 1)
    dp.append(row)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print("LCS length table:")
for row in dp:
    print(row)

# Backtrack to find LCS string
i = n
j = m
lcs_chars = []

while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:
        lcs_chars.append(s1[i - 1])
        i = i - 1
        j = j - 1
    else:
        if dp[i - 1][j] > dp[i][j - 1]:
            i = i - 1
        else:
            j = j - 1

lcs_chars.reverse()
lcs_string = "".join(lcs_chars)

print("\nString 1:", s1)
print("String 2:", s2)
print("Longest Common Subsequence:", lcs_string)
print("Length of LCS:", len(lcs_string))
