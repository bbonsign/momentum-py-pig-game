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

## Dice
### Responisbilities
  * Stores the values (1-6)
  * Can "role" itself

### Collaborators
  * Players can roll dice to update their own score

________

## Player
### Responisbilities
  * Keep track of their own score.
  * Roll a dice object

### Collaborators
  * Instantiated in a game object
  * Roll a dice object