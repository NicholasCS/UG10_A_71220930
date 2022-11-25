nama = input("Masukan nama mahasiswa :")
NIM = input("Masukan NIM-nya :")
if NIM[2:4] == '22' and NIM[0:3]:
    print(nama,"merupakan mahasiswa informatika angkatan 20 hingga 22")

elif NIM[2:4] == '21' and NIM[0:3]:
    print(nama,"merupakan mahasiswa informatika angkatan 20 hingga 22")
    
elif NIM[2:4] == '20' and NIM[0:3]:
    print(nama,"merupakan mahasiswa informatika angkatan 20 hingga 22")

else:
    print(nama,"bukan merupakan mahasiswa informatika angkatan 20 hingga 22")
