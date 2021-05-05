# Othello game with Min-Max algorithm

## Table of contents

- [Problem description](#problem-description)
- [Solution description](#solution-description)
- [Heuristic functions](#heuristic-functions)
- [Results](#results)
- [Conclution](#conclution)

## Problem description

The problem to resolve consists of programming the game named "Othello" and the "Min-Max (with depth)" algorithm.

The objective of programing these programs is to create a AI which plays Othello against another player. Both players playing the game must have the option to be a user or to be the AI programmed with the "Min-Max" algorithm.
 
After Othello is working correctly and the AI working correctly and is able to play Othello as a player, we have to do the following experiments and modifications:
-  Add the "Prunning" functionality to the Min-Max algorithm.
-  Calculate the average time the AI takes to make its move.
-  Make sure the AI is making a move in less than 15 seconds.
-  Get the total number of expanded states by the AI.

That is basicly the description of the problem and objectives.

The specific requirements are the following:

- The program reports the computer(AI) response time after each turn.
- The program reports the average response time of the computer at the end of the game.
- The program reports the number of black and white tiles that exist on the board at the end of the game, determining a winner.
- The program has an initial menu where you can choose to be black or white.
- The program shows the current state of the board after each turn.
- MinMaxWithDepthest algorithm has been successfully implemented.
- The α β prunning algorithm is properly integrated into the MinMaxWithDepth algorithm as seen in classes.
- Othello is working correctly and accordingly to the official game rules.

## Solution description





## Heuristic functions

We defined a variety of heuristic functions to be used in our Min-Max algorithm for the "Eval()" function.

The heuristic functions we defined are :

### Dummy heuristic

This dummy heristic consists of making a move which flanks more enemy tokens.

For Example:

If we reach a "Cut off" state and we have a move #1 which flanks 2 enemy tokens and a move #2 whic flanks 4 enemy tokens, the next move will be the move #2 because it has a bigger number of flanks done.

### Strategy heuristic

x

## Results

### Average decition making time from the AI

The average time the AI takes to make a move is:  ...


## Conclution

We have observed that...
