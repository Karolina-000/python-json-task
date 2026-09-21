import json

user = {
  "name": "Eteri",
  "age": 24,
  "city": "Tbilisi",
  "is_student": False,
    "skills": ["Python", "JavaScript", "SQL"]
}

with open("dict.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4, ensure_ascii=False)

print("მონაცემები შეინახა dict.json-ში")

with open("dict.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("წაკითხული მონაცემები:")
print(data)
print(f"სახელი: {data['name']}")
print(f"ასაკი: {data['age']}")