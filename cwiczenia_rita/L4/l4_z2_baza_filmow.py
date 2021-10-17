# -*- coding: utf8 -*-

"""
Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć. W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i jego oceny.
Dodaj do swojego spisu.
"""

filmy= {
    "Film1":10,
    "Film2":9,
    "Film3":8,
    "Film4":9,
    "Film5":8.5,
    "Film6":7,
    "Film7":7.4,
    "Film8":4,
    "Film9":6.6,
    "Film10":10,

}
print("Jaki film chcesz obejżeć?")
wybor_uzytkownika=(input())

if wybor_uzytkownika in filmy.keys():
    print("Ocena filmu jaki chcesz obejżeć wynosi: ", filmy[wybor_uzytkownika])
else:
    print("Nie mamy takiego filmy w bazie, chcesz dodać film i go ocenić?")
    print("Wybierz T dla tak lub N dla nie")

wybor2_uzytkownika=(input())

if wybor2_uzytkownika == "T" or wybor2_uzytkownika == "t":
    print("Tak")
    
    print("Podaj nazwę filmu: ")
    nazwa_filmu=(input())
    
    print("Jak oceniasz film w skali 1 do 10: ")    
    ocena_filmu=float(input())

    filmy.update({nazwa_filmu: ocena_filmu})
    
    print("Film został dodany do naszej listy, zobacz aktualną bazę filmów: ") 
    for x, y in filmy.items():
        print(x, y)

elif wybor2_uzytkownika == "N" or  wybor2_uzytkownika == "n":
    print("Zatem do zobaczenia")

else:
    print("Zatem do zobaczenia, papa")
