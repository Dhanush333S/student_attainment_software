import csv

with open("cie1.csv", "w", newline="") as f:
    head = ["USN", "Version", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                "1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c", "4a", "4b", "4c", "5a", "5b", "5c"]
    w = csv.DictWriter(f, fieldnames=head)
    w.writeheader()
    print("File created !")
    