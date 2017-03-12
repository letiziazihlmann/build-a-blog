sent = input('enter a sentence!')
location = {}
index = 0
character_count = {}
#program needs to cycle through each letter and create a dict entry for that letter and the amount
#of times it shows up.
#start with a for loop
for character in sent:
    #cycle through each letter and add/count the amount of times it shows up
    #if the letter is already in the dict, add 1 to the number
    if character in character_count:
        character_count[character] += 1
        location[character].append(index)
    #if letter shows up first time, add to dict
    else:
        character_count[character] = 1
        location[character] = [index]
    index += 1

#sort the keys in letter_count dict
keys = character_count.keys()


print(location)
#return a each letter and count on a seperate line
for character in keys:
    print(character,':', character_count[character])
