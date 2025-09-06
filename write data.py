# write_to_file.py

def main():
    print("Enter the text you want to write to the file.")
    print("Type 'DONE' (in all caps) on a new line to finish.\n")

    lines = []
    while True:
        line = input()
        if line == "DONE":
            break
        lines.append(line)

    filename = "output.txt"

    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"\nData has been written to '{filename}' successfully.")


if __name__ == "__main__":
    main()
