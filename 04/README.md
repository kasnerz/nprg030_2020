# Cvičení č. 4 – 23.10.2020

## Algoritmizace

### Opravy kódu

**Příběh** 

Váš nadřízený vám dal za úkol opravit projekt po předchozím programátorovi, panu X. Pan X už ve firmě nepracuje a při prohlížení jeho kódů vám dochází proč. Jeho kódy totiž fungují pouze na první pohled – při spuštění na reálných datech se chovají nepředvídatelně, zamrzají nebo vracejí nesprávné výsledky :man_shrugging:

**Úkoly**

Najděte vstupy, pro které kód nefunguje, identifikujte chyby v implementaci a  funkce opravte.

1. V souboru [euclid_notfixed.py](euclid_notfixed.py) se nachází funkce `euclid_gcd(a, b)` pro výpočet nejvyššího společného dělitele čísel `a` a `b`. Funkce prochází unit testy, ale na určitých datech se zacyklí a nevrátí žádný výsledek. 
2. V souboru [eratosthenes_notfixed.py](eratosthenes_notfixed.py) se nachází funkce `eratosthenes(n)` pro výpočet všech prvočísel `<= n`. Funkce prochází unit testy, ale s většími vstupy je příliš pomalá a na určitých datech vrací špatný výsledek.

**Vysvětlivka**

*Funkce `assert` se používá pro kontrolu podmínky, která musí být vždy splněna. Pokud je výraz uvnitř funkce `assert` vyhodnocen na False, funkce vrátí `AssertionError`. Toho se využívá např. pro automatické testování.*


### Třídění

Doplňte do [šablony](quadratic_sorts_template.py) funkce `bubble_sort(l)`, `insertion_sort(l)` a `selection_sort(l)`. Vypisujte každou záměnu prvků v poli (např. "Vyměňuji 5 a 4"), částečně setříděné pole po každé iteraci, a vraťte kromě setříděného pole i celkový počet kroků vnitřního cyklu.

[Odkaz na animace](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)


## Rychlokurz na Git

*nepovinné, není součástí předmětu*

### Odkazy
- Příručka: https://git-scm.com/docs
- Podrobný tutorial (částečně i v češtině): https://git-scm.com/book/cs/v2
- Práce se samotným Githubem: https://guides.github.com/activities/hello-world/
- Cheatsheet: https://training.github.com/downloads/github-git-cheat-sheet/
- Jak nastavit zkratky `git st` apod.: https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases

### Základní příkazy
- založení nového projektu ve složce
```
git init
```

- přidání dosud nesledovaných souborů + změn v nich do staging area
```
git add SOUBOR1 SOUBOR2 (...)
```

- přidání změn ve všech sledovaných souborech do staging area
```
git add -u
```

- kontrola stavu repozitáře (informace o (ne)commitnutých změnách, (ne)sledovaných souborech apod.)
```
git status
```

- výpis změn ve staging area
```
git diff --staged
```

- výpis změn ve sledovaných souborech nepřidaných do staging area
```
git diff
```

- commit změn s popisem
```
git commit -m "Zde stručně a výstižně popisuji, co jsem v kódu změnil"
```

- zobrazení historie commitů
```
git log
```

- nastavení propojení se vzdáleným repozitářem např. na Githubu (stačí provést jednou, Github příkaz napoví)
```
git remote add origin <adresa_vzdáleného_repozitáře>
```

- odeslání změn do vzdáleného repozitáře
```
git push
```

- poprvé je potřeba určit, které větve si navzájem odpovídají (Git napoví), od té chvíle už stačí pouze `git push`
```
git push --set-upstream origin main
```

- stáhnutí změn ze vzdáleného repozitáře
```
git pull
```

## Programování
- viz [kód](lab04.py)