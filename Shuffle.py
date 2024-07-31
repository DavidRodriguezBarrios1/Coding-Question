import random
import time

def BuiltInShuffler(N):
    """
    Shuffles a list of integers from 1 to N and prints them using the built in function random.shuffle()

    Parameters:
    N (int): The number of integers to include in the list.
    """
    SubArry = list(range(1,N+1))
    random.shuffle(SubArry)
    print(*SubArry)
    return

def PythonShuffler(N):
    SubArry = list(range(1,N+1))
    index = N-1
    for index in range(N-1,0,-1):
        randomIndex = random.randint(0,index)
        SubArry[index],SubArry[randomIndex] = SubArry[randomIndex], SubArry[index]
    print(*SubArry)
    return
def main():
    """
    Main function to prompt the user for input, validate it, and call the shuffler function.
    """
    while True: 
        try:
            numberIteration = int(input("Please enter the the length of integers you would like to iterate over:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    start_time = time.perf_counter()
    BuiltInShuffler(numberIteration)
    end_time = time.perf_counter()
    print(f"Time taken with the BuiltIn Shuffler: {end_time - start_time} seconds")

    start_time1 = time.perf_counter()
    PythonShuffler(numberIteration)
    end_time1 = time.perf_counter()
    print(f"Time taken with the Python Shuffler: {end_time1 - start_time1} seconds")

if __name__ =='__main__':
    main()