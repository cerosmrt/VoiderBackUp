from tkinter import Tk, Canvas, Entry, font

def adjust_width(event):
    # Adjust the width of the Entry widget to match the length of its content
    # Add a small offset to the width to make the Entry widget slightly wider
    entry.config(width=len(entry.get()) + 1)

root = Tk()

# Set window title (optional)
root.title("My Tkinter Interface")

# Make the window always fullscreen
root.attributes("-fullscreen", True)

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Subtract margin for aesthetics
thickness = 10

# Create a canvas widget with no border
canvas = Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)  # Fill and expand canvas

# Calculate circle center coordinates
center_x = screen_width // 2
center_y = screen_height // 2

# Create the white circle outline (using create_oval for compatibility)
# We adjust the starting and ending coordinates to create a circle
# Reduce the radius to make the circle further from the edges
radius = min(screen_width, screen_height) // 2 - thickness - 25  # Subtract an additional 50 pixels
canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="white", width=thickness)

# Create an invisible Entry widget in the middle of the screen
entry_font = font.Font(family="Consolas" ,size=11)
entry = Entry(root, borderwidth=0, highlightthickness=0, bg="black", fg="white", justify="center", font=entry_font)
entry.place(x=center_x, y=center_y, anchor="center")

# Bind the adjust_width function to the <Key> event
entry.bind("<Key>", adjust_width)

canvas.configure(bg="black")

root.mainloop()