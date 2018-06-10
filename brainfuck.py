import sys
from sys import stdin,stdout,argv

#Compile jump table to deal with loops and nested loops
def jumptable(code):
	stack = []
	jump = [None] * len(code)
	for i,o in enumerate(code):
	    if o=='[':						#Every time a "[" is encountered, push the current location  
	        stack.append(i)				#of the instruction pointer on this stack


	    elif o==']':					#Whenever  a "]" is encountered, reset the instruction pointer 
	        jump[i] = stack.pop()		#to the value that's currently on the top of the stack
	        jump[jump[i]] = i 			#When a loop is complete, pop it off the stack.
	return jump


#Brainfuck Interpreter	
def unfuck(code): 
    tape = [0] * 5000   # tape memory
    cp = 0              # code pointer
    tp = 0              # tape pointer

    # calculate the jump table
    jump=jumptable(code)

    # execute
    while cp < len(code):
        char = code[cp]
        if   char == '>':
        	tp += 1

        elif char == '<':
        	tp -= 1

        elif char == '+':
        	tape[tp] += 1 

        elif char == '-':
        	tape[tp] -= 1 

        elif char == '.':
        	stdout.write(chr(tape[tp]))

        elif char == ',':
        	tape[tp] = ord(stdin.read(1))

        elif char == '[' and not tape[tp]: # skip loop if current tape value == 0 (break condition in BrainFuck)
            cp = jump[cp]

        elif char == ']' and tape[tp]:     # loop back if !=0
            cp = jump[cp]

        else:
        	pass

        cp += 1

def main():
    
	if len(argv)>1:

	    if argv[1]=='--help':
	    	print("""
	    			BRAINFUCK INTERPRETER
	    						-Krash
Usage :
python3 brainfuck.py FILE

Takes input from the FILE and compiles the BrainFuck code""")

	    else:
	    	file=open(argv[1])
	    	unfuck(file)
	else:
		print("Enter the BrainFuck code :")
		code=input()
		unfuck(code)



if __name__ == "__main__":
    main()