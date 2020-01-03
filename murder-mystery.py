name1 = input('enter a name')
adj1 = input('enter an adjective')
animal1 = input('enter plural animals')
verb1 = input('enter past tense verb')
con1 = input('enter a conjunction')


#print(f"""
#Humpty {name1} sat on a wall.
#Humpty {name1} had a {adj1} fall.
#All the king's {animal1] and all the king's men,
#Couldn't put Humpty together again.
#They {verb1} and they {verb1}.
#{con1} no matter how hard,
#They couldn't stick him together,
#Not even with lard.
#""")

output = "Humpty " + name1 + " sat on a wall.\n" + \
  "Humpty " + name1 + " had a " + adj1 + " fall.\n" + \
  "All the king's " + animal1 + " and all the king's men,\n" + \
  "Couldn't put Humpty together again.\n" + \
  "They " + verb1 + " and they " + verb1 + " .\n" + \
  con1 + " no matter how hard,\n" + \
  "They couldn't stick him together,\n" + \
  "Not even with lard.\n"

print("")
print(output)