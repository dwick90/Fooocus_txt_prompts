# 🎨 Fooocus Batch Processor

**Automatikus képgenerálás TXT fájlokból, korlátlan mennyiségben!**

Ez a Fooocus fork lehetővé teszi, hogy TXT fájlokból olvass be promptokat és automatikusan generálj belőlük képeket 32-es batch-ekben. Tökéletes nagy mennyiségű kép előállításához!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dwick90/Fooocus_txt_prompts/blob/main/fooocus_batch_colab.ipynb)

## ✨ Főbb Funkciók

- 📝 **TXT-alapú batch feldolgozás** - Egy sor = egy prompt
- 🔄 **Automatikus feldolgozás** - 32-es batch-ekben
- 🗑️ **Auto-cleanup** - Törli a feldolgozott fájlokat
- ☁️ **Google Colab támogatás** - Ingyenes GPU használat
- ⚙️ **Testreszabható** - Batch méret, könyvtárak, stb.

## 🚀 Gyors Kezdés

### Lokális Használat

```bash
# 1. Klónozás
git clone https://github.com/dwick90/Fooocus_txt_prompts.git
cd Fooocus_txt_prompts

# 2. Függőségek telepítése
pip install -r requirements_versions.txt

# 3. Prompts létrehozása
mkdir prompts
echo "a beautiful sunset over mountains" > prompts/test.txt
echo "a cute cat sitting on a windowsill" >> prompts/test.txt

# 4. Generálás!
python batch_processor.py
```

### Google Colab Használat

1. Kattints a fenti Colab badge-re
2. Futtasd az összes cellát
3. Töltsd fel a TXT fájljaidat
4. Töltsd le a generált képeket

## 📖 Dokumentáció

- **[README_BATCH.md](README_BATCH.md)** - Részletes magyar dokumentáció
- **[GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)** - GitHub feltöltési útmutató

## 💡 Használati Példák

### Egyszerű Batch
```bash
# Prompts fájl
echo "beautiful landscape" > prompts/batch1.txt
echo "cute animals" >> prompts/batch1.txt

# Generálás
python batch_processor.py
```

### Nagy Mennyiség
```bash
# 100 teszt prompt
python create_test_prompts.py --prompts-per-file 100

# Feldolgozás
python batch_processor.py
```

### Folyamatos Mód
```bash
# Figyeli az új fájlokat
python batch_processor.py --continuous
```

## 🎯 Használati Esetek

- ✅ Több száz kép automatikus generálása
- ✅ Nagy prompt listák feldolgozása
- ✅ Variációk batch generálása
- ✅ Képadatbázis létrehozása

## 🔧 Paraméterek

```bash
python batch_processor.py --help

Opciók:
  --prompts-dir DIR      Prompts mappa (default: prompts)
  --batch-size N         Batch méret, max 32 (default: 32)
  --keep-files           Ne törölje a TXT fájlokat
  --continuous           Folyamatos mód (10 mp-enként ellenőriz)
```

## 📁 Projekt Struktúra

```
Fooocus_txt_prompts/
├── batch_processor.py          # Fő batch processor
├── simple_batch_processor.py   # API-alapú alternatíva
├── create_test_prompts.py      # Teszt fájl generátor
├── fooocus_batch_colab.ipynb   # Google Colab notebook
├── README_BATCH.md             # Magyar dokumentáció
├── GITHUB_UPLOAD_GUIDE.md      # GitHub útmutató
└── prompts/                    # TXT fájlok helye
    └── example.txt
```

## 🎓 TXT Fájl Formátum

```txt
# Ez egy megjegyzés (ignorálva)
a beautiful sunset over mountains, highly detailed, 8k
a cute cat sitting on a windowsill, photorealistic

# Üres sorok is ignorálva
a futuristic city with flying cars, cyberpunk style
```

## 🤝 Eredeti Fooocus

Ez a projekt a [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus) fork-ja, batch processing funkciókkal bővítve.

## 📜 Licenc

GPL-3.0 (ugyanaz, mint az eredeti Fooocus)

## 🙏 Köszönet

- **Eredeti Fooocus**: [lllyasviel](https://github.com/lllyasviel)
- **Batch Processing**: [dwick90](https://github.com/dwick90)

---

**⭐ Ha hasznos volt, adj egy csillagot a repo-nak!**

**🐛 Hibát találtál? Nyiss egy issue-t!**

**💬 Kérdésed van? Írj a Discussions-be!**
