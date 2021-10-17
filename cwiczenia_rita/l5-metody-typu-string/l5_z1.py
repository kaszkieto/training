# -*- coding: utf8 -*-
"""
    Do zmiennej sentence przypisz zdanie: „Kurs Pythona jest prosty i przyjemny.”, a następnie:

        *Policz wszystkie znaki w napisie
        *Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
        *Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?):
            7
            12
            -4
            37
"""

sentence = "Kurs Pythona jest prosty i przyjemny."

print(len(sentence))
print(sentence[18:25])
print(sentence[7])
print(sentence[12])
print(sentence[-4])
print(sentence[37]) #IndexError: string index out of range = ciąg indeksu poza zakrese
