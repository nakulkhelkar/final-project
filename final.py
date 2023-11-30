import sys
import csv
import tabulate

def main():
    action = input(
        "Enter R to read, W to write scientist data, Z to exit, and N to add a new scientist "
    )

    if action.upper() == "R":
        scientist_id = input("Scientist ID: ")
        result = read_file(scientist_id)
        if result:
            print(tabulate.tabulate([result], headers="keys", tablefmt="plain"))

    elif action.upper() == "N":
        write_new()

    elif action.upper() == "W":
        write_file()

    elif action.upper() == "Z":
        sys.exit("System exit")

    else:
        sys.exit("Wrong Output")

def read_file(scientist_id):
    scientist_id = str(scientist_id)
    with open("scientists.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["scientist ID"] == str(scientist_id):
                return {
                    "scientist ID": row["scientist ID"],
                    "name": row["name"],
                    "job description": row["job description"],
                    "years worked": row["years worked"],
                    "clearance": row["clearance"],
                }

    print(f"No scientist found with ID {scientist_id}")
    return None

def write_file():
    scientist_id = input("Scientist ID: ")
    job_description = input("Enter new job description: ")
    years_worked = input("Enter new number of years worked: ")

    fieldnames = [
        "scientist ID",
        "name",
        "job description",
        "years worked",
        "clearance",
    ]

    rows = []

    try:
        with open("scientists.csv", "r", newline="") as read_file:
            reader = csv.DictReader(read_file)
            rows = list(reader)
    except FileNotFoundError:
        pass

    found_scientist = False

    for row in rows:
        if row["scientist ID"] == str(scientist_id):
            row["job description"] = job_description
            row["years worked"] = years_worked
            found_scientist = True
            break

    if not found_scientist:
        print(f"No scientist found with ID {scientist_id}")
        return

    with open("scientists_temp.csv", "w", newline="") as write_file:
        writer = csv.DictWriter(write_file, fieldnames)

        if not rows or rows[0]["scientist ID"] != fieldnames[0]:
            writer.writeheader()

        writer.writerows(rows)

    # Rename the temp file to the original file after updating the rows
    import os
    os.remove("scientists.csv")
    os.rename("scientists_temp.csv", "scientists.csv")

    print(f"Scientist with ID {scientist_id} updated successfully.")

def write_new():
    scientist_id = input("Enter new Scientist ID: ")
    name = input("Enter name: ")
    job_description = input("Enter job description: ")
    years_worked = input("Enter number of years worked: ")
    clearance = input("Enter clearance level: ")

    fieldnames = [
        "scientist ID",
        "name",
        "job description",
        "years worked",
        "clearance",
    ]

    new_scientist = {
        "scientist ID": scientist_id,
        "name": name,
        "job description": job_description,
        "years worked": years_worked,
        "clearance": clearance,
    }

    rows = []

    try:
        with open("scientists.csv", "r", newline="") as read_file:
            reader = csv.DictReader(read_file)
            rows = list(reader)
    except FileNotFoundError:
        pass

    for row in rows:
        if row["scientist ID"] == scientist_id:
            print(f"Scientist with ID {scientist_id} already exists.")
            return

    rows.append(new_scientist)

    with open("scientists.csv", "w", newline="") as write_file:
        writer = csv.DictWriter(write_file, fieldnames)
        if not rows or rows[0]["scientist ID"] != fieldnames[0]:
            writer.writeheader()
        writer.writerows(rows)

    print(f"Scientist with ID {scientist_id} added successfully.")

if __name__ == "__main__":
    main()
