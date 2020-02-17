# Roguelike

## Story

"La Speluna", a company from San Escobar contacted Codecool and asked about creating a roguelike game for them. They didn't tell us much about their needs, only a few details about the game's framework. They are big fans of old-fashioned RPG games when graphics didn't matter that much, but the most important things were gameplay and a story.

The game should be about a creature (human? alien? bear? ant?) who is travelling through a dangerous and wild world (planet? table?). In the beginning, the creature is weak and fragile, but through the game he (she? it? apache helicopter?) will be levelling up, getting tougher, collecting powerful items and finally be able to defeat an ultimate boss! Of course, the way to the ultimate boss isn't a bed of roses, there will be a lot of obstacles (rivers? lavas? mountains?) and many dangerous enemies (use your imagination!).

In this project your job is to implement a
[Roguelike](https://en.wikipedia.org/wiki/Roguelike) game.

## What are you going to learn?

You will learn and practice how to do the following things in Python:
 - variables,
 - functions,
 - loops and conditionals,
 - nested lists,
 - dictionaries,
 - print formatting,
 - handling user input,
 - error handling,
 - clean code.

## Tasks

0. Warm up - prepare a proof-of-concept of your game by implementing:
 - `create_board` function from `engine` module, which creates a rectangular game board with `#` as borders,
 - `put_player_on_board` function from `engine` module, which puts a player icon on board on given coordinates,
 - `display_board` function from `ui` module, which prints complete game board on the screen,
 - player movement - by presing WASD keys. 

1. Use this template for planning and project management: [Burndown chart for Rogulike project](https://docs.google.com/spreadsheets/d/10aKB7z7BrmpwgjYtEsT3BwVBQysnWWlu0Ehy2OO9w-Y/edit?usp=sharing)

1. Implement at least **three different levels/areas**. Each of them should have an unique "feel" - different color and objects, different enemies, etc.

2. A player should be able to collect various items during their journey. Each item should be described by at least two characteristics - name and type (weapon, armour, food, etc.)

3. A player should be able to display detailed information about their inventory - list of collected items.

4. A player should be able to display detailed information about their character - name, statistics, number of killed enemies, etc.

5. At the end of the game player would like to meet THE BOSS (use ASCII art, at least 5x5 characters, different colors). To defeat boss you have to play hot-cold game.

6. Prepare a story:

    * an introduction screen,
    * a character creation screen,
    * a win/lose screen,

7. Create a hall of fame screen (highscores) - name, max level, time spent, monsters killed etc.

8. Create an about screen (info about authors!) and how-to-play screen (how to move, attack, drink potions etc.) 


## General requirements

 - Try to use feature branches.
 - Variable names in the program are meaningful nouns and not abbreviated.
 - Function names in the program are meaningful verbs and not abbreviated.
 - There are no unnecessary (dead) code or comments in the program.
 - There are no duplicating code parts or code parts doing the same thing differently in the program.
 - There are no functions that doing more than one thing in the program.