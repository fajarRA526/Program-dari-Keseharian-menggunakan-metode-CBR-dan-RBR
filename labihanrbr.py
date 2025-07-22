def rule_based_diagnosis(gejala):
    if gejala == "demam dan batuk":
        return "Kemungkinan: Flu biasa. Disarankan istirahat dan minum obat penurun demam."
    elif gejala == "demam tinggi dan nyeri otot":
        return "Kemungkinan: Demam Berdarah. Segera periksa ke dokter untuk tes darah."
    elif gejala == "sakit perut dan diare":
        return "Kemungkinan: Keracunan makanan. Minum oralit dan jaga asupan cairan."
    elif gejala == "batuk kering dan sesak napas":
        return "K andiri."
    elif gejala == "pusing dan lemas":
        return "Kemungkinan: Tekanan darah rendah. Istirahat cukup dan minum air putih."
    else:
        return "Gejala tidak dikenali. Silakan konsultasikan ke dokter."

# Input dari pengguna
input_gejala = input("Masukkan gejala yang dirasakan (contoh: demam dan batuk / sakit perut dan diare): ").lower()

# Diagnosa
hasil = rule_based_diagnosis(input_gejala)

# Output hasil
print("\n" + hasil)
