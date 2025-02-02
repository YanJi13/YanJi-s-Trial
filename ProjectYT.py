import turtle
import time
import tkinter as tk

startTime = None

def dragging(x, y):             # Function that handles the player movement
    trPlayer.ondrag(None)           
    trPlayer.setheading(trPlayer.towards(x, y))
    trPlayer.goto(x, y)

    winConTrue()
    
    trPlayer.ondrag(dragging)

def winConTrue():
    if trPlayer.distance(trGoal) < 50: # Function that checks if player has reached the goal
        screen.bgcolor('lightgreen')
        stopTimer()

def reset():                    # Function that resets the game
    trPlayer.setheading(180)
    trPlayer.goto(350, 350)
    trPlayer.clear()
    trPlayer.ondrag(dragging)
    screen.bgcolor('white')
    print("Game Reset")

def startTimer(x, y):           # Function that starts the timer on click
    global startTime
    startTime = time.time()
    print("Timer started.")

def stopTimer():                # Function that stops the timer, and records the elapsed time and player name to a file
    global startTime
    elapsed_time = time.time() - startTime
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, remainder = divmod(remainder, 60)
    seconds, milliseconds = divmod(remainder, 1)
    milliseconds = int(milliseconds * 1000)
    print(f"Timer stopped. Elapsed time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds, {int(milliseconds)} ms.")
    
    tkWindow = tk.Tk()
    tkWindow.title("What is your name?")
    tkWindow.geometry("300x100")
    tkWindow.configure(bg = 'lightgreen')

    label = tk.Label(tkWindow, text = "Enter your name:", font = ('Courier'))
    label.configure(bg = 'lightgreen')
    label.pack()

    entry = tk.Entry(tkWindow)
    entry.pack()

    def savePlayerName():       # Nested function that saves player name and their time based on the previous given inputs
        playerName = entry.get()
        with open('Trial Times.txt', 'a') as file:
            file.write(f"Player Name: {playerName} - ")
            file.write(f"Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds, {int(milliseconds)} ms.\n")
        tkWindow.destroy()

    button = tk.Button(tkWindow, text="Save", command = savePlayerName)
    button.pack(pady = 10)

    startTime = None

def instructions():                                             # Function that shows the instructions for the game and additional information
    instructionsWindow = tk.Tk()                                # This function also makes it easier for laptop users to use the program 
    instructionsWindow.title("Instructions and Information")   # as it separates the parts to accomodate their small screens
    instructionsWindow.geometry("900x100")

    instructionsCanvas = turtle.Canvas(instructionsWindow, width = 900, height = 100, bg = 'lightgreen')
    instructionsCanvas.create_text(400, 50, text = "Click and drag the turtle to the finish area.\nThe timer will start at the first click and stop when reaching the finish.\n\
Author Record: 9 secs 850 ms (without the lines touching the wall)", fill = 'black', font = ('Courier', 12, 'bold'))
    instructionsCanvas.pack() 

