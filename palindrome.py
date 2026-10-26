def normalize(text: str) -> str:
    lowrtext = text.lower()
    textlist = []
    
    for char in lowrtext:
        if char.isalnum():
            textlist.append(char)
    parsedlist = "".join(textlist)
    return parsedlist

def is_palindrome(s: str) -> bool:
    st = normalize(s)
    st_reversed = st[::-1]
    return st == st_reversed

def longest_palindrome(text: str) -> str:
    s = normalize(text)
    best = ""
    for center in range(len(s)):
        # Odd-length palindrome: "aba" centered on 'b'
        odd = expand_around_center(s, center, center)
        # Even-length palindrome: "abba" centered between the two 'b's
        even = expand_around_center(s, center, center + 1)
        if len(odd) > len(best):
            best = odd
        if len(even) > len(best):
            best = even
    return best

def expand_around_center(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
       left -= 1
       right += 1
    # Loop exits when either: left < 0, right >= len(s), or chars don't match.
    # Slice [left + 1:right] gives the palindrome without th mismatched pair.
    return s[left + 1:right]

def main():
    text = input("Enter text: ")
    result = longest_palindrome(text)
    print(f"Longest palindrome: {result} length: {len(result)}")

if __name__ == "__main__":
    import time
    
    # Correctness
    assert normalize("A man, a plan!") == "amanaplan"
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("aa") is True
    assert is_palindrome("ab") is False
    assert is_palindrome("racecar") is True
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ab") in ("a", "b")
    assert longest_palindrome("abacdfgdcaba") == "aba"
    assert longest_palindrome("A man, a plan, a canal: Panama") == "amanaplanacanalpanama"

    # Performance scaling
    for n in (500, 1000, 2000):
        s = "a" * n
        t = time.perf_counter()
        longest_palindrome(s)
        print(f"n={n}:  {time.perf_counter() - t:.4f}s")

    main()
