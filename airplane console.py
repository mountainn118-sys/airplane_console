import tkinter as tk

class AirplaneConsole(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Airplane Console")
        self.geometry("400x340")
        self.configure(bg="black")
        self.altitude = 0
        self.speed = 0
        self.flying = False

        self.status = tk.Label(
            self,
            text="",
            font=("Consolas", 12),
            justify="left",
            bg="black",
            fg="white",
            anchor="w"
        )
        self.status.pack(pady=10, fill="x")

        # Entry for command input (terminal style)
        self.cmd_entry = tk.Entry(
            self,
            font=("Consolas", 12),
            bg="#222",
            fg="white",
            insertbackground="white"
        )
        self.cmd_entry.pack(pady=10, fill="x")
        self.cmd_entry.bind("<Return>", self.process_command)
        self.cmd_entry.focus_set()

        # Prompt label for command input
        prompt = tk.Label(
            self,
            text="> Type command and press Enter:",
            font=("Consolas", 11),
            bg="black",
            fg="#44ff44",
            anchor="w"
        )
        prompt.pack(pady=(0,2), fill="x")

        self.update_status()

    def process_command(self, event):
        cmd = self.cmd_entry.get().strip().lower()
        self.cmd_entry.delete(0, tk.END)
        if cmd == "takeoff":
            self.takeoff()
        elif cmd == "land":
            self.land()
        elif cmd == "ascend":
            self.ascend()
        elif cmd == "descend":
            self.descend()
        elif cmd == "accelerate":
            self.accelerate()
        elif cmd == "decelerate":
            self.decelerate()
        elif cmd == "exit":
            self.exit_console()
        else:
            self.update_status(f"Unknown command: {cmd}")

    def update_status(self, msg=""):
        # ASCII airplane drawing based on status
        if not self.flying:
            plane_art = (
                "    __|__\n"
                "--o--(_)--o--\n"
                "     / \\   \n"
                "   LANDED"
            )
        elif msg.startswith("Ascending"):
            plane_art = (
                "    __|__\n"
                "--o--(_)--o--\n"
                "    /   \\  ↑\n"
                "  ASCENDING"
            )
        elif msg.startswith("Descending"):
            plane_art = (
                "    __|__\n"
                "--o--(_)--o--\n"
                "    \\   /  ↓\n"
                "  DESCENDING"
            )
        else:
            plane_art = (
                "    __|__\n"
                "--o--(_)--o--\n"
                "     / \\   \n"
                "   FLYING"
            )

        status_text = (
            f"{plane_art}\n\n"
            f"Altitude: {self.altitude} meters\n"
            f"Speed: {self.speed} km/h\n"
            f"Flying: {'Yes' if self.flying else 'No'}\n"
        )
        if msg:
            status_text += f"\n{msg}"
        self.status.config(text=status_text)

    def takeoff(self):
        if not self.flying:
            self.flying = True
            self.altitude = 1000
            self.speed = 300
            self.update_status("Taking off...")
        else:
            self.update_status("Already flying!")

    def land(self):
        if self.flying:
            self.flying = False
            self.altitude = 0
            self.speed = 0
            self.update_status("Landing...")
        else:
            self.update_status("Already landed!")

    def ascend(self):
        if self.flying:
            self.altitude += 500
            self.update_status("Ascending...")
        else:
            self.update_status("You need to take off first!")

    def descend(self):
        if self.flying and self.altitude > 500:
            self.altitude -= 500
            self.update_status("Descending...")
        elif self.flying:
            self.altitude = 500
            self.update_status("Descending to minimum safe altitude...")
        else:
            self.update_status("You need to take off first!")

    def accelerate(self):
        if self.flying:
            self.speed += 50
            self.update_status("Accelerating...")
        else:
            self.update_status("You need to take off first!")

    def decelerate(self):
        if self.flying and self.speed > 100:
            self.speed -= 50
            self.update_status("Decelerating...")
        elif self.flying:
            self.speed = 100
            self.update_status("Decelerating to minimum safe speed...")
        else:
            self.update_status("You need to take off first!")

if __name__ == "__main__":
    AirplaneConsole().mainloop()