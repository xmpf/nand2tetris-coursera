// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

(INIT)
@R2
M=0

(CHECK)
// CHECK IF EITHER RAM[1] == 0
// AND GOTO OUTPUT
@R1
D=M
@OUTPUT
D;JEQ

// CHECK IF EITHER RAM[0] == 0
// AND GOTO OUTPUT
@R0
D=M     // D = RAM[0]
@OUTPUT
D;JEQ

// USE A TEMPORARY VARIABLE
// AS A COUNTER
@R1
D=M     // D = RAM[1]
@temp
M=D     // RAM[temp] = D <= RAM[1]

(LOOP)
// LOAD NUMBER STORED IN RAM[0]
@R0
D=M
// AND ADD IT TO RAM[2]
// WHICH IS USED AS AN ACCUMULATOR
@R2
M=M+D

// LOAD COUNTER FROM RAM[temp]
// DECREMENT IT
// GOTO LOOP IF > 0
@temp
MD=M-1
@LOOP   
D;JGT    // IF D > 0 => repeat

(OUTPUT)
// LOAD ACCUMULATOR RAM[2]
// AND STORE IT IN D FOR OUTPUT
@R2
D=M

(END)
// END OF PROGRAM
// INFINITE LOOP
@END
0;JMP