import tkinter as tk

window = tk.Tk()

window.title("TCP Handshake Visualizer")
window.geometry("1000x500")
window.configure(bg="black")

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
    text="TCP Three-Way Handshake",
    fill="white",
    font=("Arial", 24)
)

# Client
canvas.create_rectangle(
    100, 180, 250, 280,
    fill="blue"
)

canvas.create_text(
    175, 230,
    text="CLIENT",
    fill="white",
    font=("Arial", 16)
)

# Server
canvas.create_rectangle(
    750, 180, 900, 280,
    fill="red"
)

canvas.create_text(
    825, 230,
    text="SERVER",
    fill="white",
    font=("Arial", 16)
)

# Status text
status_text = canvas.create_text(
    500,
    120,
    text="Waiting...",
    fill="yellow",
    font=("Arial", 18)
)

# Packet
packet = canvas.create_oval(
    160,
    140,
    190,
    170,
    fill="yellow"
)

# Packet label
packet_label = canvas.create_text(
    175,
    130,
    text="",
    fill="white",
    font=("Arial", 12)
)


def move_packet(start_x, end_x, label):

    canvas.itemconfig(packet_label, text=label)

    y = 140

    step = 5 if end_x > start_x else -5

    for x in range(start_x, end_x, step):

        canvas.coords(
            packet,
            x,
            y,
            x + 30,
            y + 30
        )

        canvas.coords(
            packet_label,
            x + 15,
            y - 10
        )

        window.update()
        window.after(10)


def start_handshake():

    # SYN
    canvas.itemconfig(
        status_text,
        text="Client → Server : SYN"
    )

    move_packet(
        160,
        760,
        "SYN"
    )

    window.after(500)

    # SYN ACK
    canvas.itemconfig(
        status_text,
        text="Server → Client : SYN-ACK"
    )

    move_packet(
        760,
        160,
        "SYN-ACK"
    )

    window.after(500)

    # ACK
    canvas.itemconfig(
        status_text,
        text="Client → Server : ACK"
    )

    move_packet(
        160,
        760,
        "ACK"
    )

    window.after(500)

    canvas.itemconfig(
        status_text,
        text="Connection Established ✅"
    )

    canvas.itemconfig(
        packet_label,
        text=""
    )


# Button
start_button = tk.Button(
    window,
    text="Start Handshake",
    command=start_handshake,
    font=("Arial", 14),
    bg="orange"
)

start_button.place(
    x=420,
    y=420
)

window.mainloop()