import tkinter as tk
from tkinter import ttk

# Logic functions
def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return ~a & 1
def XOR(a, b): return a ^ b

# GUI Class
class LogicGateSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Gate Simulator")
        self.root.geometry("350x300")

        self.input_a = tk.IntVar()
        self.input_b = tk.IntVar()

        # Input checkboxes
        input_frame = ttk.LabelFrame(root, text="Inputs")
        input_frame.pack(padx=10, pady=10)

        ttk.Checkbutton(input_frame, text="Input A", variable=self.input_a).grid(row=0, column=0, padx=10)
        ttk.Checkbutton(input_frame, text="Input B", variable=self.input_b).grid(row=0, column=1, padx=10)

        # Gate Buttons
        gate_frame = ttk.LabelFrame(root, text="Logic Gates")
        gate_frame.pack(padx=10, pady=10)

        ttk.Button(gate_frame, text="AND", command=self.calc_and).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(gate_frame, text="OR", command=self.calc_or).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(gate_frame, text="NOT A", command=self.calc_not).grid(row=1, column=0, padx=10, pady=5)
        ttk.Button(gate_frame, text="XOR", command=self.calc_xor).grid(row=1, column=1, padx=10, pady=5)

        # Output display
        self.output_label = ttk.Label(root, text="Output: ", font=("Arial", 14))
        self.output_label.pack(pady=10)

    def update_output(self, result):
        self.output_label.config(text=f"Output: {result}")

    def calc_and(self):
        self.update_output(AND(self.input_a.get(), self.input_b.get()))

    def calc_or(self):
        self.update_output(OR(self.input_a.get(), self.input_b.get()))

    def calc_not(self):
        self.update_output(NOT(self.input_a.get()))

    def calc_xor(self):
        self.update_output(XOR(self.input_a.get(), self.input_b.get()))

# Main app launcher
if __name__ == "__main__":
    root = tk.Tk()
    app = LogicGateSimulator(root)
    root.mainloop()
