# Fooocus Batch Processing Enhancement

This fork adds automatic batch processing capabilities to Fooocus, allowing you to generate unlimited images from TXT files containing prompts.

## 🆕 New Features

- **📝 TXT-based batch processing**: Read prompts from text files (one per line)
- **🔄 Automatic processing**: Process prompts in batches of 32
- **🗑️ Auto-cleanup**: Automatically delete processed TXT files
- **☁️ Google Colab support**: Easy cloud-based generation with GPU
- **⚙️ Flexible configuration**: Customize batch size, directories, and more

## 🚀 Quick Start

### Local Usage

1. Clone this repository:
```bash
git clone https://github.com/[YOUR-USERNAME]/Fooocus.git
cd Fooocus
```

2. Install dependencies:
```bash
pip install -r requirements_versions.txt
```

3. Create a `prompts` folder and add TXT files:
```bash
mkdir prompts
echo "a beautiful sunset over mountains" > prompts/batch1.txt
echo "a cute cat sitting on a windowsill" >> prompts/batch1.txt
```

4. Run the batch processor:
```bash
python batch_processor.py
```

5. Find your images in the `outputs/` folder!

### Google Colab Usage

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[YOUR-USERNAME]/Fooocus/blob/main/fooocus_batch_colab.ipynb)

1. Click the badge above
2. Run all cells
3. Upload your TXT files
4. Download generated images

## 📖 Documentation

- **[README_BATCH.md](README_BATCH.md)** - Detailed Hungarian documentation
- **[Original Fooocus README](readme.md)** - Original project documentation

## 🎯 Use Cases

- Generate hundreds of images automatically
- Process large prompt lists overnight
- Batch generate variations of concepts
- Automate image dataset creation

## 🔧 Advanced Usage

```bash
# Custom batch size
python batch_processor.py --batch-size 16

# Keep TXT files after processing
python batch_processor.py --keep-files

# Continuous mode (watch for new files)
python batch_processor.py --continuous

# Custom prompts directory
python batch_processor.py --prompts-dir my_prompts
```

## 📁 Project Structure

```
Fooocus/
├── batch_processor.py          # Main batch processor
├── simple_batch_processor.py   # API-based alternative
├── create_test_prompts.py      # Test file generator
├── fooocus_batch_colab.ipynb   # Google Colab notebook
├── README_BATCH.md             # Hungarian documentation
├── prompts/                    # TXT files go here
│   └── example.txt
└── outputs/                    # Generated images
```

## 🤝 Contributing

This is a fork of [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus). All batch processing features are additions to the original project.

## 📜 License

Same as the original Fooocus project (GPL-3.0).

## 🙏 Credits

- Original Fooocus: [lllyasviel](https://github.com/lllyasviel)
- Batch processing enhancement: [YOUR-USERNAME]

---

**Original Fooocus README below:**

---

