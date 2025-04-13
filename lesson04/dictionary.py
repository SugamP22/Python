# dictionary in python where it has key and value
info={
  "Nombre": "Sugam",
  "Asignatura":["JAVA", "Python", "SQL", "HTMLCSS"],
  "Temas" :("Variable","Conditional","tuple","list","dic"),
  "Edad": 23,
  "Curso" : "DAM",
  "Nota": 9.5,
  "Aprobado": True
  
}
print(info)
print(info["Asignatura"][0])
print(info.get("Asignatura")[0])
info.update({"new1":23})
print(info)
info["new2"]=12
print(info)
new_list=list(info.items())
print(new_list)
second_list=list(new_list[1])
print(second_list)
print(second_list[1][0])
print(info)
print(type(info))
# dict are unordered they(list and tuple have index) but no index in dict listand dict are mutable and i cannot create same key twice it will just cahnge the value
print(info["Nombre"])
print(info["Temas"] )
print(info["Edad"] )
print(info["Curso"] )
info["Nombre"]="suman"
info["Surname"]="Poudel"
print(info)
new_dict={}
print(new_dict)
new_dict["Name"]="new name"
print(new_dict)
new_dict["subjects"]={
    "chem":98,
    "phy":10
  }

print(new_dict["subjects"]["chem"])
print(new_dict)
print(info.items())
res=list(info)
print(res[1][0])  # Outputs: JAVA


