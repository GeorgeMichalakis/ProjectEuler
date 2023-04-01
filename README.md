# About
Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems.

The motivation for starting Project Euler, and its continuation, is to provide a platform for the inquiring mind to delve into unfamiliar areas and learn new concepts in a fun and recreational context.

## Problems

### Problem1 (Solved)

#### Question

If we list all the natuural numbers below 10 that are multipels of 3 and 5 we get 3,5,6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below N.

#### Solution
Apart from the typical brute force for loop, we can think of something a bit more sophisticated. There is a formula for O(1) computation of the amount of numbers below N that are multiples of a number X.


Also the sum of all numbers less than n that divides d equals d times the sum of all numbers less than n/d.

The sum of all numbers from 1 to n is equal to n*(n+1)/2.
Why? 

1 + 2 + 3 + 4 + ....
100 + 99 + 98

all equal to 101. How many times? 101 * 100 = (n + 1) * n. Ok but we need to remove half cause we are adding it two times. So [(n+1) * n]/2

Now I have all the numbers until number N. Now I want the ones that are multiple by N. Like

3 + 6 + 9 = 3(1+2+3+4...) so 3 * [n/3(n/3+1)]/2

SUM_OF_NUMBER_X : X * (N DIV X) * ((N DIV X) + 1) DIV 2

We'll just have to make sure (in case we are talking about more than 1 number, to remove the duplicates from their multiplication)