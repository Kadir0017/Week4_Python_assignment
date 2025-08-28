# error_handling_lab.py

def read_file():
    filename = input("📂 Enter the filename to read: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\n✅ File read successfully!\n")
            print("---- File Content ----")
            print(content)
            print("----------------------")
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"⚠️ Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    read_file()
