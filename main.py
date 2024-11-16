import tkinter as tk
import time

class Kronometre:
    def __init__(self, root):
        self.root = root
        self.root.title("Gelişmiş Kronometre")

        self.baslangic_zamani = None
        self.toplam_sure = 0
        self.calismakta = False
        self.tur_zamanlari = []

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.start_button = tk.Button(self.buttons_frame, text="Başlat", command=self.baslat, width=10)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(self.buttons_frame, text="Durdur", command=self.durdur, width=10)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(self.buttons_frame, text="Sıfırla", command=self.sifirla, width=10)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.lap_button = tk.Button(self.buttons_frame, text="Tur Zamanı", command=self.tur_zamani, width=10)
        self.lap_button.grid(row=0, column=3, padx=5)

        self.lap_frame = tk.Frame(root)
        self.lap_frame.pack(pady=20)

        self.lap_label = tk.Label(self.lap_frame, text="Tur Zamanları:", font=("Helvetica", 14))
        self.lap_label.pack()

        self.lap_listbox = tk.Listbox(self.lap_frame, width=50, height=10)
        self.lap_listbox.pack()

        self.update_clock()

    def baslat(self):
        if not self.calismakta:
            self.baslangic_zamani = time.time()
            self.calismakta = True
            self.update_clock()
            print("Kronometre başlatıldı.")

    def durdur(self):
        if self.calismakta:
            self.toplam_sure += time.time() - self.baslangic_zamani
            self.calismakta = False
            print("Kronometre durduruldu. Toplam süre:", self.format_sure(self.toplam_sure))

    def sifirla(self):
        self.baslangic_zamani = None
        self.toplam_sure = 0
        self.tur_zamanlari = []
        self.calismakta = False
        self.label.config(text="00:00:00")
        self.lap_listbox.delete(0, tk.END)
        print("Kronometre sıfırlandı.")

    def tur_zamani(self):
        if self.calismakta:
            current_time = time.time()
            tur_suresi = current_time - self.baslangic_zamani + self.toplam_sure
            formatted_tur_suresi = self.format_sure(tur_suresi)
            self.tur_zamanlari.append(formatted_tur_suresi)
            self.lap_listbox.insert(tk.END, formatted_tur_suresi)
            print(f"Tur Zamanı: {formatted_tur_suresi}")

    def format_sure(self, sure):
        saat = int(sure // 3600)
        dakika = int((sure % 3600) // 60)
        saniye = int(sure % 60)
        return f"{saat:02}:{dakika:02}:{saniye:02}"

    def update_clock(self):
        if self.calismakta:
            sure = self.toplam_sure + (time.time() - self.baslangic_zamani)
            self.label.config(text=self.format_sure(sure))
        else:
            self.label.config(text=self.format_sure(self.toplam_sure))
        self.root.after(1000, self.update_clock)

root = tk.Tk()
app = Kronometre(root)
root.mainloop()
