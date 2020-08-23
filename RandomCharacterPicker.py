import random
import math

print("Hello Madam, my name is Sir Westershire, and I shall be your character creator today.  Please answer the following questions so I can make you the best character possible.")


while True:
    strroll = []
    dexroll = []
    conroll = []
    introll = []
    wisroll = []
    charroll = []
    i = 0
    cclass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Wizard"]
    race = ["Human", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling"]
    ability = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    ggender = ["Male", "Female", "Non-Binary"]
    crandom = input("Would you like your character to be real or a joke?")
    level = input("What level would you like your character to be?")
    repeat = input("Would you like to make more than one character?")
    
    if crandom == "joke":
        gggender = random.choice(ggender)
        ccclass = random.choice(cclass)
        rrace = random.choice(race)
        while i != 4:
            strength = random.randint(1,6)
            dexterity = random.randint(1,6)
            constitution = random.randint(1,6)
            intelligence = random.randint(1,6)
            wisdom = random.randint(1,6)
            charisma = random.randint(1,6)
            strroll.append(strength)
            dexroll.append(dexterity)
            conroll.append(constitution)
            introll.append(intelligence)
            wisroll.append(wisdom)
            charroll.append(charisma)            
            i += 1
            strroll.sort()
            dexroll.sort()
            conroll.sort()
            introll.sort()
            wisroll.sort()
            charroll.sort()
        if i == 4:
            pass

        stren = strroll[1] + strroll[2] + strroll[3]
        dext = dexroll[1] + dexroll[2] + dexroll[3]
        const = conroll[1] + conroll[2] + conroll[3]
        inte = introll[1] + introll[2] + introll[3]
        wisd = wisroll[1] + wisroll[2] + wisroll[3]
        charis = charroll[1] + charroll[2] + charroll[3]

    if crandom == "real":
        gggender = random.choice(ggender)
        rrace = random.choice(race)
        while i != 4:
            strength = random.randint(1,6)
            dexterity = random.randint(1,6)
            constitution = random.randint(1,6)
            intelligence = random.randint(1,6)
            wisdom = random.randint(1,6)
            charisma = random.randint(1,6)
            strroll.append(strength)
            dexroll.append(dexterity)
            conroll.append(constitution)
            introll.append(intelligence)
            wisroll.append(wisdom)
            charroll.append(charisma)            
            i += 1
            strroll.sort()
            dexroll.sort()
            conroll.sort()
            introll.sort()
            wisroll.sort()
            charroll.sort()
        if i == 4:
            pass

        stren = strroll[1] + strroll[2] + strroll[3]
        dext = dexroll[1] + dexroll[2] + dexroll[3]
        const = conroll[1] + conroll[2] + conroll[3]
        inte = introll[1] + introll[2] + introll[3]
        wisd = wisroll[1] + wisroll[2] + wisroll[3]
        charis = charroll[1] + charroll[2] + charroll[3]

        Strenlist = ["Barbarian", "Fighter"]
        Dexlist = ["Rogue", "Monk", "Ranger"]
        Intelist = ["Cleric", "Ranger", "Sorcerer", "Wizard", "Bard", "Druid"]
        Wislist = ["Druid", "Paladin", "Cleric", "Monk", "Sorcerer", "Wizard"]
        Charlist = ["Bard", "Barbarian", "Fighter", "Paladin", "Rogue"]
        Conlist = ["Barbarian", "Fighter", "Paladin", "Monk"]

        if max(stren, dext, const, inte, wisd, charis) is stren:
            ccclass = random.choice(Strenlist)
        if max(stren, dext, const, inte, wisd, charis) is dext:
            ccclass = random.choice(Dexlist)
        if max(stren, dext, const, inte, wisd, charis) is const:
            ccclass = random.choice(Conlist)
        if max(stren, dext, const, inte, wisd, charis) is inte:
            ccclass = random.choice(Intelist)
        if max(stren, dext, const, inte, wisd, charis) is wisd:
            ccclass = random.choice(Wislist)
        if max(stren, dext, const, inte, wisd, charis) is charis:
            ccclass = random.choice(Charlist)

    if ccclass == "Barbarian":
        HD = "1d12"
    if ccclass == "Bard":
        HD = "1d6"
    if ccclass == "Cleric":
        HD = "1d8"
    if ccclass == "Druid":
        HD = "1d8"
    if ccclass == "Fighter":
        HD = "1d10"
    if ccclass == "Monk":
        HD = "1d8"
    if ccclass == "Paladin":
        HD = "1d10"
    if ccclass == "Ranger":
        HD = "1d8"
    if ccclass == "Rogue":
        HD = "1d6"
    if ccclass == "Sorcerer":
        HD = "1d4"
    if ccclass == "Wizard":
        HD = "1d4"

    n = 0
    conmod = math.floor((const - 10) / 2)
    die = HD[2:4]
    totalhealth = 0
    if level !=0:
        while n != int(level):
            health = random.randint(1, int(die))
            totalhealth += health + int(conmod)
            n += 1
    
            if n == level:
                pass



    print("Your character is a " + gggender + " who is a " + ccclass + ", is " + rrace + " race and are level " + level + ". They have the following stats:  Strength: " + str(stren) + ", Dexterity: " + str(dext) + ", Constitution: " + str(const) + ", Intelligence: " + str(inte) + ", Wisdom: " + str(wisd) + ", Charisma: " + str(charis) + ".  This character's health is " + str(totalhealth) + ".  I hope this character works well for you!")

    if repeat =="no":
        print("Thank you for using Sir Westershire's Character Creation.  If this has pleased you, feel free to drop some gold in me pocket!")
        break