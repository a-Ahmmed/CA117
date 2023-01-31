import sys

vowels = {
    "a": True,
    "e": True,
    "i": True,
    "o": True,
    "u": True,
}

s = sys.stdin.readline()
while s != "":
    s = s.strip()
    suffix = s[-2:]
    
    if suffix == "ch" or suffix == "sh" or suffix[1] == "x" or suffix[1] == "s" or suffix[1] == "z" or suffix[1] == "o":
        print(s + "es")
    elif suffix[1] == "y" and suffix[0] not in vowels:
        print(s[:len(s) - 1] + "ies")
    elif suffix[1] == "f":
        print(s[:len(s) - 1] + "ves")
    elif suffix == "fe":
        print(s[:len(s) - 2] + "ves")
    else:
        print(s + "s")
    
    s = sys.stdin.readline()