# Fooocus Batch Processor

Automatikusan generál képeket TXT fájlokból beolvasott promptok alapján, 32-es batch-ekben.

## Telepítés

1. Klónozd le ezt a repository-t:
```bash
git clone https://github.com/[YOUR-USERNAME]/Fooocus.git
cd Fooocus
```

2. Telepítsd a függőségeket (ugyanaz, mint az eredeti Fooocus):
```bash
pip install -r requirements_versions.txt
```

## Használat

### 1. Készíts TXT fájlokat a promptokkal

Hozz létre egy `prompts` mappát (vagy használd a meglévőt), és helyezz bele TXT fájlokat:

```
prompts/
  ├── batch_001.txt
  ├── batch_002.txt
  └── batch_003.txt
```

Minden TXT fájl formátuma:
- **Egy sor = egy prompt**
- A `#`-tel kezdődő sorok megjegyzések (ignorálva)
- Üres sorok ignorálva

Példa (`prompts/my_prompts.txt`):
```
# Tájképek
a beautiful sunset over mountains, highly detailed, 8k
a serene forest with a waterfall, nature photography

# Állatok
a cute cat sitting on a windowsill, photorealistic
a majestic lion in the savanna, wildlife photography
```

### 2. Futtasd a batch processort

Alapértelmezett használat (32-es batch-ek, automatikus törlés):
```bash
python batch_processor.py
```

Egyéni beállítások:
```bash
# Kisebb batch méret (pl. 16)
python batch_processor.py --batch-size 16

# Ne törölje a TXT fájlokat
python batch_processor.py --keep-files

# Folyamatos mód (vár új fájlokra)
python batch_processor.py --continuous

# Egyéni prompts mappa
python batch_processor.py --prompts-dir my_custom_prompts
```

### 3. Találd meg a generált képeket

A képek az alapértelmezett Fooocus output mappában lesznek:
- Windows: `outputs/`
- Linux/Mac: `outputs/`

## Teszt fájlok létrehozása

Gyors teszteléshez használd a teszt script-et:

```bash
# 3 fájl, egyenként 10 prompttal
python create_test_prompts.py

# Egyéni beállítások
python create_test_prompts.py --num-files 5 --prompts-per-file 20
```

## Paraméterek

### batch_processor.py

| Paraméter | Leírás | Alapértelmezett |
|-----------|--------|-----------------|
| `--prompts-dir` | TXT fájlok mappája | `prompts` |
| `--output-dir` | Kimeneti mappa | Fooocus alapértelmezett |
| `--batch-size` | Képek száma batch-enként (max 32) | `32` |
| `--keep-files` | Ne törölje a feldolgozott TXT fájlokat | `False` |
| `--continuous` | Folyamatos mód (10 mp-enként ellenőriz) | `False` |

## Példák

### 1. Egyszerű batch generálás
```bash
# 1. Készíts egy TXT fájlt
echo "a beautiful cat" > prompts/test.txt
echo "a cute dog" >> prompts/test.txt

# 2. Futtasd
python batch_processor.py

# 3. A képek az outputs/ mappában lesznek
```

### 2. Nagy mennyiségű prompt feldolgozása
```bash
# 100 prompt, 32-es batch-ekben
python create_test_prompts.py --num-files 1 --prompts-per-file 100
python batch_processor.py
```

### 3. Folyamatos generálás
```bash
# Indítsd el folyamatos módban
python batch_processor.py --continuous

# Másik terminálban adj hozzá új TXT fájlokat
echo "new prompt 1" > prompts/new_batch.txt
echo "new prompt 2" >> prompts/new_batch.txt

# A processor automatikusan észreveszi és feldolgozza
```

## Google Colab használat

Nyisd meg a `fooocus_batch_colab.ipynb` notebookot Google Colab-ban:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[YOUR-USERNAME]/Fooocus/blob/main/fooocus_batch_colab.ipynb)

A notebook:
1. Telepíti a Fooocus-t
2. Lehetővé teszi TXT fájlok feltöltését
3. Futtatja a batch processort
4. Letölti a generált képeket

## Hibaelhárítás

### "No TXT files found"
- Ellenőrizd, hogy a `prompts/` mappa létezik
- Ellenőrizd, hogy vannak `.txt` fájlok benne

### "Error during generation"
- Ellenőrizd, hogy a Fooocus modellek letöltődtek
- Próbálj kisebb batch méretet (`--batch-size 16`)

### Memória problémák
- Csökkentsd a batch méretet: `--batch-size 8`
- Használj kisebb felbontást a Fooocus beállításokban

## Fejlesztés

Eredeti Fooocus dokumentáció: [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)

## Licenc

Ugyanaz, mint az eredeti Fooocus projekt.
