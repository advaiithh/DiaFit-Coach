import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from exercises import EXERCISE_DB  # Separate file with all exercise data

def get_age_group(age):
    return 'young' if age < 30 else 'medium' if age < 60 else 'older'

def get_weight_class(w):
    return 'underweight' if w < 50 else 'normal' if w <= 80 else 'overweight'

class ExercisePlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diabetic Exercise Planner")
        self.create_ui()

    def create_ui(self):
        self.name = self.add_input("Name:")
        self.level = self.add_combo("Diabetic Level:", ["low", "normal", "high"])
        self.age = self.add_input("Age:")
        self.weight = self.add_input("Weight (kg):")

        ttk.Button(text="Generate Plan", command=self.generate_plan).pack(pady=10)
        self.output = tk.Text(height=25, width=90)
        self.output.pack()

        # Make links look clickable
        self.output.tag_config("hyperlink", foreground="blue", underline=1)

    def add_input(self, label):
        ttk.Label(text=label).pack()
        entry = ttk.Entry()
        entry.pack()
        return entry

    def add_combo(self, label, options):
        ttk.Label(text=label).pack()
        combo = ttk.Combobox(values=options, state="readonly")
        combo.pack()
        return combo

    def generate_plan(self):
        self.output.delete(1.0, tk.END)
        try:
            name = self.name.get()
            level = self.level.get()
            age = int(self.age.get())
            weight = float(self.weight.get())

            if not name or level not in EXERCISE_DB: raise ValueError("Invalid input")

            age_group = get_age_group(age)
            weight_class = get_weight_class(weight)
            exercises = EXERCISE_DB[level][age_group]

            self.output.insert(tk.END, f"\n{name}'s Plan\nAge: {age_group}, Weight: {weight_class}, Level: {level}\n\n")

            for place in ['indoor', 'outdoor']:
                if place in exercises:
                    self.output.insert(tk.END, f"{place.title()} Exercises:\n" + "-"*60 + "\n")
                    for ex, d in exercises[place].items():
                        self.output.insert(tk.END, f"➤ {ex} ({d['duration']})\n")
                        for i, step in enumerate(d['instructions'], 1):
                            self.output.insert(tk.END, f"  {i}. {step}\n")
                        if 'video' in d:
                            url = d['video']
                            self.output.insert(tk.END, "▶ Video: ", "hyperlink")
                            self.output.insert(tk.END, url + "\n", ("hyperlink", url))
                            self.output.tag_bind(url, "<Button-1>", lambda e, u=url: webbrowser.open(u))
                            self.output.tag_bind(url, "<Enter>", lambda e: self.output.config(cursor="hand2"))
                            self.output.tag_bind(url, "<Leave>", lambda e: self.output.config(cursor="arrow"))
                        self.output.insert(tk.END, "-"*60 + "\n")

            self.output.insert(tk.END, "\n⚠️ Safety Tips:\n• Monitor sugar\n• Stay hydrated\n• Stop if dizzy\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ExercisePlannerApp(root)
    root.mainloop()
