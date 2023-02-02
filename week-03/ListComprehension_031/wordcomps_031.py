import sys

a = sys.stdin.readlines()

len17 = [line.strip() for line in a if len(line.strip()) == 17]
len18plus = [line.strip() for line in a if len(line.strip()) >= 18]
a4 = [line.strip() for line in a if line.strip().lower().count("a") == 4]
q2plus = [line.strip() for line in a if line.strip().lower().count("q") >= 2]
cie = [line.strip() for line in a if "cie" in line]
angleana = [line.strip() for line in a if sorted(line.strip().lower()) == ['a', 'e', 'g', 'l', 'n']]
angleana.remove("angle")

print(f'Words containing 17 letters: {len17}')
print(f'Words containing 18+ letters: {len18plus}')
print(f"Words with 4 a's: {a4}")
print(f"Words with 2+ q's: {q2plus}")
print(f'Words containing cie: {cie}')
print(f'Anagrams of angle: {angleana}')