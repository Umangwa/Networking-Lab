import tkinter as tk

window = tk.Tk()
window.title("ARP Broadcast Visualizer")
window.geometry("1200x700")
window.configure(bg="black")

canvas = tk.Canvas(
    window,
    width=1200,
    height=700,
    bg="black",
    highlightthickness=0
)

canvas.pack()

# =========================
# TITLE
# =========================

canvas.create_text(
    600,
    50,
    text="ARP Broadcast Visualizer",
    fill="white",
    font=("Arial", 28)
)

status_text = canvas.create_text(
    600,
    100,
    text="Press Start ARP",
    fill="yellow",
    font=("Arial", 18)
)

# =========================
# DEVICES
# =========================

canvas.create_rectangle(
    100, 250,
    240, 320,
    fill="blue"
)

canvas.create_text(
    170, 285,
    text="Your PC",
    fill="white",
    font=("Arial", 16)
)

canvas.create_rectangle(
    350, 120,
    490, 190,
    fill="green"
)

canvas.create_text(
    420, 155,
    text="Phone",
    fill="white",
    font=("Arial", 16)
)

canvas.create_rectangle(
    350, 420,
    490, 490,
    fill="orange"
)

canvas.create_text(
    420, 455,
    text="Printer",
    fill="white",
    font=("Arial", 16)
)

canvas.create_rectangle(
    650, 120,
    790, 190,
    fill="purple"
)

canvas.create_text(
    720, 155,
    text="Smart TV",
    fill="white",
    font=("Arial", 16)
)

canvas.create_rectangle(
    900, 250,
    1040, 320,
    fill="red"
)

canvas.create_text(
    970, 285,
    text="Target PC",
    fill="white",
    font=("Arial", 16)
)

# =========================
# SPEECH BUBBLES
# =========================

phone_text = canvas.create_text(
    420, 90,
    text="",
    fill="white",
    font=("Arial", 12)
)

printer_text = canvas.create_text(
    420, 540,
    text="",
    fill="white",
    font=("Arial", 12)
)

tv_text = canvas.create_text(
    720, 90,
    text="",
    fill="white",
    font=("Arial", 12)
)

target_text = canvas.create_text(
    970, 220,
    text="",
    fill="white",
    font=("Arial", 12)
)

# =========================
# PACKETS
# =========================

arp_packet = canvas.create_oval(
    160,
    220,
    190,
    250,
    fill="lime"
)

data_packet = canvas.create_oval(
    0,
    0,
    0,
    0,
    fill="yellow"
)

# =========================
# ANIMATION
# =========================

def smooth_move(packet, target_x, target_y):

    x1, y1, x2, y2 = canvas.coords(packet)

    steps = 80

    dx = (target_x - x1) / steps
    dy = (target_y - y1) / steps

    for _ in range(steps):

        canvas.move(
            packet,
            dx,
            dy
        )

        window.update()

        window.after(10)


# =========================
# ARP PROCESS
# =========================

def start_arp():

    # RESET STATE

    canvas.coords(
        arp_packet,
        160,
        220,
        190,
        250
    )

    canvas.coords(
        data_packet,
        0,
        0,
        0,
        0
    )

    canvas.itemconfig(
        phone_text,
        text=""
    )

    canvas.itemconfig(
        printer_text,
        text=""
    )

    canvas.itemconfig(
        tv_text,
        text=""
    )

    canvas.itemconfig(
        target_text,
        text=""
    )

    canvas.itemconfig(
        status_text,
        text="Your PC: WHO HAS 192.168.1.50 ?"
    )

    window.update()

    # BROADCAST

    smooth_move(
        arp_packet,
        550,
        250
    )

    window.after(500)

    # EVERYONE RESPONDS

    canvas.itemconfig(
        phone_text,
        text="Not me!"
    )

    canvas.itemconfig(
        tv_text,
        text="Not me!"
    )

    canvas.itemconfig(
        target_text,
        text="Not me!"
    )

    canvas.itemconfig(
        printer_text,
        text="THAT'S ME!"
    )

    window.after(2000)

    # MAC DISCOVERED

    canvas.itemconfig(
        status_text,
        text="Printer: MAC = AA:BB:CC:DD:EE:FF"
    )

    window.after(1500)

    # DATA PHASE

    canvas.coords(
        data_packet,
        160,
        220,
        190,
        250
    )

    canvas.itemconfig(
        status_text,
        text="Sending Data Packet To Printer..."
    )

    smooth_move(
        data_packet,
        400,
        430
    )

    window.after(1000)

    canvas.itemconfig(
        status_text,
        text="Communication Established ✅"
    )

    window.after(2000)

    canvas.itemconfig(
        status_text,
        text="Press Start ARP"
    )

# =========================
# BUTTON
# =========================

start_button = tk.Button(
    window,
    text="Start ARP",
    command=start_arp,
    bg="orange",
    font=("Arial", 14)
)

start_button.place(
    x=540,
    y=620
)

window.mainloop()