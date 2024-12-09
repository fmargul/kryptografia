# Opis algorytmów i zmiennych

## Generowanie klucza publicznego ECDH

##### Algorytmy:

- **Obliczanie pierwiastka modularnego** – Algorytm oblicza pierwiastek modularny z liczby `a mod p`, jeśli istnieje. Sprawdza istnienie pierwiastka przy użyciu symbolu Legendre’a, a dla specjalnych przypadków `p ≡ 3 mod 4` stosuje uproszczone formuły. W pozostałych przypadkach wykorzystuje algorytm Tonellego–Shanksa. Wykorzystywany m.in. do znajdowania punktów na krzywej eliptycznej.
- **Sprawdzanie przynależności punktu do krzywej** – Algorytm weryfikuje, czy podany punkt `(x, y)` spełnia równanie krzywej `y^2 ≡ x^3 + ax + b mod p`.
- **Znajdowanie najbliższej liczby pierwszej** – Algorytm szuka pierwszej liczby pierwszej większej od `n`, korzystając z testu pierwszości Millera-Rabina.
- **Rozszerzony algorytm Euklidesa** – wyznaczanie największego wspólnego dzielnika dwóch liczb naturalnych (wykorzystywany do odnajdywanie odwrotności modularnej).
- **Dodawanie punktów na krzywej eliptycznej** – Algorytm dodający dwa punkty `P` i `Q` na krzywej eliptycznej. Oblicza współczynnik nachylenia `s` (dla `P = Q` stosuje inne wzory niż dla `P ≠ Q` i wylicza nowe współrzędne punktu `R = P + Q`).
- **Metoda podwajania i dodawania (Double-and-Add)** – Optymalna metoda mnożenia punktu `G` przez skalar `k` na krzywej eliptycznej. Wykorzystuje binarną reprezentację `k`, iteracyjnie podwajając i dodając punkty.
- **Walidacja danych** - Algorytmy realizujące wyznaczanie i walidację kluczy w protokole wymiany klucza ECDH.

##### Dane:

- **Parametry krzywej:**

  - **Moduł `p`:** Liczba pierwsza definiująca pole skończone.
  - **Współczynniki `a` i `b`:** Parametry równania krzywej eliptycznej `y^2 ≡ x^3 + ax + b mod p`.
  - **Generator `(X, Y)`:** Punkt bazowy krzywej.

- **Opcje klucza prywatnego:**

  - **Klucz prywatny `A`:** Losowo wybrana liczba całkowita.
  - **Nazwy standardowych krzywych:** Możliwość wyboru predefiniowanej krzywej, np. „NIST256p” lub „NIST384p”.

##### Walidacja poprawności danych:

Podczas ręcznego wprowadzania danych, system weryfikuje:

1. Czy wszystkie wymagane dane zostały podane.
2. Czy liczba `p` jest liczbą pierwszą.
3. Czy liczba `a` zawiera się w przedziale `1 < a < p`.
4. Czy liczba `b` zawiera się w przedziale `1 < b < p`.
5. Czy punkt o podanych współrzędnych `(X, Y)` należy do krzywej o rónaniu `y^2 ≡ x^3 + ax + b mod p`.
6. Czy liczba `A` zawiera się w przedziale `1 < A < p`.

### Opis zmiennych

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych przez kalkulator.

| Zmienna  | Typ   | Opis                                                                                                                       |
| -------- | ----- | -------------------------------------------------------------------------------------------------------------------------- |
| `p`      | `int` | Moduł krzywej eliptycznej (liczba pierwsza definiująca pole skończone).                                                    |
| `a`      | `int` | Współczynnik `a` krzywej eliptycznej `y^2 ≡ x^3 + ax + b mod p`.                                                           |
| `b`      | `int` | Współczynnik `b` krzywej eliptycznej `y^2 ≡ x^3 + ax + b mod p`.                                                           |
| `X`, `Y` | `int` | Współrzędne generatora na krzywej eliptycznej.                                                                             |
| `A`      | `int` | Prywatny klucz użytkownika (losowa liczba).                                                                                |
| `curve`  | `str` | Nazwa standardowej krzywej eliptycznej, np. "NIST256p", "NIST384p" za pomocą której można wygenerować dane do kalkulatora. |

