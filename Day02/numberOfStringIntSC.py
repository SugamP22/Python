a="dd3d3d@3a$da&"
digits=0
char=0
specialChar=0
for i in a:
  if i.isdigit():
    digits+=1
  elif i.isalpha():
    char+=1
  else:
    specialChar+=1

print(f"Total number of digits are {digits}, characters are {char} and special charatcers are {specialChar}")