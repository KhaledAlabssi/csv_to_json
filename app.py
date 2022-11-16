import json
import csv

with open ("qqq.csv", "r", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"quote": row[0],
        "author": row[1],
        "tag": row[2]})

with open("quotes.json", "w") as f:
    json.dump(data, f, indent=1)