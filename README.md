# BrainFuck
A simple BrainFuck interpreter in Python

**Brainfuck** (BF) is an incredibly popular esoteric programming language created in 1993 by Urban Müller. The language consists of what some might refer to as "pure" memory management, as all one does while programming in it is increment or decrement values, along with a single data pointer. It contains a grand total of 8 instructions, which only allow for basic looping, user input, and output. 
Here's a list of the instructions...

| Instruction | Description |
| --- | --- |
| + | Increments the value at the data pointer |
| - | Decrements the value at the data pointer |
| > | Increment the data pointer's address |
| < | Decrements the data pointer's address |
| , | Get 1 character of user input and store it at the data pointer |
| . | Print the character at the data pointer |
| \[ | Jumps to next \] if the value at the data pointer is 0 |
| \] | Jumps back to the previous \[ if the value at the data pointer is not 0 |


#### Usage
Usage : **`python3 brainfuck.py FILE`** where file contains the BrainFuck code.
`--help` for more info

#### TODO's
Code simple programs until i get BrainFucked xD!
You're welcome to join me in this quest!  
