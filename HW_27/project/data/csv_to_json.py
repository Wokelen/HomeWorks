import json
from csv import DictReader


def convert_file(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding="utf-8") as file:
        for row in DictReader(file):
            del row["id"]
            if "price" in row:
                row["price"] = int(row["price"])
            if "is_published" in row:
                if "is_published" == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            result.append({"model": model, "fields": row})
    with open(json_file, "w", encoding="utf-8") as new_file:
        new_file.write(json.dumps(result,indent=4, ensure_ascii=False, sort_keys=True))


convert_file("categories.csv", "categories.json", "ads.category")
convert_file("ads.csv", "ads.json", "ads.ad")