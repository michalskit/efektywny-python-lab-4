# Elementy programowania funkcyjnego
# Zaimplementuj poniższą funkcję tak, aby działała identycznie jak jej
# wbudowany odpowiednik. Pamiętaj, że w Pythonie ta funkcja zwracaja
# generator.

# Zadanie 1:
# Funkcja filter() w Pythonie służy do filtrowania elementów sekwencji (np. listy).
# Przyjmuje dwa argumenty: funkcję oraz sekwencję. Funkcja jest wywoływana
# dla każdego elementu sekwencji i jeśli funkcja zwraca 'True', element
# jest dołączany do nowej listy, w przeciwnym razie jest pomijany.
# Ostatecznie filter() zwraca iterator zawierający elementy, dla których
# funkcja zwróciła 'True'. Poniżej przykład użycia filter() do filtrowania
# liczb parzystych z listy.
# Podpowiedź: użyj funkcji bool() jako domyślnej wartości dla parametru func

# Przykład użycia filter():
# definiowanie funkcji sprawdzającej parzystość liczby
def czy_parzysta(n):
    return n % 2 == 0

# lista z różnymi liczbami
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# użycie filter() do otrzymania tylko liczb parzystych
parzyste_liczby = filter(czy_parzysta, liczby)

# konwersja iteratora na listę i wydruk wyniku
print(list(parzyste_liczby))

def _filter(func, iterable=[]):
    pass