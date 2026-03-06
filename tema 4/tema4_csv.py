import csv

def init_db(file, header):
    try:
        with open(file, "x") as f:
            writer = csv.writer(f)
            writer.writerow(header)
    except:
        return 'File already exists'
    
def add_record(file, record):
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(record)

def view_records(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def search_record(file, search_value):
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if search_value in row:
                print(row)

def delete_record(file, delete_id):
    rows = []
    with open(file, "r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != str(delete_id):
                rows.append(row)
    with open(file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def main():
    file = "example.csv"
    header = ["ID", "NAME", "AGE", "GRADE"]
    record_1 = [1, "Ana", "21", 4]
    record_2 = [2, "David", "22", 10]
    init_db(file, header)
    add_record(file, record_1)
    # add_record(file, record_2)
    view_records(file)
    print("")
    search_record(file, "David")
    print("")
    delete_record(file, 1)
    view_records(file)
main()