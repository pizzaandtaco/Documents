def cek_palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]

kata_input = input("Masukkan Kata : ")

hasil = cek_palindrom(kata_input)

if hasil:
    print(f"{kata_input} adalah True (palindrom)")
else:
    print(f"{kata_input} adalah False (bukan Palindrom)")