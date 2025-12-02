# Advent_of_Code_2025

Repo for Advent of Code 2025 challenges.

# Task 1

The script takes a text file with the task input, processes the rotations and calculates the number of times that the dial hits 0.

For every hit, a success message is printed into the console. The total sum of left (L) and right (R) rotations is displayed for testing purposes.

The starting point of 100,000 was chosen as a replacement for dial 0 to avoid writing a wrap-around solution for the dial crossing the 0 mark.

## Usage

`python 3 main.py <file path>`

## Example

The input:

```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

The result:

```
Hit 1 at direction R and number 48
Hit 2 at direction L and number 55
Hit 3 at direction L and number 99
sum_of_L is 340
sum_of_R is 122
(99832, 3)
``` 