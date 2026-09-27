def longestBalancedSubstring(s: str) -> int:
    stack = []
    dp = [0] * (len(s) + 1)  # dp[i] stores longest valid substring ending at i-1
    max_len = 0
    
    for i, ch in enumerate(s):
        if ch in "([{":
            stack.append((ch, i))
        else:
            if stack:
                top, idx = stack[-1]
                if (top == "(" and ch == ")") or \
                   (top == "[" and ch == "]") or \
                   (top == "{" and ch == "}"):
                    stack.pop()
                    length = i - idx + 1
                    dp[i+1] = dp[idx] + length
                    max_len = max(max_len, dp[i+1])
                else:
                    stack.clear()
            else:
                dp[i+1] = 0
    return max_len
