# Classes

## Game
### Responisbilities
  * Starting play, updating, and ending the game (inlcuding asking to start a new game)
  * Initializing Players and Dice
  * Keeping track of turns and scores

### Collaborators
  * Players: Game can get scores to compare
  * Dice: game instantiates dice objects

_________

## Die
### Responisbilities
  * Stores the values (1-6)
  * Can "role" itself

### Collaborators
  * Players can roll dice to update their own score

________

## Player
### Responisbilities
  * Knows their current hold amount, which is reset to 0 if they roll a pig
  * Keep track of their own score.
  * Roll a die, which will update their hold amount
  * Has a name to distinguish between human and bot
  * Has a turn method that asks for input to roll or hold

### Collaborators
  * Instantiated in a game object
  * Roll a die object

________

## Robot and Bot
### Responisbilities
  * Inheret from player.
  * Different behaviors (risk-levels), identified in their name, including one with random thresholds for holding.

### Collaborators
  * Chosen by human player when a game starts