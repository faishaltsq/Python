import tkinter as tk
from tkinter import ttk
import time

def check_weather():
    # Create a progress bar (determinate style)
    progress_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(side="bottom", padx=10, pady=10)
    progress_bar.start(50)  # Start progress bar with a delay of 50 milliseconds
    # Simulate some time-consuming task (e.g., fetching weather data)
    time.sleep(5)  # Sleep for 5 seconds (simulating a task)
    progress_bar.stop()  # Stop progress bar
    result_label.config(text="Weather checked!")

def quit_app():
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("ai weather")
root.geometry("300x120")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=2, pady=2)



# Create the "Check Weather" button
check_button = tk.Button(frame, text="Check Weather", command=check_weather)
check_button.pack(side="bottom", padx=1, pady=0)


# Create a progress bar (determinate style)
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(side="bottom", padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(frame, text="", font=("Helvetica", 12))
result_label.pack(side="bottom")

# Start the Tkinter main event loop
root.mainloop()
