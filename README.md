# Opis algorytmów i zmiennych

## Generowanie klucza publicznego ECDH
Poniżej znajduje się opis funkcji, ich zastosowania oraz wykorzystywanych algorytmów.

### Wykorzystane algorytmy:

- Algorytm obliczający pierwiastek modularny z liczby (`a` mod `p`), jeżeli istnieje. Wykorzystuje symbol Legendre'a, by sprawdzić, czy pierwiastek istnieje. W szczególnych przypadkach, takich jak (`p` ≡ `3` mod `4`), stosuje uproszczone formuły. Dla bardziej ogólnych przypadków wykorzystuje algorytm Tonellego–Shanksa. Stosowany do poszukiwania punktów na krzywej.

- Algorytm sprawdzający, czy podany punkt należy do krzywej.

- Algorytm znajdujący najbliższą większą liczbę pierwszą od `n` przy użyciu testu Millera-Rabina. Sprawdza kolejne liczby (`n+1`, `n+2`, `...`) aż znajdzie pierwszą liczbę pierwszą.

- Algorytm dodający dwa punkty `P` i `Q` na krzywej eliptycznej. Oblicza współczynnik nachylenia `s` (dla `P` = `Q` stosuje inne wzory niż dla `P` ≠ `Q` i wylicza nowe współrzędne punktu `R` = `P` + `Q`).

- Algorytm metody podwajania i dodawania (ang. *Double-and-Add*) do obliczania mnożenia punktu `G` przez skalar `k` na krzywej eliptycznej. Przekształca `k` na postać binarną i iteracyjnie podwaja/dodaje punkt.

- Algorytmy związane z wyliczaniem i walidacją ECDH.


### Opis zmiennych
Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych przez kalkulator.

| Zmienna | Typ        | Opis                                                                                                                                   |
|---------|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `p`     | `int`      | Moduł krzywej eliptycznej (liczba pierwsza definiująca pole skończone).                                                                 |
| `a`     | `int`      | Współczynnik `a` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`.                                                          |
| `b`     | `int`      | Współczynnik `b` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`.                                                                                                |
| `X`, `Y`| `int`      | Współrzędne generatora na krzywej eliptycznej.                                                                                             |
| `A`     | `int`      | Prywatny klucz użytkownika (losowa liczba).                                                                                             |
| `curve` | `str`      | Nazwa standardowej krzywej eliptycznej, np. "NIST256p", "NIST384p" za pomocą której można wygenerować dane do kalkulatora.                                                                     |

---

## Generowanie klucza sesji w ECDH
Poniżej znajduje się opis funkcji, ich zastosowania oraz wykorzystywanych algorytmów.

### Wykorzystane algorytmy:

- Algorytm sprawdzający, czy podany punkt należy do krzywej.

- Algorytm sprawdzający, czy podana liczba jest pierwsza z wykorzystaniem testu Millera-Rabina.

- Algorytm dodający dwa punkty `P` i `Q` na krzywej eliptycznej. Oblicza współczynnik nachylenia `s` (dla `P` = `Q` stosuje inne wzory niż dla `P` ≠ `Q` i wylicza nowe współrzędne punktu `R` = `P` + `Q`).

- Algorytm metody podwajania i dodawania (ang. *Double-and-Add*) do obliczania mnożenia punktu `G` przez skalar `k` na krzywej eliptycznej. Przekształca `k` na postać binarną i iteracyjnie podwaja/dodaje punkt.

- Algorytmy związane z wyliczaniem i walidacją ECDH.


### Opis zmiennych
Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych przez kalkulator.

| Zmienna | Typ        | Opis                                                                                                                                   |
|---------|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `p`     | `int`      | Moduł krzywej eliptycznej (liczba pierwsza definiująca pole skończone).                                                                 |
| `a`     | `int`      | Współczynnik `a` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`.                                                          |
| `b`     | `int`      | Współczynnik `b` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`.                                                                                                |
| `X`, `Y`| `int`      | Współrzędne oytzymanego klucza publicznego na krzywej eliptycznej.                                                                                             |
| `A`     | `int`      | Prywatny klucz użytkownika (losowa liczba).                                                                                             |

---