---

## Generowanie klucza sesji ECDH

##### Algorytmy:

- **Obliczanie pierwiastka modularnego** – Algorytm oblicza pierwiastek modularny z liczby `a mod p`, jeśli istnieje. Sprawdza istnienie pierwiastka przy użyciu symbolu Legendre’a, a dla specjalnych przypadków `p ≡ 3 mod 4` stosuje uproszczone formuły. W pozostałych przypadkach wykorzystuje algorytm Tonellego–Shanksa. Wykorzystywany m.in. do znajdowania punktów na krzywej eliptycznej.
- **Sprawdzanie przynależności punktu do krzywej** – Algorytm weryfikuje, czy podany punkt `(x, y)` spełnia równanie krzywej `y^2 ≡ x^3 + ax + b mod p`.
- **Test Millera-Rabina** – probabilistyczny test pierwszości.
- **Rozszerzony algorytm Euklidesa** – wyznaczanie największego wspólnego dzielnika dwóch liczb naturalnych (wykorzystywany do odnajdywanie odwrotności modularnej).
- **Dodawanie punktów na krzywej eliptycznej** – Algorytm dodający dwa punkty `P` i `Q` na krzywej eliptycznej. Oblicza współczynnik nachylenia `s` (dla `P = Q` stosuje inne wzory niż dla `P ≠ Q` i wylicza nowe współrzędne punktu `R = P + Q`).
- **Metoda podwajania i dodawania (Double-and-Add)** – Optymalna metoda mnożenia punktu `G` przez skalar `k` na krzywej eliptycznej. Wykorzystuje binarną reprezentację `k`, iteracyjnie podwajając i dodając punkty.
- **Walidacja danych** - Algorytmy realizujące wyznaczanie i walidację kluczy w protokole wymiany klucza ECDH.

##### Dane:

- **Parametry krzywej:**

  - **Moduł `p`:** Liczba pierwsza definiująca pole skończone.
  - **Współczynniki `a` i `b`:** Parametry równania krzywej eliptycznej `y^2 ≡ x^3 + ax + b mod p`.
  - **Klucz publiczny `(X, Y)`:** Punkt krzywej.

- **Opcje klucza prywatnego:**

  - **Klucz prywatny `A`:** Wygenerowany wcześniej klucz prywatny.

##### Walidacja poprawności danych:

Podczas ręcznego wprowadzania danych, system weryfikuje:

1. Czy wszystkie wymagane dane zostały podane.
2. Czy liczba `p` jest liczbą pierwszą.
3. Czy liczba `a` zawiera się w przedziale `1 < a < p`.
4. Czy liczba `b` zawiera się w przedziale `1 < b < p`.
5. Czy punkt o podanych współrzędnych `(X, Y)` należy do krzywej o rónaniu `y^2 ≡ x^3 + ax + b mod p`.
6. Czy liczba `A` zawiera się w przedziale `1 < A < p`.

### Opis zmiennych

Poniżej przedstawiono szczegółowy opis zmiennych przyjmowanych przez kalkulator.

| Zmienna  | Typ   | Opis                                                                    |
| -------- | ----- | ----------------------------------------------------------------------- |
| `p`      | `int` | Moduł krzywej eliptycznej (liczba pierwsza definiująca pole skończone). |
| `a`      | `int` | Współczynnik `a` krzywej eliptycznej `y^2 ≡ x^3 + ax + b mod p`.        |
| `b`      | `int` | Współczynnik `b` krzywej eliptycznej `y^2 ≡ x^3 + ax + b mod p`.        |
| `X`, `Y` | `int` | Współrzędne oytzymanego klucza publicznego na krzywej eliptycznej.      |
| `A`      | `int` | Prywatny klucz użytkownika (losowa liczba).                             |

