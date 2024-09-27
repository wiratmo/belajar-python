nilai = int(input("masukan nilai anda"))

# if akan selalu diesksekusi walaupun pernyataan dalam if sebelumnya sudah bernilai benar
if(nilai > 80):
    print("lulus dengan predikat sangat memuaskan")
elif(nilai > 70):
    print("lulus dengan predikat memuaskan")
else:
    print("tidak lulus ")