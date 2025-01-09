import csv

head = ['USN', 'Name', 'Department', 'Semester']
with open('students.csv', 'w', newline="") as f:
	w = csv.DictWriter(f, fieldnames=head)
	w.writeheader()
	print("Done")
