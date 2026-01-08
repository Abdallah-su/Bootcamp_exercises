#exercis 1
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
#key value of history
print(sample_dict["class"] ["student"] ["marks"] ["history"])


#exercise 2
#keys_to_remove = ["name", "salary"]
ample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

del ample_dict ["name"], ample_dict ["salary"]
print(ample_dict)







