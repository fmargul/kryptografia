# Opis algorytmów i zmiennych

## Generowanie klucza publicznego ECDH

Poniżej znajduje się opis funkcji, ich zastosowania oraz wykorzystywanych algorytmów.

### Wykorzystane algorytmy:

- Algorytm obliczający pierwiastek modularny z liczby (`a` mod `p`), jeżeli istnieje. Wykorzystuje symbol Legendre'a, by sprawdzić, czy pierwiastek istnieje. W szczególnych przypadkach, takich jak (`p` ≡ `3` mod `4`), stosuje uproszczone formuły. Dla bardziej ogólnych przypadków wykorzystuje algorytm Tonellego–Shanksa. Stosowany do poszukiwania punktów na krzywej.

- Algorytm sprawdzający, czy podany punkt należy do krzywej.

- Algorytm znajdujący najbliższą większą liczbę pierwszą od `n` przy użyciu testu Millera-Rabina. Sprawdza kolejne liczby (`n+1`, `n+2`, `...`) aż znajdzie pierwszą liczbę pierwszą.

- Algorytm dodający dwa punkty `P` i `Q` na krzywej eliptycznej. Oblicza współczynnik nachylenia `s` (dla `P` = `Q` stosuje inne wzory niż dla `P` ≠ `Q` i wylicza nowe współrzędne punktu `R` = `P` + `Q`).

- Algorytm metody podwajania i dodawania (ang. _Double-and-Add_) do obliczania mnożenia punktu `G` przez skalar `k` na krzywej eliptycznej. Przekształca `k` na postać binarną i iteracyjnie podwaja/dodaje punkt.

- Algorytmy związane z wyliczaniem i walidacją ECDH.

### Opis zmiennych

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych przez kalkulator.

| Zmienna  | Typ   | Opis                                                                                                                       |
| -------- | ----- | -------------------------------------------------------------------------------------------------------------------------- |
| `p`      | `int` | Moduł krzywej eliptycznej (liczba pierwsza definiująca pole skończone).                                                    |
| `a`      | `int` | Współczynnik `a` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`.                                                   |
| `b`      | `int` | Współczynnik `b` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`.                                                   |
| `X`, `Y` | `int` | Współrzędne generatora na krzywej eliptycznej.                                                                             |
| `A`      | `int` | Prywatny klucz użytkownika (losowa liczba).                                                                                |
| `curve`  | `str` | Nazwa standardowej krzywej eliptycznej, np. "NIST256p", "NIST384p" za pomocą której można wygenerować dane do kalkulatora. |

---

## Generowanie klucza sesji ECDH

Poniżej znajduje się opis funkcji, ich zastosowania oraz wykorzystywanych algorytmów.

### Wykorzystane algorytmy:

- Algorytm sprawdzający, czy podany punkt należy do krzywej.

- Algorytm sprawdzający, czy podana liczba jest pierwsza z wykorzystaniem testu Millera-Rabina.

- Algorytm dodający dwa punkty `P` i `Q` na krzywej eliptycznej. Oblicza współczynnik nachylenia `s` (dla `P` = `Q` stosuje inne wzory niż dla `P` ≠ `Q` i wylicza nowe współrzędne punktu `R` = `P` + `Q`).

- Algorytm metody podwajania i dodawania (ang. _Double-and-Add_) do obliczania mnożenia punktu `G` przez skalar `k` na krzywej eliptycznej. Przekształca `k` na postać binarną i iteracyjnie podwaja/dodaje punkt.

- Algorytmy związane z wyliczaniem i walidacją ECDH.

### Opis zmiennych

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych przez kalkulator.

