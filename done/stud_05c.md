Zbalansowane drzewa wyszukiwań
Zbalansowane drzewo wyszukiwań (balanced search tree)

Zbalansowane drzewa wyszukiwań
Drzewo wyszukiwań 2-3 – to drzewo, które jest puste, albo jest:
• Węzłem podwójnym – o jednym kluczu (+powiązanej wartości) oraz
dwóch odnośnikach:
• Lewy – prowadzi do drzewa wyszukiwań 2-3 z mniejszymi kluczami
• Prawy – do drzewa wyszukiwań 2-3 z większymi kluczami

• Węzłem potrójnym – o dwóch kluczach (+powiązanych wartości) oraz
trzech odnośnikach:
• Lewy – prowadzi do drzewa wyszukiwań 2-3 z mniejszymi kluczami
• Środkowy – do drzewa wyszukiwań 2-3 z kluczami o wartościach pomiędzy
wartościami kluczy z węzła
• Prawy – do drzew wyszukiwań 2-3 z większymi kluczami

Odnośnik do drzewa pustego nazywamy odnośnikiem pustym.

Zbalansowane drzewa wyszukiwań
Drzewo wyszukiwań 2-3
• Zachowany jest porządek
symetryczny: przechodzenie w
porządku INORDER daje klucze w
porządku rosnącym.
• Pełne zbalansowanie: Każda
ścieżka z korzenia do odnośnika
pustego ma taką samą długość

[SW-2018]

1


15.06.2023

Zbalansowane drzewa wyszukiwań
Wyszukiwanie
1. Porównaj poszukiwany klucz z kluczem w wierzchołku. Jeśli
równe to stop, jeśli nie – przejdź dalej.
2. Znajdź przedział zawierający poszukiwany klucz
3. Na podstawie powyższego wyniku przejdź do odpowiedniej
gałęzi i powtórz proces rekurencyjnie

Przykład: Znajdź H, Znajdź B

[SW-2018]

Zbalansowane drzewa wyszukiwań
Wstawienie do węzła podwójnego
Jeśli nie znajdziemy węzła w drzewie, to:
• nowy węzeł dodajemy na dole drzewa,
jak w BST – zły pomysł (zbalansowanie!)
• zastępujemy ten węzeł (jest on
podwójny) węzłem potrójnym,
zawierającym dawny klucz oraz klucz
wstawiany – dobry pomysł.

[SW-2018]

Zbalansowane drzewa wyszukiwań
Wstawienie do węzła potrójnego
• Wstawienie do drzewa składającego się z jednego węzła
potrójnego
• Wstawienie do węzła potrójnego, którego rodzicem jest węzeł
podwójny
• Wstawienie do węzła potrójnego, którego rodzicem jest węzeł
potrójny
• Podział korzenia
• Lokalne transformacje

2


15.06.2023

Zbalansowane drzewa wyszukiwań
Wstawienie do węzła potrójnego
Wstawienie do drzewa składającego się z jednego
węzła potrójnego:
1. Dodaj nowy klucz do węzła potrójnego tworząc
tymczasowo węzeł poczwórny
2. Przesuń środkowy klucz w węźle poczwórnym
do roli rodzica.
3. Powtarzaj procedurę w górę, jeśli potrzeba.
4. Jeśli osiągnięto korzeń i jest on węzłem
poczwórnym, podziel go na trzy podwójne
węzły.
[SW-2018]

Zbalansowane drzewa wyszukiwań
Wstawienie do węzła potrójnego
Wstawienie do węzła potrójnego, którego
rodzicem jest węzeł podwójny:
1. Dodaj nowy klucz do węzła potrójnego tworząc
tymczasowy węzeł poczwórny
2. Przesuń środkowy klucz w węźle poczwórnym
do węzła rodzica (ale nie tworzymy nowego
węzła, tylko dotychczasowy podwójny staje się
potrójnym).
3. Z pozostałego węzła potrójnego utwórz dwa
węzły podwójne

[SW-2018]

Zbalansowane drzewa wyszukiwań
Wstawienie do węzła potrójnego
Wstawienie do węzła potrójnego, którego
rodzicem jest węzeł potrójny:
1.
﻿Dodaj nowy klucz do węzła potrójnego tworząc
tymczasowy węzeł poczwórny
2. Przesuń środkowy klucz w węźle poczwórnym
do węzła rodzica (ale nie tworzymy nowego
węzła, tylko dotychczasowy potrójny staje się
poczwórnym).
[SW-2018]

3


15.06.2023

Zbalansowane drzewa wyszukiwań
Wstawienie do węzła potrójnego
Wstawienie do węzła potrójnego, którego rodzicem
jest węzeł potrójny (cd.):
3. Powtarzamy takie samo przekształcenie jak
poprzednio w węźle rodzica, czyli dzielimy
tymczasowy węzeł poczwórny, poprzez
przesunięcie jego środkowego klucza do rodzica.
4. Uogólniając, przechodzimy w górę drzewa, dzieląc
tymczasowe węzły poczwórne i wstawiając ich
środkowe klucze do ich rodziców aż osiągniemy
węzeł podwójny, który zamienimy na węzeł
potrójny, który nie musi być już dalej dzielony lub
aż osiągniemy węzeł potrójny w korzeniu.
[SW-2018]

