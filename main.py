"""
Image Compressor
Kompres gambar tanpa mengurangi kualitas secara signifikan.

Author: Mhd Dimas Naufal
"""

import os
import sys
from PIL import Image


def compress_image(input_path, output_path, quality=85):
    """
    Kompres gambar ke ukuran yang lebih kecil.
    
    Args:
        input_path (str): Path gambar asli
        output_path (str): Path gambar hasil kompres
        quality (int): Kualitas gambar (1-100), default 85
    
    Returns:
        tuple: (ukuran_asli, ukuran_kompres, persentase_hemat)
    """
    try:
        # Buka gambar
        img = Image.open(input_path)
        
        # Convert ke RGB kalau RGBA (biar bisa disimpen jadi JPEG)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Simpen dengan kualitas yang ditentukan
        img.save(output_path, "JPEG", quality=quality, optimize=True)
        
        # Hitung ukuran
        size_before = os.path.getsize(input_path)
        size_after = os.path.getsize(output_path)
        hemat = ((size_before - size_after) / size_before) * 100
        
        return size_before, size_after, hemat
    
    except FileNotFoundError:
        print(f"❌ File tidak ditemukan: {input_path}")
        return None, None, None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None, None, None


def format_size(bytes_size):
    """Format ukuran bytes jadi KB/MB."""
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.2f} KB"
    else:
        return f"{bytes_size / (1024 * 1024):.2f} MB"


def main():
    print("=" * 50)
    print("   🖼️  IMAGE COMPRESSOR")
    print("=" * 50)
    print()
    
    # Cek argumen
    if len(sys.argv) < 2:
        print("Cara pakai:")
        print("  python main.py <input_gambar> [output_gambar] [kualitas]")
        print()
        print("Contoh:")
        print("  python main.py foto.jpg")
        print("  python main.py foto.jpg hasil.jpg 80")
        print()
        print("Kualitas: 1-100 (default: 85, semakin kecil semakin kompres)")
        return
    
    input_path = sys.argv[1]
    
    # Output default: nama_file_compressed.jpg
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        nama, ext = os.path.splitext(input_path)
        output_path = f"{nama}_compressed.jpg"
    
    # Kualitas default 85
    quality = int(sys.argv[3]) if len(sys.argv) >= 4 else 85
    quality = max(1, min(100, quality))  # Batasi 1-100
    
    print(f"📁 Input   : {input_path}")
    print(f"📁 Output  : {output_path}")
    print(f"⚙️  Kualitas: {quality}")
    print()
    print("⏳ Sedang mengkompres...")
    
    # Proses kompres
    size_before, size_after, hemat = compress_image(input_path, output_path, quality)
    
    if size_before is None:
        return
    
    print()
    print("=" * 50)
    print("   ✅ BERHASIL!")
    print("=" * 50)
    print(f"📊 Ukuran asli    : {format_size(size_before)}")
    print(f"📊 Ukuran kompres : {format_size(size_after)}")
    print(f"💾 Hemat           : {hemat:.2f}%")
    print("=" * 50)


if __name__ == "__main__":
    main()