import csv


def get_csv_data():
    data = []
    with open("meterusage.csv", "r") as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                continue
            else:
                obj = {"time": row[0], "meterusage": float(row[1])}
                data.append(obj)

                if i == 20:
                    break
            i += 1
    return data
