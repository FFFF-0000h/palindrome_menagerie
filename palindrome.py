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
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) > len(best):
                best = substr
    return best

def main():
    text = input("Enter text: ")
    result = longest_palindrome(text)
    print(f"Longest palindrome: {result} length: {len(result)}")

if __name__ == "__main__":
    main()
