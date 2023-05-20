import tkinter as tk
from tkinter import ttk, Label
from tkinter import Canvas
from PIL import ImageTk, Image
import math
import openpyxl
import os.path
import numpy as np
from kiot_GUI import GUI_Nhap_SP, GUI_Ktra_TTSP, GUI_Tinh_Excel, GUI_Xuat_Kho, GUI_Sign

def create_GUI(file_path):
    window = tk.Tk()
    window.configure(background="light blue")
    window.title("Phần Mềm Quản Lý và Bán Hàng Quy Mô Nhỏ")
    window_width = 1200
    window_height = 650

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = math.floor((screen_width-window_width)/2)
    y_position = math.floor((screen_height-window_height)/2)

    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    # Load the image file
    image = Image.open("attachments/20221231_000741.jpg")

    # Resize the image to fit the window size
    image = image.resize((window_width, window_height))

    # Convert the image to a Tkinter-compatible format
    background_image = ImageTk.PhotoImage(image)

    # Create a Canvas widget with the image as the background
    canvas = Canvas(window, width=window_width, height=window_height)
    # canvas.place(relx=1, rely=1, anchor="se")
    canvas.place(x=0, y=0)

    # Add the image to the canvas
    canvas.create_image(0, 0, anchor="nw", image=background_image)

    GUI_Nhap_SP(file_path, window, 0, 0)
    GUI_Ktra_TTSP(file_path, window, 0, 3)
    GUI_Xuat_Kho(file_path, window, 1, 0)
    GUI_Tinh_Excel(file_path, window, 3, 0)
    GUI_Sign(window, 4, 3)
    window.mainloop()

if __name__ == "__main__":
    file_path = 'Bang_Tong_Hop.xlsx'
    create_GUI(file_path)
