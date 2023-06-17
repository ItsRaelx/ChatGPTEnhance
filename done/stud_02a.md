Algorytmy i Struktury Danych
Dr hab. Dariusz Barbucha, prof. UMG
Katedra Systemów Informacyjnych
Uniwersytet Morski w Gdyni
II

Podstawowe struktury danych
Tablice, Listy powiązane (z dowiązaniami), Kolejki, Stosy, Wielozbiory

Struktury danych
Struktura danych – sposobu przechowywania i organizowania danych,
umożliwiający wykonywanie operacji na nich, jak dostęp do danych,
dodawanie, usuwanie, modyfikacja danych, itp.

1


Struktury danych
Struktury danych mogą być:
• Statyczne – nie zmieniają swojego rozmiaru ani struktury w trakcie
działania algorytmu, np.

• Tablica


• Dynamiczne – mogą zmieniać swój rozmiar i strukturę w trakcie
działania algorytmu, np.

• Lista
• Drzewo
• Graf
• …

Struktury danych
Struktury danych mogą być:
• Liniowe – struktury danych, których każdy element posiada swojego
poprzednika i następnika, z wyjątkami: pierwszy element nie posiada
poprzednika, a ostatni nie posiada następnika

• tablica
• lista z dowiązaniami
• stos
• kolejka


• Nieliniowe – bez cechy powyższej
• grafowe struktury danych
• drzewiaste struktury danych

Tablica
Tablica – jednorodna struktura danych pozwalająca przechowywać obiekty
tego samego typu, np. liczby całkowite, teksty, czy też bardziej złożone
obiekty, np. dane o studentach (NrAlbumu, Nazwisko, Imię, DataUrodzenia).
• Tablice mogą być:
• Jednowymiarowe (odp. wektora)
• Dwuwymiarowe (odp. macierzy)
• Wielowymiarowe

• Posiada deklarowany z góry stały rozmiar, np.
• tablica jednowymiarowa N liczb rzeczywistych double[] T = new double[N]
• tablica dwuwymiarowa MxN liczb całkowitych int[][] T = new int[M][N]
(przypadek: nie znamy z góry liczby elementów, które będą przechowywane w tablicy?)

2

Tablica
• Dostęp do danych swobodny, inaczej bezpośredni, poprzez indeks i =
0,…, N-1, np. T[4] – dostęp do piątego elementu
• Dodawanie elementu do tablicy – nie można elementu wstawić
bezpośrednio, np. T[5]=19, gdyż spowodowałoby to nadpisanie
elementu, zatem należy przesunąć elementy o jedną pozycję w
„prawo” (jednocześnie zwiększając rozmiar tablicy, ale czy zawsze?)
• Usuwanie elementu – wymaga przesunięcia elementów o jedną
pozycję w „lewo” (co z rozmiarem tablicy?)
• Zwykle kolejne elementy znajdują się w kolejnych komórkach pamięci
2

4

9

11

12

21

29

43

Lista z dowiązaniami
Lista z dowiązaniami, inaczej: lista powiązana (ang. linked list) –
liniowa, dynamiczna struktura danych, zbudowana z:
• Węzłów (ang. nodes), zawierających dane określonego typu
• Dowiązań (ang. links) łączących te węzły (referencje do węzłów)

…

Lista z dowiązaniami
Item –
typ sparametryzowany
Listy mogą być:
• jednokierunkowe (ang. singly-linked list) – występuje odnośnik
(referencja) do kolejnego węzła
private class Node
{
Item item;
Node next;

null
}

• dwukierunkowe (ang. doubly-linked list) – dodatkowo występuje
private class Node
odnośnik do węzła poprzedniego.
{

null

Item item;
Node next;
Node prev;

null
}

3


01.06.2023

Lista z dowiązaniami
Lista posiada dwa wyróżnione
wskaźniki:
• Głowę (ang. head) – wskazujący na początek listy, czyli na pierwszy
element (czasami oznaczany jako first)
• Ogon (ang. tail) – wskazujący na koniec listy, czyli na ostatni element
(czasami oznaczany jako last)
private class Node
{
Item item;
Node next;
}

null

Head (first)

Tail (last)

Lista z dowiązaniami

class LinkedList
{
Node head;
Node tail;
}

Lista jednokierunkowa

null

Head (first)

Tail (last)

