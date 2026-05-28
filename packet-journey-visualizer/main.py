import tkinter as tk

window = tk.Tk()

window.title("Packet Journey Visualizer")
window.geometry("1000x500")
window.configure(bg="black")


# Create canvas
canvas = tk.Canvas(
    window,
    width=1000,
    height=500,
    bg="black",
    highlightthickness=0
)

canvas.pack()


# Title
canvas.create_text(
    500,
    50,
    text="Packet Journey Visualizer",
    fill="white",
    font=("Arial", 24)
)


# Devices
canvas.create_rectangle(50, 200, 180, 260, fill="blue")
canvas.create_text(115, 230, text="Computer", fill="white", font=("Arial", 16))

canvas.create_rectangle(300, 200, 430, 260, fill="green")
canvas.create_text(365, 230, text="Router", fill="white", font=("Arial", 16))

canvas.create_rectangle(550, 200, 680, 260, fill="purple")
canvas.create_text(615, 230, text="ISP", fill="white", font=("Arial", 16))

canvas.create_rectangle(800, 200, 930, 260, fill="red")
canvas.create_text(865, 230, text="Server", fill="white", font=("Arial", 16))


# Connection lines
canvas.create_line(180, 230, 300, 230, fill="white", width=3)
canvas.create_line(430, 230, 550, 230, fill="white", width=3)
canvas.create_line(680, 230, 800, 230, fill="white", width=3)


# Packet
packet = canvas.create_oval(
    90,
    150,
    120,
    180,
    fill="yellow"
)


# Packet movement function
def move_packet():

    positions = [
        (90, 150),
        (340, 150),
        (590, 150),
        (840, 150)
    ]

    for x, y in positions:

        canvas.coords(packet, x, y, x + 30, y + 30)

        window.update()

        window.after(800)


# Send button
send_button = tk.Button(
    window,
    text="Send Packet",
    command=move_packet,
    font=("Arial", 14),
    bg="orange"
)

send_button.place(x=430, y=420)


window.mainloop()