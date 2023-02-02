import sys

try:
    with open(sys.argv[1], "r") as f1:
        with open(sys.argv[2], "r") as f2:
            i , s1, s2 = 0, f1.readline(), f2.readline()
        
            while s1 != "" and s2 != "":
                if i % 2 == 0:
                    sys.stdout.write(s1)
                    s1 = f1.readline()
                else:
                    sys.stdout.write(s2)
                    s2 = f2.readline()

                i += 1
        
            if s1 == "":
                while s2 != "":
                    sys.stdout.write(s2)
                    s2 = f2.readline()
            else:
                while s1 != "":
                    sys.stdout.write(s1)
                    s1 = f1.readline()

except FileNotFoundError:
    print(f"The file {sys.argv[1]} or {sys.argv[2]} does not exist. Exiting.")

except IndexError:
    print(f'2 files required. Exiting.')

except UnicodeDecodeError:
    print(f'Unsupported file format(s). Exiting.')