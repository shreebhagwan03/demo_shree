import tkinter as tk
import math


class SmartCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Calculator")
        self.geometry("400x600")
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to show calculations and results
        self.result_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge", justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', '^', 'sin', 'cos',
            'tan', 'log', 'exp', 'ln',
            'C', '(', ')', 'pi'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.button_click(x)
            tk.Button(self, text=button, command=action, font=("Arial", 18), width=5, height=2).grid(row=row_val,
                                                                                                     column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == 'C':
            self.result_var.set('')
        elif button_text == '=':
            try:
                expression = self.result_var.get()
                # Replace '^' with '**' for exponentiation
                expression = expression.replace('^', '**')
                # Evaluate the expression
                result = eval(expression,
                              {'sqrt': math.sqrt, 'log': math.log10, 'ln': math.log, 'exp': math.exp, 'pi': math.pi,
                               'sin': math.sin, 'cos': math.cos, 'tan': math.tan})
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set(f"Error: {e}")
        else:
            # Append the clicked button's text to the current text
            self.result_var.set(current_text + button_text)


if __name__ == "__main__":
    app = SmartCalculator()
    app.mainloop()
