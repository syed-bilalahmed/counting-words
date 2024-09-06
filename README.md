# Word Counter in Python

This simple Python script reads a text file and counts the total number of words. It demonstrates basic file handling and string manipulation in Python.

## How It Works
- The script opens a file in read-only mode using the `open()` function.
- It reads the entire content of the file using `read()`.
- The file's content is then split into individual words using the `split()` function.
- The total word count is calculated by getting the length of the resulting list of words.
- The word count is printed to the console.

## Prerequisites
- Python 3.x must be installed on your system.
- A text file named `sampleFile.txt` should be present in the same directory as the script.

## Code Example
```python
# Initialize the number of words variable
num_of_words = 0

# Open file and read content
with open(r'sampleFile.txt', 'r') as file:

    # Reading the content of the file
    data = file.read()

    # Splitting the content into words
    lines = data.split()

    # Counting the number of words
    num_of_words += len(lines)

    # Printing the total word count
    print(num_of_words)