| Zmienna  | Typ   | Opis                                                                     |
| -------- | ----- | ------------------------------------------------------------------------ |
| `p`      | `int` | Moduł krzywej eliptycznej (liczba pierwsza definiująca pole skończone).  |
| `a`      | `int` | Współczynnik `a` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`. |
| `b`      | `int` | Współczynnik `b` krzywej eliptycznej `y^2` ≡ `x^3` + `ax` + `b` mod `p`. |
| `X`, `Y` | `int` | Współrzędne oytzymanego klucza publicznego na krzywej eliptycznej.       |
| `A`      | `int` | Prywatny klucz użytkownika (losowa liczba).                              |

---

## Protokół Diffiego-Hellmana

Projekt implementuje algorytm Diffie-Hellmana do wymiany kluczy kryptograficznych. Zawiera funkcjonalności umożliwiające generowanie i walidację danych kryptograficznych, takich jak liczby pierwsze, generator grupy, klucze prywatne, klucze publiczne, oraz wspólny sekret. System wspiera zarówno generowanie danych, jak i ich ręczne wprowadzanie z walidacją poprawności.

#### Generowanie klucza publicznego, według protokołu Diffiego-Hellmana

##### Algorytmy:

- **Algorytm modularnego potęgowania** – szybkie potęgowanie w ciele skończonym.
- **Test Millera-Rabina** – probabilistyczny test pierwszości.
- **Generowanie bezpiecznej liczby pierwszej** – liczba `p` o postaci `p = 2q + 1`, gdzie `q` jest liczbą pierwszą.
- **Generowanie generatora `g`** – wybór elementu generującego grupę w ciele skończonym modulo `p`.
- **Walidacja danych wejściowych** – sprawdzenie poprawności liczb i kluczy.

##### Dane:

- **Rozmiary liczb:**

  - **Liczba pierwsza `p`:** Domyślnie generowana o długości **256 bitów** (możliwość dostosowania długości - wpływa to na szybkość).
  - **Generator `g`:** Losowy element grupy, spełniający kryteria generatora w grupie modulo `p`.
  - **Klucz prywatny:** Losowana liczba w zakresie `[1, p-2]`.

- **Opcje użytkownika:**
  - **Ręczne wprowadzanie danych:** Użytkownik może podać własne wartości liczb `p`, `g` oraz klucza prywatnego. Dane są walidowane pod kątem poprawności.
  - **Automatyczne generowanie danych:** Wartości `p`, `g` oraz klucza prywatnego mogą zostać wygenerowane automatycznie.

##### Walidacja poprawności danych:

Podczas ręcznego wprowadzania danych, system weryfikuje:

1. Czy liczba `p` jest liczbą pierwszą oraz ma postać `p = 2q + 1`.
2. Czy liczba `g` jest poprawnym generatorem grupy modulo `p`.
3. Czy klucz prywatny mieści się w zakresie `[1, p-2]`.

##### Opis zmiennych:

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych i obliczanych przez kalkulator.
| Zmienna | Typ | Opis |
|---------------|-------|-------------------------------------------------------|
| `p` | `int` | Liczba pierwsza definiująca grupę modulo. |
| `g` | `int` | Generator grupy modulo `p`. |
| `private_key` | `int` | Klucz prywatny użytkownika, losowa liczba `[1, p-2]`. |
| `public_key` | `int` | Klucz publiczny obliczony z `p`, `g` i `private_key`. |

---

#### Obliczanie wspólnego sekretu, według protokołu Diffiego-Hellmana

##### Algorytmy:

- **Modularne potęgowanie** – obliczenie wspólnego sekretu jako $ \text{partner's public key}^{\text{private key}} \mod p $.
- **Walidacja danych wejściowych** – sprawdzenie poprawności liczb i kluczy.

##### Dane:

- **Rozmiary liczb:**

  - Liczby `p` i `g` oraz klucze prywatne i publiczne muszą być spójne z wcześniejszymi danymi.

- **Opcje użytkownika:**
  - **Ręczne wprowadzanie danych:** Użytkownik może podać liczby `p`, `g`, klucz publiczny partnera i swój klucz prywatny, aby obliczyć wspólny sekret.
  - **Automatyczne generowanie danych:** System może automatycznie wygenerować dane, takie jak liczby `p`, `g`, klucz publiczny partnera i klucz prywatny.

##### Walidacja poprawności danych:

Podczas ręcznego wprowadzania danych, system sprawdza:

1. Czy liczba `p` jest liczbą pierwszą oraz ma postać `p = 2q + 1`.
2. Czy liczba `g` jest poprawnym generatorem grupy modulo `p`.
3. Czy klucz publiczny partnera mieści się w zakresie `[1, p-1]`.
4. Czy klucz prywatny użytkownika mieści się w zakresie `[1, p-2]`.

##### Opis zmiennych:

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych i obliczanych przez kalkulator.
| Zmienna | Typ | Opis |
|-----------------------|-------|-------------------------------------------------|
| `p` | `int` | Liczba pierwsza definiująca grupę modulo. |
| `g` | `int` | Generator grupy modulo `p`. |
| `partners_public_key`| `int` | Klucz publiczny partnera. |
| `private_key` | `int` | Klucz prywatny użytkownika. |
| `shared_secret` | `int` | Wspólny sekret obliczony z danych. |

---

## Generowanie par kluczy RSA

##### Algorytmy:

- **Test Millera-Rabina** – probabilistyczny test pierwszości.
- **Rozszerzony algorytm Euklidesa** – wyznaczanie największego wspólnego dzielnika dwóch liczb naturalnych (wykorzystywany do odnajdywanie odwrotności modularnej).

##### Dane:

- **Rozmiary liczb:**

  - **Liczba pierwsze `p` i `q`:** generowane o długości **512 bitów**.
  - **Współczynnik klucza publicznego `e`:** generowany o długości **N-1 bitów**, gdzie **N** to długość bitowa wartości `φ(n)`, czyli tocjenta iloczynu liczb `p` i `q`.

- **Opcje użytkownika:**
  - **Ręczne wprowadzanie danych:** Użytkownik może podać własne wartości liczb `p`, `q` oraz `e`. Dane są walidowane pod kątem poprawności.
  - **Automatyczne generowanie danych:** Wartości `p`, `q` oraz `e` mogą zostać wygenerowane automatycznie.

##### Walidacja poprawności danych:

Podczas ręcznego wprowadzania danych, system weryfikuje:

1. Czy wszystkie wymagane dane zostały podane.
2. Czy liczba `p` jest liczbą pierwszą.
3. Czy liczba `q` jest liczbą pierwszą.
4. Czy iloczyn liczb `p` i `q` jest większy lub równy 256 - wymagane aby móc zaszyfrować wiadomość tekstową.
5. Czy liczba `e` jest liczbą pierwszą, zawiera się w przedziale `(1 < e < φ(n))`, gdzie `n=p\*q`, a także jest względnie pierwsza z `φ(n)`

##### Opis zmiennych:

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych i obliczanych przez kalkulator.
| Zmienna | Typ | Opis |
|---------------|-------|-------------------------------------------------------------------------------|
| `p` | `int` | Liczba pierwsza, będąca pierwszym składnikiem iloczynu `n`. |
| `q` | `int` | Liczba pierwsza, będąca drugim składnikiem iloczynu `n`. |
| `e` | `int` | Współczynnik klucza publicznego. |
| `n` | `int` | Iloczyn liczb pierwszych `p` i `q` |
| `d` | `int` | Współczynnik klucza prywatnego, odwrotność modularna liczby `e` |

---

## Szyfrowanie wiadomości przy użyciu RSA

##### Algorytmy:

- **Podział wiadomości na bloki oraz konwersja ich na postać liczbową:** – rozmiar bloku uzależniony od długości klucza, jest równy **log<sub>2</sub>(`n`)/8**, gdzie `n` to składnik klucza publicznego.
- **Potęgowanie modularne:** – do wydajnego obliczania zaszyfrowanych bloków.
- **Konwersja zaszyfrowanych bloków na postać tekstową:** lista zaszyfrowanych bloków zostaje przekształcona do formatu JSON, a następnie zakodowana w base64.

##### Dane:

- **Opcje użytkownika:**
  - **Wprowadzanie składowych klucza publicznego:** Użytkownik podaje wartości składowych `e` oraz `n`.
  - **Wprowadzenie wiadomości do zaszyfrowania:** Użytkownik wprowadza wiadomość.

##### Walidacja poprawności danych:

Podczas wprowadzania danych, system weryfikuje:

1. Czy wszystkie wymagane dane zostały podane.
2. Czy `n` jest różne od 0, celem uniknięcia błedu spowodowanego dzieleniem przez 0.
3. Czy `n` jest większe lub równe 256, celem uniknięcia błędu spowodowanego ustawieniem rozmiaru bloku na 0.

Reszta walidacji pominięta, zakładamy uprzednie wygenerowanie zwalidowanego klucza.

##### Opis zmiennych:

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych i obliczanych przez kalkulator.
| Zmienna | Typ | Opis |
|---------------|-------|-------------------------------------------------------------------------------|
| `e` | `int` | Współczynnik klucza publicznego. |
| `n` | `int` | Iloczyn liczb pierwszych `p` i `q` |
| `msg` | `string` | Treść wiadomości do zaszyfrowania |
| `encrypted` | `string` | Zaszyfrowana wiadomość w formacie base64 |

---

## Deszyfrowanie wiadomości przy użyciu RSA

##### Algorytmy:

- **Dekodowanie zaszyfrowanej wiadomości na postać blokową:** – Zaszyfrowana wiadomość w postaci base64 zostaje odkodowana do formatu JSON, a następnie w pierwotną postać listy zaszyfrowanych bloków. W przypadku danych uszkodzonych (błąd dekodowania base64 lub JSON), użytkownik otrzymuje informacje o użytkownik otrzymuje informacje o uszkodzonej zaszyfrowanej wiadomości.
- **Deszyfrowanie z zastosowaniem chińskiego twierdzenia o resztach:** - Odszyfrowywanie zostaje znacząco przyspieszone.
- **Potęgowanie modularne:** – wykorzystywane przez chińskie twierdzenie o resztach.
- **Rozszerzony algorytm Euklidesa** – wyznaczanie największego wspólnego dzielnika dwóch liczb naturalnych (wykorzystywany do odnajdywanie odwrotności modularnej w ramach chińskiego twierdzenia o resztach).
- **Przekształcanie odszyfrowanych bloków na postać tekstową i ich konkatenacja** - następuje złączenie fragmentów odszyfrowanej wiadomości w jedną całość. W przypadku nieudanej konwersji na tekst, użytkownik otrzymuje informację o błędnym kluczu lub błędnie zaszyfrowanej wiadomości.

##### Dane:

- **Opcje użytkownika:**
  - **Wprowadzanie składowych klucza prywatnego:** Użytkownik podaje wartości składowych `d`, `p` oraz `q`.
  - **Wprowadzenie wiadomości do odszyfrowania:** Użytkownik wprowadza zaszyfrowaną wiadomość.

##### Walidacja poprawności danych:

Podczas wprowadzania danych, system weryfikuje:

1. Czy wszystkie wymagane dane zostały podane.
2. Czy `p` oraz `q` są różne od 0, celem uniknięcia błedu spowodowanego dzieleniem przez 0.

Reszta walidacji pominięta, zakładamy uprzednie wygenerowanie zwalidowanego klucza.

##### Opis zmiennych:

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych i obliczanych przez kalkulator.
| Zmienna | Typ | Opis |
|---------------|-------|-------------------------------------------------------------------------------|
| `d` | `int` | Współczynnik klucza prywatnego. |
| `p` | `int` | Pierwsza składowa iloczynu `n` |
| `q` | `int` | Druga składowa iloczynu `n` |
| `msg` | `string` | Treść wiadomości do odszyfrowania |
| `decrypted` | `string` | Odszyfrowana wiadomość |

---
