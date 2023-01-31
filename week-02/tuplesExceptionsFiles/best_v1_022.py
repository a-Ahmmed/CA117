import sys

try:
    with open(sys.argv[1], "r") as f:
        a = [0, ""]
        
        for line in f:
            s = line.split()
            if int(s[0]) > a[0]:
                a[0] = int(s[0])
                a[1] = " ".join(s[1:])
        
        print(f"Best student: {a[1]}\nBest mark: {a[0]}")

except FileNotFoundError:
    print(f'The file {sys.argv[1]} could not be opened.')