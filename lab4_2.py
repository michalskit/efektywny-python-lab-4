# Elementy programowania funkcyjnego
# Zaimplementuj poniższą funkcję tak, aby działała identycznie jak jej
# wbudowany odpowiednik. Pamiętaj, że w Pythonie ta funkcja zwracaja
# generator.

# Funkcja 'map' w Pythonie stosowana jest do stosowania funkcji
# na każdym elemencie iterowalnym (np. listy) w sposób sekwencyjny.
# Jest to szczególnie przydatne, gdy potrzebujemy zastosować
# przekształcenie lub operację na wielu elementach iterowalnych.

# Podstawowa składnia wygląda następująco:
# map(funkcja, iterowalny_obiekt)

# Gdzie 'funkcja' to funkcja, którą chcemy zastosować do elementów,
# a 'iterowalny_obiekt' to np. lista, na której elementach funkcja
# ma być stosowana.

# Wynikiem działania funkcji 'map' jest obiekt mapy, który można
# łatwo przekonwertować na listę lub inny typ danych, aby zobaczyć
# wyniki operacji.

# Przykład użycia:
# >>> lista = [1, 2, 3, 4]
# >>> wynik = map(lambda x: x * 2, lista)
# >>> print(list(wynik))
# [2, 4, 6, 8]

# W tym przykładzie funkcja 'map' stosuje funkcję lambda, która
# mnoży każdy element przez 2, do każdego elementu w liście.
# Podpowiedź: funkcja map zwraca TypeError, gdy przekazana funkcja
# jest None lub gdy przekazana lista jest pusta.

def _map(func, *iterables):
    pass