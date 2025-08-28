# file_modifier.py

def modify_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, "r",) as infile:
            lines = infile.readlines()
        
        # Modify each line (reverse text)
        modified_lines = [line.strip()[::-1] + "\n" for line in lines]
        
        # Write modified content to the output file
        with open(output_file, "w") as outfile:
            outfile.writelines(modified_lines)
        
        print(f"✅ File '{input_file}' processed successfully! Results saved in '{output_file}'.")
    
    except FileNotFoundError:
        print(f"❌ Error: '{input_file}' not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# Run the program
if __name__ == "__main__":
    modify_file("input.txt", "output.txt")
