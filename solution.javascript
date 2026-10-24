function longestBalancedSubstring(s) {
    let stack = [-1]; // stores indices
    let maxLen = 0;

    const pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];

        if (ch === '(' || ch === '[' || ch === '{') {
            stack.push(i);
        } else {
            if (
                stack.length > 1 &&
                s[stack[stack.length - 1]] === pairs[ch]
            ) {
                stack.pop();

                maxLen = Math.max(
                    maxLen,
                    i - stack[stack.length - 1]
                );
            } else {
                // invalid closing bracket
                stack.push(i);
            }
        }
    }

    return maxLen;
}
