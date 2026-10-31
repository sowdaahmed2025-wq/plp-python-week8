# Personal Mini-Toolkit

## What it does
A menu-driven Python program with three tools:
- **Number Guessing Game:** guess a secret number from 1-10 with Too low/Too high hints.
- **To-Do List:** add, view, and remove tasks.
- **Simple Calculator:** add, subtract, multiply, and divide two numbers.

## How to run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run: `python toolkit.py`
4. Choose a number from the menu. Choose 4 to quit.

## Reflection
The hardest part of this project was putting the code in the right place in toolkit.py and keeping the indentation correct, because I was working with several functions in one file for the first time. The bug that took longest to fix was a NameError saying that "calculator" was not defined. It happened because I connected the menu to calculator() before the function existed, and later a copy of the function ended up below the menu loop, where Python never reached it. I fixed it by deleting the duplicate copy and moving one copy above the menu loop, and I learned that Python reads a file from top to bottom. I also learned to build and test one tool at a time, which made mistakes easier to find. With one more week, I would save the to-do list to a file so the tasks are not lost when the program closes. I would also add a score tracker to the guessing game and more calculator operations, like powers and percentages.
