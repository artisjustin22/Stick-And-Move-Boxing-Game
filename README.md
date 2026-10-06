# 🥊 Stick and Move

Stick and Move is a text-based boxing adventure game built in Python. The player explores different locations, trains their boxer, collects equipment, improves fighter stats, and prepares for a championship fight against Drago.

This project was originally designed as a college Python project and later rebuilt and expanded to improve the gameplay, structure, and overall user experience.

## 🎮 Game Features

- Navigate between multiple locations using directional commands
- Train your boxer to improve fighter stats
- Collect boxing equipment and training items
- View current stats and inventory
- Repeat training and recovery activities
- Meet minimum requirements to unlock the Championship Arena
- Fight Drago using multiple attacks
- Earn the Championship Belt
- Win, lose, or replay the game

## 🥊 Fighter Stats

The player develops four main attributes:

- Health
- Power
- Skill
- Endurance

Training locations and equipment affect these stats differently throughout the game.

## 🏆 Championship Requirements

Before entering the Championship Arena, the player must have at least:

- 120 Health
- 50 Power
- 50 Skill
- 30 Endurance

Once qualified, the player can enter the arena and fight Drago for the Championship Belt.

## 💻 Python Concepts Used

- Variables
- Lists
- Dictionaries
- Nested dictionaries
- `if`, `elif`, and `else` statements
- `while` loops
- Functions
- User input
- Boolean conditions
- Inventory management
- Basic game-state management
- Integer arithmetic

## 🗺️ Game Design

Before coding the game, I created a visual map outlining the rooms, navigation paths, training locations, items, stat bonuses, and final Championship Arena.

The map helped translate the original game concept into Python using a nested dictionary to control player movement.
### Original Game Map

![Stick and Move Game Map](stick-and-move-game-map.png)

## 📸 Gameplay

### Training & Fighter Stats

Track Health, Power, Skill, Endurance, and collected equipment while preparing for the championship.

![Fighter Stats](stick-and-move-screen1.png)

### Championship Fight

After meeting the minimum requirements, the player can enter the Championship Arena and face Drago.

![Drago Fight](stick-and-move-screen2.png)

### Becoming Champion

Defeat Drago to win the fight and add the Championship Belt to your inventory.


## 🚀 What I Improved

When rebuilding the original project, I expanded the game by:

- Improving room navigation
- Adding a fighter stats command
- Preventing one-time items from being collected repeatedly
- Adding repeatable training and recovery mechanics
- Creating minimum stat requirements for the championship
- Making fighter stats influence combat damage
- Adding win and loss conditions
- Adding a replay system

## ▶️ Running the Game

Make sure Python 3 is installed.

Run:

```bash
python stick_and_move.py

Follow the prompts in the terminal to navigate, train, check your stats, and fight for the championship.

📚 Project Background
Stick and Move began as a Python project while I was studying Information Technology. I later revisited the concept and rebuilt it as a portfolio project after completing my degree.
Rebuilding the game gave me an opportunity to revisit Python fundamentals while improving the original design and adding features beyond the initial version.

