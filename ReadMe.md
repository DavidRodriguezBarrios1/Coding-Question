# Integer Shuffler

This Python script generates a list of integers from 1 to N, shuffles them using the Fisher-Yates algorithm, and prints the shuffled list. The shuffling is performed using both the random.shuffle method and a manually implemented Fisher-Yates algorithm for comparison. The script also measures and reports the time taken to perform the shuffling and printing operations.

## Features

- Generates a list of integers from 1 to N.
- Shuffles the list using an efficient built-in method and a manually implemented Fisher-Yates shuffling algorithm.
- Prints the shuffled list in a space-separated format.
- Measures and reports the time taken for the shuffling and printing process.

## How to Run the Script

1. Clone the repository or download the script file.
2. Run the script using Python:

```
    python Shuffle.py
```

3. When prompted enter the N value you would like to iterate over.

## Explanation of Language of Choice and Built-In Function

The reason I chose Python is because syntactically it is easy to read. In any high-level interpreted languages such as JavaScript, Python, etc implementing a Shuffle algorithm would take longer than lower level languages.

The random.shuffle() function in Python uses the Fisher-Yates shuffle algorithm. It operates in an O(N) time complexity, where N is the number of items in the list. If I were always optimizing for speed, I would always opt for a lower-level built-in function when possible.

## Explanation of the Fisher-Yates Shuffle Algorithm

The Fisher-Yates algorithm works by iterating through the list from the last element to the first and swapping each element with a randomly chosen element that comes before or at the current position. This ensures that every permutation of the list is equally as likely.

### Fisher-Yates Shuffle Algorithm Broken Down

1. Start from the last index of the list.
2. Pick a random index from 0 to the current index.
3. Swap the element at the current index with the randomly chosen index's element.
4. Move to the previous index and repeat until the beginning of the list is reached.

### Limitations of The Fisher-Yates Shuffle Algorithm

As larger integers are selected the memory complexity becomes too high, making it impractical.

### Why Fisher-Yates over a random generator with a "Seen" set to avoid duplicates?

Although a random generator with a set to avoid duplicates can initially have less memory complexity, it would eventually reach a similar complexity as the Fisher-Yates' list would have. Searching through the set and ensuring there are no duplicates would grow increasingly. Additionally, if we randomly generate the same number by coincidence it would be redundant.
