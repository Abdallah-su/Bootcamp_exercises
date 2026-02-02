
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
json_object = json.loads(sampleJson)
salary_object =json_object["company"]["employee"]["payable"]["salary"]
print(salary_object)
json_object_new = json_object.copy()
json_object_new["company"]["employee"]['birth_date'] = "1990-01-01"
json_object.update(json_object_new)
print(json_object)
with open('sample.json', 'w') as json_file:
    json.dump(json_object, json_file, indent=4)

with open('sample.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)
