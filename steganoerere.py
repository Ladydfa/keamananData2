import os
from stegano import lsb
import tkinter as tk
from tkinter import filedialog, messagebox

def get_image_path():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])
    if file_path:
        return file_path
    else:
        return None

def hide_message_gui():
    img_path = get_image_path()
    if not img_path:
        messagebox.showerror("Error", "Path gambar tidak valid atau tidak dipilih.")
        return

    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Pesan tidak boleh kosong.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not save_path:
        messagebox.showerror("Error", "Path untuk menyimpan gambar tidak valid atau tidak dipilih.")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        messagebox.showinfo("Success", f"Pesan berhasil disembunyikan dalam gambar.\nGambar disimpan di: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan gambar: {e}")

def show_message_gui():
    img_path = get_image_path()
    if not img_path:
        messagebox.showerror("Error", "Path gambar tidak valid atau tidak dipilih.")
        return

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
        else:
            messagebox.showinfo("Info", "Tidak ada pesan tersembunyi dalam gambar ini.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menampilkan pesan dari gambar: {e}")

def exit_app():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Steganography Tool - GUI Version")
root.geometry("400x300")
root.configure(bg="purple")

# Widgets
frame = tk.Frame(root, padx=10, pady=10, bg="purple")
frame.pack(expand=True)

title_label = tk.Label(frame, text="Steganography Tool", font=("Helvetica", 16), bg="purple", fg="white")
title_label.pack(pady=10)

message_label = tk.Label(frame, text="Pesan Rahasia:", bg="purple", fg="white")
message_label.pack()

message_entry = tk.Entry(frame, width=40)
message_entry.pack(pady=5)

hide_button = tk.Button(frame, text="Sembunyikan Pesan", command=hide_message_gui, width=20, bg="white", fg="purple")
hide_button.pack(pady=5)

reveal_button = tk.Button(frame, text="Tampilkan Pesan", command=show_message_gui, width=20, bg="white", fg="purple")
reveal_button.pack(pady=5)

exit_button = tk.Button(frame, text="Keluar", command=exit_app, width=20, bg="white", fg="purple")
exit_button.pack(pady=10)

# Run the GUI
root.mainloop()
