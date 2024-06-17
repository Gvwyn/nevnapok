# Magyar névnapok

*Egy minimális script, minimális függőségekkel, ami lekéri az összes névnapot, majd JSON formátumban elmenti.*

*Hasznos lehet bárkinek, aki egy statikus adatbázisból akarja lekérni a névnapokat.*

## Fájlok

``nevnapok.json`` (példa)

```json
{
    "1": {
        "1": [
            "Aglája",
            "Algernon",
            "Álmos",
            "Bazil",
            "Csoma",
            "Csombor",
            "Csomor",
            "Eufrozina",
            "Fruzsina",
            "Konkordia",
            "Odiló",
            "Ruzsinka",
            "Tóbiás",
            "Vazul"
        ],
        "..."
```

Ez a fájl teljes egésze elérhető [itt](https://github.com/Gvwyn/nevnapok/releases).

## Futtatás

### Előfeltételek

3 könyvtár, melyeket a következő paranccsal tudtok letölteni/csekkolni:

```bash
pip install requests beautifulsoup4
```

### Program futtatása

```bash
python nevnapok.py
```

Ez egy **nevnapok.json** fájlt fog generálni, ami az összes névnapot, dátum szerint tartalmazni fogja.

A forrás struktúrája miatt a nevek maguktól abécé sorrendben vannak.

## Források

[Wikipédia](https://hu.wikipedia.org/wiki/Magyar_n%C3%A9vnapok_list%C3%A1ja_bet%C5%B1rendben)
