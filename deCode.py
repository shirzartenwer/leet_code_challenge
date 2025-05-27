def decodeVariations(S: str) -> int:
    l = 0
    r = 0
    cnt = 1
    while l <= r < len(S):

        if l != r:
            if int(S[l:r+1]) <= 26:
                if int(S[l]) != 0:
                    cnt += 1
                l += 1
            else:
                l = r
        else:
            if int(S[l]) == 0:
                cnt -= 1
        r += 1

    return cnt


def decodeVariations(S: str) -> int:
    if not S:
        return 0

    pre, cur = 27, 0
    first, second = 1, 1

    for i in range(len(S) - 1, -1, -1):
        d = int(S[i])
        if d == 0:
            cur = 0
        else:
            cur = first
            # pre represents the previously seen number S[i+1]
            # If d*10 + pre < 27 (and d != 0), it is valid to
            # write a letter that uses two digits of encoding length,
            # so we count 'second = dp[i+2]' in our current answer.
            if d * 10 + pre < 27:
                cur += second

        pre = d
        first, second = cur, first

    return cur
