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
           
    
def highest_val_lcs(input_file):
    numChars, vals, firstStr, secondStr = read_input(input_file)
    #compute a common subsequence of A and B that maximizes the total value
    #print a single integer which is the maximum value of a common subsequence o A and B
    #print one optimal subsequence of A and B with the maximum value, if multiple exist output any one of them
    n = len(firstStr)
    p = len(secondStr)
    dp = [[0] * (p + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, p + 1):
            if firstStr[i - 1] == secondStr[j - 1]:
                #if the characters match then add the char value to the previous value
                dp[i][j] = dp[i - 1][j - 1] + int(vals[firstStr[i - 1]])
            else:
                #if chars dont match take the max
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_value = dp[n][p]

    #find subsequence
    res = []
    while n > 0 and p > 0:
        if firstStr[n - 1] == secondStr[p - 1]:
            res.append(firstStr[n - 1])
            n -= 1
            p -= 1
        elif dp[n - 1][p] > dp[n][p - 1]:
            n -= 1
        else:
            p -= 1
    res.reverse()
    opt_res = "".join(res)
    print(max_value)
    print(opt_res) 

        

    ## input_file = "input1.txt"           

input_file = "tests/input6.txt"
highest_val_lcs(input_file)