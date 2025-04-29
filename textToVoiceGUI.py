import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import os

def choose_text_file():
    filepath = filedialog.askopenfilename(
        title="Chọn file văn bản định dạng txt",
        filetypes=[("Text files", "*.txt")]
    )
    if filepath:
        text_file_path.set(filepath)

def choose_output_folder():
    folder = filedialog.askdirectory(title="Chọn thư mục lưu file âm thanh")
    if folder:
        output_folder_path.set(folder)

def convert_text_to_speech():
    txt_path = text_file_path.get()
    output_name = output_filename.get().strip()
    output_dir = output_folder_path.get()

    if not txt_path or not output_name or not output_dir:
        messagebox.showerror("Thiếu thông tin", "Vui lòng điền đầy đủ thông tin.")
        return

    if not output_name.endswith(".mp3"):
        output_name += ".mp3"

    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read()

        tts = gTTS(text=text, lang='vi')
        full_path = os.path.join(output_dir, output_name)
        tts.save(full_path)

        messagebox.showinfo("Thành công", f"Đã lưu file âm thanh tại:\n{full_path}")

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


# GUI setup
root = tk.Tk()
root.title("Chuyển văn bản thành giọng nói (.mp3)")
root.geometry("500x300")
root.resizable(False, False)

text_file_path = tk.StringVar()
output_folder_path = tk.StringVar()
output_filename = tk.StringVar()

tk.Label(root, text="1. Chọn file văn bản (.txt):").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=text_file_path, width=60).pack(padx=10)
tk.Button(root, text="Chọn file", command=choose_text_file).pack(pady=5)

tk.Label(root, text="2. Nhập tên file âm thanh (.mp3):").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=output_filename, width=40).pack(padx=10)

tk.Label(root, text="3. Chọn thư mục lưu file:").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=output_folder_path, width=60).pack(padx=10)
tk.Button(root, text="Chọn thư mục", command=choose_output_folder).pack(pady=5)

tk.Button(root, text="Chuyển thành giọng nói", command=convert_text_to_speech, bg="#4CAF50", fg="white").pack(pady=20)

root.mainloop()
