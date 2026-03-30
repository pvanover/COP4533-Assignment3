def read_input(input_file):
    vals = {}
    with open(input_file, "r") as f:
        numChars = int(f.readline().strip())
        for i in range(numChars):
            line = f.readline().strip()
            char, val = line.split()
            vals[char] = val
        firstStr = f.readline().strip()
        secondStr = f.readline().strip()
    return numChars, vals, firstStr, secondStr
           
    
def highest_val_lcs():
    numChars, vals, firstStr, secondStr = read_input("input.txt")
    #print a single integer which is the maximum value of a common subsequence o A and B
    #print one optimal subsequence of A and B with the maximum value, if multiple exist output any one of them