nums = [12, -7, 20, 1, 4, -10, -1]

def subsetsum(numbers: list, target: int) -> bool:
    complements = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in complements:
            print(True, num, complement)
            return True
        complements[num] = i
    print(False)
    return False 

subsetsum(nums, 2)