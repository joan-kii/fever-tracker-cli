import os
import sys
import csv
from datetime import datetime
from fpdf import FPDF # type: ignore
from tabulate import tabulate # type: ignore


def main() -> None:

    """
    Run Fever Tracker
    :return: None
    """

    # Get csv files
    csv_files: list[str] = os.listdir("./csv_files/")

    # Input user option loop
    while True:
        user_option: str = input(
            "What you want to do?\n" \
            "1 -> Create new track\n" \
            "2 -> Add temperature to an existing track\n" \
            "3 -> Check a track\n" \
            "4 -> Convert track to a pdf file\n"
            "5 -> Quit\n"
            )

        if user_option == "1":
            new_track()
            break

        elif user_option == "2":
            n_2: int = choose_track(csv_files)
            add_row(csv_files[n_2])
            break

        elif user_option == "3":
            n_3: int = choose_track(csv_files)
            open_track(csv_files[n_3])
            break

        elif user_option == "4":
            n_4: int = choose_track(csv_files)
            convert_track(csv_files[n_4])
            break

        elif user_option == "5":
            sys.exit()

        else:
            print("Please, choose a valid option\n")


def new_track():

    """
    Create new track stored in a csv file
    and print tabulate data
    :return: None
    """

    # Get user inputs
    name: str = input("Patient name: ")

    while True:
        try:
            temp: str = input("Temperature: ")
            # Only accepts a valid temperature
            if 35.0 < float(temp) < 42.0:
                break
            else:
                print("Temperature has not a valid value")
        except ValueError:
            print("Temperature must be a number")

    medicine: str = input("Medicine: ")

    try:
        dose: str = abs(int(input("Dose: ")))
    except ValueError:
        print("Dose must be a number")

    # Path and file name
    date: datetime = datetime.now()
    day: str = date.strftime("%d-%m-%Y")
    hour: str = date.strftime("%H:%M")
    path: str = "./csv_files/"
    file_path: str = os.path.join(path, f"{name}_{day}.csv")

    # Create csv file
    with open(file_path, "w", newline="") as track_file:
        fieldnames: list[str] = ["Name", "Date", "Hour", "Temperature", "Medicine", "Dose"]
        track_writer = csv.DictWriter(track_file, fieldnames=fieldnames)

        track_writer.writeheader()
        track_writer.writerow({
            "Name": name,
            "Date": day,
            "Hour": hour,
            "Temperature": temp,
            "Medicine": medicine,
            "Dose": dose
        })

    # Read csv file and print tabulate data
    print_tabulate(file_path)


def add_row(f: str) -> None:

    """
    Add a row to the track stored in the csv file
    and print tabulate data
    :param f: csv file with track data
    :return: None
    """

    # Get user inputs
    while True:
        try:
            temp: str = input("Temperature: ")
            # Only accepts a valid temperature
            if 35.0 < float(temp) < 42.0:
                break
            else:
                print("Temperature has not a valid value")
        except ValueError:
            print("Temperature must be a number")

    medicine: str = input("Medicine: ")
    dose: str = input("Dose: ")

    date: datetime = datetime.now()
    day: str = date.strftime("%d-%m-%Y")
    hour: str = date.strftime("%H:%M")
    path: str = "./csv_files/"
    file_path: str = path + f

    # Add row to track
    with open(file_path, "a", newline="") as track_file:
        fieldnames: list[str] = ["Name", "Date", "Hour", "Temperature", "Medicine", "Dose"]
        track_writer = csv.DictWriter(track_file, fieldnames=fieldnames)

        track_writer.writerow({
            "Name": "",
            "Date": day,
            "Hour": hour,
            "Temperature": temp,
            "Medicine": medicine,
            "Dose": dose
        })

    # Read csv file and print tabulate data
    print_tabulate(file_path)


def open_track(f: str) -> None:

    """
    Print tabulate data
    and give the user convert to pdf option
    :param f: csv file with track data
    :return: None
    """

    file_path: str = "./csv_files/" + f

    # Read csv file and print tabulate data
    print_tabulate(file_path)

    # Give user convert to pdf option
    while True:
        convert: str = input("Do you want to create a pdf file?: Y/n\n")
        if convert.lower() in ["y", "yes"]:
            convert_track(f)
            break
        elif convert.lower() in ["n", "no"]:
            sys.exit()
        else:
            print("Please, choose a valid option\n")


def convert_track(f: str) -> None:

    """
    Convert the csv file to a pdf file
    :param f: csv file with track data
    :return: None
    """

    # Seguir aquí (bug create pdf con print(data), raise ValueError en user inputs, crear tests)

    # Get data
    data: list[dict[str, str]] = get_track_data(f)
    print("---")

    # Format fieldnames
    format_name: str = "Name: " + data[0]["Name"].title()
    format_date: str = "Date: " + data[0]["Date"]

    # Delete no needed fields
    for row in data:
        del row["Name"]

    path: str = "./pdf_files/"

    # Create pdf file
    pdf = FPDF()
    pdf.add_page()

    # Add header
    pdf.set_font("Helvetica", size=16, style="BU")
    pdf.cell(w=180, h=30, txt="Fever Tracker", align="C", new_x="LMARGIN", new_y="NEXT")

    # Add patient info
    pdf.set_font("Helvetica", size=11)
    pdf.cell(w=80, h=8, txt=format_name, new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=80, h=8, txt=format_date, new_x="LMARGIN", new_y="NEXT")

    # Set cells sizes
    line_height: int = pdf.font_size * 2
    col_width: int = pdf.epw / 5

    pdf.ln(line_height)

    # Add fieldnames to table
    for field in data[0]:
        pdf.multi_cell(col_width, line_height, field, border=1, align="C",
            new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
    pdf.ln(line_height)

    # Add data cells
    pdf.set_font("Helvetica", size=10)
    for row in data:
        for d in row:
            pdf.multi_cell(col_width, line_height, row[d], border=1, align="C",
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height)

    # Create output pdf
    pdf.output(f"{path + f.strip('.csv')}.pdf")
    print(f"You can find {f.strip('.csv')}.pdf in the pdf files folder")


def choose_track(csv_files: list[str]) -> int:

    """
    Iterate over csv files and get user option
    :param csv_files: list with csv file names
    :return: index of csv files list selected by user
    :rtype: int
    """

    print("Tracks: \n")

    for idx, file in enumerate(csv_files):
        print(f"{idx + 1} -> {file.strip('.csv')}")

    # Choose valid track
    while True:
        try:
            track_to_open: int = abs(int(input("Choose a number track: ")))
        except ValueError:
            print("Number track must be a positive number")
        else:
            if track_to_open > len(csv_files):
                print("Please, choose a valid track: ")
            else:
                return track_to_open - 1


def print_tabulate(f: str) -> None:

    """
    Open a csv file and print tabulate data
    :param f: csv file with track data
    :return: None
    """

    with open(f, "r") as track_file:
        track_reader = csv.reader(track_file)
        print(tabulate(track_reader, headers="firstrow", tablefmt="grid"))


def get_track_data(f: str) -> list[dict[str, str]]:

    """
    Open a track stored in the csv file
    :param f: csv file with track data
    :return: A list of dicts with data
    :rtype: list[dict[str, str]]
    """

    rows: list[dict[str, str]] = []
    with open("./csv_files/" + f, "r") as track_file:
        track_reader = csv.DictReader(track_file)

        for row in track_reader:
            rows.append(row)

    return rows


if __name__ == "__main__":
    main()