---

## Protokół Diffiego-Hellmana

Projekt implementuje algorytm Diffie-Hellmana do wymiany kluczy kryptograficznych. Zawiera funkcjonalności umożliwiające generowanie i walidację danych kryptograficznych, takich jak liczby pierwsze, generator grupy, klucze prywatne, klucze publiczne oraz wspólny sekret. System wspiera zarówno automatyczne generowanie danych, jak i ich ręczne wprowadzanie z walidacją poprawności.

---

#### Generowanie klucza publicznego, według protokołu Diffiego-Hellmana

##### Algorytmy:

- **Algorytm modularnego potęgowania** – szybkie potęgowanie w ciele skończonym.
- **Test Millera-Rabina** – probabilistyczny test pierwszości.
- **Generowanie bezpiecznej liczby pierwszej** – liczba `p` o postaci `p = 2q + 1`, gdzie `q` jest liczbą pierwszą.
- **Generowanie generatora `g`** – wybór elementu generującego grupę w ciele skończonym modulo `p`.
- **Walidacja danych wejściowych** – sprawdzenie poprawności liczb i kluczy.

##### Dane:

- **Rozmiary liczb:**

  - **Liczba pierwsza `p`:** Możliwość wyboru z predefiniowanych liczb pierwszych (np. 1024-bit, 2048-bit, 3072-bit, 4096-bit) lub podanie własnej liczby.
  - **Generator `g`:** Losowy element grupy, spełniający kryteria generatora w grupie modulo `p`.
  - **Klucz prywatny:** Losowana liczba w zakresie `[1, p-2]`.

- **Opcje użytkownika:**

  - **Ręczne wprowadzanie danych:** Użytkownik może podać własne wartości liczb `p`, `g` oraz klucza prywatnego. Dane są walidowane pod kątem poprawności.
  - **Automatyczne generowanie danych:** System umożliwia automatyczne wygenerowanie `p`, `g` oraz klucza prywatnego. Dodatkowo generowany jest losowy klucz publiczny drugiej strony dla celów testowych.

##### Walidacja poprawności danych:

Podczas ręcznego wprowadzania danych, system weryfikuje:

1. Czy liczba `p` jest liczbą pierwszą oraz ma postać `p = 2q + 1`.
2. Czy liczba `g` jest poprawnym generatorem grupy modulo `p`.
3. Czy klucz prywatny mieści się w zakresie `[1, p-2]`.

##### Generowane wartości:

Podczas generowania danych automatycznie obliczane są następujące wartości:

- **Liczba `p`** – liczba pierwsza spełniająca kryteria bezpieczeństwa.
- **Generator `g`** – poprawny generator grupy modulo `p`.
- **Klucz prywatny** – losowa liczba z zakresu `[1, p-2]`.
- **Klucz publiczny** – obliczony z wzoru `g^(private_key) % p`.
- **Losowy klucz publiczny drugiej strony** – generowany losowo do testowania wymiany kluczy.

##### Opis zmiennych:

| Zmienna            | Typ   | Opis                                                    |
| ------------------ | ----- | ------------------------------------------------------- |
| `p`                | `int` | Liczba pierwsza definiująca grupę modulo.               |
| `g`                | `int` | Generator grupy modulo `p`.                             |
| `private_key`      | `int` | Klucz prywatny użytkownika, losowana liczba `[1, p-2]`. |
| `public_key`       | `int` | Klucz publiczny obliczony z `p`, `g` i `private_key`.   |
| `other_public_key` | `int` | Losowy klucz publiczny drugiej strony.                  |

---

#### Obliczanie wspólnego sekretu, według protokołu Diffiego-Hellmana

##### Algorytmy:

