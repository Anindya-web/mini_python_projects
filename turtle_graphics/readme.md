# Turtle Square Drawer

## Overview
This project is a simple Python script that uses the built-in `turtle` module to draw a square. 
It allows users to customize the drawing by entering their desired background color, pen color, and pen size through the console.

## Features
- **User Input:** Customize the background color, pen color, and pen size.
- **Turtle Graphics:** Draws a square based on user preferences.
- **Interactive Exit:** The turtle graphics window waits for a mouse click before closing.

___________________________________________________________________________

# Drawing a T with Turtle

This project uses Python's `turtle` module to draw a simple letter "T" on the screen.

## Features
- Demonstrates basic turtle graphics.
- Uses two turtles with different colors to create a simple design.
- Illustrates basic turtle movements and drawing commands.

## Code Overview

- **Turtle 1 (Blue):**  
  Draws the vertical line of the "T".

- **Turtle 2 (Orange):**  
  Draws the horizontal line of the "T".


______________________________________________________________________________

# Simple Turtle L-Shape

This project demonstrates a basic example of Python's `turtle` module by drawing an L-shaped design with two turtles in different colors.

## Features

- **Blue Turtle:** Draws a vertical line.
- **Orange Turtle:** Draws a horizontal line.
- Simple and fun introduction to turtle graphics.

_____________________________________________________________________________
# spiral_turtle.py 

This project uses Python's `turtle` module to create a dynamic spiral pattern. With each iteration, the turtle moves forward a little further and turns by a slightly smaller angle, producing an intriguing design.

## How It Works

- **Starting Values:**  
  The turtle begins with an initial forward distance of 50 units and an initial turning angle of 90 degrees.
  
- **Dynamic Changes:**  
  In each of the 15 iterations:
  - The turtle moves forward by the current distance.
  - It then turns right by the current angle.
  - The forward distance is increased by 4 units.
  - The turning angle is decreased by 4 degrees.


## How to Run

1. **Save the Code:**  
   Save the following code in a file named `spiral_turlte.py`:

2. **Execute the Script:**  
   Open your terminal or command prompt, navigate to the directory where `dynamic_turtle_spiral.py` is located, and run:
   ```
   python dynamic_turtle_spiral.py
   ```

3. **Enjoy the Pattern:**  
   A window will open showing the dynamic spiral pattern drawn by the turtle.

_________________________________________________________

# Stamp Spiral

This program uses Python's turtle graphics to create a spiral pattern by stamping a turtle shape repeatedly as it moves.

## How It Works

- **Window Setup:**  
  A window with a light green background is created.
  
- **Turtle Creation:**  
  A blue turtle (named `u1`) with a turtle shape is created.

- **Drawing Process:**  
  The turtle's pen is lifted so that no lines are drawn. In a loop:
  - The turtle stamps its current position.
  - It moves forward by an increasing distance.
  - It turns right slightly (2 degrees) before the next stamp.
  
- **Exit Condition:**  
  The window remains open until you click on it.

