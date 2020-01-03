adj1 = input('Enter an adjective: ')
name1 = input('Enter a name: ')
verb1 = input('Enter a verb (infinitive): ')
adj2 = input('Enter an adjective: ')
noun1 = input('Enter a plural noun: ')

#print(f"""
#Here is my story:
#
#
#
#There once was a feared pirate named {adj1.capitalize()} {name1.capitalize()}.
#The reason they were so feared was...
#
#
#
#... they used to {verb1} people with {adj2} {noun1}.
#
#Wow, scary!
#    """)

output = "\n" + "Here is my story: \n\n\n\n" + \
  "There once was a feared pirate named " + adj1.capitalize() + " " + name1.capitalize() + ".\n" + \
  "The reason they were so feared was... \n\n\n\n" + \
  "... they used to " + verb1 + " people with " + adj2 + " " + noun1 + ".\n" + \
  "\nWow, scary!"

print(output)