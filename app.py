import tkinter as tk
from tkinter import ttk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")

        # Create display
        self.display = tk.Entry(root, font=('Arial', 18), bd=10, relief='ridge', justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Define buttons
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'log', 'sin', 'cos',
            'tan', 'exp', '(', ')'
        ]

        # Create button grid
        row_val = 1
        col_val = 0
        for button in self.buttons:
            action = lambda x=button: self.on_button_click(x)
            ttk.Button(root, text=button, command=action, width=5, padding=10).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.display.get()

        if button in '0123456789.':
            self.display.insert(tk.END, button)
        elif button in '+-*/':
            self.display.insert(tk.END, ' ' + button + ' ')
        elif button == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'sqrt':
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'log':
            try:
                result = math.log10(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'sin':
            try:
                result = math.sin(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'cos':
            try:
                result = math.cos(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'tan':
            try:
                result = math.tan(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == 'exp':
            try:
                result = math.exp(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif button == '(':
            self.display.insert(tk.END, '(')
        elif button == ')':
            self.display.insert(tk.END, ')')

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()