- **Modularne potęgowanie** – obliczenie wspólnego sekretu jako `other_public_key^(private_key) % p`.
- **Walidacja danych wejściowych** – sprawdzenie poprawności liczb i kluczy.

##### Dane:

- **Rozmiary liczb:**

  - Liczba `p` oraz klucze prywatny i publiczny muszą być spójne z wcześniejszymi danymi.

- **Opcje użytkownika:**

  - **Ręczne wprowadzanie danych:** Użytkownik może podać liczbę `p`, klucz publiczny partnera i swój klucz prywatny, aby obliczyć wspólny sekret.

##### Walidacja poprawności danych:

Podczas ręcznego wprowadzania danych, system sprawdza:

1. Czy liczba `p` jest liczbą pierwszą oraz ma postać `p = 2q + 1`.
2. Czy klucz publiczny partnera mieści się w zakresie `[1, p-1]`.
3. Czy klucz prywatny użytkownika mieści się w zakresie `[1, p-2]`.

##### Generowane wartości:

Podczas obliczania wspólnego sekretu generowane są następujące dane:

- **Wspólny sekret** – obliczony z wzoru `other_public_key^(private_key) % p`.

##### Opis zmiennych:

| Zmienna            | Typ   | Opis                                      |
| ------------------ | ----- | ----------------------------------------- |
| `p`                | `int` | Liczba pierwsza definiująca grupę modulo. |
| `other_public_key` | `int` | Klucz publiczny partnera.                 |
| `private_key`      | `int` | Klucz prywatny użytkownika.               |
| `shared_secret`    | `int` | Wspólny sekret obliczony z danych.        |

---

## Dokumentacja funkcji modularnego potęgowania

#### Funkcja: `modular_exponentiation`

Implementacja szybkiego potęgowania modularnego pozwalająca efektywnie obliczyć wartość `base^exp % mod`. Jest to kluczowa operacja w algorytmach kryptograficznych, takich jak Diffie-Hellman.

##### Parametry wejściowe:

- **`base`** (`int`): Podstawa potęgowania.
- **`exp`** (`int`): Wykładnik potęgowania.
- **`mod`** (`int`): Moduł, względem którego obliczana jest reszta.

##### Zwracana wartość:

- **`result`** (`int`): Wynik obliczeń `base^exp % mod`.

##### Działanie funkcji:

1. Inicjalizuje wynik jako `1`.
2. Redukuje podstawę modulo: `base = base % mod`.
3. Wykorzystuje metodę "kwadratowania i mnożenia":
   - Jeśli wykładnik jest nieparzysty, wynik jest mnożony przez podstawę i redukowany modulo.
   - Podstawa jest podnoszona do kwadratu i redukowana modulo.
   - Wykładnik jest dzielony przez 2 (całkowita część).
4. Zwraca wynik.

##### Złożoność obliczeniowa:

- **Czasowa**: `O(log(exp))`, dzięki redukcji wykładnika o połowę w każdej iteracji.
- **Pamięciowa**: `O(1)`, ponieważ wykorzystuje stałą ilość pamięci.

---

## Dokumentacja funkcji probabilistycznego testu pierwszości

#### Funkcja: `is_prime_by_probability`

Implementacja probabilistycznego testu pierwszości oparta na algorytmie Millera-Rabina. Funkcja ocenia, czy dana liczba `n` jest prawdopodobnie pierwsza, z uwzględnieniem zadanego poziomu dokładności.

##### Parametry wejściowe:

- **`n`** (`int`): Liczba, której pierwszość ma zostać oceniona.
- **`accuracy`** (`int`): Liczba prób, które zostaną przeprowadzone w celu zwiększenia pewności wyniku.

##### Zwracana wartość:

- **`result`** (`bool`): Wartość `True`, jeśli liczba jest prawdopodobnie pierwsza; `False`, jeśli liczba na pewno nie jest pierwsza.

##### Działanie funkcji:

