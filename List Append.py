i=0
nama = []
nim = []
tugas = []
uts = []
uas = []
akhir = []
while True :
    na = raw_input("Nama\t\t: ")
    nama.append(na)
    ni = input("NIM\t\t: ")
    nim.append(ni)
    tu = input("Nilai Tugas\t: ")
    tugas.append(tu)
    ut = input("Nilai UTS\t: ")
    uts.append(ut)
    us = input("Nilai UAS\t: ")
    uas.append(us)
    
    akhiri =(tu+ut+us)/3
    akhir.append(akhiri)

    tambahan = ' '
    while tambahan!='y' and tambahan!='t':
        tambahan= raw_input("tambah data (y/t)? ")
    i+=1
    if(tambahan == "t"):
        break


print "*****************************************"
print "no | nama | tugas | uts | uas | akhir "
print "*****************************************"
for d in range(i):
    print " ",d+1, "|  ",nama[d]," | ",nim[d]," | ",tugas[d]," | ",uts[d]," | ",uas[d]," | ",akhir[d],""
