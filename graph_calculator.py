import tkinter as tk

class GraphicalCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the input field
        self.input_field = tk.Entry(self, width=30)
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create the buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.handle_button_click(x)
            tk.Button(self, text=button, width=5, command=command).grid(row=row, column=col)
            col += 1
            if col > 3:
                row += 1
                col = 0

        # Set the window title and size
        self.title("Graphical Calculator")
        self.geometry("200x200")

    def handle_button_click(self, key):
        if key == '=':
            # Evaluate the expression and display the result
            result = eval(self.input_field.get())
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, str(result))
        elif key == 'C':
            # Clear the input field
            self.input_field.delete(0, tk.END)
        else:
            # Add the key to the input field
            self.input_field.insert(tk.END, key)

if __name__ == '__main__':
    calculator = GraphicalCalculator()
    calculator.mainloop()
