#inital 
num_of_word= 0
#open file and read
with open(r'sampleFile.txt', 'r') as file:
     
    # Reading the content of the file
     data = file.read()

    # Splitting the data into separate lines
    # using the split() function
     lines= data.split()
     num_of_words += len(lines)