# Fooocus Batch Processing - GitHub Feltöltési Útmutató

## 1. Git Repository Inicializálás

```bash
cd "c:\Users\danwi\Documents\AI PROGRAMOK\Fooocus"

# Git inicializálás (ha még nincs)
git init

# Remote hozzáadása (cseréld ki a USERNAME-t!)
git remote add origin https://github.com/[YOUR-USERNAME]/Fooocus.git

# Vagy ha már van remote, frissítsd:
git remote set-url origin https://github.com/[YOUR-USERNAME]/Fooocus.git
```

## 2. Fájlok Hozzáadása

```bash
# Új fájlok hozzáadása
git add batch_processor.py
git add simple_batch_processor.py
git add create_test_prompts.py
git add fooocus_batch_colab.ipynb
git add README_BATCH.md
git add README_ENHANCED.md
git add prompts/example.txt

# .gitignore frissítése (opcionális)
echo "prompts/*.txt" >> .gitignore
echo "!prompts/example.txt" >> .gitignore
git add .gitignore
```

## 3. Commit és Push

```bash
# Commit
git commit -m "Add batch processing feature

- Add batch_processor.py for automatic TXT-based batch generation
- Add simple_batch_processor.py as API-based alternative
- Add create_test_prompts.py for testing
- Add Google Colab notebook (fooocus_batch_colab.ipynb)
- Add Hungarian documentation (README_BATCH.md)
- Add enhanced README with quick start guide"

# Push (első alkalommal)
git push -u origin main

# Vagy ha már létezik a branch:
git push origin main
```

## 4. GitHub Repository Létrehozása

Ha még nincs GitHub repo-d:

1. Menj a https://github.com/new oldalra
2. Repository név: `Fooocus`
3. Leírás: `Fooocus with automatic batch processing from TXT files`
4. Public vagy Private (ajánlott: Public)
5. **NE** add hozzá a README, .gitignore vagy license-t (már vannak)
6. Kattints a "Create repository"-ra
7. Kövesd a "push an existing repository" utasításokat

## 5. README Frissítése GitHub-on

A `README_ENHANCED.md` tartalmát másold át a fő `README.md`-be, vagy:

```bash
# Eredeti README átnevezése
git mv readme.md README_ORIGINAL.md

# Új README létrehozása
cat README_ENHANCED.md readme.md > README.md

# Commit
git add README.md README_ORIGINAL.md
git commit -m "Update README with batch processing features"
git push
```

## 6. Colab Badge Frissítése

A `README.md` és `fooocus_batch_colab.ipynb` fájlokban cseréld ki:

```
[YOUR-USERNAME]
```

a saját GitHub felhasználónevedre, például:

```
danwi
```

## 7. Release Készítése (Opcionális)

1. Menj a GitHub repo-dba
2. Kattints a "Releases" → "Create a new release"
3. Tag: `v1.0.0-batch`
4. Title: `Batch Processing Feature v1.0.0`
5. Leírás:
```markdown
## 🎉 Batch Processing Feature

Automatic batch image generation from TXT files!

### Features
- Process unlimited prompts in batches of 32
- Automatic TXT file cleanup
- Google Colab support
- Continuous mode for watching new files

### Quick Start
See [README_BATCH.md](README_BATCH.md) for detailed instructions.
```

## 8. Ellenőrzés

Ellenőrizd, hogy minden rendben van:

```bash
# Státusz ellenőrzése
git status

# Remote ellenőrzése
git remote -v

# Branch ellenőrzése
git branch -a
```

## 9. Colab Link Tesztelése

1. Menj a GitHub repo-dba
2. Nyisd meg a `fooocus_batch_colab.ipynb` fájlt
3. Kattints a "Open in Colab" badge-re
4. Ellenőrizd, hogy betöltődik-e a notebook

## 10. Dokumentáció Linkek

Frissítsd a következő fájlokban a linkeket:

- `README.md` - Colab badge
- `README_BATCH.md` - GitHub linkek
- `fooocus_batch_colab.ipynb` - GitHub repo link

## Hasznos Git Parancsok

```bash
# Változások megtekintése
git diff

# Commit history
git log --oneline

# Fájl törlése
git rm filename
git commit -m "Remove file"

# Fájl átnevezése
git mv oldname newname
git commit -m "Rename file"

# Utolsó commit visszavonása (ha még nem push-oltad)
git reset --soft HEAD~1

# Branch létrehozása
git checkout -b batch-processing
git push -u origin batch-processing
```

## Troubleshooting

### "Permission denied (publickey)"
```bash
# SSH kulcs generálása
ssh-keygen -t ed25519 -C "your_email@example.com"

# Kulcs hozzáadása GitHub-hoz
cat ~/.ssh/id_ed25519.pub
# Másold be a GitHub Settings → SSH Keys-be
```

### "Repository not found"
```bash
# Ellenőrizd a remote URL-t
git remote -v

# Frissítsd a helyes URL-re
git remote set-url origin https://github.com/[YOUR-USERNAME]/Fooocus.git
```

### "Merge conflict"
```bash
# Pull először
git pull origin main

# Konfliktusok feloldása
# Szerkeszd a fájlokat, majd:
git add .
git commit -m "Resolve merge conflicts"
git push
```

---

**Kész!** A Fooocus batch processing feature most már elérhető a GitHub-on! 🎉
