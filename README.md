# CS32 Final Project
## Final Project Goal: Hangman Game Using Wikipedia Articles

OLD: For our final project, we would like to create a computer vs. player game of Hangman. We will be using server and client logic, where the client is always responsible for making guesses. This is a computational subtask for creating our own original game, learning by making a game that already exists.

OLD: For our final project, we are creating a Hangman game that uses random articles titles from Wikipedia as the secret word.

UPDATE: For our final project, we have created a Hangman game with three modes(wiki, tv, song), that uses three API's to to grab words/phrases as the secret word.

##  Breaking it Down - Final
1. Run using: python3 prototype_2.py
2. Choose a game mode (wiki, tv, song)
3. 'Scrape' one of the three websites depending on mode, pick a random title for game
4. Extract and clean up the title by removing punctuation
5. Display the Title including punctuation but only require guesses for letters
6. Take a player's guess for each letter in the word, one at a time
7. Update the 'man' based on whether the guess is correct or incorrect,
8. Loop the game until the player either wins or loses

### External Contributions
- 
- (Chatgpt)

## Breaking it Down - Status(old)
1. Run using: python3 prototype_2.py
2. 'Scrape' a random wikipedia article, using wikipedia's built-in random URL
3. Extract and clean up the title by removing punctuation
5. Display the Title including punctuation but only require guesses for letters
4. Take a player's guess for each letter in the word, one at a time
5. Update the 'man' based on whether the guess is correct or incorrect,
6. Loop the game until the player either wins or loses


## Breaking it Down(old)

1. Have the server pick a random word
2. Take a player's guess for each letter in the word, one at a time
3. Update the visual display based on whether the guess is correct or incorrect
4. Loop the game until the player either wins or loses
