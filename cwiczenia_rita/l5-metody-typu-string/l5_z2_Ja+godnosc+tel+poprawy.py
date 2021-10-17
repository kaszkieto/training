imie = input("Podaj imię: ")
nazwisko = input("Podaj Nazwisko: ")
numer_telefonu = input("Podaj numer telefonu: ")

print("Twoje dane to: " +imie.capitalize().replace("-", "").replace(" ", "") +" "+nazwisko.capitalize().replace("-", "").replace(" ", "")+" "+numer_telefonu.replace("-", "").replace(" ", "") )

print(imie.isalpha())
print(nazwisko.isalpha())
print(numer_telefonu.isdigit())
