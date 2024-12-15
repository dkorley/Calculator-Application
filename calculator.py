from customtkinter import *

# Set appearance and theme
set_appearance_mode("dark")  # Options: "light", "dark", "system"
set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class CalculatorApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("iPhone Calculator")
        self.geometry("350x500")
        self.resizable(False, False)

        # Display frame
        self.display_frame = CTkFrame(self, height=100, fg_color="black")
        self.display_frame.pack(fill=BOTH)

        # Display label
        self.display_text = CTkLabel(self.display_frame, text="0", font=("Helvetica", 40), anchor="e", fg_color="black", text_color="white")
        self.display_text.pack(fill=BOTH, padx=10, pady=10)

        # Button frame
        self.button_frame = CTkFrame(self, fg_color="gray20")
        self.button_frame.pack(fill=BOTH, expand=True)

        # Calculator state
        self.current_input = ""
        self.result = ""

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        # Button layout (row by row)
        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        # Colors for buttons
        operator_color = "#ff9500"
        number_color = "#333333"
        special_color = "#a5a5a5"

        # Create buttons dynamically
        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                if button_text in "C±%":
                    color = special_color
                elif button_text in "÷×−+=":
                    color = operator_color
                else:
                    color = number_color

                # Button configuration
                button = CTkButton(
                    self.button_frame,
                    text=button_text,
                    font=("Helvetica", 20),
                    fg_color=color,
                    hover_color="gray50",
                    text_color="white",
                    corner_radius=10,
                    command=lambda text=button_text: self.on_button_click(text)
                )

                # Layout configuration
                if button_text == "0":
                    button.grid(row=row_index, column=col_index, columnspan=2, sticky="nsew", padx=5, pady=5)
                else:
                    button.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5)

        # Configure row and column weights for responsiveness
        for i in range(5):
            self.button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.button_frame.columnconfigure(j, weight=1)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.current_input = ""
            self.result = ""
            self.update_display("0")
        elif button_text == "±":
            if self.current_input:
                if self.current_input.startswith("-"):
                    self.current_input = self.current_input[1:]
                else:
                    self.current_input = "-" + self.current_input
                self.update_display(self.current_input)
        elif button_text == "%":
            if self.current_input:
                self.current_input = str(float(self.current_input) / 100)
                self.update_display(self.current_input)
        elif button_text in "÷×−+":
            if self.current_input:
                self.result += self.current_input + button_text
                self.current_input = ""
        elif button_text == "=":
            if self.current_input:
                self.result += self.current_input
                try:
                    self.current_input = str(eval(self.result.replace("÷", "/").replace("×", "*").replace("−", "-")))
                    self.result = ""
                    self.update_display(self.current_input)
                except Exception:
                    self.update_display("Error")
                    self.current_input = ""
                    self.result = ""
        elif button_text == ".":
            if "." not in self.current_input:
                self.current_input += button_text
                self.update_display(self.current_input)
        else:  # Numbers
            self.current_input += button_text
            self.update_display(self.current_input)

    def update_display(self, text):
        self.display_text.configure(text=text[:10])  # Limit display length to 10 characters

# Create and run the calculator app
app = CalculatorApp()
app.mainloop()
