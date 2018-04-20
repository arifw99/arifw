def ff():
    print ("Tugas Kalkulator")
tambah,kurang,kali,bagi=range(4)

def hitung(a, b, operator=Tambah, frmtOut=float):
    hasil = 0
    if operator == Tambah:
        hasil = a + b
    elif operator == Kurang:
        hasil = a-b
    elif operator == Kali:
        hasil = a*b
    elif operator == Bagi:
        hasil = a/b
    else:
        ValueError("Operator yang dijalankan Tambah, Kurang, Kali, Bagi")
if frmtOut == float:
        hasil = float(hasil)
    elif frmtOut == int:
        hasil = round(hasil)
    else:

        ValueError("Format yang di jalankan yaitu Int atau Float")

    return hasil  
