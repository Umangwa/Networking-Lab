import tkinter as tk

window = tk.Tk()

window.title("DNS Lookup Visualizer")
window.geometry("1200x600")
window.configure(bg="black")

# Canvas
canvas = tk.Canvas(
    window,
    width=1200,
    height=600,
    bg="black",
    highlightthickness=0
)
canvas.pack()

# Title
canvas.create_text(
    600,
    50,
    text="DNS Lookup Visualizer",
    fill="white",
    font=("Arial", 24)
)

# Devices
canvas.create_rectangle(50, 250, 200, 320, fill="blue")
canvas.create_text(125, 285, text="Computer", fill="white")

canvas.create_rectangle(250, 250, 400, 320, fill="green")
canvas.create_text(325, 285, text="DNS Resolver", fill="white")

canvas.create_rectangle(450, 250, 600, 320, fill="purple")
canvas.create_text(525, 285, text="Root Server", fill="white")

canvas.create_rectangle(650, 250, 800, 320, fill="orange")
canvas.create_text(725, 285, text=".com TLD", fill="white")

canvas.create_rectangle(850, 250, 1000, 320, fill="red")
canvas.create_text(925, 285, text="Authoritative", fill="white")

canvas.create_rectangle(1050, 250, 1180, 320, fill="cyan")
canvas.create_text(1115, 285, text="IP Address", fill="black")

# Connection lines
canvas.create_line(200, 285, 250, 285, fill="white", width=3)
canvas.create_line(400, 285, 450, 285, fill="white", width=3)
canvas.create_line(600, 285, 650, 285, fill="white", width=3)
canvas.create_line(800, 285, 850, 285, fill="white", width=3)
canvas.create_line(1000, 285, 1050, 285, fill="white", width=3)

# Packet
packet = canvas.create_oval(
    110,
    180,
    140,
    210,
    fill="yellow"
)

# Status text
status_text = canvas.create_text(
    600,
    500,
    text="Press Start Lookup",
    fill="white",
    font=("Arial", 18)
)


def move_packet(x, y):
    canvas.coords(packet, x, y, x + 30, y + 30)
    window.update()
    window.after(1000)


def start_lookup():

    canvas.itemconfig(
        status_text,
        text="Computer → Resolver : Where is google.com?"
    )
    move_packet(300, 180)

    canvas.itemconfig(
        status_text,
        text="Resolver → Root : Where is google.com?"
    )
    move_packet(500, 180)

    canvas.itemconfig(
        status_text,
        text="Root → TLD : Ask .com server"
    )
    move_packet(700, 180)

    canvas.itemconfig(
        status_text,
        text="TLD → Authoritative : Find google.com"
    )
    move_packet(900, 180)

    canvas.itemconfig(
        status_text,
        text="Authoritative → IP Address"
    )
    move_packet(1100, 180)

    canvas.itemconfig(
        status_text,
        text="Answer Found: 142.250.x.x"
    )


# Button
start_button = tk.Button(
    window,
    text="Start Lookup",
    command=start_lookup,
    bg="yellow",
    font=("Arial", 14)
)

start_button.place(x=520, y=540)

window.mainloop()