private class Node
{
Item item;
Node next;
}

Lista z dowiązaniami
Listy mogą być również cykliczne (jedno- i dwukierunkowe).

null
private class Node
{
Item item;
Node next;
}

4


01.06.2023

Lista z dowiązaniami
Listy mogą być również posortowane lub nieposortowane.
Lista posortowana:
• kolejność elementów na liście jest zgodna z porządkiem na ich
kluczach;
• element o najmniejszym kluczu znajduje się na początku (w głowie
listy), o największym kluczu – na końcu (w jej ogonie).

Lista z dowiązaniami
• Lista nie zapewnia bezpośredniego dostępu do jej elementów, z
wyjątkiem pierwszego i ew. ostatniego (w przeciwieństwie do tablicy,
w której dostęp do każdego elementu jest możliwy bezpośrednio
przez jego indeks)
• Dostęp do elementów tablicy ma charakter sekwencyjny
• Implementacja listy może być:
• Tablicowa
• Wskaźnikowa

Lista z dowiązaniami
Lista jednokierunkowa, implementacja wskaźnikowa
• Opiera się na kolekcji powiązanych ze sobą obiektów określonego
typu utworzonych dynamicznie
• Faktycznie dynamiczna, ograniczona jedynie ilością dostępnej pamięci
• Kolejne elementy listy mogą być umieszczone w różnych miejscach
pamięci, niekoniecznie w kolejnych komórkach

5


01.06.2023

Lista z dowiązaniami
Lista jednokierunkowa, implementacja wskaźnikowa
null
first

Przykłady
a)
10

100

private class Node
{
Item item;
Node next;
}

null

1000

null

b)

„Warszawa”
„Gdańsk”

„Kraków”

„Olsztyn”

Lista z dowiązaniami
Lista jednokierunkowa,
implementacja wskaźnikowa
Zbudowanie listy z dowiązaniami

private class Node
{
Item item;
Node next;
}
[SW-2018]

Lista z dowiązaniami
Lista jednokierunkowa, implementacja wskaźnikowa
Operacje
• Wstawienie elementu:

• na początek listy,
• na koniec listy,
• w dowolne wskazane miejsce (za/przed wskazanym konkretnym elementem)

• Usuwanie elementu z listy (jak przy wstawianiu)
• Wyszukiwanie elementu w liście
• Znalezienie min/max elementu na liście
• Znalezienie poprzednika/następnika konkretnego elementu
• Sprawdzenie, czy lista jest pusta
• Podanie rozmiaru listy

6


01.06.2023

Lista z dowiązaniami
Lista jednokierunkowa,
implementacja wskaźnikowa
Wstawienie elementu na początek

private class Node
{
Item item;
Node next;
}
[SW-2018]

Lista z dowiązaniami
Lista jednokierunkowa,
implementacja wskaźnikowa
Wstawienie elementu na koniec

private class Node
{
Item item;
Node next;
}
[SW-2018]

Lista z dowiązaniami
Lista jednokierunkowa,
implementacja wskaźnikowa
Usunięcie elementu z początku

private class Node
{
Item item;
Node next;
}
[SW-2018]

7


01.06.2023

Lista przykład przykład przykład przykład przykład przykład przykład przykład przykład przykład przykład przykład przykład przykład
Lista
jednokierunkowa,
implementacja wskaźnikowa
Wstawianie i usuwanie elementów na innych pozycjach (może być
nieco trudniejsze, wskaż na czym polegają trudności, jeżeli faktycznie
istnieją?):
• Wstawienie nowego węzła przed/po danym elemencie
• Usuwanie ostatniego elementu z listy
• Usuwanie węzła leżącego przed/po danym elemencie

Lista z dowiązaniami
Lista jednokierunkowa, implementacja wskaźnikowa
Przechodzenie po liście a przechodzenie po tablicy, np. w celu
sprawdzenia, czy lista/tablica zawiera jakiś element:
Przechodzenie po liście
Node x = first;
while (x!=null)
{
// wykonaj operacje na x.item
x = x.next;
}

Lista z dowiązaniami
Lista jednokierunkowa, implementacja wskaźnikowa
Przechodzenie po liście a przechodzenie po tablicy, np. w celu
sprawdzenia, czy lista/tablica zawiera jakiś element:
Przechodzenie po liście

Przechodzenie po tablicy