1. Obsługuje przypadki brzegowe:
   - Jeśli `n ≤ 1`, zwraca `False`.
   - Jeśli `n` wynosi 2 lub 3, zwraca `True`.
   - Jeśli `n` jest parzysta, zwraca `False`.
2. Znajduje rozkład `n - 1` w postaci `2^s ⋅ d`, gdzie `d` jest liczbą nieparzystą:
   - Iteracyjnie dzieli `n - 1` przez `2`, zwiększając `s`, aż do uzyskania `d`.
3. Wykonuje `accuracy` prób losowych:
   - Losuje bazę `a` z przedziału `[2, n - 2]`.
   - Oblicza `x = a^d mod n`.
   - Jeśli `x` wynosi `1` lub `n - 1`, próba kończy się sukcesem i algorytm przechodzi do kolejnej próby.
   - W przeciwnym razie wykonuje `s - 1` kolejnych potęgowań modularnych `x^2^r mod n`, aby sprawdzić, czy `x` osiąga wartość `n - 1`.
   - Jeśli w żadnym kroku `x` nie osiągnie `n - 1`, liczba `n` jest uznawana za złożoną, a funkcja zwraca `False`.
4. Jeśli wszystkie próby zakończą się sukcesem, liczba jest uznawana za prawdopodobnie pierwszą i funkcja zwraca `True`.

##### Złożoność obliczeniowa:

- **Czasowa**: `O(accuracy*log(n))`.
- **Pamięciowa**: `O(1)`, ponieważ wykorzystuje stałą ilość pamięci.

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

## Dokumentacja funkcji deszyfrującej wykorzystującej chińskie twierdzenie o resztach

#### Funkcja: `chinese_remainder_theorem_decryption`

Implementacja deszyfrowania przy użyciu chińskiego twierdzenia o resztach, według którego dla dowolnych parami względnie pierwszych liczb naturalnych _n<sub>1</sub>_,_n<sub>2</sub>_,...,_n<sub>k</sub>_ oraz dowolnych liczb całkowitych _y<sub>1</sub>_,_y<sub>2</sub>_,...,_y<sub>k</sub>_ istnije liczba całkowita _x<sub></sub>_, spełniająca układ kongruencji

_x ≡ a<sub>1</sub> (mod m<sub>1</sub>)_

_x ≡ a<sub>2</sub> (mod m<sub>2</sub>)_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⋮

_x ≡ a<sub>k</sub> (mod m<sub>k</sub>)_

##### Parametry wejściowe:

- **`m`** (`int`): Blok wiadomości do odszyfrowania.
- **`p`** (`int`): Składowa `p` klucza prywatnego.
- **`q`** (`int`): Składowa `q` klucza prywatnego.
- **`d`** (`int`): Współczynnik `d` klucza prywatnego.

##### Zwracana wartość:

- **`msg`** (`int`): Odszyfrowany blok wiadomości

##### Działanie funkcji:

1. Obliczenie wartości `dp` oraz `dq`, gdzie:
   - `dp = d (mod p-1)`.
   - `dq = d (mod q-1)`.
   - Wykładniki te pozwalają zmniejszyć ilość obliczeń w modularnej potędze, co przyspiesza deszyfrowanie
2. Obliczenie częściowych wyników deszyfrowania `m1` i `m2`, gdzie:
   - `m1 = m^dp mod(p)`.
   - `m1 = m^dq mod(q)`.
3. Znalezienie odwrotności modularnej liczby `q` w modulo `p`, jako `q_inv`.
4. Wyliczenie odszyfrowanego bloku ze wzoru:
   - `msg = m2 + h * q`, gdzie:
     - `h = (q_inv * (m1-m2)) (mod p)`.
5. Zwrócenie odszyfrowanego bloku.

##### Złożoność obliczeniowa:

- **Czasowa**: `O(k^3)`.
- **Pamięciowa**: `O(k)`.

---
