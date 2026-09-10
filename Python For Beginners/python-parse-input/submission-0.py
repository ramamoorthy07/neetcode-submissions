from typing import List

def read_integers() -> List[int]:
    line = input()
    integers = [int(num) for num in line.split(',')]
    return integers
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
