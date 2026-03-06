import json

def init_db(file):
    try:
        with open(file, "x") as f:
            json.dump({"students": []}, f, indent=4)
    except:
        return 'File already exists'
    
def add_record(file, record):
    with open(file, "r") as f:
        data = json.load(f)

    next_id = max((s.get("id", 0) for s in data["students"]), default=0) + 1
    record["id"] = next_id
    data["students"].append(record)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)    

def view_records(file):
    with open(file, "r") as f:
        data = json.load(f)
        print(data)

def delete_record(file_path, id):
    with open(file_path, "r") as f:
        data = json.load(f)

    new_students = []
    for student in data["students"]:
        if student["id"] == id:
            continue
        new_students.append(student)

    data["students"] = new_students
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def update_record(file_path, id, updates):
    with open(file_path, "r") as f:
        data = json.load(f)

    for student in data["students"]:
        if student["id"] == id:
            student.update(updates)
            break

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def main():
    file = "example.json"
    data = {"name": "David", "age": 22, "city": "Timisoara"}
    updated = {"name": "David", "age": 22, "city": "Arad"}
    init_db(file)
    # add_record(file, {"name": "Alice", "age": 30, "city": "New York"})
    add_record(file, data)
    view_records(file)
    print("")
    
    update_record(file, 2, updated)
    view_records(file)
    print("")

    delete_record(file, 2)
    view_records(file)
main()