Zbalansowane drzewa wyszukiwań
Podział korzenia
Jeśli węzły potrójne znajdują się na całej ścieżce od
punktu wstawiania do korzenia, ostatecznie węzeł
poczwórny powstanie w korzeniu.
Możemy postąpić wtedy tak samo, jak przy
wstawianiu do węzła składającego się jednego
węzła potrójnego, czyli podzielić tymczasowy
węzeł poczwórny na trzy węzły podwójne.
Wysokość drzewa zwiększy się wtedy o 1.
[SW-2018]

Zbalansowane drzewa wyszukiwań
Podsumowanie przekształceń
Właściwość: przekształcenia zachowują porządek symetryczny i pełne
zbalansowanie.

[SW-2018]

4


15.06.2023

Zbalansowane drzewa wyszukiwań
Analiza najgorszego przypadku
Operacje wyszukiwania i wstawiania w drzewach 2-3 o N kluczach
wymagają sprawdzenia co najwyżej log N węzłów.
Wysokość drzewa
• Worst case: log N (gdy wszystkie wierzchołki są podwójne)
• Best case: log3 N ≈ .631 log N (gdy wszystkie wierzchołki są potrójne)
Milion wierzchołków -> wysokość 12-20.
Miliard wierzchołków -> wysokość 18-30.

Zbalansowane drzewa wyszukiwań
Analiza najgorszego przypadku
Głównym celem zbalansowania jest zabezpieczenie się przed najgorszym
przypadkiem.

Zbalansowane drzewa wyszukiwań
Implementacja
Problemy:
• Konieczne jest przechowywanie dwóch różnych rodzajów węzłów
• Porównywanie kluczy wyszukiwania z każdym z kluczy węzła określonego
(różnego) rodzaju
• Konieczne są wykonywanie transformacji, prowadzących od węzła jednego
typu do innego,
• Ogólniej: bardzo często wykonywane są przekształcania węzłów z jednego
typu na inny
• Generalnie, wykonywanie transformacji na różnych typach danych
reprezentujących węzły podwójne i potrójne wymaga obsłużenia dużej liczby
przypadków

5


15.06.2023

Zbalansowane drzewa wyszukiwań
Implementacja
Propozycja ominięcia problemów:
Implementacja w postaci
Czerwono-czarnych drzew BST (ang. red-black BST), czyli drzew BST
reprezentujących drzewa 2-3.
Kolory odnoszą się tutaj do krawędzi, tj. każda krawędź jest albo
czerwona, albo czarna.

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Równoważna definicja
Drzewo czerwono-czarne to drzewo BST z czerwonymi i czarnymi
odnośnikami, spełniające warunki:
• Odnośniki czerwone znajdują się w treli niekory.
po lewej stronie
• Żaden węzeł nie jest powiązany z dwoma odnośnikami czerwonymi
• Drzewo jest w pełni zbalansowane ze względu na czarne odnośniki, tzn.
każda ścieżka z korzenia do pustego odnośnika obejmuje taką samą liczbę
czarnych odnośników.
Między czerwono-czarnymi drzewami BST zdefiniowanymi w ten sposób a
drzewami 2-3 występuje zależność 1-1.

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Zapisywanie węzłów potrójnych
• W postaci zwykłego drzewa BST (brak możliwości
przekształcenia z powrotem do pierwotnej postaci)
• W postaci drzewa BST z wyróżnioną krawędzią (brak wady
powyższej; zakładamy, że zawsze w lewym poddrzewie)

6


Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Zapisywanie węzłów potrójnych

[SW-2018]

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Zapisywanie węzłów potrójnych

[SW-2018]

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Zależność 1 do 1

[SW-2018]

7


Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Reprezentacja kolorów

[SW-2018]

private static final boolean RED = true;
private static final boolean BLACK = false;
private class Node
{
Key key;
Value val;
Node left, right;
boolean color; // kolor linku do rodzica
}
private boolean isRed(Node x)
{
if (x == null) return false; // zakładamy,
że „pusty” wierzchołek ma kolor BLACK
return x.color == RED;
}

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Wyszukiwanie
Technicznie wyszukiwanie w czerwono-czarnym drzewie BST
realizowane jest tak samo, jak w zwykłym drzewie BST
… ale szybciej z uwagi na lepsze zbalansowanie.

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Wstawianie
Kluczowe jest, aby wykonanie tej operacji zachowywało zależność 1
do 1 z drzewami 2-3:
• Porządek symetryczny
• Pełne zbalansowanie ze względu na czarne odnośniki

8


