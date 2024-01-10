import tkinter as tk

# Default color when the application starts
current_color = "#FF0000"

# Height of the color legend area at the top of the canvas
legend_height = 50

def on_canvas_click(event):
    """
    Handles left-click events on the canvas. This function is responsible for coloring the grid cells based on the currently selected color and updating the color lists accordingly.
    """
    global color_lists  # Access the global dictionary of color lists
    if event.y > legend_height:  # Ensures click is within the grid area
        # Calculate which column and row is clicked
        col_width = canvas.winfo_width() / 18
        row_height = (canvas.winfo_height() - legend_height) / 30  # Updated to 30 rows
        row_clicked = int((event.y - legend_height) // row_height)
        col_clicked = int(event.x // col_width)

        # Adjust column for zigzag numbering if row is even
        if row_clicked % 2 == 0:  # Adjusted condition to match even rows
            col_clicked = 17 - col_clicked

        cell_id = grid_cells[29 - row_clicked][col_clicked]  # Calculate cell id based on row and column clicked
        canvas.itemconfig(cell_id, fill=current_color)  # Change the cell color
        
        # Update the color list
        cell_number = (29 - row_clicked) * 18 + col_clicked  # Calculate linear cell number
        remove_number_from_color_lists(cell_number)
        color_lists[current_color].add(cell_number)

def on_legend_click(event):
    """
    Handles left-click events on the color legend area. This function updates the current color based on the user's selection from the color legend.
    """
    global current_color
    if event.y <= legend_height:  # Check if click is in the legend area
        selected_color = int(event.x // (canvas.winfo_width() / len(colors)))
        current_color = colors[selected_color]

def on_canvas_right_click(event):
    """
    Handles right-click events on the canvas. This function resets the color of a grid cell to black and updates the color lists accordingly.
    """
    if event.y > legend_height:  # Check if click is within the grid area
        # Calculate which column and row is clicked
        col_width = canvas.winfo_width() / 18
        row_height = (canvas.winfo_height() - legend_height) / 30  # Updated to 30 rows
        row_clicked = int((event.y - legend_height) // row_height)
        col_clicked = int(event.x // col_width)

        # Adjust column for zigzag numbering if row is even
        if row_clicked % 2 == 0:  # Adjusted condition to match even rows
            col_clicked = 17 - col_clicked

        cell_id = grid_cells[29 - row_clicked][col_clicked]  # Calculate cell id based on row and column clicked
        canvas.itemconfig(cell_id, fill="black")  # Reset the cell color to black

        # Update the color list
        cell_number = (29 - row_clicked) * 18 + col_clicked  # Calculate linear cell number
        remove_number_from_color_lists(cell_number)

def create_grid(canvas, rows, cols):
    """
    Creates a grid layout on the canvas. Each cell of the grid is initialized with a black background and a white text displaying the cell number. The numbering starts from the bottom left and follows a zigzag pattern upwards.
    """
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height() - legend_height
    row_height = canvas_height / rows
    col_width = canvas_width / cols

    number = 1  # Initialize cell numbering starting with 1
    for row_num in range(rows):
        row = []  # Initialize the list for the current row
        for col_num in range(cols):
            # Determine the position based on the zigzag pattern
            if row_num % 2 == 0:
                # Even rows go left to right
                col_index = col_num
            else:
                # Odd rows go right to left
                col_index = (cols - 1) - col_num

            # Calculate rectangle coordinates for cell
            x0 = col_index * col_width
            y0 = (rows - 1 - row_num) * row_height + legend_height
            x1 = x0 + col_width
            y1 = y0 + row_height
            # Draw the cell on the canvas
            rect = canvas.create_rectangle(x0, y0, x1, y1, fill="black", outline="black")
            # Place the cell number in the center
            canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(number), fill="white", font=("Arial", 10))
            number += 1  # Increment cell number
            row.append(rect)  # Add the cell to the current row
        grid_cells.append(row)  # Add the current row to the grid cells

def create_color_legend(canvas, colors):
    """
    Creates a color legend at the top of the canvas. This area allows users to select a color
    for coloring the grid cells.
    """
    color_width = canvas.winfo_width() / len(colors)
    for i, color in enumerate(colors):
        x0 = i * color_width
        x1 = x0 + color_width
        canvas.create_rectangle(x0, 0, x1, legend_height, fill=color, outline="black")

# List of colors used in the color legend
colors = [
    "#FF0000", "#FF7F00", "#FFFF00", "#7FFF00",
    "#00FF00", "#00FF7F", "#00FFFF", "#007FFF",
    "#0000FF", "#7F00FF", "#FF00FF", "#FF007F",
    "#FFFFFF"
]

# Mapping of color hex codes to their names
color_names = {
    "#FF0000": "Red", "#FF7F00": "Orange", "#FFFF00": "Yellow",
    "#7FFF00": "Chartreuse", "#00FF00": "Green", "#00FF7F": "Spring Green",
    "#00FFFF": "Cyan", "#007FFF": "Azure", "#0000FF": "Blue",
    "#7F00FF": "Violet", "#FF00FF": "Magenta", "#FF007F": "Rose",
    "#FFFFFF": "White"
}

# Dictionary to store the list of cells colored with each color
color_lists = {color: set() for color in colors}

def remove_number_from_color_lists(cell_number):
    """
    Removes a cell number from all color lists. This function is used to ensure that a cell
    number is only listed under its current color.
    """
    for color, number_set in color_lists.items():
        number_set.discard(cell_number)

def generate_color_lists():
    """
    Generates a string representation of the color lists. This string is used to update the
    text widget displaying the list of cells colored with each color.
    """
    lists_str = ""
    for color, grid_set in color_lists.items():
        color_name = color_names.get(color, "Unknown")
        sorted_numbers = sorted(grid_set)
        sorted_numbers = [i+1 for i in sorted_numbers]
        lists_str += f"{color_name} List: {', '.join(map(str, sorted_numbers))}\n"
    return lists_str[:-1]

def generate_pin_dict():
    pin_dict = {}
    for color, grid_set in color_lists.items():
        color_name = color_names.get(color, "Unknown")
        sorted_numbers = sorted(grid_set)
        sorted_numbers = [i+1 for i in sorted_numbers]
        pin_dict[color_name] = sorted_numbers
    
    return pin_dict
    
def display_color_lists():
    """
    Updates the text widget with the current color lists. This function is called when the
    'Generate Lists' button is pressed.
    """
    lists_str = generate_color_lists()
    pin_dict = generate_pin_dict()
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, lists_str)
    text_output.insert(tk.END, "\nDictionary: ")
    text_output.insert(tk.END, str(pin_dict))

def reset_grid():
    """
    Resets the grid to its default state. All cells are turned black, and the color lists are cleared.
    This function is called when the 'Reset Grid' button is pressed.
    """
    global color_lists
    for row in grid_cells:
        for cell in row:
            canvas.itemconfig(cell, fill="black")
    color_lists = {color: set() for color in colors}
    text_output.delete("1.0", tk.END)

# Initialize the main window
root = tk.Tk()
root.geometry("1200x1000")

# Create and pack the canvas into the window
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# Create and pack the text widget for displaying color lists
text_output = tk.Text(root, height=13, width=125)
text_output.pack(pady=10)

# Create a frame for buttons and pack it into the window
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)

# Create and pack buttons for generating lists and resetting the grid
generate_button = tk.Button(button_frame, text="Generate Lists", command=display_color_lists)
generate_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Reset Grid", command=reset_grid)
reset_button.pack(side=tk.LEFT, padx=5)

# Update the window to ensure all widgets are displayed correctly
root.update()

# Initialize the grid and color legend
grid_cells = []
create_grid(canvas, 30, 18)
create_color_legend(canvas, colors)

# Bind event handlers for mouse clicks on the canvas
canvas.bind("<Button-1>", on_canvas_click)
canvas.bind("<Button-1>", on_legend_click, add="+")
canvas.bind("<Button-2>", on_canvas_right_click)

# Start the application
root.mainloop()