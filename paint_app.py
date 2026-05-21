'''
Paint App Project
Author: Armin Dhadli
Date: August 12 2024

[Project Description]

This project is a simple paint application. You can draw on the canvas by dragging your mouse, and you can change the colour and size of your brush using the buttons and slider at the top. You can also clear the canvas with the CLEAR button.

'''

from tkinter import *

root = Tk()
root.title('Paint')

top_frame = Frame(root)
top_frame.pack(side=TOP, fill=X)

canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=True)
'''
This project will use some global variables.
COLOUR represents the current colour being used, and
SIZE is the current size of the paintbrush.
'''
COLOUR = 'black'
SIZE = 10

class ColourButton():
     '''
     A ColourButton is the class for the buttons at the
     top of the screen that change the brush colour.
     '''
     def __init__(self, parent, colour):
          '''
          This is the function called when creating a ColourButton.
          TODO:
          - fill in the line indicated below.
          '''
          self.colour = colour
          self.Button = Button(parent, bg=colour, width=5, command=self.update)

     
     def update(self):
          '''
          This is the method that is the command for a ColourButton.

          When a ColourButton is pressed, it must ONLY change the global COLOUR
          variable to be this ColourButton's colour attribute/
          TODO:
          - fill in this function. It should be 2 lines.
          '''
          global COLOUR
          COLOUR = self.colour
     
def draw_circle(event):
    '''
    This function is called whenever the user is dragging their mouse on the
    canvas. Use the canvas method 'createoval' to draw a circle there.
    Remember to refer to your global variables to draw the correct circle.
    TODO:
    - finish this function (should be 1-2 lines)
    '''
    x, y = event.x, event.y
    size = SIZE.get()  # Get the integer value of SIZE
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=COLOUR, outline=COLOUR)

def clear_canvas():
    '''
    This function is called whent the user presses the CLEAR button.
    It must clear all drawings from the canvas.
    TODO:
    - finish this function (1 line)
    '''
    canvas.delete('all')

#################### MAIN CODE #########################

'''
Here we first are making the ColourButtons. We will do this in a quick
and expandable way using a list. Add all the colours you want buttons for
to the list 'colours'.
The for loop will create the ColourButton objects.
TODO:
- add at least 4 more colours to the colours list
'''

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white']
for i in range(len(colours)):
    x = ColourButton(top_frame, colours[i])
    x.Button.grid(row=0, column=i)

'''
Next create the CLEAR button and the width slider.

TODO:
- complete the code fragments below
'''
clear_button = Button(top_frame, text='CLEAR', command=clear_canvas)
clear_button.grid(row = 0, column = i + 1)

SIZE = IntVar() # We are using the global variable as the int var so it is always updated
scalebar = Scale(top_frame, from_=1, to=50, orient=HORIZONTAL, variable=SIZE)
scalebar.grid(row = 0, column = i + 2)

'''
TODO:
- bind the event of mouse button held down while moving ON THE CANVAS to the draw_circle function
- bind the letter q to quitting the program
- mainloop!
'''
canvas.bind('<B1-Motion>', draw_circle)
root.bind('q', lambda event: root.quit())
root.mainloop()