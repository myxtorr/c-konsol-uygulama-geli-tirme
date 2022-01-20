harfler = "şçöğüİı"
parola = input("Parolanız: ")
for karakter in parola:
    if karakter in harfler:
        print("Parolada Türkçe karakter kullanılamaz.")
