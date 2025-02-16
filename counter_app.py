import tkinter as tk
import json
import os

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Counter")
        self.master.geometry("300x250")
        
        self.task_name = tk.StringVar()
        self.count = 0
        self.load_count()
        
        tk.Label(master, text="Enter Task Name:").pack(pady=5)
        self.task_entry = tk.Entry(master, textvariable=self.task_name)
        self.task_entry.pack(pady=5)
        
        self.count_label = tk.Label(master, text=f"Count: {self.count}", font=("Arial", 14))
        self.count_label.pack(pady=10)
        
        tk.Button(master, text="Increment", command=self.increment).pack(pady=5)
        tk.Button(master, text="Reset", command=self.reset_count).pack(pady=5)
        tk.Button(master, text="Save & Exit", command=self.save_and_exit).pack(pady=5)
    
    def load_count(self):
        if os.path.exists("counter_data.json"):
            with open("counter_data.json", "r") as file:
                data = json.load(file)
                self.count = data.get("count", 0)
                self.task_name.set(data.get("task", ""))
    
    def increment(self):
        self.count += 1
        self.update_label()
    
    def reset_count(self):
        self.count = 0
        self.update_label()
    
    def update_label(self):
        self.count_label.config(text=f"Count: {self.count}")
    
    def save_and_exit(self):
        data = {"task": self.task_name.get(), "count": self.count}
        with open("counter_data.json", "w") as file:
            json.dump(data, file)
        self.master.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
