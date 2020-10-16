import csv

def first():
    sheet = [
        ["Last, First", "Age"],
        ["Bailey, Mark", 29],
        ["Campbell, Alistair", 27],
        ]
    with open("profs.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        for row in sheet:
            writer.writerow(row)
    
if __name__ == "__main__":
    first()
