# Advent_of_Code_2025

Repo for [Advent of Code 2025](https://adventofcode.com/2025/) challenges.

# Day 1, Task 1

<details>
<summary>Usage and example</summary>

The script takes a text file with the task input, processes the rotations and calculates the number of times that the dial stops exactly at 0.

For every hit, a success message is printed into the console. The total sum of left (L) and right (R) rotations is displayed for testing purposes.

The starting point of 100,000 was chosen as a replacement for dial 0 to avoid writing a wrap-around solution for the dial crossing the 0 mark. The resulting tuple shows the final position of the dial and the total number of 0 hits.

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
</details>

# Day 1, Task 2

<details>
<summary>Usage and example</summary>

I attempted to rewrite the script to calculate the number of times that the dial passes through 0.

The idea was to split each input number above 100 into the integral and fractional parts and increase the counter by the integral part (as it indicates the number of revolutions of the dial), then add the fractional part multiplied by (100 * number of decimal points) to "normalize" it into a whole number. 

Afterwards, I compare whether the initial number changed its sign, which would indicate whether it passed the 0 mark on the dial

The idea is incomplete and does not work, because it does not account for cases where the initial number did not change the sign (for instance, if the dial sits at 90 and rotates right for 20; the dial passed the 0 mark, but the sign remained the same).

A better approach would be to clamp the number in the range (0, 100) and calculate how many times it crossed either threshold. I would still need to "normalize" numbers equal or higher than 100 by dividing them by 100, adding the integral part to the counter and then turning the fractional part into a new whole to add it to the dial.

## Usage

`python 3 main.py <file path>`