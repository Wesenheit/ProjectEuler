# ProjectEuler
Biblioteka zawierające podstawowe funkcje przydatne przy rozwiązywaniu zadań z projektu Euler.
Biblioteka obecnie zawiera nastęujące funkcje
Teoria liczb:
    sito(x)-funkcja inicjująca tablicą od 0 do N która na i-tej pozycji ma najmniejszą liczbę pierwszą dzielącą i.
    fact(x,licz)- funkcja zwracająca tablicę dwóch tablic: jedna zwraca wszystkie dzielniki pierwsze liczby x, druga zwraca ich krotność
(wymaga zainicjowania tablicy licz funkcją sito).
    primes(x,licz)- funkcja zwracająca tylko liczby pierwsze dzielące x, wymaga zainicjowania tablicy licz funkcją sito.
    tot(x,licz)- zwraca tocjent liczby x oraz tak jak poprzednie funkcje wymaga tablicy zainicjowanej funkcją sito.
    nwd(a,b)- zwykły algorytm euclidesa zwracający nwd(a,b).
    modular_sqrt(a,p)-algorytm toneliego shanksa zwracający pierwiastek modularny a mod p.
    inverse(a,p)-zwraca odwrotność a modulo p z algorytmu euklidesa.
    ext_euc(a,b)- rozszerzony algorytm euklidesa zwracający także współczynniki z tożsamości bezouta.
    chin(M,ytab,ntab)- implementacja chińskiego twierdzenia o resztach która zwraca taką liczbę x, że x mod M jest spełnieniem układu równań
x=yi mod ni oraz iloczyn liczb z ntab daje nam M.

Moduł do programowania równoległego- biblioteka zawiera manager pozwalający na równoległe wykonywanie obliczeń na wielu rdzeniach procesora. Obiektowi manager przypisujemy tablicę liczb oraz funkcję która ma zostać wykonana na każdym z elementów tablicy, po wszystkim należy wywołać obiekt jako funkcję a zwróci on sumę wartości funkcji dla liczb z tablicy. 
