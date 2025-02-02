import tkinter as tk

def on_button_click():
    user_input = entry.get()
    print("User input:", user_input)

# Create main window
root = tk.Tk()
root.title("Input Window")

# Create Entry widget for text input with width 100 and height 5 (5 lines)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create Button widget to trigger an action
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()



