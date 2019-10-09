// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

@CHECK
0;JMP

(LOAD_BASE_ADDR_1)
@SCREEN // A = SCREEN = 16834
D=A     // D => HOLDS THE BASE ADDRESS OF SCREEN MEMORY-MAP
@ADDR   // TEMPORARY VARIABLE => WILL BE USED AS POINTER
M=D     // RAM[ADDR] = 16384

@8192   // *** IT MIGHT BE OFF BY ONE ***
D=A     // LOAD #ROWS IN D
@COUNTER
M=D     // INITIALIZE COUNTER TO #ROWS

// ---------------------------------

(LOOP_WHITE)
@ADDR   // A = ADDR
A=M     // A = RAM[ADDR]
M=0     // SET PIXELS TO WHITE

@ADDR
M=M+1   // ADVANCE POINTER TO THE NEXT ROW

@COUNTER
MD=M-1   // DECREMENT COUNTER
@LOOP_WHITE
D;JGT    // IF IS GREATER THAN ZERO, REPEAT

// ---------------------------------

// CHECK IF ANY KEY IS PRESSED
(CHECK)
@KBD
D=M
@LOAD_BASE_ADDR_1
D;JEQ

// ---------------------------------

(LOAD_BASE_ADDR_2)
@SCREEN // A = SCREEN = 16834
D=A     // D => HOLDS THE BASE ADDRESS OF SCREEN MEMORY-MAP
@ADDR   // TEMPORARY VARIABLE => WILL BE USED AS POINTER
M=D     // RAM[ADDR] = 16384

@8192   // *** IT MIGHT BE OFF BY ONE ***
D=A     // LOAD #ROWS IN D
@COUNTER
M=D     // INITIALIZE COUNTER TO #ROWS

// ---------------------------------

// WRITE 1 (=> BLACK) TO EACH PIXEL
(LOOP_BLACK)
@ADDR   // A = ADDR
A=M     // A = RAM[ADDR]
M=-1

@ADDR
M=M+1   // ADVANCE POINTER TO THE NEXT ROW

@COUNTER
MD=M-1   // DECREMENT COUNTER
@LOOP_BLACK
D;JGT    // IF IS GREATER THAN ZERO, REPEAT

// ---------------------------------

// INFINITE LOOP
@CHECK
0;JMP