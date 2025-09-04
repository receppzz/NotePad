import customtkinter as ctk
from tkinter import filedialog

# ---------- Uygulama Ayarları ----------
ctk.set_appearance_mode("dark")   # dark / light
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Not Defteri")
app.geometry("600x400")


# ---------- Fonksiyonlar ----------
def kaydet():
    dosya = filedialog.asksaveasfile(defaultextension=".txt",
                                     filetypes=[("Text Files", "*.txt")])
    if dosya:
        dosya.write(text_area.get("1.0", "end-1c"))
        dosya.close()

def ac():
    dosya = filedialog.askopenfile(filetypes=[("Text Files", "*.txt")])
    if dosya:
        text_area.delete("1.0", "end")
        text_area.insert("1.0", dosya.read())

def cikis():
    # Animasyonlu çıkış
    for i in range(1, 11):
        app.attributes("-alpha", 1 - i*0.1)  # saydamlık
        app.update()
        app.after(30)  # 30ms bekle
    app.destroy()


# ---------- Not Alanı ----------
text_area = ctk.CTkTextbox(app, width=500, height=250)
text_area.pack(pady=20)


# ---------- Butonlar ----------
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

ac_btn = ctk.CTkButton(btn_frame, text="Aç", command=ac)
ac_btn.grid(row=0, column=0, padx=10)

kaydet_btn = ctk.CTkButton(btn_frame, text="Kaydet", command=kaydet)
kaydet_btn.grid(row=0, column=1, padx=10)

cikis_btn = ctk.CTkButton(app, text="Çıkış", command=cikis)
cikis_btn.pack(pady=10)


# ---------- Çalıştır ----------
app.mainloop()
