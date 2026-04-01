# COP4533-Assignment3

Paige Vanover
UFID: 22473613

## Question 1

## Question 2
Let $dp[i][j]$ = maximum value of a common subsequence of $A[0...i-1]$ and $B[0...j-1]$

$$
dp[i][j] = \begin{cases}
    0 & \text{if } i = 0 \text{ or } j = 0 \\
    dp[i-1][j-1] + val(A[i-1]) & \text{if } A[i-1] = B[j-1] \text{ and } i,j > 0 \\
    \max(dp[i-1][j], dp[i][j-1]) & \text{if } A[i-1] \neq B[j-1] \text{ and } i,j > 0
\end{cases}
$$

If either of the strings are empty, then there is automatically no common subsequence which explains the correctness of the base case. If there are characters that match, we include that character in the subsequence and add its value to the optimal solution. This works because dynamic programming breaks a problem into subproblems, so adding a matching character value to the optimal subsequence ensures a new optimal subsequence up to this point. If the characters don’t match then we don’t include those characters and choose the optimal subsequence to be the max of the optimal solution for A or the optimal solution for B and that makes sure that we are taking the most optimal value.

## Question 3
