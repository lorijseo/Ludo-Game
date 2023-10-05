# LUDO
A 2-4 player board game using decision-making algorithm to automate a gameplay using OOP.
A decision-making algorithm was implemented for a player to choose a certain token to move based on the predetermined dice roll. 
This is a simplified version of the original [Ludo game](https://en.wikipedia.org/wiki/Ludo) 

## What to Expect:
Users will decide the number of players from 2-4. Once decided, the program will autoplay the game utilizing decision-making algorithm with a randomly generated dice(1d6).

* Here is an example if the user decided to have 2 players
* You will notice there is a pattern of 3 lines repeating:
  1. Round # represent each player rolling once
  2. The current position of all the tokens. The first two elements represent PLAYER A's tokens. The next two represents PLAYER B's tokens.
  3. References the PLAYER by their letter (A,B,C,D) and the dice they rolled (1d6)
     
![image](https://github.com/lorijseo/Ludo-Game/blob/master/ludo.gif/2-player-intro.JPG?raw=true)


* Here is an example if the user decides to have 4 players

![image](https://github.com/lorijseo/Ludo-Game/blob/master/ludo.gif/4-players.gif?raw=true)


## Game Rules:
Each player has 2 tokens and takes a turn rolling the dice. On a turn, a player can move a token that is on the board clockwise the number of steps indicated by the die. The winner is determined by the first player whose 2 tokens land on the finishing square.
There are five locations a player’s token must navigate through: their **home yard**, their **ready to go** position, the **general board**, their **home squares**, and the **finishing square**. 

All players begin with two tokens in their respective “home  yard”. A player must roll a 6 to move a token out of the “home yard” to “ready to go” position. A player’s token must go through the “general board” with 50 squares until they reach their “home squares”. Once a token enters the player’s “home squares”, the token can only reach the “finishing square” on an exact roll. If the roll number is larger than the steps needed to get to the “finishing square”, the token will bounce back the remaining number of steps.

![Ludo_board](https://user-images.githubusercontent.com/99004250/191935384-8ce54b8a-32f3-46f0-8fad-9536ad83d293.png)

**Additional playing rules:**

**1)** When a token finishes one move, if it lands on a space occupied by an opponent's (other player’s) token, the opponent token will be returned to its home yard. 


![image](https://github.com/lorijseo/Ludo-Game/blob/master/ludo.gif/token-kick.JPG?raw=true)

* PLAYER C was on position 53. They rolled a 3, so their new updated position would be 56. However, PLAYER D is on position 56, kicking both of PLAYER C's token back to HOME


**2)** If the player’s two tokens land on the same space on the board, the player will stack the two tokens and move them as one piece until they reach the finishing square. When stacked pieces are sent back to their home yard by an opponent landing on them, they are no longer stacked. Note that if two tokens are both at the “ready to go” position, they are not stacked.


## Decision-Making Algorithm
A **decision-making** algorithm was implemented for a player to choose a certain token to move.  If the player has two tokens on the board that can be moved, then player will use the following priority rules to decide which token to move:

![image](https://github.com/lorijseo/Ludo-Game/blob/master/ludo.gif/roll-6.JPG?raw=true)

* Once a player rolls a 6, the algorithm will place a token from HOME to READY position
  

**1)** If the die roll is 6, try to let the token that still in the home yard get out of the home yard (if both tokens are in the home yard, choose the first one ‘p’)

**2)** If one token is already in the home square and the step number is exactly what is needed to reach the end square, let that token move and finish

**3)** If one token can move and kick out an opponent token, then move that token

**4)** Move the token that is further away from the finishing square

## How do I know who won?
![image](https://github.com/lorijseo/Ludo-Game/blob/master/ludo.gif/win.JPG?raw=true)

* Once both tokens from a player reaches the "finishing square" represented by "E", they win and the game immediately terminates.


