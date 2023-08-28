import tkinter as tk
import random

total_points = 0
root = tk.Tk()
root.title("Sierpiński Triangle")
def draw_points():
    global total_points
    one = (450, 100)
    two = (200, 500)
    three = (700, 500)

    canvas = tk.Canvas(root, width=900, height=600)
    canvas.pack()
    canvas.create_oval(one[0] - 1, one[1] - 1, one[0] + 1, one[1] + 1, fill="black")
    canvas.create_oval(two[0] - 1, two[1] - 1, two[0] + 1, two[1] + 1, fill="black")
    canvas.create_oval(three[0] - 1, three[1] - 1, three[0] + 1, three[1] + 1, fill="black")
    update_number(total_points+3)
    x = random.randint(200, 700)
    y = random.randint(100, 500)
    canvas.create_oval(x-1, y-1, x+1, y+1, fill="black")
    for i in range(1, 45001):
        point = random.randint(1, 3)
        if point == 1:
            canvas.create_oval((one[0]+x)/2 - 1, (one[1]+y)/2 - 1, (one[0]+x)/2 + 1, (one[1]+y)/2 + 1, fill="black")
            x = (one[0]+x)/2
            y = (one[1]+y)/2
        elif point == 2:
            canvas.create_oval((two[0]+x)/2 - 1, (two[1]+y)/2 - 1, (two[0]+x)/2 + 1, (two[1]+y)/2 + 1, fill="black")
            x = (two[0]+x)/2
            y = (two[1]+y)/2
        elif point == 3:
            canvas.create_oval((three[0]+x)/2 - 1, (three[1]+y)/2 - 1, (three[0]+x)/2 + 1, (three[1]+y)/2 + 1, fill="black")
            x = (three[0]+x)/2
            y = (three[1]+y)/2
        total_points+=1
        update_number(total_points)
    
def update_number(total_points):
    label.config(text=f"Total points: {total_points}")
    root.update() 

label = tk.Label(root, text="Total points: 0")
label.pack(padx=20, pady=20)
draw_points()

root.mainloop()