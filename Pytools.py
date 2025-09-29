from pathlib import Path
import shutil
import pyfiglet
import qrcode
import psutil
import platform
from datetime import datetime


# ---------------------------
# 1. File Organizer
# ---------------------------
def file_organizer():
    user_input = input("Enter the folder path to organize: ").strip()
    folder = Path(user_input)

    if not folder.exists() or not folder.is_dir():
        print("Error: The path you entered is not a valid folder.")
        return

    categories = {
        # Images
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
        ".bmp": "Images", ".tiff": "Images", ".svg": "Images", ".heic": "Images",

        # Documents
        ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
        ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents",
        ".pptx": "Documents", ".odt": "Documents", ".rtf": "Documents",
        ".csv": "Documents", ".md": "Documents", ".txt": "Documents",

        # Code / Web
        ".html": "WebFiles", ".css": "WebFiles", ".js": "WebFiles",
        ".ts": "WebFiles", ".jsx": "WebFiles", ".tsx": "WebFiles",
        ".json": "WebFiles", ".xml": "WebFiles",
        ".py": "Code", ".java": "Code", ".c": "Code", ".cpp": "Code",
        ".cs": "Code", ".php": "Code", ".rb": "Code", ".go": "Code",
        ".rs": "Code", ".swift": "Code",

        # Audio
        ".mp3": "Audio", ".wav": "Audio", ".aac": "Audio",
        ".flac": "Audio", ".ogg": "Audio", ".m4a": "Audio",

        # Video
        ".mp4": "Video", ".mkv": "Video", ".mov": "Video",
        ".avi": "Video", ".wmv": "Video", ".flv": "Video", ".webm": "Video",

        # Archives
        ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
        ".tar": "Archives", ".gz": "Archives", ".bz2": "Archives",

        # Apps / Executables
        ".exe": "Executables", ".msi": "Executables",
        ".dmg": "Executables", ".pkg": "Executables",
        ".sh": "Executables", ".bat": "Executables"
    }

    print("Organizing files...")

    for item in folder.iterdir():
        if item.is_file():
            try:
                ext = item.suffix.lower()
                category = categories.get(ext, "Unknown")
                target_folder = folder / category
                target_folder.mkdir(exist_ok=True)
                target_path = target_folder / item.name

                shutil.move(str(item), str(target_path))
                print(f"Moved {item.name} → {category}")
            except Exception as e:
                print(f"Could not move {item.name}: {e}")

    print("Organizing complete!")


# ---------------------------
# 2. ASCII Art Generator
# ---------------------------
def ascii_art_generator():
    text = input("Enter text to turn into ASCII art: ")
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)


# ---------------------------
# 3. QR Code Generator
# ---------------------------
def qr_code_generator():
    data = input("Enter text or URL to generate QR code: ")
    qr_img = qrcode.make(data)
    qr_img.save("my_qr.png")
    print("QR Code saved as my_qr.png")




#System Info
def pc_status():
    print("\n System Information\n" + "-"*30)

    uname = platform.uname()
    print(f"System: {uname.system} {uname.release}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print(f"Node Name: {uname.node}")

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    print(f"Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n Memory Info")
    svmem = psutil.virtual_memory()
    print(f"Total: {svmem.total // (1024**3)} GB")
    print(f"Available: {svmem.available // (1024**3)} GB")
    print(f"Used: {svmem.used // (1024**3)} GB ({svmem.percent}%)")

    print("\n🖴 Disk Info")
    partitions = psutil.disk_partitions()
    for part in partitions:
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"{part.device} - {usage.used // (1024*3)}GB / {usage.total // (1024*3)}GB ({usage.percent}%)")
        except PermissionError:
            continue

    print("\nCPU Info")
    print(f"Cores: {psutil.cpu_count(logical=False)}")
    print(f"Threads: {psutil.cpu_count(logical=True)}")
    print(f"Usage: {psutil.cpu_percent(interval=1)}%")

#b7e0cafa5b7d3d0ad71821f0d19d5d3f
#Currency converter
import requests

def currency_converter():
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD, INR, EUR): ").upper()
    to_curr = input("To currency (e.g., USD, INR, EUR): ").upper()
    access_key = "b7e0cafa5b7d3d0ad71821f0d19d5d3f"
    url = f"http://api.exchangeratesapi.io/v1/convert?access_key={access_key}&from={from_curr}&to={to_curr}&amount={amount}"
    #url = f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("DEBUG JSON:", data)
            result = data.get("result")
            if result:
                print(f"\n{amount} {from_curr} = {result:.2f} {to_curr}\n")
            else:
                print("Conversion error.")
        else:
            print("API error.")
    except Exception as e:
        print(f"Error: {e}")


# ---------------------------
# Main Menu
# ---------------------------
def main():
    while True:
        print("\n=== PyTools Menu ===")
        print("1. File Organizer")
        print("2. ASCII Art Generator")
        print("3. QR Code Generator")
        print("4. System Info")
        print("5.Currency converter")
        print("6.Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            file_organizer()
        elif choice == "2":
            ascii_art_generator()
        elif choice == "3":
            qr_code_generator()
        elif choice == "4":
            pc_status()
        elif choice == "5":
            currency_converter()
        elif choice == "6":
            print("Exiting PyTools. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()