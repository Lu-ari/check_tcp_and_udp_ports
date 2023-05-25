import socket
from tkinter import *

def check_port(host, port, protocol):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == 'TCP' else socket.SOCK_DGRAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        return True
    else:
        return False

def display_result():
    host = host_entry.get()
    port = int(port_entry.get())
    protocol = var.get()
    if check_port(host, port, protocol):
        result_label.config(text=f"Port {port} is open")
    else:
        result_label.config(text=f"Port {port} is closed")

root = Tk()
root.title("Port Checker")

source_label = Label(root, text="Source Computer:")
source_label.pack()

hostname = socket.gethostname()
source_entry = Label(root, text=hostname)
source_entry.pack()

host_label = Label(root, text="Destination IP:")
host_label.pack()

host_entry = Entry(root)
host_entry.pack()

port_label = Label(root, text="Port:")
port_label.pack()

port_entry = Entry(root)
port_entry.pack()

var = StringVar(value="TCP")
tcp_radio = Radiobutton(root, text="TCP", variable=var, value="TCP")
tcp_radio.pack()

udp_radio = Radiobutton(root, text="UDP", variable=var, value="UDP")
udp_radio.pack()

check_button = Button(root, text="Check", command=display_result)
check_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
