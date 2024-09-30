# konversi jam ke menit
def jamKeMenit(jam):
    menit = jam * 60
    return menit

# konversi menit ke detik
def menitToDetik(menit):
    detik = menit * 60
    return detik

print(menitToDetik(jamKeMenit(1)))
print(jamKeMenit(6))