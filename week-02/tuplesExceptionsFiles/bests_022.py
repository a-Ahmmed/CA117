import sys

try:
    with open(sys.argv[1], "r") as f:
        a = [-1, ""]
        
        for line in f:
            try:
                s = line.split()
                if int(s[0]) > a[0]:
                    a[0] = int(s[0])
                    a[1] = " ".join(s[1:])
                elif int(s[0]) == a[0]:
                        a[1] = f'{a[1]}, {" ".join(s[1:])}'
            
            except ValueError:
                print(f'Invalid mark {s[0]} encountered. Skipping.')
        
        print(f"Best student(s): {a[1]}\nBest mark: {a[0]}")

except FileNotFoundError:
    print(f'The file {sys.argv[1]} could not be opened.')