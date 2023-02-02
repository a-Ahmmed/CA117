import sys

a = [line.strip() for line in sys.stdin]

shortestVowel = [word.strip() for word in a if "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower()]
i, j = 0, 0
while i < len(shortestVowel):
    if len(shortestVowel[i]) < len(shortestVowel[j]):
        j = i
    i += 1

iaryWords = [word for word in a if word[-4:] == "iary"]

count = 0
for line in a:
    e = line.lower().count("e")
    if e > count:
        count = e
mostE = [line.strip() for line in a if line.lower().count("e") == count]

print(f'Shortest word containing all vowels: {shortestVowel[j]}')
print(f'Words ending in iary: {len(iaryWords)}')
print(f"Words with most e's: {mostE}")