"""
Ubuntu Image Fetcher
--------------------
A Python tool for downloading and organizing images from the web.

Features:
- Download images directly from URLs
- Extract the first <img> tag from webpage URLs
- Accept multiple URLs at once (comma-separated)
- Read URLs from a text file (one per line)
- Create an organized 'Fetched_Images' folder
- Prevent duplicate filenames by auto-renaming
- Graceful error handling for failed requests

Philosophy:
Inspired by Ubuntu — community, respect, sharing, and practicality.
"""

import requests
import os
from urllib.parse import urlparse
from pathlib import Path
from bs4 import BeautifulSoup


def get_image_url_from_page(url, headers):
    """
    Attempt to extract the first image URL from an HTML page.

    Args:
        url (str): The webpage URL.
        headers (dict): HTTP headers for requests.

    Returns:
        str | None: The extracted image URL, or None if not found.
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        img_tag = soup.find("img")

        if img_tag and img_tag.get("src"):
            img_url = img_tag["src"]

            # Handle relative URLs (convert them to absolute)
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            elif img_url.startswith("/"):
                parsed = urlparse(url)
                img_url = f"{parsed.scheme}://{parsed.netloc}{img_url}"

            return img_url

    except Exception as e:
        print(f"✗ Could not extract image from {url}: {e}")

    return None


def fetch_image(url, save_dir):
    """
    Download an image or extract one from a webpage and save it locally.

    Args:
        url (str): The URL of the image or webpage.
        save_dir (Path): Directory where the image will be stored.
    """

    # Custom headers (mimic a browser) to avoid being blocked
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )
    }

    try:
        # Fetch the content at the URL
        response = requests.get(url, timeout=10, stream=True, headers=headers)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")

        # If the URL points directly to an image
        if content_type.startswith("image/"):
            image_url = url

        # If the URL is a webpage, try to extract the first image
        elif "text/html" in content_type:
            print(f"ℹ Detected webpage, extracting image from {url}...")
            image_url = get_image_url_from_page(url, headers)
            if not image_url:
                print(f"✗ No image found at {url}")
                return

            # Re-fetch the extracted image
            response = requests.get(image_url, timeout=10, stream=True, headers=headers)
            response.raise_for_status()

        # Skip unsupported content types (e.g., PDF, text, etc.)
        else:
            print(f"✗ Skipping {url} (unsupported type: {content_type})")
            return

        # Derive a filename from the image URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
        filepath = save_dir / filename

        # Avoid overwriting files by appending a counter
        counter = 1
        while filepath.exists():
            stem, ext = os.path.splitext(filename)
            filename = f"{stem}_{counter}{ext}"
            filepath = save_dir / filename
            counter += 1

        # Save the file in chunks (good for large images)
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Saved: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error fetching {url}: {e}")
    except Exception as e:
        print(f"✗ Error with {url}: {e}")


def main():
    """
    Entry point for the Ubuntu Image Fetcher.
    Handles user input, prepares directories, and triggers downloads.
    """
    print("Ubuntu Image Fetcher")
    print("Mindfully collecting images from the web\n")

    # Prompt for URLs or a file containing URLs
    user_input = input(
        "Enter one or more image URLs (comma-separated)\n"
        "Or enter a filename (e.g., urls.txt) with URLs listed line by line:\n> "
    ).strip()

    # Load URLs either from file or directly from input
    if os.path.isfile(user_input):
        print(f"ℹ Reading URLs from {user_input}...")
        with open(user_input, "r", encoding="utf-8") as file:
            urls = [line.strip() for line in file if line.strip()]
    else:
        urls = [u.strip() for u in user_input.split(",") if u.strip()]

    # Prepare the storage directory
    save_dir = Path("Fetched_Images")
    save_dir.mkdir(exist_ok=True)

    # Process each URL
    for url in urls:
        fetch_image(url, save_dir)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
