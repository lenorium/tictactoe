# tictactoe
hyperskill project

### Description
In this project, you'll write a game called Tic-Tac-Toe that you can play against your computer. The computer will have three levels of difficulty — easy, medium, and hard.

To begin with, let's write a program that knows how to work with coordinates and determine the state of the game.

The top-left cell will have the coordinates (1, 1) and the bottom-right cell will have the coordinates (3, 3), as shown in this table:

```
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
```

The program should ask the user to enter the coordinates of the cell where they want to make a move.

Keep in mind that the first coordinate goes from left to right, and the second coordinate goes from top to bottom. Also, notice that coordinates start with 1 and can be 1, 2, or 3.

But what if the user attempts to enter invalid coordinates? This could happen if they try to enter letters or symbols instead of numbers, or the coordinates of an already occupied cell. Your program needs to prevent these things from happening by checking the user's input and catching possible exceptions.

### Objectives
The program should work in the following way:

1. Ask the user to provide the initial state of the 3x3 table with the first input line. This must include nine symbols that can be X, O or _ (the latter represents an empty cell).
2. Output the specified 3x3 table before the user makes a move.
3. Request that the user enters the coordinates of the move they wish to make.
4. The user then inputs two numbers representing the cell in which they wish to place their X or O. The game always starts with X, so the user's move should be made with this symbol if there are an equal number of X's and O's in the table. If the table contains an extra X, the move should be made with O.
5. Analyze the user input and show messages in the following situations:
    - ```This cell is occupied! Choose another one!``` — if the cell is not empty;
    - ```You should enter numbers!``` — if the user tries to enter letters or symbols instead of numbers;
    - ```Coordinates should be from 1 to 3!``` — if the user attempts to enter coordinates outside of the table's range.
6. Display the table again with the user's most recent move included.
7. Output the state of the game.

The possible states are:

  - ```Game not finished``` — when no side has three in a row, but the table still has empty cells;
  - ```Draw``` — when no side has three in a row, and the table is complete;
  - ```X wins``` — when there are three X's in a row;
  - ```O wins``` — when there are three O's in a row.

If the user provides invalid coordinates, the program should repeat the request until numbers that represent an empty cell on the table are supplied. You should ensure that the program only outputs the table twice — before the move and after the user makes a legal move.
