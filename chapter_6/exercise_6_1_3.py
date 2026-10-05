"""Reveal an answer image below a question using tkinter.

Reference: https://docs.python.org/3/library/tkinter.html
"""
import tkinter as tk
from tkinter import ttk


def create_window():
    window = tk.Tk()
    window.title('A picture answers the question')
    ttk.Label(window, text='What color is the sky on a clear day?', padding=15).pack()
    image = tk.PhotoImage(master=window, width=320, height=180)
    image.put('#70bfff', to=(0, 0, 320, 180))
    # Draw the sun into the image without requiring a separate asset.
    for y in range(30, 81):
        for x in range(235, 286):
            if (x - 260) ** 2 + (y - 55) ** 2 <= 25 ** 2:
                image.put('#ffe060', (x, y))
    answer = ttk.Label(window, image=image)
    answer.image = image  # Keep the PhotoImage alive.

    def show_answer():
        answer.pack(padx=15, pady=15)

    ttk.Button(window, text='Show the answer', command=show_answer).pack(pady=5)
    return window


if __name__ == '__main__':
    create_window().mainloop()
