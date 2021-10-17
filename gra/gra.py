
# zmienna potrzebna przy uruchomieniu programu
wybór_użytkownika = -1

# Tablice, zawierają dane w tym przypadku pytania
pytania = []
odpowiedzi = []

#Funkcje w programie

def pokaz_pytania():
    if len(pytania) >0:
        print("Oto lista pytań:")
        pytanie_index = 0
        odpowiedz_index = 0
        for pytanie in pytania:
            print(pytanie +" [ "+(str(pytanie_index)) +" ]" )
            pytanie_index += 1
        print()
        print("Oto lista odpowiedzi:")
        for odpowiedz in odpowiedzi:
            print(odpowiedz +" [ "+(str(odpowiedz_index)) +" ]" )
            odpowiedz_index += 1
    else:
        print ("Nie ma pytań, dodaj pierwsze pytanie wybierając z Menu opcję")       

def dodaj_pytanie():
    pytanie = input("Wpisz nowe pytanie: ")
    pytania.append(pytanie)
    print()
    print("Dodano pytanie!")

    odpowiedz = input("Wpisz odpowiedź do pytania: ")
    odpowiedzi.append(odpowiedz)
    print()
    print("Dodano odpowiedź!")

def usun_pytanie():
    try:
        pytanie_index = int(input("Wpisz ID pytania które chcesz usunąć: "))
        if pytanie_index <0 or pytanie_index > len(pytania)-1:
               print("Pytanie o takim ID nie istnieje")
               return   
        pytania.pop(pytanie_index)
        odpowiedzi.pop(pytanie_index)
        print()
        print("Usunięto pytanie!")
    except ValueError:
        print("Aby usunąć pytanie należy podać jego ID zawierające liczbę całkowitą. Pierwsze pytanie ma ID 0, drigie 1, kolejne 2 itd.")
    return
    

def ilosc_pytanie():
    print ("Ilość pytań w bazie " + str(len(pytania )) + " i odpowiedzi " + str(len(odpowiedzi )))

def zapisz_pytanie():
    plik_pytania = open("training/gra/pytania.txt", "w")
    for pytanie in pytania:
        plik_pytania.write(pytanie+"\n")
    plik_pytania.close()

    plik_odpowiedzi = open("training/gra/odpowiedzi.txt", "w") 
    for odpowiedz in odpowiedzi:
        plik_odpowiedzi.write(odpowiedz+"\n")
    plik_odpowiedzi.close()
    print ("Zmiany zostały zapisane")
 

def wczytaj_pytanie():
    try:
        plik_pytania = open("training/gra/pytania.txt")
        for linia in plik_pytania.readlines():
            pytania.append(linia.strip())
        plik_pytania.close()
        
    except FileNotFoundError:
        return

    try:
        plik_odpowiedzi = open("training/gra/odpowiedzi.txt")
        for linia in plik_odpowiedzi.readlines():
            odpowiedzi.append(linia.strip())
        plik_odpowiedzi.close()
        
    except FileNotFoundError:
        return

#  C:\Users\marek\Desktop\programowanie\python\training\gra\odpowiedzi.txt
# gra\odpowiedzi.txt

 # Główny widok menu programu.
wczytaj_pytanie()  
print()
print("Witaj w pierwszym programie:)")

# Pętla w Menu programu 

while wybór_użytkownika !=7:
    try:
        print()

        # Warunki wyboru użytkownika
        if wybór_użytkownika == 1:
            print("Gra dostępna wkrótce")

        if wybór_użytkownika == 2:
            pokaz_pytania()
            
        if wybór_użytkownika == 3:
            dodaj_pytanie()

        if wybór_użytkownika == 4:
            usun_pytanie()

        if wybór_użytkownika == 5:
            ilosc_pytanie()
            
        if wybór_użytkownika == 6:
            zapisz_pytanie()

        if wybór_użytkownika < 1 or wybór_użytkownika > 7:
            print("Menu programu składa się z opisanych niżej opcji między 1 a 7, wybierz żądaną opcję w tym przedziale.") 

        # Lista opcji w menu

        print("---------------------")
        print("GŁÓWNE MENU PROGRAMU")
        print("1. Zagraj (Gra dostępna wkrótce)")
        print("2. Pokaż pytania i odpowiedzi")
        print("3. Dodaj pytanie i odpowiedź")
        print("4. Usuń pytanie i odpowiedź")
        print("5. Ilość pytań w bazie " + str(len(pytania )) + " i odpowiedzi " + str(len(odpowiedzi )))
        print("6. Zapisz zmiany w plikach")
        print("7. Zakończ")
        print()
        # print(pytania[0])

        # zmienna którą wprowadza użytkownik w głównym menu programu
        wybór_użytkownika = int(input("Wybierz opcję: "))
        print()
        print("-------------------------------------------")
    
    except ValueError:
        print("Program nie obsługuje wprowadzonych danych.")
    