15.06.2023

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Wstawianie
Zastosowanie operacji na czerwono-czarnym drzewie BST:
• Rotacje
• Odwrócenie kolorów

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Rotacja (tymczasowego) czerwonego linku prawego na lewy (rotacja w lewo)

[SW-2018]

private Node rotateLeft(Node h)
{
Node x = h.right;
h.right = x.left;
x.left = h;
x.color = h.color;
h.color = RED;
return x;
}

Zachowuje porządek symetryczny oraz pełne zbalansowanie ze względu na
czarne odnośniki

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Rotacja lewego czerwonego linku na (tymczasowy) prawy (rotacja w prawo)
Analogicznie.

private Node rotateRight(Node h)
{
Node x = h.left;
h.left = x.right;
x.right = h;
x.color = h.color;
h.color = RED;
return x;
}

Zachowuje porządek symetryczny oraz pełne zbalansowanie ze względu na
czarne odnośniki.

9


15.06.2023

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Odwrócenie kolorów w celu podziału (tymczasowego) węzła
poczwórnego
private void flipColors(Node h)
{
h.color = RED;
h.left.color = BLACK;
h.right.color =
BLACK;
}

## SW-2018
- Zbalansowane drzewa wyszukiwań
- Czerwono-czarne drzewa
- BST
- Wstawianie, wybrane przykłady
  1. Wstawienie do drzewa składającego się tylko z jednego węzła

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa
BST
Wstawianie, wybrane
przykłady
Przypadek 1a. Wstawienie
do drzewa składającego się
tylko z jednego węzła

[SW-2018]

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Wstawianie, wybrane przykłady
Przypadek 1b. Wstawienie do jednego
węzła podwójnego:
1. Wstaw jak do zwykłego drzewa BST,
nadaj kolor czerwony odnośnikowi.
2. Jeśli nowy link jest prawym, dokonaj
rotacji w lewo.

[SW-2018]

10


Zbalansowane drzewa wyszukiwań
Czerwono-czarne
drzewa BST
Wstawianie, wybrane
przykłady
Przypadek 2a.
Wstawienie do
drzewa z dokładnie
dwoma węzłami

[SW-2018]

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa
BST
Wstawianie, wybrane
przykłady
Przypadek 2b.
Wstawienie do jednego
węzła potrójnego:
1. Wstaw jak do
zwykłego drzewa BST,
nadaj kolor czerwony
odnośnikowi.
[SW-2018]

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa
BST
Wstawianie, wybrane
przykłady
Przypadek 2b.
Wstawienie do jednego
węzła potrójnego:
2. Dokonaj rotacji w
celu zbalansowania
poczwórnego
wierzchołka (jeśli
potrzebne).
[SW-2018]

11


15.06.2023

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa
BST
Wstawianie, wybrane
przykłady
Przypadek 2b.
Wstawienie do jednego
węzła potrójnego:
3. Odwróć kolory w
celu przekazania
odnośnika
czerwonego jeden
poziom wyżej
[SW-2018]

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa
BST
Wstawianie, wybrane
przykłady
Przypadek 2b.
Wstawienie do jednego
węzła potrójnego:
4. Dokonaj rotacji w
celu przeniesienia
czerwonego
odnośnika na lewo
(jeśli potrzebne).
[SW-2018]

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Wstawianie, wybrane przykłady
Przypadek 2b. Wstawienie do jednego węzła potrójnego

[SW-2018]

12


15.06.2023

Zbalansowane drzewa wyszukiwań
Czerwono-czarne drzewa BST
Wstawianie, wybrane przykłady
private Node put(Node h, Key key, Value val)
{
if (h == null) return new Node(key, val, RED);
int cmp = key.compareTo(h.key);
if (cmp < 0) h.left = put(h.left, key, val);
else if (cmp > 0) h.right = put(h.right, key, val);
else if (cmp == 0) h.val = val;
[SW-2018]

if (isRed(h.right) && !isRed(h.left)) h = rotateLeft(h);
if (isRed(h.left) && isRed(h.left.left)) h = rotateRight(h);
if (isRed(h.left) && isRed(h.right)) flipColors(h);
return h;
}

Zbalansowane drzewa wyszukiwań
Implementacja

WORST CASE
Wyszukanie

WORST CASE
Wstawienie

WORST CASE
Usuwanie

AVG CASE
Wyszukanie

AVG CASE
Wstawienie

AVG CASE
Usuwanie

Porównanie
kluczy

Przeszukiwanie
sekwencyjne w tablicy
symboli (lista powiązana
nieuporządkowana)

N

N

N

N/2

N

N/2

equals()

Przeszukiwanie binarne
w tablicy symboli
(tablica
uporządkowana)

log N

N

N

log N

N/2

N/2

compareTo()

Drzewa wyszukiwań
binarnych

N

N

N

1.39 log N

1.39 log N

𝑁

compareTo()

Drzewa 2-3
Czerwono-czarne BST

2 log N

2 log N

2 log N

1.00 log N

1.00 log N

1.00 log N

compareTo()

13

