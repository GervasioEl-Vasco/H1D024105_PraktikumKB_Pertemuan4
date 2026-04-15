import tkinter as tk
from tkinter import messagebox

database_penyakit = {
    "Malaria Tertiana": ["nyeri_otot", "muntah", "kejang"],
    "Malaria Quartana": ["nyeri_otot", "menggigil", "tidak_enak_badam"],
    "Malaria Tropika": ["keringat_dingin", "sakit_kepala", "mimisan", "mual"],
    "Malaria Pernisiosa": ["menggigil", "tidak_enak_badan", "demam", "mimisan", "mual"]
}

semua_gejala = [
    ("nyeri_otot", "Apakah Anda merasa nyeri otot?"),
    ("muntah", "Apakah Anda muntah-muntah"),
    ("kejang", "Apakah Anda mengalami kejang-kejang?"),
    ("menggigil", "Apakah Anda sering menggigil?"),
    ("tidak_enak_badan", "Apakah Anda merasa tidak enak badan?"),
    ("keringat_dingin", "Apakah Anda keluar keringat dingin?"),
    ("sakit_kepala", "Apakah Anda merasa sakit kepala?"),
    ("mimisan", "Apakah Anda mengalami mimisan?"),
    ("mual", "Apakah Anda merasa mual?"),
    ("demam", "Apakah Anda mengalami demam?")
]

class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Malaria")