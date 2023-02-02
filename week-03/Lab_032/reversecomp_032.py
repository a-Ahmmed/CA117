import sys
import time
start_time = time.time()

def binsearch(query, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid].lower() < query:
            low = mid + 1
        elif sorted_list[mid].lower() > query:
            high = mid - 1
        else:
            return True
    return False

def linsearch(query, sorted_list):
    i = 0
    while i < len(sorted_list):
        if query == sorted_list[i].lower():
            return True
        i += 1
    return False

a = [word.rstrip() for word in sys.stdin if len(word.rstrip()) >= 5]
print([word for word in a if binsearch(word.lower()[::-1], a)])
print(f'Execution Time: {(time.time() - start_time):.5f} seconds')