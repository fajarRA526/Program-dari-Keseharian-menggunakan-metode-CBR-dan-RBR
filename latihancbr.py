# Definisi class untuk kasus penyakit
class DiseaseCase:
    def __init__(self, gejala, diagnosis):
        self.gejala = [g.lower() for g in gejala]
        self.diagnosis = diagnosis

 
penyakit_cases = [
    DiseaseCase(["demam", "batuk", "pilek"], "Kemungkinan: Flu biasa"),
    DiseaseCase(["demam tinggi", "nyeri otot", "mual", "sakit kepala"], "Kemungkinan: Demam Berdarah"),
    DiseaseCase(["batuk kering", "sakit tenggorokan", "sesak napas"], "Kemungkinan: Covid-19"),
    DiseaseCase(["sakit perut", "mual", "diare"], "Kemungkinan: Keracunan makanan"),
    DiseaseCase(["pusing", "mata kabur", "lemas"], "Kemungkinan: Tekanan darah rendah")
]


def cari_kasus_terdekat(gejala_input, cases):
    hasil = []
    for case in cases:
        match = set(gejala_input) & set(case.gejala)
        similarity = len(match) / len(case.gejala)
        hasil.append((similarity, case))
    hasil.sort(reverse=True, key=lambda x: x[0])
    return hasil


user_input = input("Masukkan gejala yang dirasakan (pisahkan dengan koma):\n")
gejala_user = [g.strip().lower() for g in user_input.split(",")]


hasil = cari_kasus_terdekat(gejala_user, penyakit_cases)

# Output hanya satu hasil terbaik, tanpa persen
if hasil and hasil[0][0] > 0:
    print("\n=== Hasil Diagnosa ===")
    print(hasil[0][1].diagnosis)
else:
    print("Tidak ditemukan kasus penyakit yang cocok.")
