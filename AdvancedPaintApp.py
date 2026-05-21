from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()
root.title('Paint')

top_frame = Frame(root)
top_frame.pack(side=TOP, fill=X)

canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=True)

COLOUR = 'black'
SIZE = IntVar(value=10)

def open_colour_picker():
    '''Opens a color wheel for selection and updates COLOUR.'''
    global COLOUR
    color = askcolor()[1]  # Get hex color
    if color:
        COLOUR = color

def eyedropper(event):
    '''Gets color from the canvas at the clicked position.'''
    x, y = event.x, event.y
    color = canvas.winfo_rgb(canvas.itemcget(canvas.find_closest(x, y), 'fill'))
    if color:
        COLOUR = f'#{color[0]//256:02x}{color[1]//256:02x}{color[2]//256:02x}'

def draw_circle(event):
    '''Draws a circle where the user drags the mouse.'''
    x, y = event.x, event.y
    size = SIZE.get()
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=COLOUR, outline=COLOUR)

def clear_canvas():
    '''Clears all drawings from the canvas.'''
    canvas.delete('all')

# UI Elements
change_colour_button = Button(top_frame, text='Change Colour', command=open_colour_picker)
change_colour_button.grid(row=0, column=0)

clear_button = Button(top_frame, text='CLEAR', command=clear_canvas)
clear_button.grid(row=0, column=1)

scalebar = Scale(top_frame, from_=1, to=50, orient=HORIZONTAL, variable=SIZE)
scalebar.grid(row=0, column=2)

# Bindings
canvas.bind('<B1-Motion>', draw_circle)
canvas.bind('<Button-3>', eyedropper)  # Right-click to pick color
root.bind('q', lambda event: root.quit())

root.mainloop()
