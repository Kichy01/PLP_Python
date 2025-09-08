# Ubuntu Image Fetcher

A Python tool for respectfully collecting and organizing images from the web.  
Inspired by the Ubuntu philosophy — **"I am because we are"** — this project emphasizes community, respect, sharing, and practicality.

## ✨ Features
- Download images directly from image URLs
- Extract and fetch the first image from a webpage URL
- Accept multiple URLs at once (comma-separated)
- Read URLs from a text file (e.g., `urls.txt`)
- Automatically create a `Fetched_Images` directory
- Prevent overwriting by renaming duplicates
- Graceful error handling for failed requests

## 📂 Project Structure
```
Ubuntu_Requests/
│── ubuntu_image_fetcher.py   # Main script
│── urls.txt            # Sample list of image URLs
│── Fetched_Images/     # Created automatically when fetching images
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Kichy01/Ubuntu_Requests.git
cd Ubuntu_Requests
```

### 2. Install dependencies
Make sure you have Python 3.8+ installed, then install required libraries:
```bash
pip install requests beautifulsoup4
```

### 3. Run the script

#### Option A: Enter URLs manually
```bash
python ubuntu_image_fetcher.py
```
Example input:
```
https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d, https://images.pexels.com/photos/15286/pexels-photo.jpg
```

#### Option B: Use a text file (`urls.txt`)
Add one URL per line inside `urls.txt`. Example:
```txt
https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d
https://images.pexels.com/photos/15286/pexels-photo.jpg
https://upload.wikimedia.org/wikipedia/commons/9/99/Blue_marble_2002.png
```

Then run:
```bash
python ubuntu_fetcher.py
```
and simply type:
```
urls.txt
```

### 4. Output
- All images are saved inside the `Fetched_Images/` directory.
- Duplicate filenames are auto-renamed (e.g., `image.jpg`, `image_1.jpg`).

Example:
```
Ubuntu Image Fetcher
Mindfully collecting images from the web

✓ Saved: Fetched_Images/photo-1503023345310-bd7c1de61c7d
✓ Saved: Fetched_Images/pexels-photo.jpg
✓ Saved: Fetched_Images/Blue_marble_2002.png

Connection strengthened. Community enriched.
```

## 🌍 Philosophy
This project is built with the spirit of **Ubuntu**:
- **Community**: Connects to the global web to fetch shared resources.  
- **Respect**: Handles errors gracefully without crashing.  
- **Sharing**: Organizes images in a common folder for easy access.  
- **Practicality**: Provides a useful tool for mindful resource collection.  

> “A person is a person through other persons.” – Ubuntu Philosophy

## 🔗 Repository
[GitHub: Ubuntu_Requests](https://github.com/Kichy01/Ubuntu_Requests)
