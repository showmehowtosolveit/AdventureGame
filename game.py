import tkinter as tk
from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Lost Library: A Journey of Choices")
        self.geometry("600x650")
        self.configure(bg="white")

        # Initialize current stage
        self.current_stage = 0

        # Load stages and outcomes
        self.stages = [
            ("You find a mysterious map in an old bookstore. Do you:", "Follow the map", "Ignore the map", "map.jpg"),
            ("You arrive at a fork in the road. Do you:", "Take the left path", "Take the right path", "fork_in_road.jpg"),
            ("You encounter a wise old man. Do you:", "Ask for advice", "Continue on your own", "wise_old_man.jpg"),
            ("You find a hidden cave. Do you:", "Enter the cave", "Keep walking", "hidden_cave.jpg"),
            ("You reach a river with a broken bridge. Do you:", "Try to fix the bridge", "Find another way around", "river.jpg"),
            ("You discover a village. Do you:", "Ask villagers for help", "Keep your presence hidden", "village.jpg"),
        ]

        self.outcomes = [
            ("You get lost and must start over.", "lost.jpg"),
            ("You find a hidden treasure and move forward!", "treasure.jpg"),
            ("You encounter a dangerous animal and must start over.", "lost.jpg"),
            ("You find a hidden shortcut and move forward!", "treasure.jpg"),
            ("The old man gives you a magic item and you move forward!", "treasure.jpg"),
            ("You wander aimlessly and must start over.", "lost.jpg"),
            ("The cave is dark and you get lost. Start over.", "lost.jpg"),
            ("You find a secret passage in the cave and move forward!", "treasure.jpg"),
            ("The bridge collapses and you fall. Start over.", "lost.jpg"),
            ("You find a boat and cross the river safely. Move forward!", "treasure.jpg"),
            ("The villagers are friendly and help you. Move forward!", "treasure.jpg"),
            ("You get caught and must start over.", "lost.jpg")
        ]

        self.next_stages = {
            0: (1, 6),   # Follow the map or Ignore the map
            1: (2, 3),   # Left path or Right path
            2: (4, 5),   # Ask for advice or Continue on your own
            3: (6, 7),   # Enter the cave or Keep walking
            4: (8, 9),   # Fix the bridge or Find another way around
            5: (10, 11)  # Ask villagers for help or Keep presence hidden
        }

        self.create_widgets()

    def create_widgets(self):
        self.story_label = tk.Label(self, text="Welcome to the Lost Library Adventure!", font=("Helvetica", 20), wraplength=600)
        self.story_label.pack(pady=20)

        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

        self.option1_button = tk.Button(self, text="Option 1", command=lambda: self.next_stage(1))
        self.option2_button = tk.Button(self, text="Option 2", command=lambda: self.next_stage(2))

        self.option1_button.pack(pady=10)
        self.option2_button.pack(pady=10)

        self.update_story()

    def update_story(self):
        if self.current_stage < len(self.stages):
            self.story_label.config(text=self.stages[self.current_stage][0])
            self.option1_button.config(text=self.stages[self.current_stage][1])
            self.option2_button.config(text=self.stages[self.current_stage][2])
            image_path = self.stages[self.current_stage][3]
        else:
            outcome_index = self.current_stage - len(self.stages)
            self.story_label.config(text=self.outcomes[outcome_index][0])
            image_path = self.outcomes[outcome_index][1]
            self.option1_button.pack_forget()
            self.option2_button.pack_forget()

        self.display_image(image_path)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((550, 400))
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

    def next_stage(self, choice):
        if self.current_stage in self.next_stages:
            self.current_stage = self.next_stages[self.current_stage][choice - 1]
        else:
            self.current_stage += 1

        self.update_story()

if __name__ == "__main__":
    app = AdventureGame()
    app.mainloop()
