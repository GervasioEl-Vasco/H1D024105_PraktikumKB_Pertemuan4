import tkinter as tk
from tkinter import messagebox

class DiagnosaKomputer:
    def __init__(self, jendela):
        self.jendela = jendela
        self.jendela.geometry("500x600")
        self.jendela.configure(bg="#fafafa")

        # Database kerusakan - Pake Dictionary biar rapi
        self.data_pakar = {
            "RAM Bermasalah": {
                "gejala": ["Muncul bunyi BIP berulang", "Layar Biru / BSOD", "Sering nge-hang"],
                "solusi": "Coba copot RAM-nya, gosok pin emasnya pake penghapus pensil pelan-pelan, terus pasang lagi."
            },
            "Power Supply (PSU) Lemah": {
                "gejala": ["PC tiba-tiba restart sendiri", "Kipas muter tapi pelan", "Kelistrikan casing nyetrum"],
                "solusi": "Pinjem PSU temen buat tes. Kalau normal, berarti PSU kamu harus ganti yang watt-nya murni."
            },
            "Overheat (Panas Berlebih)": {
                "gejala": ["Mati mendadak pas lagi berat", "Suara kipas kenceng banget", "Casing panas kalau dipegang"],
                "solusi": "Wajib bersihin debu di dalem. Terus ganti thermal paste prosesornya, mungkin udah kering."
            },
            "VGA/Grafis Rusak": {
                "gejala": ["Layar muncul garis warna-warni", "Tampilan layar pecah", "Sering crash pas main game"],
                "solusi": "Update driver VGA dulu. Kalau tetep muncul garis (artifact), kemungkinan hardware VGA-nya kena."
            },
            "Hardisk/SSD Bermasalah": {
                "gejala": ["Loading Windows lama banget", "Bunyi krek-krek dari dalem", "File sering gak bisa dibuka"],
                "solusi": "Jangan ditunda, langsung backup data penting! Cek kesehatan pake HDD Sentinel buat mastiin."
            }
        }

        self.pilihan_checkbox = {}
        self.tampilan_utama()

    def tampilan_utama(self):
        # Header simpel
        tk.Label(self.jendela, text="Cek Kerusakan Komputer", font=("Arial", 14, "bold"), bg="#fafafa", fg="#333").pack(pady=15)
        
        # Frame buat daftar gejala
        frame_gejala = tk.Frame(self.jendela, bg="white", padx=15, pady=15, relief="ridge", bd=1)
        frame_gejala.pack(padx=20, fill="both", expand=True)

        tk.Label(frame_gejala, text="Pilih apa yang kamu rasain:", font=("Arial", 10), bg="white").pack(anchor="w", pady=5)

        # Ambil semua gejala unik
        semua_gejala = []
        for d in self.data_pakar.values():
            semua_gejala.extend(d["gejala"])
        
        for g in sorted(list(set(semua_gejala))):
            var = tk.IntVar()
            cb = tk.Checkbutton(frame_gejala, text=g, variable=var, bg="white", font=("Arial", 10), activebackground="#eee")
            cb.pack(anchor="w")
            self.pilihan_checkbox[g] = var

        # Tombol Diagnosa
        btn = tk.Button(self.jendela, text="Cek Sekarang", command=self.mulai_diagnosa, 
                        bg="#4a90e2", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10, bd=0, cursor="hand2")
        btn.pack(pady=20)

    def mulai_diagnosa(self):
        terpilih = [g for g, v in self.pilihan_checkbox.items() if v.get() == 1]
        
        hasil = []
        for nama, detail in self.data_pakar.items():
            # Hitung kecocokan
            cocok = set(terpilih) & set(detail["gejala"])
            skor = len(cocok)
            
            # Masukkan semua ke list hasil (supaya tidak ada yang "tidak cocok")
            # Kalau user gak pilih apa-apa, skornya 0 tapi tetep masuk list
            hasil.append({
                "nama": nama,
                "skor": skor,
                "solusi": detail["solusi"]
            })

        # Urutkan dari skor tertinggi ke terendah
        hasil.sort(key=lambda x: x["skor"], reverse=True)
        
        self.jendela_hasil(hasil)

    def jendela_hasil(self, list_hasil):
        win = tk.Toplevel(self.jendela)
        win.title("Analisis")
        win.geometry("400x450")
        
        txt = tk.Text(win, padx=15, pady=15, font=("Arial", 10), wrap="word")
        txt.pack(fill="both", expand=True)

        txt.insert("end", "KEMUNGKINAN PENYEBAB:\n", "bold")

        # Tampilkan semua data, yang paling cocok ada di atas
        for h in list_hasil:
            status = f" (Sangat Cocok)" if h["skor"] > 0 else " (Kemungkinan Lain)"
            txt.insert("end", f"• {h['nama']}{status}\n", "bold")
            txt.insert("end", f"  Saran: {h['solusi']}\n\n")
        
        txt.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosaKomputer(root)
    root.mainloop()