def makeLevel(): # Creates the level
    trLevel.speed(8) # Phase 1 speed
    trLevel.up()
    trLevel.goto(400, 0)
    trLevel.down()
    trLevel.goto(400, 400)
    trLevel.goto(-400, 400)
    trLevel.goto(-400, -400)
    trLevel.down()
    trLevel.goto(400, -400)
    trLevel.goto(400, 300)
    trLevel.goto(-300, 300)
    trLevel.up()
    trLevel.goto(-400, 200)
    trLevel.down()
    trLevel.goto(300, 200)
    trLevel.goto(300, 100)
    trLevel.up()
    trLevel.goto(400, 0)
    trLevel.down()
    trLevel.goto(200, 0)
    trLevel.goto(200, 100)
    trLevel.goto(-300, 100)
    trLevel.up()
    trLevel.goto(-400, -100)
    trLevel.down()
    trLevel.goto(300, -100)
    trLevel.up()
    trLevel.goto(400, -200)
    trLevel.down()
    trLevel.goto(-300, -200)
    trLevel.up()
    trLevel.goto(-400, -300)
    trLevel.down()
    trLevel.goto(300, -300)
    trLevel.up()
    trLevel.speed('fastest') # Phase 2 speed
    trLevel.goto(300, 300)
    trLevel.down()
    trLevel.setheading(90), trLevel.forward(60) # Upward
    trLevel.up()
    trLevel.goto(200, 400)
    trLevel.down()
    trLevel.setheading(270), trLevel.forward(60) # Downward
    trLevel.up()
    trLevel.goto(100, 300)
    trLevel.down()
    trLevel.setheading(90), trLevel.forward(60)
    trLevel.up()
    trLevel.goto(0, 400)
    trLevel.down()
    trLevel.setheading(270), trLevel.forward(60)
    trLevel.up()
    trLevel.goto(-100, 300)
    trLevel.down()
    trLevel.setheading(90), trLevel.forward(60)
    trLevel.up()
    trLevel.goto(-200, 400)
    trLevel.down()
    trLevel.setheading(270), trLevel.forward(60)
    trLevel.up()
    trLevel.speed(5) # Phase 2.1 speed
    trLevel.goto(-300, 260)
    trLevel.down()
    trLevel.goto(360, 260)
    trLevel.goto(360, 40)
    trLevel.goto(240, 40)
    trLevel.goto(240, 140)
    trLevel.goto(-340, 140)
    trLevel.goto(-340, 0)
    trLevel.goto(0, -85)
    trLevel.goto(100, -85)
    trLevel.up()
    trLevel.speed('fastest') # Phase 2.2 speed
    trLevel.goto(300, -100)
    trLevel.down()
    trLevel.goto(300, -140)
    trLevel.up()
    trLevel.goto(300, -200)
    trLevel.down()
    trLevel.goto(300, -160)
    trLevel.up()
    trLevel.goto(0, -200)
    trLevel.down()
    trLevel.goto(0, -140)
    trLevel.up()
    trLevel.goto(0, -100)
    trLevel.down()
    trLevel.goto(0, -120)
    trLevel.up()
    trLevel.goto(-300, -200)
    trLevel.down()
    trLevel.goto(-300, -190)
    trLevel.up()
    trLevel.goto(-300, -100)
    trLevel.down()
    trLevel.goto(-300, -170)
    trLevel.up()
    trLevel.goto(-300, -200)
    trLevel.down()
    trLevel.speed(5) # Phase 2.3 speed
    trLevel.goto(-300, -270)
    trLevel.goto(300, -200)
    trLevel.up()
    trLevel.goto(300, -300)
    trLevel.down()
    trLevel.goto(300, -230)
    trLevel.goto(-300, -300)
    trLevel.goto(-300, -335)
    trLevel.goto(300, -335)
    trLevel.up()
    trLevel.goto(300, -365)
    trLevel.down()
    trLevel.goto(-300, -365)
    trLevel.goto(-300, -400)

turtle.title("YanJi's Trial: A Mouse Training Program for Beginners") # Screen set up
screen = turtle.Screen()
screen.setup(850, 850)

trGoal = turtle.Turtle('square')   # Finish postion turtle
trGoal.color('lightgreen')
trGoal.shapesize(4)
trGoal.speed(7)

trLevel = turtle.Turtle()   # Turtle that handles the making of the level
trLevel.hideturtle()
trLevel.pensize(2)

trPlayer = turtle.Turtle('turtle') # Turtle which the player controls by dragging
trPlayer.setheading(180)
trPlayer.speed(7)

trPlayer.up()               # Sets up the starting position of the player turtle
trPlayer.goto(350, 350)
trPlayer.down()
trPlayer.speed('fastest')

trGoal.up()                 # Sets up the position of the finish position turtle
trGoal.goto(-350, -350)

makeLevel()
instructions()
trPlayer.ondrag(dragging) # Movement for the player turtle
    
turtle.listen()
screen.onscreenclick(startTimer) # Stars the timer on the first click
turtle.onkey(reset, 'r') # Reset the game

tk.mainloop()
screen.mainloop()