import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class Counter:
    @staticmethod
    def increase_count_by(number, multiply):
        return number + 1 * multiply

    @staticmethod
    def reduce_count_by(initial, number):
        return initial - number


class ClickerFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {"padx": 5, "pady": 5}

        # temperature label
        self.count_label = ttk.Label(self, text="Counter")
        self.count_label.grid(column=0, row=0, sticky=tk.W, **options)

        # count entry
        self.count = tk.IntVar()
        self.count.set(1)
        self.current_count = ttk.Label(self, textvariable=self.count)
        self.current_count.grid(column=1, row=0, **options)

        self.multiplier_label = ttk.Label(self, text="Current Multiplier : x")
        self.multiplier_label.grid(column=0, row=2, sticky=tk.W, **options)

        self.multiplier = tk.IntVar()
        self.multiplier.set(1)
        self.current_multiplier = ttk.Label(self, textvariable=self.multiplier)
        self.current_multiplier.grid(column=1, row=2, **options)

        self.increase_button = ttk.Button(self, text="Click here to increase")
        self.increase_button["command"] = self.increment
        self.increase_button.grid(column=2, row=0, sticky=tk.W, **options)

        self.multiplier_button_by_2x = ttk.Button(
            self, text="Buy 2x multiplier (costs 10)"
        )
        self.multiplier_button_by_2x["command"] = self.buy_multiplier_2x
        self.multiplier_button_by_2x.grid(column=2, row=2, sticky=tk.W, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def increment(self):
        """Handle button click event"""
        try:
            current_count = int(self.count.get())
            current_multiplier = int(self.multiplier.get())
            new_count = Counter.increase_count_by(current_count, current_multiplier)
            self.count.set(new_count)
        except ValueError as error:
            showerror(title="Error", message=error)

    def buy_multiplier_2x(self):
        try:
            current_count = int(self.count.get())
            if current_count >= 10:
                current_count = Counter.reduce_count_by(current_count, 10)
                self.count.set(current_count)
            else:
                raise ValueError("Not enough money")
            current_multiplier = int(self.multiplier.get())
            current_multiplier = self.multiplier.set(current_multiplier + 1)
        except ValueError as error:
            showerror(title="Error", message=error)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Clicker Game")
        self.geometry("400x100")
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    ClickerFrame(app)
    app.mainloop()
