def normalize(text: str) -> str:
    lowrtext = text.lower()
    textlist = []
    
    for char in lowrtext:
        if char.isalnum():
            textlist.append(char)
    parsedlist = "".join(textlist)
    return parsedlist

