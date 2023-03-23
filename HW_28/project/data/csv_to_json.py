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
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if "location_id" in row:
                row["location"] = [row["location_id"]]
                del row["location_id"]
            if "age" in row:
                row["age"] = int(row["age"])

            result.append({"model": model, "fields": row})
    with open(json_file, "w", encoding="utf-8") as new_file:
        new_file.write(json.dumps(result,indent=4, ensure_ascii=False, sort_keys=True))


convert_file("category.csv", "converted_files/category.json", "ads.category")
convert_file("ad.csv", "converted_files/ad.json", "ads.ad")
convert_file("user.csv", "converted_files/user.json", "users.user")
convert_file("location.csv", "converted_files/location.json", "users.location")
