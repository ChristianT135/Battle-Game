gameCharacter = [" Wizard" , "Elf" , "Human"]

#wizardInfo ={"Character":"Wizard", "myHP": "70"}

# GameCharacter
wizard = "Wizard"
elf="Elf"
human = "Human"

# Health Point
wizard_hp = 70
elf_hp = 100
human_hp = 150


# Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragron Info
dragon_damage = 50
dragon_hp = 300

#  First While Loop

while True:
    print ("1. Wizard")
    print ("2. Elf")
    print ("3. Human")
    gameCharacter=input("Choose Your Character, by select the corresponding on the right hand side!. " )
    
# First IF Statement
    
    if gameCharacter == "1":
        gameCharacter = "Wizard"
#print (f" You have selected your character the {wizard}!.")
        
        my_hp = wizard_hp
#print("Wizard Health " , wizard_hp , "!")
        
        my_damage = wizard_damage
#print("Wizard Damage " , wizard_damage , "!")
        
        break

    elif gameCharacter == "2":
        gameCharacter = "Elf"
#print (f" You have selected  your character the {elf}!.")
        
        my_hp = elf_hp
#print("Elf Health " , elf_hp , "!")
        
        my_damage = elf_damage
#print("Elf Damage " , elf_damage , "!")
        
        break

    elif gameCharacter == "3":
        gameCharacter ="Human"
#print(f" You have selected your character the {human}! ")
        
        my_hp = human_hp
#print("Human Health " , human_hp , "!")
        
        my_damage = human_damage
#print("Human Damage " , human_damage ,"!")
        
        break

    else:
        print ("Unknown Character, Please choose form the List")
        
# Second IF Statement
        
if gameCharacter == wizard:
    print(f"You have selected your character the {wizard}!")
    print(f"Health {wizard_hp}!")
    print(f"Damage {wizard_damage}!")

elif gameCharacter == elf:
    print(f"You have selected your character the {elf}")
    print(f"Health {elf_hp}!")
    print(f"Damage {elf_damage}!")

elif gameCharacter == human:
    print(f" You have selected your character the {human}! ")
    print(f"Health {human_hp}!")
    print(f"Damage {human_damage}!")

# Second While Loop

while True:
    
    dragon_hp = dragon_hp - my_damage
    
    print("")
    print(f"The {gameCharacter} damaged the dragon!")
    print(f"The Dragon's hitpoints are now {dragon_hp}")
    print("")
    
    #Third IF Statement
    
    if dragon_hp <= 0:
        print(f"The Dragon was Defected by {gameCharacter}!")
        break
    
    print(f"The Dragon strikes back at the {gameCharacter}")
    
    my_hp = my_hp - dragon_damage
    
    print(f" The {gameCharacter}'s hitpoints are now {my_hp}")
    
    if my_hp <= 0:
        print("")
        print(f"The {gameCharacter} was defeated by the Dragon")
        print("")
        break
