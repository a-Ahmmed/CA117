import sys

contacts = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        l  = line.split()
        contacts[l[0]] = [l[1], l[2]]

for line in sys.stdin:
    s = line.rstrip()
    print(f'Name: {s}')
    try:
        print(f'Phone: {contacts[s][0]}\nEmail: {contacts[s][1]}')
    except KeyError:
        print("No such contact")