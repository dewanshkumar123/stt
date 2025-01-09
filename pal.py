def check_pal(s):
    n = len(s)
    for i in range(n//2):
        if (s[i] != s[n-1-i]):
            return False

    return True

print(check_pal("aabbaa"))