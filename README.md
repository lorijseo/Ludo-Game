#LUDO

##Description:

This is a simplified version of the original Ludo game where 2 - 4 players can play. Each player has 2 tokens and takes a turn rolling the dice. On a turn, a player can move a token that is on the board clockwise the number of steps indicated by the die. The winner is determined by the first player whose 2 tokens land on the finishing square.

##Game Rules:

There are five locations a player’s token must navigate through: their **home yard**, their **ready to go** position, the **general board**, their **home squares**, and the **finishing square**. 

All players begin with two tokens in their respective “home  yard”. A player must roll a 6 to move a token out of the “home yard” to “ready to go” position. A player’s token must go through the “general board” with 50 squares until they reach their “home squares”. Once a token enters the player’s “home squares”, the token can only reach the “finishing square” on an exact roll. If the roll number is larger than the steps needed to get to the “finishing square”, the token will bounce back the remaining number of steps.


**Additional playing rules:**

**1)** When a token finishes one move, if it lands on a space occupied by an opponent's (other player’s) token, the opponent token will be returned to its home yard. 

**2)** If the player’s two tokens land on the same space on the board, the player will stack the two tokens and move them as one piece until they reach the finishing square. When stacked pieces are sent back to their home yard by an opponent landing on them, they are no longer stacked. Note that if two tokens are both at the “ready to go” position, they are not stacked.


##Decision-making Algorithm
A **decision-making** algorithm was implemented for a player to choose a certain token to move.  If the player has two tokens on the board that can be moved, then player will use the following priority rules to decide which token to move:

**1)** If the die roll is 6, try to let the token that still in the home yard get out of the home yard (if both tokens are in the home yard, choose the first one ‘p’)
**2)** If one token is already in the home square and the step number is exactly what is needed to reach the end square, let that token move and finish
**3)** If one token can move and kick out an opponent token, then move that token
**4)** Move the token that is further away from the finishing square



Here is an example:

```
players = ['A', 'B']
turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
game = LudoGame()
current_tokens_space = game.play_game(players, turns)
player_A = game.get_player_by_position('A')
print(player_A.get_completed())
print(player_A.get_token_p_step_count())
print(current_tokens_space)
player_B = game.get_player_by_position('B')
print(player_B.get_space_name(55))

And the output will be:
False
28
[‘28’, ‘28’, ‘21’, ‘H’]
B5

```


