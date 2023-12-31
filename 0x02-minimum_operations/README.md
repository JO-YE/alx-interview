# 0x02. Minimum Operations

## Details [method 1](./0-minoperations1.py)
```
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```
- **Problem Explanation:**
We have a text file with a single character `"H"` in it. We can perform two operations: `"Copy All"` and `"Paste."` The "Copy All" operation copies all the characters in the file, and the "Paste" operation appends the copied characters to the end of the file. We want to find the minimum number of operations required to have exactly n H characters in the file.

- **Approach:**
The idea is to find the divisors of `n` (excluding 1) and for each divisor `d`, check if it is possible to reach `n` `H` characters by copying `d` `Hs` and pasting `n//d - 1` *times.* We'll choose the divisor that requires the fewest number of operations.

```
Using **float('inf')** is a common way to initialize a variable to a value that will be overwritten with a smaller value during calculations.
n Python, inf is a floating-point value that represents an unbounded positive value, which is greater than any other numeric value. Similarly, there is a constant -inf, representing negative infinity.

The float('inf') syntax is used to create a floating-point representation of positive infinity in Python. When you use float('inf'), you are essentially creating a floating-point number that is larger than any other numeric value, including any finite floating-point number.
```

#### The recursive approach used to solve this problem can be explained as follows:

> If n is less than or equal to 1, we don't need any operations, and we return 0 as the base case of the recursion.
>
> For each divisor d of n, we calculate the number of operations required to reach n H characters using d as the base and recursively find the minimum operations needed for n // d H characters.
>
> We then choose the minimum of all the operations calculated for each divisor to get the final result.

```
The reason for using n + 1 in the range for the loop for divisor in range(2, n + 1): is to include the value of n in the range of possible divisors.

In Python, when using range(start, stop), the range starts at start and goes up to, but does not include, stop. Therefore, if we want to include n as one of the possible divisors, we need to use n + 1 as the upper bound in the range.
```

- The `min` method is used to update the value of min_ops to be the minimum between its current value and the value of num_operations.

***Error***
- using recursion can lead to issues like reaching the maximum recursion depth and consuming a significant amount of memory, especially for large inputs.
> The failure is due to the size limit of recursion in Python. 
>
> Python raises a "RecursionError: maximum recursion depth exceeded."

## SECOND METHOD
### [Prime Factorization Approach:](./0-minoperations.py)
- The prime factorization approach involves breaking down the number n into its prime factors and calculating the minimum operations based on those factors.

```
Step-by-step Explanation:

We start by initializing num_operations to 0 and divisor to 2.
While n is greater than 1, we perform the following steps:
Check if n is divisible by divisor.
If n is divisible, it means divisor is a prime factor of n.
We divide n by divisor and add divisor to the num_operations counter.
We continue this process until n becomes 1.
The final value of num_operations will represent the minimum number of operations needed to achieve the desired number of H characters.
```
***the prime factorization approach focuses on finding the prime factors of n and calculating the minimum operations based on those factors.***

> The prime factorization approach simplifies the calculation process by focusing on the key prime factors of n and reduces the complexity of finding the minimum operations.



