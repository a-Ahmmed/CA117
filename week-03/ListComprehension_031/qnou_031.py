import sys

qnou = [line.strip() for line in sys.stdin if line.lower().count("q") != line.lower().count("qu")]
print(f"Words with q but no u: {qnou}")