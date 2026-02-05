# Fooocus Batch Processor - Használati Útmutató

## ⚠️ FONTOS MEGJEGYZÉS

A `batch_processor.py` **NEM MŰKÖDIK** közvetlenül, mert a Fooocus `args_manager` modulja felülírja az argumentum kezelést.

## 🔧 Megoldások

### 1. Opció: Standalone Processor (Ajánlott Colab-hoz)

```bash
python standalone_batch_processor.py --prompts-dir prompts
```

**Mit csinál:**
- Beolvassa a TXT fájlokat
- Kilistázza a promptokat
- **NEM generál képeket** (csak listázza őket)

**Használat:**
1. Futtasd a scriptet
2. Másold ki a promptokat
3. Illeszd be őket a Fooocus web interface-be

### 2. Opció: Manuális Használat (Legegyszerűbb)

```bash
# 1. Indítsd el a Fooocus-t
python launch.py

# 2. Nyisd meg a böngészőben (általában http://127.0.0.1:7865)

# 3. Másold be a promptokat egyesével vagy használd a web interface-t
```

### 3. Opció: API-alapú Processor (Ha fut a Fooocus)

```bash
# 1. Terminál 1: Indítsd el a Fooocus-t
python launch.py

# 2. Terminál 2: Futtasd az API processort
python simple_batch_processor.py
```

## 📝 TXT Fájl Formátum

Mindhárom módszernél ugyanaz:

```txt
# Megjegyzés (ignorálva)
a beautiful sunset over mountains
a cute cat sitting on a windowsill

# Üres sorok ignorálva
a futuristic city with flying cars
```

## 🎯 Ajánlott Workflow Google Colab-hoz

### Colab Notebook Módosítás

A `fooocus_batch_colab.ipynb` 4. cellájában cseréld le:

```python
# RÉGI (nem működik):
!python batch_processor.py --batch-size 32

# ÚJ (működik):
!python standalone_batch_processor.py --keep-files
```

Majd:
1. A standalone processor kilistázza a promptokat
2. Másold ki őket
3. Használd a Fooocus web interface-t a generáláshoz

## 🔍 Miért nem működik a batch_processor.py?

A Fooocus `args_manager.py` modulja automatikusan betöltődik és felülírja az `argparse` működését. Ez azt jelenti, hogy amikor futtatod:

```bash
python batch_processor.py --batch-size 32
```

Az `args_manager` a Fooocus saját argumentumait várja (--listen, --port, stb.), nem a mi batch processor argumentumainkat.

## ✅ Megoldás: Használd a standalone_batch_processor.py-t

Ez a verzió:
- ✅ Nem importál Fooocus modulokat
- ✅ Saját argparse-t használ
- ✅ Működik minden környezetben
- ⚠️ Csak listázza a promptokat (nem generál)

## 🚀 Teljes Workflow

### Lokálisan:

```bash
# 1. Készíts promptokat
echo "beautiful sunset" > prompts/test.txt
echo "cute cat" >> prompts/test.txt

# 2. Listázd ki őket
python standalone_batch_processor.py

# 3. Indítsd el a Fooocus-t
python launch.py

# 4. Másold be a promptokat a web interface-be
```

### Colab-on:

```python
# 1. Töltsd fel a TXT fájlokat
from google.colab import files
uploaded = files.upload()

# 2. Listázd ki a promptokat
!python standalone_batch_processor.py --keep-files

# 3. Használd a Fooocus web interface-t
# (A Colab notebook már elindítja)
```

## 📊 Összehasonlítás

| Script | Működik? | Generál képeket? | Használat |
|--------|----------|------------------|-----------|
| `batch_processor.py` | ❌ Nem | - | Nem használható |
| `standalone_batch_processor.py` | ✅ Igen | ❌ Nem | Prompt listázás |
| `simple_batch_processor.py` | ✅ Igen | ⚠️ API-val | Fooocus futnia kell |
| Manuális | ✅ Igen | ✅ Igen | Web interface |

## 💡 Javaslat

**Legegyszerűbb megoldás:**
1. Használd a `standalone_batch_processor.py`-t a promptok listázásához
2. Másold ki őket
3. Illeszd be a Fooocus web interface-be egyesével

**Vagy:**
- Módosítsd a Colab notebookot, hogy közvetlenül a web interface-t használja
- Készíts egy egyszerű Python scriptet, ami egyesével küldi a promptokat

---

**Frissítve**: 2026-02-05  
**Probléma**: args_manager konfliktus  
**Megoldás**: standalone_batch_processor.py használata
