Algorytmy i Struktury Danych
Dr hab. Dariusz Barbucha, prof. UMG
Katedra Systemów Informacyjnych
Uniwersytet Morski w Gdyni
III
#### Rekurencja

Rekurencja
• Rekurencja dotyczy sytuacji, w której funkcja wywołuje samą siebie w
celu rozwiązania pewnego problemu
• Każda definicja rekurencyjna potrzebuje przynajmniej jednego
przypadku bazowego (nie rekurencyjnego. Inaczej, algorytm może
nigdy się nie zatrzymać

1


Projektowanie algorytmów
Metoda „dziel i zwyciężaj”
Wiele ważnych algorytmów ma strukturę rekurencyjną, co oznacza, że
w celu rozwiązania problemu algorytm wywołuje sam siebie przy
rozwiązywaniu podobnych podproblemów.
W algorytmach tych często stosuje się metodę „dziel i zwyciężaj” (ang.
divide-and-conquer): problem jest dzielony na kilka mniejszych
podproblemów podobnych do początkowego problemu, problemy te są
rozwiązywane rekurencyjnie, a następnie rozwiązania wszystkich
podproblemów są łączone w celu utworzenia rozwiązania całego
problemu.

Projektowanie algorytmów
Metoda „dziel i zwyciężaj”
W metodzie „dziel i zwyciężaj” każdy poziom rekursji składa się z
następujących trzech etapów:
1. Dziel: Dzielimy problem na podproblemy.
2. Zwyciężaj: Rozwiązujemy podproblemy rekurencyjnie, chyba, że są
one małego rozmiaru i już nie wymagają zastosowania rekursji –
używamy wtedy bezpośrednich metod.
3. Połącz: Łączymy rozwiązania podproblemów, aby otrzymać
rozwiązanie całego problemu.

Rekurencja
Silnia

1,
𝑛=0
𝑛! = ቊ
𝑛 𝑛 − 1 !,
𝑛≥0

int silnia(int n)

int silnia(int n)

{

{
if (n==0)

if (n==0)

return 1;

return 1;

else

else

{

return n*silnia(n-1);

wynik = 1;
for (int i=1; i<=n; i++)

}

wynik = wynik*i;
return wynik;
}
}

2


Rekurencja
Potęga
int potega(int podst, int wykl)

int potega(int podst, int wykl)

{

{
int wynik=1;

if (wykl = 0)

for (int i=1; i<=wykl; i++)

return 1;

wynik = wynik*podst;

else

return wynik;
}

return podst*potega(podst, wykl-1;
}

Rekurencja
Suma elementów tablicy
int sumuj(int[] T, int od, int do)
{
int suma=0;
for (int i=od; i<=do; i++)
suma = suma + T[i];
return suma;
}

Rekurencja
Suma elementów tablicy
int sumuj(int[] T, int od, int do)

int sumuj( int[] T; int od, int do)

{

{
int suma=0;

if (od==do)

for (int i=od; i<=do; i++)

return T[od];

suma = suma + T[i];

else

return suma;
}

return T[od]+sumuj(T, od+1, do);
}

3


Rekurencja
• Wyrazy ciągu Fibonacciego
0,
𝑛=0
1,
𝑛=1
𝐹𝑛 = ቐ
𝐹𝑛−1 + 𝐹𝑛−2 ,
𝑛>1
• Wyszukiwanie binarne
• Sortowanie przez scalanie (mergersort)
-> do ćwiczeń własnych

Podsumowanie

4