for (Node x=first; x!=null; x=x.next)
{
// wykonaj operacje na x.item
}

for (int i=0; i<N; i++)
{
// wykonaj operacje na a[i]
}

8

Lista z dowiązaniami
Lista jednokierunkowa, implementacja wskaźnikowa
Generalnie, operacje typu wyszukiwanie elementu na liście nie są zbyt
efektywne gdyż:
• Mogą być wykonywane tylko sekwencyjnie, a zatem w najgorszym
przypadku wymagają przejrzenia całej listy
• Nie można efektywnie wykorzystać operacji typu przeszukiwania
binarnego znanego z tablic, zakładając, że lista jest posortowana
Ale
• Czy mając listę posortowaną można operacje wstawiania/usuwania
wykonać łatwiej (bardziej efektywnie) niż dla listy nieposortowanej?

Lista z dowiązaniami
Lista dwukierunkowa, implementacja wskaźnikowa
• Każdy element listy Node jest obiektem składającym się z pól: wartość
(klucz elementu), next oraz prev.
• Dla każdego elementu x na liście dwukierunkowej: x.next wskazuje na
jego następnik na liście, a x.prev wskazuje na jego poprzednik.

null

null

private class Node
{
Item item;
Node next;
Node prev;
}

Lista z dowiązaniami
Lista dwukierunkowa, implementacja wskaźnikowa
• Jeśli:
• x.prev == null, to element x nie ma poprzednika (jest pierwszym elementem
na liście - głowa tej listy).
• x.next == null, to element x nie ma następnika (jest ostatnim elementem na
liście - ogon tej listy).

private class Node
{
Item item;
Node next;
Node prev;
Tail (last) }

null

null
Head (first)

9

Lista z dowiązaniami
Lista dwukierunkowa, implementacja wskaźnikowa
Operacje
• Wstawienie elementu:

• na początek listy,
• na koniec listy,
• w dowolne wskazane miejsce (za/przed wskazanym konkretnym elementem)

• Usuwanie elementu z listy (jak przy wstawianiu)
• Wyszukiwanie elementu w liście
• Znalezienie min/max elementu na liście
• Znalezienie poprzednika/następnika konkretnego elementu
• Sprawdzenie, czy lista jest pusta
• Podanie rozmiaru listy

Lista z dowiązaniami
Lista dwukierunkowa, implementacja wskaźnikowa
Operacje
• Czy operacje te można wykonać łatwiej (bardziej efektywnie) niż dla
listy jednokierunkowej?
• Czy mając listę posortowaną można wykonać te operacje
łatwiej
(bardziej efektywnie) niż dla listy nieposortowanej?

Lista a tablica
Porównanie
Cecha

Tablica

Lista z dowiązaniami

Rozmiar

Statyczny, trzeba znać w czasie
inicjowania

Dynamiczny

Zmiana rozmiaru

Bardziej kosztowne

Mniej kosztowne

Operacje dostępu do danych

Dostęp bezpośredni

Dostęp sekwencyjny,
wymaga referencji

Operacje dostępu do danych związane z
przeglądaniem

Podobnie kosztowne

Podobnie kosztowne

Operacje modyfikujące strukturę
(wstawianie/usuwanie)

Bardziej kosztowne

Mniej kosztowne

Pamięć

Ok. MxN, gdzie M-pamięć dla
danej określonego typu, N –
rozmiar tablicy

Dodatkowy narzut
związany z pamięcią
dla wskaźników

10


01.06.2023

Lista a tablica
Porównanie złożoności
Operacja

Lista
jednokierunkowa

Lista
dwukierunkowa

###Znalezienie rozmiaru struktury

Tablica
O(1)

O(n)

O(n)

###Dostęp do elementu pierwszego/ostatniego

O(1)

O(1)

O(1)

###Dostęp do elementu innego niż pierwszy/ostatni

O(1)

O(n)

O(n)

###Dostęp do elementu następnego

O(1)

O(1)

O(1)

###Dostęp do elementu poprzedniego

O(1)

O(n)

O(1)

Wstawianie/usuwanie na początku

O(n)

O(1)

O(1)

Wstawianie/usuwanie na końcu

O(1)

O(1)

O(1)

Wstawianie/usuwanie za/przed wskazanym obiektem

O(n)

O(1)

O(1)

11

