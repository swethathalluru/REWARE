import os
import shutil
from PIL import Image

def resize_and_organize_photos():
    """
    This script helps you organize and resize downloaded clothing photos
    """
    
    # Create a downloads folder for organizing
    downloads_folder = "downloaded_photos"
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)
    
    print("Photo Organization Helper for Reware Website")
    print("=" * 50)
    
    # Photo mapping for easy organization
    photo_mapping = {
        "Men's Photos": {
            "men-product1.jpg": "Classic Suit Jacket (Ralph Lauren)",
            "men-product2.jpg": "Casual Polo Shirt (Lacoste)", 
            "men-product3.jpg": "Premium Denim Jeans (Levi's)",
            "men-product4.jpg": "Leather Dress Shoes (Cole Haan)",
            "men-product5.jpg": "Winter Wool Coat (Hugo Boss)",
            "men-product6.jpg": "Cotton T-Shirt (Calvin Klein)",
            "men-product7.jpg": "Formal Trousers (Armani)",
            "men-product8.jpg": "Designer Sneakers (Adidas)"
        },
        "Women's Photos": {
            "women-product1.jpg": "Elegant Evening Dress (Chanel)",
            "women-product2.jpg": "Silk Designer Blouse (Versace)",
            "women-product3.jpg": "Classic High Heels (Jimmy Choo)",
            "women-product4.jpg": "Luxury Handbag (Coach)",
            "women-product5.jpg": "Cashmere Cardigan (Burberry)",
            "women-product6.jpg": "Designer Skinny Jeans (Guess)",
            "women-product7.jpg": "Summer Sandals (Michael Kors)",
            "women-product8.jpg": "Cocktail Dress (Diane von Furstenberg)"
        },
        "General Shop Photos": {
            "product1.jpg": "Vintage Denim Jacket (Levi's)",
            "product2.jpg": "Classic White Shirt (Ralph Lauren)",
            "product3.jpg": "Floral Summer Dress (Zara)",
            "product4.jpg": "Leather Handbag (Coach)",
            "product5.jpg": "Wool Sweater (J.Crew)",
            "product6.jpg": "Black Blazer (H&M)"
        }
    }
    
    print("\nPhotos you need to download:")
    for category, items in photo_mapping.items():
        print(f"\n{category}:")
        for filename, description in items.items():
            print(f"  • {filename} - {description}")
    
    print("\n" + "=" * 50)
    print("INSTRUCTIONS:")
    print("1. Download photos from Unsplash/Pexels")
    print("2. Place them in the 'downloaded_photos' folder")
    print("3. Run this script again to resize and organize them")
    print("4. The script will move them to static/images/ with correct names")
    
    # Check if there are photos to process
    if os.path.exists(downloads_folder):
        photos = [f for f in os.listdir(downloads_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if photos:
            print(f"\nFound {len(photos)} photos to process:")
            for photo in photos:
                print(f"  • {photo}")
            
            process = input("\nDo you want to resize and organize these photos? (y/n): ")
            if process.lower() == 'y':
                resize_photos(downloads_folder, photos)
        else:
            print(f"\nNo photos found in {downloads_folder} folder.")
    
def resize_photos(downloads_folder, photos):
    """Resize photos to 300x400 and move to static/images"""
    
    target_size = (300, 400)
    static_folder = "static/images"
    
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)
    
    print(f"\nResizing photos to {target_size[0]}x{target_size[1]}...")
    
    for i, photo in enumerate(photos):
        try:
            # Open and resize image
            img_path = os.path.join(downloads_folder, photo)
            img = Image.open(img_path)
            
            # Resize maintaining aspect ratio
            img.thumbnail(target_size, Image.Resampling.LANCZOS)
            
            # Create new image with exact target size and paste resized image
            new_img = Image.new('RGB', target_size, (255, 255, 255))
            
            # Calculate position to center the image
            x = (target_size[0] - img.size[0]) // 2
            y = (target_size[1] - img.size[1]) // 2
            new_img.paste(img, (x, y))
            
            # Save with new name
            new_filename = f"photo_{i+1}.jpg"
            new_path = os.path.join(static_folder, new_filename)
            new_img.save(new_path, 'JPEG', quality=85)
            
            print(f"  ✓ Resized {photo} → {new_filename}")
            
        except Exception as e:
            print(f"  ✗ Error processing {photo}: {e}")
    
    print(f"\nPhotos saved to {static_folder}/")
    print("\nNext steps:")
    print("1. Rename the photos to match your product names")
    print("2. For example: photo_1.jpg → men-product1.jpg")
    print("3. Refresh your website to see the new photos!")

def show_search_urls():
    """Show helpful search URLs for finding clothing photos"""
    
    search_urls = {
        "Men's Clothing": [
            "https://unsplash.com/s/photos/mens-suit-jacket",
            "https://unsplash.com/s/photos/polo-shirt-men",
            "https://unsplash.com/s/photos/mens-jeans",
            "https://unsplash.com/s/photos/dress-shoes-men",
            "https://unsplash.com/s/photos/mens-coat",
            "https://unsplash.com/s/photos/mens-t-shirt",
            "https://unsplash.com/s/photos/mens-trousers",
            "https://unsplash.com/s/photos/mens-sneakers"
        ],
        "Women's Clothing": [
            "https://unsplash.com/s/photos/evening-dress",
            "https://unsplash.com/s/photos/womens-blouse",
            "https://unsplash.com/s/photos/high-heels",
            "https://unsplash.com/s/photos/luxury-handbag",
            "https://unsplash.com/s/photos/womens-cardigan",
            "https://unsplash.com/s/photos/womens-jeans",
            "https://unsplash.com/s/photos/womens-sandals",
            "https://unsplash.com/s/photos/cocktail-dress"
        ]
    }
    
    print("\nHelpful Search URLs:")
    print("=" * 30)
    for category, urls in search_urls.items():
        print(f"\n{category}:")
        for url in urls:
            print(f"  {url}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Show photo organization guide")
    print("2. Process downloaded photos")
    print("3. Show search URLs")
    
    choice = input("\nEnter choice (1-3): ")
    
    if choice == "1":
        resize_and_organize_photos()
    elif choice == "2":
        if os.path.exists("downloaded_photos"):
            photos = [f for f in os.listdir("downloaded_photos") if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            if photos:
                resize_photos("downloaded_photos", photos)
            else:
                print("No photos found in downloaded_photos folder.")
        else:
            print("Please create 'downloaded_photos' folder and add photos first.")
    elif choice == "3":
        show_search_urls()
    else:
        print("Invalid choice. Running default guide...")
        resize_and_organize_photos()
