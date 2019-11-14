import csv


class FormCsv:
    def __init__(self, filename, fieldnames):
        self.filename = filename
        self.fieldnames = fieldnames
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def save_row(self, row_data):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow(row_data)


def save_row(fieldnames, row_data):
    with open(r'output/page_index.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(row_data)