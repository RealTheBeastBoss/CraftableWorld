from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


class Item:
    def __init__(self, name, description, uses):
        self.name = name
        self.description = description
        self.id = 0
        self.discovered = False
        self.uses = uses


class Craft:
    def __init__(self, input1, input2, *outputs, **uses):
        self.input1 = input1
        self.input2 = input2
        self.outputs = outputs
        self.uses = uses


def clear_console():
    keyboard.press(Key.alt_l)
    keyboard.press('x')
    keyboard.release(Key.alt_l)
    keyboard.release('x')
    time.sleep(0.4)


def item_discovered(item):
    clear_console()
    print("Well Done! You have made an item!")
    print("")
    print("Item: " + item.name)
    print("Description: " + item.description)
    item.discovered = True
    inventory.append(item)
    global items_crafted
    items_crafted += 1
    print("")
    input("Press Enter to Continue: ")


def show_inventory():
    clear_console()
    print("Items Acquired: " + str(items_crafted) + "/" + str(TOTAL_ITEMS))
    print("")
    x = 1
    for item in inventory:
        item.id = x
        x += 1
    print("\t\t\tYour Inventory:")  # Item Uses in Inventory are temporary
    print("---------------------------------------")
    for i in range(0, len(inventory), 4):
        try:
            print(
                str(inventory[i].id) + ". " + inventory[i].name + " - " + str(inventory[i].uses) + "\t\t" + str(inventory[i + 1].id) + ". " + inventory[
                    i + 1].name + " - " + str(inventory[i + 1].uses) + "\t\t" + str(inventory[i + 2].id) + ". " + inventory[i + 2].name + " - " + str(inventory[i + 2].uses) + "\t\t" + str(
                    inventory[i + 3].id) + ". " + inventory[i + 3].name + " - " + str(inventory[i + 3].uses))
        except IndexError:
            try:
                print(str(inventory[i].id) + ". " + inventory[i].name + " - " + str(inventory[i].uses) + "\t\t" + str(inventory[i + 1].id) + ". " +
                      inventory[i + 1].name + " - " + str(inventory[i + 1].uses) + "\t\t" + str(inventory[i + 2].id) + ". " + inventory[i + 2].name + " - " + str(inventory[i + 2].uses))
            except IndexError:
                try:
                    print(str(inventory[i].id) + ". " + inventory[i].name + " - " + str(inventory[i].uses) + "\t\t" + str(inventory[i + 1].id) + ". " +
                          inventory[i + 1].name + " - " + str(inventory[i + 1].uses))
                except IndexError:
                    print(str(inventory[i].id) + ". " + inventory[i].name + " - " + str(inventory[i].uses))
    print("---------------------------------------")


def input_items():
    print("")
    x = 0
    z = 0
    found = False
    while not found:
        try:
            choice = input("Enter first item here: ")
            choice = int(choice)
            print("")
        except ValueError:
            print("")
        if type(choice) == type(x):  # If the player has entered an integer
            for item in inventory:
                if item.id == choice:
                    found = True
                    x = item.id - 1
        elif type(choice) == type(air.name):  # If the player has entered a string
            for item in inventory:
                if item.name.lower() == choice.lower():
                    found = True
                    x = item.id - 1
    found = False
    print("You have selected " + inventory[x].name)
    print("")
    while not found:
        try:
            choice = input("Enter second item here: ")
            choice = int(choice)
            print("")
        except ValueError:
            print("")
        if type(choice) == type(z):  # If the player has entered an integer
            for item in inventory:
                if item.id == choice:
                    found = True
                    z = item.id - 1
        elif type(choice) == type(air.name):  # If the player has entered a string
            for item in inventory:
                if item.name.lower() == choice.lower():
                    found = True
                    z = item.id - 1
    print("You have selected " + inventory[z].name)
    print("")
    create_item(inventory[x], inventory[z])


def check_depleted():
    for item in inventory:
        if item.uses == 0:
            deplete(item)


def deplete(item):
    clear_console()
    print("Item Depleted: " + item.name)
    print("You have made everything this item can make")
    print("")
    inventory.remove(item)
    input("Press Enter to Continue: ")


def create_item(item1, item2):
    for craft in crafts:
        if item1 == craft.input1 and item2 == craft.input2 or item1 == craft.input2 and item2 == craft.input1:
            for output in craft.outputs:
                if not output.discovered:
                    item_discovered(output)
                    if craft.outputs.index(output) == 0:
                        letter = 'a'
                    elif craft.outputs.index(output) == 1:
                        letter = 'b'
                    else:
                        letter = 'c'
                    for key, value in craft.uses.items():
                        if key[0] == letter:
                            value.uses -= int(key[2:])
                elif len(craft.outputs) == 1:
                    print("You have already discovered " + output.name)
                    input_items()
                else:
                    print("You have already discovered " + output.name)
                    input("Press Enter to Continue: ")
                    print("")
            return
    print("Sorry, " + item1.name + " and " + item2.name + " do not make anything")
    input_items()


# ITEMS:
air = Item("Air", "The stuff you breath in", 42)  # 22/42 Uses
water = Item("Water", "Hydrogen and Oxygen", 78)  # 24/78 Uses
earth = Item("Earth", "We love the Earth...", 56)  # 30/56 Uses
fire = Item("Fire", "Harry's Diss Tracks", 69)  # 43/69 Uses
steam = Item("Steam", "A gaming platform or the gas form of water", 14)  # 5/14 Uses, 4/4 Ways to Craft
pressure = Item("Pressure", "Life be like that sometimes", 31)  # 15/31 Uses, 5/5 Ways to Craft
geyser = Item("Geyser", "He's a right geyser, he is", 1)  # 1/1 Use, 2/4 Ways to Craft
puddle = Item("Puddle", "Peppa Pig approves", 15)  # 3/15 Uses, 2/2 Ways to Craft
pond = Item("Pond", "The Doctor's Companion", 20)  # 3/20 Uses, 4/4 Ways to Craft
lake = Item("Lake", "There might be a monster in there", 47)  # 10/47 Uses, 4/4 Ways to Craft
sea = Item("Sea", "The third letter of the alphabet", 65)  # 13/65 Uses, 4/4 Ways to Craft
ocean = Item("Ocean", "Ocean man...", 64)  # 11/64 Uses, 3/4 Ways to Craft
land = Item("Land", "Fallen Kingdom", 25)  # 14/25 Uses, 5/5 Ways to Craft
continent = Item("Continent", "So, basically... Your Mother", 9)  # 4/9 Uses, 3/4 Ways to Craft
planet = Item("Planet", "...It is our planet", 25)  # 14/25 Uses, 5/5 Ways to Craft
solar_system = Item("Solar System", "One of many Chocolate bar references", 13)  # 8/13 Uses, 2/9 Ways to Craft
galaxy = Item("Galaxy", "Another chocolate reference", 6)  # 3/6 Uses, 3/9 Ways to Craft
galaxy_cluster = Item("Galaxy Cluster", "A box of chocolates", 5)  # 3/5 Uses, 1/2 Ways to Craft
universe = Item("Universe", "Shut up woman, get on my horse", 3)  # 2/3 Uses, 1/3 Ways to Craft
energy = Item("Energy", "NRG", 26)  # 10/26 Uses, 4/4 Ways to Craft
heat = Item("Heat", "Don't burn yourself", 29)  # 10/29 Uses, 4/4 Ways to Craft
lava = Item("Lava", "The floor", 17)  # 15/17 Uses, 2/3 Ways to Craft
stone = Item("Stone", "Fine, I'll do it myself", 57)  # 23/57 Uses, 2/3 Ways to Craft
metal = Item("Metal", "A type of music", 81)  # 21/81 Uses, 2/5 Ways to Craft
mud = Item("Mud", "Somebody once told me...", 11)  # 2/11 Uses, 2/2 Ways to Craft
clay = Item("Clay", "Do do doo do", 11)  # 1/11 Uses, 5/7 Ways to Craft
primordial_soup = Item("Primordial Soup", "Good Soup", 7)  # 6/7 Uses, 6/6 Ways to Craft
life = Item("Life", "Hope you get lucky", 41)  # 17/41 Uses, 12/12 Ways to Craft
human = Item("Human", "Nothin' but Rag N Bones", 191)  # 33/191 Uses, 3/5 Ways to Craft
tool = Item("Tool", "Aren't we all", 97)  # 35/97 Uses, 9/9 Ways to Craft
wheel = Item("Wheel", "The wheels in the game go round and round", 35)  # 6/35 Uses, 5/7 Ways to Craft
time_item = Item("Time", "Don't let it run out", 62)  # 12/62 Uses
science = Item("Science", "Nothing to do with rockets", 29)  # 15/29 Uses, 1/3 Ways to Craft
gas = Item("Gas", "Unfortunately, I've already used up my 'Your Mum' joke", 3)  # 2/3 Uses, 2/3 Ways to Craft
smoke = Item("Smoke", "It's bad for you", 14)  # 2/14 Uses, 5/9 Ways to Craft
atmosphere = Item("Atmosphere", "Watch out for Sontarans", 30)  # 10/30 Uses, 2/2 Ways to Craft
cloud = Item("Cloud", "No silver linings for you", 25)  # 10/25 Uses, 4/4 Ways to Craft
sky = Item("Sky", "Mr. Blue Sky", 46)  # 22/46 Uses, 4/4 Ways to Craft
sun = Item("Sun", "Boring Newspaper", 50)  # 19/50 Uses, 4/7 Ways to Craft
obsidian = Item("Obsidian", "Ice Bucket Challenge", 0)  # 0 Uses, 2/3 Ways to Craft
mist = Item("Mist", "Hit or Mist, I guess the never mist huh", 3)  # 3/3 Uses, 3/3 Ways to Craft
horizon = Item("Horizon", "Microsoft's second best game series", 0)  # 0 Uses, 6/6 Ways to Craft
aurora = Item("Aurora", "Steamed Hams Reference", 0)  # 0 Uses, 2/7 Ways to Craft
space = Item("Space", "' '", 29)  # 6/29 Uses, 1/5 Ways to Craft
sand = Item("Sand", "Omega is still counting them to this day", 43)  # 8/43 Uses, 7/7 Ways to Craft
moon = Item("Moon", "The Big Cheese", 14)  # 3/14 Uses, 4/9 Ways to Craft
eclipse = Item("Eclipse", "Not to be confused with...", 0)  # 0 Uses, 1/1 Ways to Craft
rain = Item("Rain", "An old man is snoring", 29)  # 8/29 Uses, 3/3 Ways to Craft
lightning = Item("Lightning", "It comes before the Thunder", 11)  # 8/11 Uses, 7/7 Ways to Craft
electricity = Item("Electricity", "The Thinker's Enemy", 51)  # 22/51 Uses, 3/10 Ways to Craft
ozone = Item("Ozone", "Earth is like Ogres, it has layers", 1)  # 1/1 Use, 4/4 Ways to Craft
storm = Item("Storm", "The Capitol? Oh, you mean the weather thing", 21)  # 8/21 Uses, 4/4 Ways to Craft
wind = Item("Wind", "The Slitheen be like...", 39)  # 9/39 Uses, 3/3 Ways to Craft
motion = Item("Motion", "Going through it", 22)  # 7/22 Uses, 3/9 Ways to Craft
idea = Item("Idea", "A Java IDE", 8)  # 4/8 Uses, 7/31 Ways to Craft
philosophy = Item("Philosophy", "Hold on, I'm thinking", 36)  # 29/36 Uses, 1/3 Ways to Craft
big = Item("Big", "Ur Mum", 39)  # 11/39 Uses, 6/6 Ways to Craft
small = Item("Small", "Alfie", 31)  # 12/31 Uses, 3/12 Ways to Craft
gold = Item("Gold", "Cybermen flee before it", 12)  # 0/12 Uses, 8/12 Ways to Craft
machine = Item("Machine", "An Automatic Tool", 39)  # 3/39 Uses, 2/7 Ways to Craft
car = Item("Car", "Vroom Vroom", 39)  # 0/39 Uses, 2/9 Ways to Craft
glass = Item("Glass", "Dangerously Fragile", 54)  # 10/54 Uses, 4/4 Ways to Craft
glasses = Item("Glasses", "A Surprisingly Effective Disguise", 22)  # 1/22 Uses, 4/6 Ways to Craft
mirror = Item("Mirror", "Subject of the worst comeback remarks", 1)  # 0/1 Use, 3/3 Ways to Craft
hacker = Item("Hacker", "CBBC's Dog", 6)  # 5/6 Uses, 3/4 Ways to Craft
computer = Item("Computer", "Back in my day these were women", 14)  # 5/14 Uses, 3/5 Ways to Craft
internet = Item("Internet", "Welcome!", 4)  # 1/4 Uses, 1/4 Ways to Craft
animal = Item("Animal", "Boris", 83)  # 11/83 Uses, 1/6 Ways to Craft
soil = Item("Soil", "Don't soil yourself!", 11)  # 10/11 Uses, 4/4 Ways to Craft
meat = Item("Meat", "Waltuh, put your meat away Waltuh!", 17)  # 0/17 Uses, 5/41 Ways to Craft
sloth = Item("Sloth", "Slow but Deadly", 0)  # 0 Uses, 1/2 Ways to Craft
plant = Item("Plant", "The Bane of EVE", 63)  # 10/63 Uses, 2/10 Ways to Craft
ash = Item("Ash", "Ashes to Ashes, Dust to Dust", 3)  # 1/3 Uses, 3/11 Ways to Craft
tobacco = Item("Tobacco", "Killing you Softly", 3)  # 0/3 Uses, 1/3 Ways to Craft
dust = Item("Dust", "I don't feel so good", 5)  # 2/5 Uses, 3/3 Ways to Craft
field = Item("Field", "Databases Again!?", 33)  # 0/33 Uses, 3/9 Ways to Craft
gunpowder = Item("Gunpowder", "Gun Fuel", 13)  # 3/13 Uses, 5/5 Ways to Craft
explosion = Item("Explosion", "Geronimo!", 21)  # 2/21 Uses, 4/10 Ways to Craft
lightbulb = Item("Light Bulb", "What an Idea?", 8)  # 4/8 Uses, 1/3 Ways to Craft
light = Item("Light", "This blinded The Weekend?", 35)  # 15/35 Uses, 1/2 Ways to Craft
spotlight = Item("Spotlight", "Main Character Moment", 4)  # 0/4 Uses, 3/3 Ways to Craft
organic_matter = Item("Organic Matter", "Stuff that Life is made of", 10)  # 10/10 Uses, 3/4 Ways to Craft
mineral = Item("Mineral", "Eat your Cereal, Kids", 10)  # 7/10 Uses, 4/6 Ways to Craft
steel = Item("Steel", "Stop, Thief!", 74)  # 18/74 Uses, 4/4 Ways to Craft
coal = Item("Coal", "Cold Diamonds", 6)  # 3/6 Uses, 1/6 Ways to Craft
charcoal = Item("Charcoal", "Post-2020 Australia", 4)  # 4/4 Uses, 4/4 Ways to Craft
tree = Item("Tree", "Useless Superpower", 61)  # 14/61 Uses, 3/4 Ways to Craft
oxygen = Item("Oxygen", "It made The Doctor blind", 11)  # 3/11 Uses, 2/8 Ways to Craft
sunflower = Item("Sunflower", "Circle Plants", 7)  # 0/7 Uses, 1/2 Ways to Craft
wood = Item("Wood", "POV: you just woke up", 74)  # 21/74 Uses, 4/9 Ways to Craft
campfire = Item("Campfire", "Typically used to regain health", 25)  # 8/25 Uses, 1/1 Way to Craft
lumberjack = Item("Lumberjack", "The chin boi from Hoodwinked", 8)  # 4/8 Uses, 3/4 Ways to Craft
axe = Item("Axe", "Wood Destroyer... not like that though", 20)  # 13/20 Uses, 4/4 Ways to Craft
pebble = Item("Pebble", "Our size in the Universe", 6)  # 6/6 Uses, 3/3 Ways to Craft
rock = Item("Rock", "Makes bald jokes and gets slapped by Will Smith", 38)  # 16/38 Uses, 3/3 Ways to Craft
blade = Item("Blade", "Vampire Trilogy", 45)  # 6/45 Uses, 4/4 Ways to Craft
sword = Item("Sword", "Sharp Stick", 44)  # 9/44 Uses, 3/3 Ways to Craft
granite = Item("Granite", "Old Girl's Night", 0)  # 0 Uses, 3/3 Ways to Craft
eruption = Item("Eruption", "A Failed November", 0)  # 0 Uses, 3/3 Ways to Craft
volcano = Item("Volcano", "Dr. Evil's Evil Lair", 12)  # 5/12 Uses, 1/8 Ways to Craft
boulder = Item("Boulder", "Subject of Chris Rock's Jokes", 14)  # 2/14 Uses, 5/6 Ways to Craft
corpse = Item("Corpse", "The Guy with the Deep Voice", 33)  # 3/33 Uses, 4/7 Ways to Craft
blood = Item("Blood", "I Hated Coding this Item", 13)  # 0/13 Uses, 1/2 Ways to Craft
death = Item("Death", "One of Life's Constants", 7)  # 4/7 Uses, 2/5 Ways to Craft
phoenix = Item("Phoenix", "Bringer of Fire and Priori Incantatem", 1)  # 1/1 Uses, 3/4 Ways to Craft
egg = Item("Egg", "Alfred is the best Eggman", 41)  # 15/41 Uses, 2/35 Ways to Craft
omelette = Item("Omelette", "Crackin' Eggs", 0)  # 0 Uses, 3/3 Ways to Craft
fish = Item("Fish", "There's Plenty!", 33)  # 10/33 Uses, 8/8 Ways to Craft
roe = Item("Roe", "Fish Eggs", 2)  # 0/2 Uses, 5/6 Ways to Craft
fishing_rod = Item("Fishing Rod", "Oldschool PVP Strats", 3)  # 0/3 Uses, 2/12 Ways to Craft
rainbow = Item("Rainbow", "Gay?", 23)  # 4/23 Uses, 5/7 Ways to Craft
magic = Item("Magic", "Avada Kedavra!!", 13)  # 1/13 Uses, 1/4 Ways to Craft
wizard = Item("Wizard", "Yer a Wizard, Harry", 11)  # 5/11 Uses, 2/4 Ways to Craft
wand = Item("Wand", "Not like that though", 0)  # 0 Uses, 4/4 Ways to Craft
pencil = Item("Pencil", "Fear Her", 13)  # 1/13 Uses, 2/2 Ways to Craft
items = [air, water, earth, fire, steam, pressure, geyser, puddle, pond, lake, sea, ocean, land, continent, planet, solar_system, galaxy, galaxy_cluster, universe, energy, heat, lava, stone, metal, mud, clay, primordial_soup,
         life, human, tool, wheel, time_item, science, gas, smoke, atmosphere, cloud, sky, sun, obsidian, mist, horizon, aurora, space, sand, moon, eclipse, rain, lightning, electricity, ozone, storm, wind, motion, idea,
         philosophy, big, small, gold, machine, car, glass, glasses, mirror, hacker, computer, internet, animal, soil, meat, sloth, plant, ash, tobacco, dust, field, gunpowder, explosion, lightbulb, light, spotlight,
         organic_matter, mineral, steel, coal, charcoal, tree, oxygen, sunflower, wood, campfire, lumberjack, axe, pebble, rock, blade, sword, granite, eruption, volcano, boulder, corpse, blood, death, phoenix, egg, omelette,
         fish, roe, fishing_rod, rainbow, magic, wizard, wand, pencil]
# CRAFTS:
steam1 = Craft(fire, water, steam, aa4=water, aa1=fire, ab1=gas, ac1=heat, ad1=lava)  # Fire + Water = Steam
steam2 = Craft(gas, water, steam, aa4=water, aa1=fire, ab1=gas, ac1=heat, ad1=lava)  # Gas + Water = Steam
steam3 = Craft(heat, water, steam, aa4=water, aa1=fire, ab1=gas, ac1=heat, ad1=lava)  # Heat + Water = Steam
steam_obsidian = Craft(lava, water, steam, obsidian, aa4=water, aa1=fire, ab1=gas, ac1=heat, ad1=lava, ba3=lava, ba1=water, bb1=glass)  # Cold - B1 Lava + Water = Steam and Obsidian
pressure1 = Craft(air, air, pressure, aa2=air, ab2=atmosphere, aa1=geyser, ab1=science, ac1=ocean)  # Air x2 = Pressure
pressure2 = Craft(air, atmosphere, pressure, aa2=air, ab2=atmosphere, aa1=geyser, ab1=science, ac1=ocean)  # Air + Atmosphere = Pressure
pressure3 = Craft(science, geyser, pressure, aa2=air, ab2=atmosphere, aa1=geyser, ab1=science, ac1=ocean)  # Science + Geyser = Pressure
pressure4 = Craft(atmosphere, atmosphere, pressure, aa2=air, ab2=atmosphere, aa1=geyser, ab1=science, ac1=ocean)  # Atmosphere x2 = Pressure
pressure5 = Craft(ocean, ocean, pressure, aa2=air, ab2=atmosphere, aa1=geyser, ab1=science, ac1=ocean)  # Ocean x2 = Pressure
geyser1 = Craft(steam, earth, geyser, aa4=steam, aa1=earth, ab1=pressure)  # Hill - 1, Mountain - 1 Steam + Earth = Geyser
geyser2 = Craft(steam, pressure, geyser, aa4=steam, aa1=earth, ab1=pressure)  # Hill - 1, Mountain - 1 Steam + Pressure = Geyser
puddle1 = Craft(water, water, puddle, aa1=water, ab1=pond, ac1=small)  # Water x2 = Puddle
puddle2 = Craft(small, pond, puddle, aa1=water, ab1=pond, ac1=small)  # Small + Pond = Puddle
pond1 = Craft(puddle, puddle, pond, aa3=puddle, aa1=water, ab1=lake, ac1=big, ad1=small)  # Puddle x2 = Pond
pond2 = Craft(puddle, water, pond, aa3=puddle, aa1=water, ab1=lake, ac1=big, ad1=small)  # Puddle + Water = Pond
pond3 = Craft(puddle, big, pond, aa3=puddle, aa1=water, ab1=lake, ac1=big, ad1=small)  # Puddle + Big = Pond
pond4 = Craft(small, lake, pond, aa3=puddle, aa1=water, ab1=lake, ac1=big, ad1=small)  # Small + Lake = Pond
lake1 = Craft(pond, pond, lake, aa3=pond, aa1=water, ab1=sea, ac1=big, ad1=small)  # Pond x2 = Lake
lake2 = Craft(pond, water, lake, aa3=pond, aa1=water, ab1=sea, ac1=big, ad1=small)  # Pond + Water = Lake
lake3 = Craft(pond, big, lake, aa3=pond, aa1=water, ab1=sea, ac1=big, ad1=small)  # Pond + Big = Lake
lake4 = Craft(sea, small, lake, aa3=pond, aa1=water, ab1=sea, ac1=big, ad1=small)  # Sea + Small = Lake
sea1 = Craft(lake, lake, sea, aa3=lake, aa1=water, ab1=ocean, ac1=big, ad1=small)  # Lake x2 = Sea
sea2 = Craft(lake, water, sea, aa3=lake, aa1=water, ab1=ocean, ac1=big, ad1=small)  # Lake + Water = Sea
sea3 = Craft(lake, big, sea, aa3=lake, aa1=water, ab1=ocean, ac1=big, ad1=small)  # Lake + Big = Sea
sea4 = Craft(ocean, small, sea, aa3=lake, aa1=water, ab1=ocean, ac1=big, ad1=small)  # Ocean + Small = Sea
ocean1 = Craft(sea, sea, ocean, aa3=sea, aa1=water, ab1=big)  # Container - 1, Tide - 1 Sea x2 = Ocean
ocean2 = Craft(sea, water, ocean, aa3=sea, aa1=water, ab1=big)  # Container - 1, Tide - 1 Sea + Water = Ocean
ocean3 = Craft(sea, big, ocean, aa3=sea, aa1=water, ab1=big)  # Container - 1, Tide - 1 Sea + Big = Ocean
land1 = Craft(earth, earth, land, aa2=earth, ab2=soil, aa1=continent, ab1=stone, ac1=big, ad1=small)  # Earth x2 = Land
land2 = Craft(earth, stone, land, aa2=earth, ab2=soil, aa1=continent, ab1=stone, ac1=big, ad1=small)  # Earth + Stone = Land
land3 = Craft(small, continent, land, aa2=earth, ab2=soil, aa1=continent, ab1=stone, ac1=big, ad1=small)  # Small + Continent = Land
land4 = Craft(soil, big, land, aa2=earth, ab2=soil, aa1=continent, ab1=stone, ac1=big, ad1=small)  # Soil + Big = Land
land5 = Craft(soil, soil, land, aa2=earth, ab2=soil, aa1=continent, ab1=stone, ac1=big, ad1=small)  # Soil x2 = Land
continent1 = Craft(land, land, continent, aa3=land, aa1=earth, ab1=big)  # Mountain Range - 1 Land x2 = Continent
continent2 = Craft(land, earth, continent, aa3=land, aa1=earth, ab1=big)  # Mountain Range - 1 Land + Earth = Continent
continent3 = Craft(land, big, continent, aa3=land, aa1=earth, ab1=big)  # Mountain Range - 1 Land + Big = Continent
planet1 = Craft(continent, continent, planet, aa3=earth, aa2=continent, aa1=ocean, ab1=sky, ac1=space, ad1=solar_system)  # Continent x2 = Planet
planet2 = Craft(continent, ocean, planet, aa3=earth, aa2=continent, aa1=ocean, ab1=sky, ac1=space, ad1=solar_system)  # Continent + Ocean = Planet
planet3 = Craft(earth, solar_system, planet, aa3=earth, aa2=continent, aa1=ocean, ab1=sky, ac1=space, ad1=solar_system)  # Earth + Solar System = Planet
planet4 = Craft(earth, space, planet, aa3=earth, aa2=continent, aa1=ocean, ab1=sky, ac1=space, ad1=solar_system)  # Earth + Space = Planet
planet_horizon = Craft(earth, sky, planet, horizon, aa3=earth, aa2=continent, aa1=ocean, ab1=sky, ac1=space, ad1=solar_system, ba6=sky, ba1=earth, bb1=continent, bc1=lake, bd1=land, be1=ocean, bf1=sea)  # Earth + Sky = Planet and Horizon
solarsystem1 = Craft(planet, planet, solar_system, aa3=planet, aa2=sun)  # Container - 7, Jupiter - 1, Mars - 1, Mercury - 1, Saturn - 1, Venus - 1 Planet x2 = Solar System
solarsystem2 = Craft(planet, sun, solar_system, aa3=planet, aa2=sun)  # Container - 7, Jupiter - 1, Mars - 1, Mercury - 1, Saturn - 1, Venus - 1 Planet + Sun = Solar System
galaxy1 = Craft(space, solar_system, galaxy, aa4=solar_system, aa3=space)  # Star - 4, Container - 3, Supernova - 1 Space + Solar System = Galaxy
galaxy2 = Craft(solar_system, solar_system, galaxy, aa4=solar_system, aa3=space)  # Star - 4, Container - 3, Supernova - 1 Solar System x2 = Galaxy
galaxy3 = Craft(space, space, galaxy, aa4=solar_system, aa3=space)  # Star - 4, Container - 3, Supernova - 1 Space x2 = Galaxy
galaxycluster1 = Craft(galaxy, galaxy, galaxy_cluster, aa2=galaxy)  # Container - 1 Galaxy x2 = Galaxy Cluster
universe1 = Craft(galaxy_cluster, galaxy_cluster, universe, aa2=galaxy_cluster, aa1=space)  # Container - 1 Galaxy Cluster x2 = Universe
energy1 = Craft(fire, fire, energy, aa3=fire, aa2=science, aa1=heat, ab1=atmosphere)  # Fire x2 = Energy
energy2 = Craft(fire, atmosphere, energy, aa3=fire, aa2=science, aa1=heat, ab1=atmosphere)  # Fire + Atmosphere = Energy
energy3 = Craft(science, heat, energy, aa3=fire, aa2=science, aa1=heat, ab1=atmosphere)  # Science + Heat = Energy
energy_heat = Craft(science, fire, energy, heat, aa3=fire, aa2=science, aa1=heat, ab1=atmosphere, ba2=fire, ba1=energy, bb1=air, bc1=lava, bd1=science, be1=idea, bf1=philosophy)  # Science + Fire = Energy and Heat
heat1 = Craft(air, energy, heat, aa2=fire, aa1=energy, ab1=air, ac1=lava, ad1=science, ae1=idea, af1=philosophy)  # Air + Energy = Heat
heat2 = Craft(idea, fire, heat, aa2=fire, aa1=energy, ab1=air, ac1=lava, ad1=science, ae1=idea, af1=philosophy)  # Idea + Fire = Heat
heat3 = Craft(philosophy, lava, heat, aa2=fire, aa1=energy, ab1=air, ac1=lava, ad1=science, ae1=idea, af1=philosophy)  # Philosophy + Lava = Heat
lava1 = Craft(earth, fire, lava, aa3=earth, aa1=fire, ab1=heat)  # Liquid - 1 Earth + Fire = Lava
lava2 = Craft(earth, heat, lava, aa3=earth, aa1=fire, ab1=heat)  # Liquid - 1 Earth + Heat = Lava
stone1 = Craft(air, lava, stone, aa2=earth, aa1=air, ab1=lava, ac1=pressure)  # Solid - 1 Air + Lava = Stone
stone2 = Craft(earth, pressure, stone, aa2=earth, aa1=air, ab1=lava, ac1=pressure)  # Solid - 1 Earth + Pressure = Stone
metal1 = Craft(fire, stone, metal, aa2=fire, ab2=stone, ac2=heat, aa1=tool)  # Ore - 3 Fire + Stone = Metal
metal2 = Craft(heat, stone, metal, aa2=fire, ab2=stone, ac2=heat, aa1=tool)  # Ore - 3 Heat + Stone = Metal
mud1 = Craft(earth, water, mud, aa2=water, aa1=earth, ab1=soil)  # Earth + Water = Mud
mud2 = Craft(soil, water, mud, aa2=water, aa1=earth, ab1=soil)  # Soil + Water = Mud
clay1 = Craft(mud, stone, clay, aa3=stone, ab3=mineral, aa2=mud, ab2=sand, ac2=rock)  # Liquid - 2 Mud + Stone = Clay
clay2 = Craft(mud, sand, clay, aa3=stone, ab3=mineral, aa2=mud, ab2=sand, ac2=rock)  # Liquid - 2 Mud + Sand = Clay
clay3 = Craft(mineral, sand, clay, aa3=stone, ab3=mineral, aa2=mud, ab2=sand, ac2=rock)  # Liquid - 2 Mineral + Sand = Clay
clay4 = Craft(mineral, stone, clay, aa3=stone, ab3=mineral, aa2=mud, ab2=sand, ac2=rock)  # Liquid - 2 Mineral + Stone = Clay
clay5 = Craft(mineral, rock, clay, aa3=stone, ab3=mineral, aa2=mud, ab2=sand, ac2=rock)  # Liquid - 2 Mineral + Rock = Clay
primordialsoup1 = Craft(earth, ocean, primordial_soup, aa3=ocean, ab3=sea, aa2=earth, ab2=lava, ac2=planet)  # Earth + Ocean = Primordial Soup
primordialsoup2 = Craft(earth, sea, primordial_soup, aa3=ocean, ab3=sea, aa2=earth, ab2=lava, ac2=planet)  # Earth + Sea = Primordial Soup
primordialsoup3 = Craft(lava, ocean, primordial_soup, aa3=ocean, ab3=sea, aa2=earth, ab2=lava, ac2=planet)  # Lava + Ocean = Primordial Soup
primordialsoup4 = Craft(lava, sea, primordial_soup, aa3=ocean, ab3=sea, aa2=earth, ab2=lava, ac2=planet)  # Lava + Sea = Primordial Soup
primordialsoup5 = Craft(planet, ocean, primordial_soup, aa3=ocean, ab3=sea, aa2=earth, ab2=lava, ac2=planet)  # Planet + Ocean = Primordial Soup
primordialsoup6 = Craft(planet, sea, primordial_soup, aa3=ocean, ab3=sea, aa2=earth, ab2=lava, ac2=planet)  # Planet + Sea = Primordial Soup
life1 = Craft(energy, primordial_soup, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Energy + Primordial Soup = Life
life2 = Craft(time_item, primordial_soup, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Time + Primordial Soup = Life
life3 = Craft(lightning, lake, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Lightning + Lake = Life
life4 = Craft(lightning, ocean, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Lightning + Ocean = Life
life5 = Craft(lightning, primordial_soup, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Lightning + Primordial Soup = Life
life6 = Craft(lightning, sea, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Lightning + Sea = Life
life7 = Craft(electricity, lake, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Electricity + Lake = Life
life8 = Craft(electricity, ocean, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Electricity + Ocean = Life
life9 = Craft(electricity, primordial_soup, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Electricity + Primordial Soup = Life
life10 = Craft(electricity, sea, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Electricity + Sea = Life
life11 = Craft(storm, primordial_soup, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Storm + Primordial Soup = Life
life12 = Craft(volcano, primordial_soup, life, aa6=primordial_soup, aa4=electricity, ab4=lightning, aa2=lake, ab2=ocean, ac2=sea, aa1=time_item, ab1=storm, ac1=volcano)  # Volcano + Primordial Soup = Life
human1 = Craft(clay, life, human, aa2=time_item, ab2=tool, ac2=animal, aa1=clay, ab1=life)  # Monkey - 2 Clay + Life = Human
human_meat = Craft(animal, tool, human, meat, aa2=time_item, ab2=tool, ac2=animal, aa1=clay, ab1=life, ba10=tool, bb10=axe, ba6=sword, ba4=animal, bb4=fish)  # Monkey - 2, Butcher - B10, Chicken - B4, Cow - B4, Flying Fish - B4,
# Frog - B3, Livestock - B4, Net - B5, Pig - B4, Shark - B5, Piranha - B1, Swordfish - B4 Animal + Tool = Human and Meat
human_sloth = Craft(animal, time, human, sloth, aa2=time_item, ab2=tool, ac2=animal, aa1=clay, ab1=life, ba1=animal, bb1=time_item, bc1=tree)  # Monkey - 2, Manatee - B1 Animal + Time = Human and Sloth
tool1 = Craft(human, metal, tool, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock)  # Human + Metal = Tool
tool2 = Craft(human, stone, tool, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock)  # Human + Stone = Tool
tool3 = Craft(human, steel, tool, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock)  # Human + Steel = Tool
tool4 = Craft(wood, metal, tool, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock)  # Wood + Metal = Tool
tool5 = Craft(wood, steel, tool, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock)  # Wood + Steel = Tool
tool6 = Craft(rock, human, tool, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock)  # Rock + Human = Tool
tool7 = Craft(rock, wood, tool, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock)  # Rock + Wood = Tool
tool_lumberjack = Craft(human, wood, tool, lumberjack, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock, ba4=human, ba1=tree, bb1=wood, bc1=axe)  # Chainsaw - B1 Human + Wood = Tool and Lumberjack
tool_axe = Craft(stone, wood, tool, axe, aa5=human, ab5=wood, aa2=metal, ab2=stone, ac2=steel, ad2=rock, ba3=wood, ba2=tool, ba1=lumberjack, bb1=stone, bc1=blade)  # Stone + Wood = Tool and Axe
wheel1 = Craft(tool, water, wheel, aa4=tool, ab4=motion, aa1=water, ab1=metal, ac1=stone, ad1=steel)  # River - 1, Stream - 1 Tool + Water = Wheel
wheel2 = Craft(motion, metal, wheel, aa4=tool, ab4=motion, aa1=water, ab1=metal, ac1=stone, ad1=steel)  # River - 1, Stream - 1 Motion + Metal = Wheel
wheel3 = Craft(motion, stone, wheel, aa4=tool, ab4=motion, aa1=water, ab1=metal, ac1=stone, ad1=steel)  # River - 1, Stream - 1 Motion + Stone = Wheel
wheel4 = Craft(motion, tool, wheel, aa4=tool, ab4=motion, aa1=water, ab1=metal, ac1=stone, ad1=steel)  # River - 1, Stream - 1 Motion + Tool = Wheel
wheel5 = Craft(motion, steel, wheel, aa4=tool, ab4=motion, aa1=water, ab1=metal, ac1=stone, ad1=steel)  # River - 1, Stream - 1 Motion + Steel = Wheel
science1 = Craft(human, universe, science, aa3=human, aa1=universe)  # Microscope - 1, Telescope - 1 Human + Universe = Science
gas1 = Craft(air, science, gas, aa2=air, aa1=science, ab1=energy, ac1=idea)  # Liquid - 1 Air + Science = Gas
gas2 = Craft(air, idea, gas, aa2=air, aa1=science, ab1=energy, ac1=idea)  # Liquid - 1 Air + Idea = Gas
smoke1 = Craft(gas, earth, smoke, aa5=fire, aa3=campfire, aa1=air, ab1=gas, ac1=time_item, ad1=water, ae1=storm, af1=plant, ag1=tree, ah1=wood)  # Grass - 1 Gas + Earth = Smoke
smoke2 = Craft(air, fire, smoke, aa5=fire, aa3=campfire, aa1=air, ab1=gas, ac1=time_item, ad1=water, ae1=storm, af1=plant, ag1=tree, ah1=wood)  # Grass - 1 Air + Fire = Smoke
smoke_ash_tobacco = Craft(fire, plant, smoke, ash, tobacco, aa5=fire, aa3=campfire, aa1=air, ab1=gas, ac1=time_item, ad1=water, ae1=storm, af1=plant, ag1=tree, ah1=wood, ba5=fire, bb5=campfire, ba1=plant, bb1=rain, bc1=storm, bd1=time_item, be1=water, bf1=sun, bg1=mineral, bh1=tree, ca2=smoke, cb2=plant, ca1=fire)
# Grass - 1, Paper - B3, Vampire - B2, Dawn - B1, Grass - B1, Grass - C1 Fire + Plant = Smoke and Ash and Tobacco
smoke_ash_charcoal = Craft(tree, fire, smoke, ash, charcoal, aa5=fire, aa3=campfire, aa1=air, ab1=gas, ac1=time_item, ad1=water, ae1=storm, af1=plant, ag1=tree, ah1=wood, ba5=fire, bb5=campfire, ba1=plant, bb1=rain, bc1=storm, bd1=time_item, be1=water, bf1=sun, bg1=mineral, bh1=tree, ca4=fire, ca1=organic_matter, cb1=tree, cc1=wood, cd1=corpse)
# Grass - 1, Paper - B3, Vampire - B2, Dawn - B1, Grass - B1 Tree + Fire = Smoke and Ash and Charcoal
atmosphere1 = Craft(air, planet, atmosphere, aa2=air, aa1=planet, ab1=sky)  # Air + Planet = Atmosphere
atmosphere2 = Craft(air, sky, atmosphere, aa2=air, aa1=planet, ab1=sky)  # Air + Sky = Atmosphere
cloud1 = Craft(atmosphere, water, cloud, aa2=atmosphere, ab2=water, ac2=mist, ad2=sky)  # Atmosphere + Water = Cloud
cloud2 = Craft(atmosphere, mist, cloud, aa2=atmosphere, ab2=water, ac2=mist, ad2=sky)  # Atmosphere + Mist = Cloud
cloud3 = Craft(sky, mist, cloud, aa2=atmosphere, ab2=water, ac2=mist, ad2=sky)  # Sky + Mist = Cloud
cloud4 = Craft(sky, water, cloud, aa2=atmosphere, ab2=water, ac2=mist, ad2=sky)  # Sky + Water = Cloud
sky1 = Craft(cloud, air, sky, aa2=cloud, ab2=atmosphere, ac2=sun, aa1=air, ab1=moon)  # Cloud + Air = Sky
sky2 = Craft(cloud, atmosphere, sky, aa2=cloud, ab2=atmosphere, ac2=sun, aa1=air, ab1=moon)  # Cloud + Atmosphere = Sky
sky_aurora = Craft(sun, atmosphere, sky, aurora, aa2=cloud, ab2=atmosphere, ac2=sun, aa1=air, ab1=moon, ba4=electricity, ba3=sky, ba2=atmosphere, ba1=sun)  # Antarctica - B2, Arctic - B2 Sun + Atmosphere = Sky and Aurora
sky_eclipse = Craft(moon, sun, sky, eclipse, aa2=cloud, ab2=atmosphere, ac2=sun, aa1=air, ab1=moon, ba1=moon, bb1=sun)  # Moon + Sun = Sky and Eclipse
sun1 = Craft(fire, planet, sun, aa3=sky, ab3=light, aa2=fire, ab2=planet, aa1=space)  # Day - 3, Fire + Planet = Sun
sun2 = Craft(fire, sky, sun, aa3=sky, ab3=light, aa2=fire, ab2=planet, aa1=space)  # Day - 3, Fire + Sky = Sun
sun3 = Craft(light, planet, sun, aa3=sky, ab3=light, aa2=fire, ab2=planet, aa1=space)  # Day - 3, Light + Planet = Sun
sun4 = Craft(light, sky, sun, aa3=sky, ab3=light, aa2=fire, ab2=planet, aa1=space)  # Day - 3, Light + Sky = Sun
obsidian1 = Craft(lava, glass, obsidian, aa3=lava, aa1=water, ab1=glass)  # Cold - 1 Lava + Glass = Obsidian
mist1 = Craft(air, steam, mist, aa3=air, aa1=steam, ab1=water, ac1=rain)  # Air + Steam = Mist
mist2 = Craft(air, water, mist, aa3=air, aa1=steam, ab1=water, ac1=rain)  # Air + Water = Mist
mist3 = Craft(air, rain, mist, aa3=air, aa1=steam, ab1=water, ac1=rain)  # Air + Rain = Mist
horizon1 = Craft(continent, sky, horizon, aa6=sky, aa1=earth, ab1=continent, ac1=lake, ad1=land, ae1=ocean, af1=sea)  # Continent + Sky = Horizon
horizon2 = Craft(lake, sky, horizon, aa6=sky, aa1=earth, ab1=continent, ac1=lake, ad1=land, ae1=ocean, af1=sea)  # Lake + Sky = Horizon
horizon3 = Craft(land, sky, horizon, aa6=sky, aa1=earth, ab1=continent, ac1=lake, ad1=land, ae1=ocean, af1=sea)  # Land + Sky = Horizon
horizon4 = Craft(ocean, sky, horizon, aa6=sky, aa1=earth, ab1=continent, ac1=lake, ad1=land, ae1=ocean, af1=sea)  # Ocean + Sky = Horizon
horizon5 = Craft(sea, sky, horizon, aa6=sky, aa1=earth, ab1=continent, ac1=lake, ad1=land, ae1=ocean, af1=sea)  # Sea + Sky = Horizon
horizon6 = Craft(earth, sky, horizon, aa6=sky, aa1=earth, ab1=continent, ac1=lake, ad1=land, ae1=ocean, af1=sea)  # Earth + Sky = Horizon
space1 = Craft(sky, solar_system, space, aa2=solar_system, ab2=sky, aa1=sun, ab1=moon)  # Star - 3, Night - 1 Sky + Solar System = Space
sand1 = Craft(air, stone, sand, aa3=air, ab3=wind, ac3=pebble, aa2=stone, ab2=rock, aa1=small)  # Air + Stone = Sand
sand2 = Craft(wind, stone, sand, aa3=air, ab3=wind, ac3=pebble, aa2=stone, ab2=rock, aa1=small)  # Wind + Stone = Sand
sand3 = Craft(air, pebble, sand, aa3=air, ab3=wind, ac3=pebble, aa2=stone, ab2=rock, aa1=small)  # Air + Pebble = Sand
sand4 = Craft(small, pebble, sand, aa3=air, ab3=wind, ac3=pebble, aa2=stone, ab2=rock, aa1=small)  # Small + Pebble = Sand
sand5 = Craft(wind, pebble, sand, aa3=air, ab3=wind, ac3=pebble, aa2=stone, ab2=rock, aa1=small)  # Wind + Pebble = Sand
sand6 = Craft(air, rock, sand, aa3=air, ab3=wind, ac3=pebble, aa2=stone, ab2=rock, aa1=small)  # Air + Rock = Sand
sand7 = Craft(wind, rock, sand, aa3=air, ab3=wind, ac3=pebble, aa2=stone, ab2=rock, aa1=small)  # Wind + Rock = Sand
moon1 = Craft(planet, sky, moon, aa4=sky, aa3=planet, ab3=stone, aa1=earth, ab1=time_item)  # Night - 4, Cheese - 2 Planet + Sky = Moon
moon2 = Craft(planet, stone, moon, aa4=sky, aa3=planet, ab3=stone, aa1=earth, ab1=time_item)  # Night - 4, Cheese - 2 Planet + Stone = Moon
moon3 = Craft(sky, stone, moon, aa4=sky, aa3=planet, ab3=stone, aa1=earth, ab1=time_item)  # Night - 4, Cheese - 2 Sky + Stone = Moon
moon4 = Craft(sky, time_item, moon, aa4=sky, aa3=planet, ab3=stone, aa1=earth, ab1=time_item)  # Night - 4, Cheese - 2 Sky + Time = Moon
rain1 = Craft(cloud, heat, rain, aa3=cloud, aa1=heat, ab1=pressure, ac1=water)  # Cloud + Heat = Rain
rain2 = Craft(cloud, pressure, rain, aa3=cloud, aa1=heat, ab1=pressure, ac1=water)  # Cloud + Pressure = Rain
rain3 = Craft(cloud, water, rain, aa3=cloud, aa1=heat, ab1=pressure, ac1=water)  # Cloud + Water = Rain
lightning1 = Craft(cloud, energy, lightning, aa3=energy, ab3=electricity, ac3=storm, aa2=cloud, ab2=rain, aa1=land)  # Cloud + Energy = Lightning
lightning2 = Craft(rain, energy, lightning, aa3=energy, ab3=electricity, ac3=storm, aa2=cloud, ab2=rain, aa1=land)  # Rain + Energy = Lightning
lightning3 = Craft(rain, electricity, lightning, aa3=energy, ab3=electricity, ac3=storm, aa2=cloud, ab2=rain, aa1=land)  # Rain + Electricity = Lightning
lightning4 = Craft(storm, electricity, lightning, aa3=energy, ab3=electricity, ac3=storm, aa2=cloud, ab2=rain, aa1=land)  # Storm + Electricity = Lightning
lightning5 = Craft(storm, energy, lightning, aa3=energy, ab3=electricity, ac3=storm, aa2=cloud, ab2=rain, aa1=land)  # Storm + Energy = Lightning
lightning6 = Craft(storm, land, lightning, aa3=energy, ab3=electricity, ac3=storm, aa2=cloud, ab2=rain, aa1=land)  # Storm + Land = Lightning
lightning_storm = Craft(cloud, electricity, lightning, storm, aa3=energy, ab3=electricity, ac3=storm, aa2=cloud, ab2=rain, aa1=land, ba2=electricity, bb2=cloud, ba1=atmosphere, bb1=rain, bc1=wind)  # Cloud + Electricity = Lightning and Storm
electricity1 = Craft(lightning, metal, electricity, aa2=lightning, ab2=storm, aa1=metal, ab1=science, ac1=wind, ad1=motion, ae1=light, af1=steel)  # Wind Turbine - 4, Solar Cell - 3, Sandstorm - 1, Star - 1, Lightning + Metal = Electricity
electricity2 = Craft(storm, science, electricity, aa2=lightning, ab2=storm, aa1=metal, ab1=science, ac1=wind, ad1=motion, ae1=light, af1=steel)  # Wind Turbine - 4, Solar Cell - 3, Sandstorm - 1, Star - 1, Storm + Science = Electricity
electricity3 = Craft(lightning, steel, electricity, aa2=lightning, ab2=storm, aa1=metal, ab1=science, ac1=wind, ad1=motion, ae1=light, af1=steel)  # Wind Turbine - 4, Solar Cell - 3, Sandstorm - 1, Star - 1, Lightning + Steel = Electricity
ozone1 = Craft(electricity, air, ozone, aa3=electricity, aa2=oxygen, aa1=air, ab1=atmosphere)  # Electricity + Air = Ozone
ozone2 = Craft(electricity, oxygen, ozone, aa3=electricity, aa2=oxygen, aa1=air, ab1=atmosphere)  # Electricity + Oxygen = Ozone
ozone3 = Craft(oxygen, oxygen, ozone, aa3=electricity, aa2=oxygen, aa1=air, ab1=atmosphere)  # Oxygen + Oxygen = Ozone
storm1 = Craft(cloud, cloud, storm, aa2=electricity, ab2=cloud, aa1=atmosphere, ab1=rain, ac1=wind)  # Cloud x2 = Storm
storm2 = Craft(wind, rain, storm, aa2=electricity, ab2=cloud, aa1=atmosphere, ab1=rain, ac1=wind)  # Wind + Rain = Storm
storm_ozone_aurora = Craft(atmosphere, electricity, storm, ozone, aurora, aa2=electricity, ab2=cloud, aa1=atmosphere, ab1=rain, ac1=wind, ba3=electricity, ba2=oxygen, ba1=air, bb1=atmosphere, ca4=electricity, ca3=sky, ca2=atmosphere, ca1=sun)  # Antarctica - C2, Arctic - C2 Atmosphere + Electricity = Storm, Ozone, and Aurora
wind1 = Craft(air, pressure, wind, aa2=air, ab2=motion, aa1=pressure, ab1=atmosphere)  # Air + Pressure = Wind
wind2 = Craft(air, motion, wind, aa2=air, ab2=motion, aa1=pressure, ab1=atmosphere)  # Air + Motion = Wind
wind3 = Craft(atmosphere, motion, wind, aa2=air, ab2=motion, aa1=pressure, ab1=atmosphere)  # Atmosphere + Motion = Wind
motion1 = Craft(science, wind, motion, aa4=science, ab4=philosophy, aa3=wind, aa1=idea)  # River - 2, Stream - 2, Tornado - 2, Science + Wind = Motion
motion2 = Craft(idea, wind, motion, aa4=science, ab4=philosophy, aa3=wind, aa1=idea)  # River - 2, Stream - 2, Tornado - 2, Idea + Wind = Motion
motion3 = Craft(philosophy, wind, motion, aa4=science, ab4=philosophy, aa3=wind, aa1=idea)  # River - 2, Stream - 2, Tornado - 2, Philosophy + Wind = Motion
idea1 = Craft(science, science, idea, aa3=science, ab3=lightbulb, aa2=philosophy, aa1=human, ab1=hacker, ac1=lumberjack)  # Engineer - 2, Alchemist - 1, Angler - 1, Astronaut - 1, Baker - 1, Butcher - 1, Cyclist - 1, Diver - 1, Doctor - 1, Electrician - 1, Farmer - 1, Firefighter - 1, Gardener - 1, Knight - 1, Librarian - 1, Mailman - 1, Monarch - 1, Pilot - 1, Sailor - 1, Skier - 1, Surfer - 1, Swimmer - 1, Warrior - 1 Science x2 = Idea
idea2 = Craft(philosophy, philosophy, idea, aa3=science, ab3=lightbulb, aa2=philosophy, aa1=human, ab1=hacker, ac1=lumberjack)  # Engineer - 2, Alchemist - 1, Angler - 1, Astronaut - 1, Baker - 1, Butcher - 1, Cyclist - 1, Diver - 1, Doctor - 1, Electrician - 1, Farmer - 1, Firefighter - 1, Gardener - 1, Knight - 1, Librarian - 1, Mailman - 1, Monarch - 1, Pilot - 1, Sailor - 1, Skier - 1, Surfer - 1, Swimmer - 1, Warrior - 1 Philosophy x2 = Idea
idea3 = Craft(philosophy, science, idea, aa3=science, ab3=lightbulb, aa2=philosophy, aa1=human, ab1=hacker, ac1=lumberjack)  # Engineer - 2, Alchemist - 1, Angler - 1, Astronaut - 1, Baker - 1, Butcher - 1, Cyclist - 1, Diver - 1, Doctor - 1, Electrician - 1, Farmer - 1, Firefighter - 1, Gardener - 1, Knight - 1, Librarian - 1, Mailman - 1, Monarch - 1, Pilot - 1, Sailor - 1, Skier - 1, Surfer - 1, Swimmer - 1, Warrior - 1 Philosophy + Science = Idea
idea4 = Craft(hacker, hacker, idea, aa3=science, ab3=lightbulb, aa2=philosophy, aa1=human, ab1=hacker, ac1=lumberjack)  # Engineer - 2, Alchemist - 1, Angler - 1, Astronaut - 1, Baker - 1, Butcher - 1, Cyclist - 1, Diver - 1, Doctor - 1, Electrician - 1, Farmer - 1, Firefighter - 1, Gardener - 1, Knight - 1, Librarian - 1, Mailman - 1, Monarch - 1, Pilot - 1, Sailor - 1, Skier - 1, Surfer - 1, Swimmer - 1, Warrior - 1 Hacker x2 = Idea
idea5 = Craft(lightbulb, human, idea, aa3=science, ab3=lightbulb, aa2=philosophy, aa1=human, ab1=hacker, ac1=lumberjack)  # Engineer - 2, Alchemist - 1, Angler - 1, Astronaut - 1, Baker - 1, Butcher - 1, Cyclist - 1, Diver - 1, Doctor - 1, Electrician - 1, Farmer - 1, Firefighter - 1, Gardener - 1, Knight - 1, Librarian - 1, Mailman - 1, Monarch - 1, Pilot - 1, Sailor - 1, Skier - 1, Surfer - 1, Swimmer - 1, Warrior - 1 Light Bulb + Human = Idea
idea6 = Craft(lightbulb, science, idea, aa3=science, ab3=lightbulb, aa2=philosophy, aa1=human, ab1=hacker, ac1=lumberjack)  # Engineer - 2, Alchemist - 1, Angler - 1, Astronaut - 1, Baker - 1, Butcher - 1, Cyclist - 1, Diver - 1, Doctor - 1, Electrician - 1, Farmer - 1, Firefighter - 1, Gardener - 1, Knight - 1, Librarian - 1, Mailman - 1, Monarch - 1, Pilot - 1, Sailor - 1, Skier - 1, Surfer - 1, Swimmer - 1, Warrior - 1 Light Bulb + Science = Idea
idea7 = Craft(lumberjack, lumberjack, idea, aa3=science, ab3=lightbulb, aa2=philosophy, aa1=human, ab1=hacker, ac1=lumberjack)  # Engineer - 2, Alchemist - 1, Angler - 1, Astronaut - 1, Baker - 1, Butcher - 1, Cyclist - 1, Diver - 1, Doctor - 1, Electrician - 1, Farmer - 1, Firefighter - 1, Gardener - 1, Knight - 1, Librarian - 1, Mailman - 1, Monarch - 1, Pilot - 1, Sailor - 1, Skier - 1, Surfer - 1, Swimmer - 1, Warrior - 1 Lumberjack x2 = Idea
philosophy1 = Craft(human, idea, philosophy, aa2=human, aa1=idea, ab1=egg)  # Chicken - 1, Story - 1 Human + Idea = Philosophy
big1 = Craft(philosophy, galaxy_cluster, big, aa6=philosophy, aa1=galaxy_cluster, ab1=galaxy, ac1=planet, ad1=solar_system, ae1=sun, af1=universe)  # Philosophy + Galaxy Cluster = Big
big2 = Craft(philosophy, galaxy, big, aa6=philosophy, aa1=galaxy_cluster, ab1=galaxy, ac1=planet, ad1=solar_system, ae1=sun, af1=universe)  # Philosophy + Galaxy = Big
big3 = Craft(philosophy, planet, big, aa6=philosophy, aa1=galaxy_cluster, ab1=galaxy, ac1=planet, ad1=solar_system, ae1=sun, af1=universe)  # Philosophy + Planet = Big
big4 = Craft(philosophy, solar_system, big, aa6=philosophy, aa1=galaxy_cluster, ab1=galaxy, ac1=planet, ad1=solar_system, ae1=sun, af1=universe)  # Philosophy + Solar System = Big
big5 = Craft(philosophy, sun, big, aa6=philosophy, aa1=galaxy_cluster, ab1=galaxy, ac1=planet, ad1=solar_system, ae1=sun, af1=universe)  # Philosophy + Sun = Big
big6 = Craft(philosophy, universe, big, aa6=philosophy, aa1=galaxy_cluster, ab1=galaxy, ac1=planet, ad1=solar_system, ae1=sun, af1=universe)  # Philosophy + Universe = Big
small1 = Craft(philosophy, ozone, small, aa12=philosophy, aa1=ozone, ab1=oxygen, ac1=pebble)  # Ant - 1, Bacteria - 1, Bee - 1, Carbon Dioxide - 1, Confetti - 1, Rivulet - 1, Scorpion - 1, Seahorse - 1, Spider - 1 Philosophy + Ozone = Small
small2 = Craft(philosophy, oxygen, small, aa12=philosophy, aa1=ozone, ab1=oxygen, ac1=pebble)  # Ant - 1, Bacteria - 1, Bee - 1, Carbon Dioxide - 1, Confetti - 1, Rivulet - 1, Scorpion - 1, Seahorse - 1, Spider - 1 Philosophy + Oxygen = Small
small3 = Craft(philosophy, pebble, small, aa12=philosophy, aa1=ozone, ab1=oxygen, ac1=pebble)  # Ant - 1, Bacteria - 1, Bee - 1, Carbon Dioxide - 1, Confetti - 1, Rivulet - 1, Scorpion - 1, Seahorse - 1, Spider - 1 Philosophy + Pebble = Small
gold1 = Craft(metal, sand, gold, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow)  # Alchemist - 2, Butter - 2 Metal + Sand = Gold
gold2 = Craft(metal, sun, gold, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow)  # Alchemist - 2, Butter - 2 Metal + Sun = Gold
gold3 = Craft(steel, sand, gold, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow)  # Alchemist - 2, Butter - 2 Steel + Sand = Gold
gold4 = Craft(steel, sun, gold, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow)  # Alchemist - 2, Butter - 2 Steel + Sun = Gold
gold5 = Craft(rainbow, metal, gold, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow)  # Alchemist - 2, Butter - 2 Rainbow + Metal = Gold
gold6 = Craft(rainbow, steel, gold, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow)  # Alchemist - 2, Butter - 2 Rainbow + Steel = Gold
gold_spotlight = Craft(light, metal, gold, spotlight, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow, ba3=light, ba1=machine, bb1=metal, bc1=steel)  # Alchemist - 2, Butter - 2 Light + Metal = Gold and Spotlight
gold_spotlight2 = Craft(light, steel, gold, spotlight, aa6=metal, ab6=steel, aa2=sun, ab2=sand, ac2=light, ad2=rainbow, ba3=light, ba1=machine, bb1=metal, bc1=steel)  # Alchemist - 2, Butter - 2 Light + Steel = Gold and Spotlight
machine1 = Craft(tool, wheel, machine, aa5=tool, aa2=wheel)  # Boiler - 3, Chain - 2, Engineer - 1 Tool + Wheel = Machine
machine2 = Craft(tool, tool, machine, aa5=tool, aa2=wheel)  # Boiler - 3, Chain - 2, Engineer - 1 Tool x2 = Machine
car1 = Craft(metal, wheel, car, aa4=wheel, aa1=metal, ab1=steel, ac1=machine)  # Motorcycle - 3, Bicycle - 2, Combustion Engine - 2, Cart - 1, Wagon - 1 Metal + Wheel = Car
car2 = Craft(steel, wheel, car, aa4=wheel, aa1=metal, ab1=steel, ac1=machine)  # Motorcycle - 3, Bicycle - 2, Combustion Engine - 2, Cart - 1, Wagon - 1 Steel + Wheel = Car
glass1 = Craft(electricity, sand, glass, aa4=sand, aa1=electricity, ab1=fire, ac1=heat, ad1=lightning)  # Electricity + Sand = Glass
glass2 = Craft(fire, sand, glass, aa4=sand, aa1=electricity, ab1=fire, ac1=heat, ad1=lightning)  # Fire + Sand = Glass
glass3 = Craft(heat, sand, glass, aa4=sand, aa1=electricity, ab1=fire, ac1=heat, ad1=lightning)  # Heat + Sand = Glass
glass4 = Craft(lightning, sand, glass, aa4=sand, aa1=electricity, ab1=fire, ac1=heat, ad1=lightning)  # Lightning + Sand = Glass
glasses1 = Craft(glass, human, glasses, aa4=glass, aa2=human, aa1=metal, ab1=steel)  # Lens - 2 Glass + Human = Glasses
glasses2 = Craft(glass, glass, glasses, aa4=glass, aa2=human, aa1=metal, ab1=steel)  # Lens - 2 Glass x2 = Glasses
glasses_mirror = Craft(glass, metal, glasses, mirror, aa4=glass, aa2=human, aa1=metal, ab1=steel, ba3=glass, ba1=metal, bb1=steel, bc1=wood)  # Lens - 2 Glass + Metal = Glasses and Mirror
glasses_mirror2 = Craft(glass, steel, glasses, mirror, aa4=glass, aa2=human, aa1=metal, ab1=steel, ba3=glass, ba1=metal, bb1=steel, bc1=wood)  # Lens - 2 Glass + Steel = Glasses and Mirror
mirror1 = Craft(glass, wood, mirror, aa3=glass, aa1=metal, ab1=steel, ac1=wood)  # Glass + Wood = Mirror
hacker1 = Craft(glasses, human, hacker, aa4=human, aa1=glasses, ab1=computer, ac1=internet)  # Computer Mouse - 1 Glasses + Human = Hacker
hacker2 = Craft(computer, human, hacker, aa4=human, aa1=glasses, ab1=computer, ac1=internet)  # Computer Mouse - 1 Computer + Human = Hacker
hacker3 = Craft(internet, human, hacker, aa4=human, aa1=glasses, ab1=computer, ac1=internet)  # Computer Mouse - 1 Internet + Human = Hacker
computer1 = Craft(electricity, hacker, computer, aa4=hacker, aa1=electricity, ab1=machine, ac1=tool)  # Container - 1, Email - 1, Wire - 1 Electricity + Hacker = Computer
computer2 = Craft(machine, hacker, computer, aa4=hacker, aa1=electricity, ab1=machine, ac1=tool)  # Container - 1, Email - 1, Wire - 1 Machine + Hacker = Computer
computer3 = Craft(tool, hacker, computer, aa4=hacker, aa1=electricity, ab1=machine, ac1=tool)  # Container - 1, Email - 1, Wire - 1 Tool + Hacker = Computer
internet1 = Craft(computer, computer, internet, aa4=computer)  # Web - 1, Net - 1, Wire - 1 Computer x2 = Internet
animal_soil = Craft(land, life, animal, soil, aa6=life, aa1=land, ba2=life, bb2=earth, bc2=land, bd2=organic_matter)  # Beach - 1, Desert - 1, Forest - 1, Mountain - 1, Mountain Range - 1 Land + Life = Animal and Soil
soil1 = Craft(earth, life, soil, aa2=life, ab2=earth, ac2=land, ad2=organic_matter)  # Earth + Life = Soil
soil2 = Craft(organic_matter, land, soil, aa2=life, ab2=earth, ac2=land, ad2=organic_matter)  # Organic Matter + Land = Soil
soil_mineral = Craft(organic_matter, earth, soil, mineral, aa2=life, ab2=earth, ac2=land, ad2=organic_matter, ba6=organic_matter, ba1=earth, bb1=stone, bc1=rock, bd1=boulder)  # Hill - B1, Mountain - B1 Organic Matter + Earth = Soil and Mineral
meat1 = Craft(animal, axe, meat, aa10=tool, ab10=axe, aa6=sword, aa4=animal, ab4=fish)  # Butcher - 10, Chicken - 4, Cow - 4, Flying Fish - 4, Frog - 3, Livestock - 4, Net - 5, Pig - 4, Shark - 5, Piranha - 1, Swordfish - 4 Animal + Axe = Meat
meat2 = Craft(animal, sword, meat, aa10=tool, ab10=axe, aa6=sword, aa4=animal, ab4=fish)  # Butcher - 10, Chicken - 4, Cow - 4, Flying Fish - 4, Frog - 3, Livestock - 4, Net - 5, Pig - 4, Shark - 5, Piranha - 1, Swordfish - 4 Animal + Sword = Meat
meat3 = Craft(fish, axe, meat, aa10=tool, ab10=axe, aa6=sword, aa4=animal, ab4=fish)  # Butcher - 10, Chicken - 4, Cow - 4, Flying Fish - 4, Frog - 3, Livestock - 4, Net - 5, Pig - 4, Shark - 5, Piranha - 1, Swordfish - 4 Fish + Axe = Meat
meat_fishingrod = Craft(fish, tool, meat, fishing_rod, aa10=tool, ab10=axe, aa6=sword, aa4=animal, ab4=fish, ba4=fish, ba3=tool, bb3=wood)  # Butcher - 10, Chicken - 4, Cow - 4, Flying Fish - 4, Frog - 3, Livestock - 4, Net - 5, Pig - 4, Shark - 5, Piranha - 1, Swordfish - 4, Piranha - B4, Swordfish - B4, Thread - B3, Wire - B3 Fish + Tool = Meat and Fishing Rod
plant1 = Craft(life, soil, plant, aa3=soil, aa2=earth, ab2=land, aa1=life, ab1=rain, ac1=big, ad1=water, ae1=small)  # Seed - 4, Algae - 2, Grass - 1 Life + Soil = Plant
plant2 = Craft(rain, soil, plant, aa3=soil, aa2=earth, ab2=land, aa1=life, ab1=rain, ac1=big, ad1=water, ae1=small)  # Seed - 4, Algae - 2, Grass - 1 Rain + Soil = Plant
ash1 = Craft(mineral, fire, ash, aa5=fire, ab5=campfire, aa1=plant, ab1=rain, ac1=storm, ad1=time_item, ae1=water, af1=sun, ag1=mineral, ah1=tree)  # Paper - 3, Vampire - 2, Dawn - 1, Grass - 1 Mineral + Fire = Ash
dust1 = Craft(air, earth, dust, aa3=air, aa1=earth, ab1=land, ac1=soil)  # Air + Earth = Dust
dust2 = Craft(air, land, dust, aa3=air, aa1=earth, ab1=land, ac1=soil)  # Air + Land = Dust
dust3 = Craft(air, soil, dust, aa3=air, aa1=earth, ab1=land, ac1=soil)  # Air + Soil = Dust
field1 = Craft(earth, tool, field, aa3=earth, ab3=tool, ac3=land, ad3=soil)  # Farmer - 3, Plow - 3 Earth + Tool = Field
field2 = Craft(land, tool, field, aa3=earth, ab3=tool, ac3=land, ad3=soil)  # Farmer - 3, Plow - 3 Land + Tool = Field
field3 = Craft(soil, tool, field, aa3=earth, ab3=tool, ac3=land, ad3=soil)  # Farmer - 3, Plow - 3 Soil + Tool = Field
gunpowder1 = Craft(fire, dust, gunpowder, aa2=dust, ab2=energy, ac2=mineral, ad2=charcoal, aa1=fire)  # Fire + Dust = Gunpowder
gunpowder2 = Craft(energy, dust, gunpowder, aa2=dust, ab2=energy, ac2=mineral, ad2=charcoal, aa1=fire)  # Energy + Dust = Gunpowder
gunpowder3 = Craft(energy, mineral, gunpowder, aa2=dust, ab3=energy, ac2=mineral, ad2=charcoal, aa1=fire)  # Energy + Mineral = Gunpowder
gunpowder4 = Craft(energy, charcoal, gunpowder, aa2=dust, ab3=energy, ac2=mineral, ad2=charcoal, aa1=fire)  # Energy + Charcoal = Gunpowder
gunpowder5 = Craft(mineral, charcoal, gunpowder, aa2=dust, ab3=energy, ac2=mineral, ad2=charcoal, aa1=fire)  # Mineral + Charcoal = Gunpowder
explosion1 = Craft(electricity, gunpowder, explosion, aa3=gunpowder, aa2=fire, ab2=pressure, ac2=volcano, aa1=electricity, ab1=lightning, ac1=explosion, ad1=heat, ae1=lava)  # Petroleum - 6 Electricity + Gunpowder = Explosion
explosion2 = Craft(fire, gunpowder, explosion, aa3=gunpowder, aa2=fire, ab2=pressure, ac2=volcano, aa1=electricity, ab1=lightning, ac1=explosion, ad1=heat, ae1=lava)  # Petroleum - 6 Fire + Gunpowder = Explosion
explosion3 = Craft(lightning, gunpowder, explosion, aa3=gunpowder, aa2=fire, ab2=pressure, ac2=volcano, aa1=electricity, ab1=lightning, ac1=explosion, ad1=heat, ae1=lava)  # Petroleum - 6 Lightning + Gunpowder = Explosion
explosion_eruption = Craft(volcano, pressure, explosion, eruption, aa3=gunpowder, aa2=fire, ab2=pressure, ac2=volcano, aa1=electricity, ab1=lightning, ac1=explosion, ad1=heat, ae1=lava, ba2=pressure, bb2=volcano, ba1=lava, bb1=time_item)  # Petroleum - 6 Volcano + Pressure = Explosion and Eruption
lightbulb1 = Craft(electricity, glass, lightbulb, aa2=glass, ab2=light, aa1=electricity)  # Container - 1 Electricity + Glass = Light Bulb
light1 = Craft(electricity, lightbulb, light, aa2=electricity, aa1=lightbulb)  # Flashlight - 1 Electricity + Lightbulb = Light
spotlight1 = Craft(light, machine, spotlight, aa3=light, aa1=machine, ab1=metal, ac1=steel)  # Light + Machine = Spotlight
organicmatter1 = Craft(life, science, organic_matter, aa2=life, ab2=science, ac2=death, aa1=corpse)  # Bacteria - 1 Life + Science = Organic Matter
organicmatter2 = Craft(corpse, science, organic_matter, aa2=life, ab2=science, ac2=death, aa1=corpse)  # Bacteria - 1 Corpse + Science = Organic Matter
organicmatter3 = Craft(death, life, organic_matter, aa2=life, ab2=science, ac2=death, aa1=corpse)  # Bacteria - 1 Death + Life = Organic Matter
mineral1 = Craft(organic_matter, stone, mineral, aa6=organic_matter, aa1=earth, ab1=stone, ac1=rock, ad1=boulder)  # Hill - 1, Mountain - 1 Organic Matter + Stone = Mineral
mineral2 = Craft(organic_matter, rock, mineral, aa6=organic_matter, aa1=earth, ab1=stone, ac1=rock, ad1=boulder)  # Hill - 1, Mountain - 1 Organic Matter + Rock = Mineral
mineral3 = Craft(organic_matter, boulder, mineral, aa6=organic_matter, aa1=earth, ab1=stone, ac1=rock, ad1=boulder)  # Hill - 1, Mountain - 1 Organic Matter + Boulder = Mineral
steel1 = Craft(ash, metal, steel, aa4=metal, aa1=ash, ab1=mineral, ac1=coal, ad1=charcoal)  # Ash + Metal = Steel
steel2 = Craft(mineral, metal, steel, aa4=metal, aa1=ash, ab1=mineral, ac1=coal, ad1=charcoal)  # Mineral + Metal = Steel
steel3 = Craft(coal, metal, steel, aa4=metal, aa1=ash, ab1=mineral, ac1=coal, ad1=charcoal)  # Coal + Metal = Steel
steel4 = Craft(charcoal, metal, steel, aa4=metal, aa1=ash, ab1=mineral, ac1=coal, ad1=charcoal)  # Charcoal + Metal = Steel
coal1 = Craft(organic_matter, pressure, coal, aa2=pressure, aa1=organic_matter, ab1=earth, ac1=stone, ad1=time_item, ae1=rock)  # Peat - 5 Organic Matter + Pressure = Coal
charcoal1 = Craft(organic_matter, fire, charcoal, aa4=fire, aa1=organic_matter, ab1=tree, ac1=wood, ad1=corpse)  # Organic Matter + Fire = Charcoal
charcoal2 = Craft(corpse, fire, charcoal, aa4=fire, aa1=organic_matter, ab1=tree, ac1=wood, ad1=corpse)  # Corpse + Fire = Charcoal
charcoal_smoke_campfire = Craft(wood, fire, charcoal, smoke, campfire, aa4=fire, aa1=organic_matter, ab1=tree, ac1=wood, ad1=corpse, ba5=fire, ba3=campfire, ba1=air, bb1=gas, bc1=time_item, bd1=water, be1=storm, bf1=plant, bg1=tree, bh1=wood, ca1=wood, cb1=fire)
# Grass - B1 Wood + Fire = Charcoal, Smoke, and Campfire
tree1 = Craft(big, plant, tree, aa3=plant, aa1=big, ab1=time_item, ac1=wood)  # Container - 1, Nest - 1 Big + Plant = Tree
tree2 = Craft(wood, plant, tree, aa3=plant, aa1=big, ab1=time_item, ac1=wood)  # Container - 1, Nest - 1 Wood + Plant = Tree
tree3 = Craft(time, plant, tree, aa3=plant, aa1=big, ab1=time_item, ac1=wood)  # Container - 1, Nest - 1 Time + Plant = Tree
oxygen1 = Craft(sun, tree, oxygen, aa4=sun, aa2=plant, ab2=tree)  # Carbon Dioxide - 4, Grass - 2, Algae - 2 Sun + Tree = Oxygen
oxygen_sunflower = Craft(plant, sun, oxygen, sunflower, aa4=sun, aa2=plant, ab2=tree, ba2=sun, ba1=plant)  # Carbon Dioxide - 4, Grass - 2, Algae - 2, Flower - B1 Plant + Sun = Oxygen and Sunflower
wood1 = Craft(tree, tool, wood, aa5=tree, aa2=tool, ab2=lumberjack, ac2=axe, aa1=sword)  # Forest - 4, Chainsaw - 2 Tree + Tool = Wood
wood2 = Craft(tree, lumberjack, wood, aa5=tree, aa2=tool, ab2=lumberjack, ac2=axe, aa1=sword)  # Forest - 4, Chainsaw - 2 Tree + Lumberjack = Wood
wood3 = Craft(tree, axe, wood, aa5=tree, aa2=tool, ab2=lumberjack, ac2=axe, aa1=sword)  # Forest - 4, Chainsaw - 2 Tree + Axe = Wood
wood4 = Craft(tree, sword, wood, aa5=tree, aa2=tool, ab2=lumberjack, ac2=axe, aa1=sword)  # Forest - 4, Chainsaw - 2 Tree + Axe = Wood
lumberjack1 = Craft(tree, human, lumberjack, aa4=human, aa1=tree, ab1=wood, ac1=axe)  # Chainsaw - 1 Tree + Human = Lumberjack
lumberjack2 = Craft(axe, human, lumberjack, aa4=human, aa1=tree, ab1=wood, ac1=axe)  # Chainsaw - 1 Axe + Human = Lumberjack
axe1 = Craft(lumberjack, tool, axe, aa3=wood, aa2=tool, aa1=lumberjack, ab1=stone, ac1=blade)  # Lumberjack + Tool = Axe
axe2 = Craft(wood, tool, axe, aa3=wood, aa2=tool, aa1=lumberjack, ab1=stone, ac1=blade)  # Wood + Tool = Axe
axe_sword = Craft(wood, blade, axe, sword, aa3=wood, aa2=tool, aa1=lumberjack, ab1=stone, ac1=blade, ba3=blade, ba1=wood, bb1=metal, bc1=steel)  # Wood + Blade = Axe and Sword
pebble1 = Craft(earth, small, pebble, aa3=small, aa1=earth, ab1=stone, ac1=rock)  # Earth + Small = Pebble
pebble2 = Craft(stone, small, pebble, aa3=small, aa1=earth, ab1=stone, ac1=rock)  # Stone + Small = Pebble
pebble3 = Craft(rock, small, pebble, aa3=small, aa1=earth, ab1=stone, ac1=rock)  # Rock + Small = Pebble
rock1 = Craft(big, pebble, rock, aa2=pebble, aa1=big, ab1=small, ac1=boulder)  # Big + Pebble = Rock
rock2 = Craft(pebble, pebble, rock, aa2=pebble, aa1=big, ab1=small, ac1=boulder)  # Pebble + Pebble = Rock
rock3 = Craft(boulder, small, rock, aa2=pebble, aa1=big, ab1=small, ac1=boulder)  # Boulder + Small = Rock
blade1 = Craft(metal, rock, blade, aa2=metal, ab2=rock, ac2=steel, ad2=stone)  # Metal + Rock = Blade
blade2 = Craft(metal, stone, blade, aa2=metal, ab2=rock, ac2=steel, ad2=stone)  # Metal + Stone = Blade
blade3 = Craft(steel, rock, blade, aa2=metal, ab2=rock, ac2=steel, ad2=stone)  # Steel + Rock = Blade
blade4 = Craft(steel, stone, blade, aa2=metal, ab2=rock, ac2=steel, ad2=stone)  # Steel + Stone = Blade
sword1 = Craft(blade, metal, sword, aa3=blade, aa1=wood, ab1=metal, ac1=steel)  # Blade + Metal = Sword
sword2 = Craft(blade, steel, sword, aa3=blade, aa1=wood, ab1=metal, ac1=steel)  # Blade + Steel = Sword
granite1 = Craft(rock, pressure, granite, aa3=pressure, aa1=lava, ab1=rock, ac1=stone)  # Rock + Pressure = Granite
granite2 = Craft(stone, pressure, granite, aa3=pressure, aa1=lava, ab1=rock, ac1=stone)  # Stone + Pressure = Granite
granite_eruption = Craft(lava, pressure, granite, eruption, aa3=pressure, aa1=lava, ab1=rock, ac1=stone, ba2=pressure, bb2=volcano, ba1=lava, bb1=time_item)  # Lava + Pressure = Granite and Eruption
eruption1 = Craft(time, volcano, eruption, aa2=pressure, ab2=volcano, aa1=lava, ab1=time_item)  # Time + Volcano = Eruption
volcano1 = Craft(lava, earth, volcano, aa4=lava, aa2=pressure, ab2=fire, aa1=earth)  # Mountain - 3, Hill - 3, Container - 1 Lava + Earth = Volcano
boulder1 = Craft(big, rock, boulder, aa4=rock, aa2=big, ab2=stone, aa1=small, ab1=earth)  # Hill - 1 Big + Rock = Boulder
boulder2 = Craft(big, stone, boulder, aa4=rock, aa2=big, ab2=stone, aa1=small, ab1=earth)  # Hill - 1 Big + Stone = Boulder
boulder3 = Craft(earth, rock, boulder, aa4=rock, aa2=big, ab2=stone, aa1=small, ab1=earth)  # Hill - 1 Earth + Rock = Boulder
boulder4 = Craft(stone, rock, boulder, aa4=rock, aa2=big, ab2=stone, aa1=small, ab1=earth)  # Hill - 1 Stone + Rock = Boulder
boulder5 = Craft(rock, rock, boulder, aa4=rock, aa2=big, ab2=stone, aa1=small, ab1=earth)  # Hill - 1 Rock x2 = Boulder
corpse1 = Craft(explosion, human, corpse, aa7=human, aa1=blade, ab1=explosion, ac1=time_item, ad1=death)  # Arrow - 1, Bullet - 1, Grim Reaper - 1 Explosion + Human = Corpse
corpse2 = Craft(time, human, corpse, aa7=human, aa1=blade, ab1=explosion, ac1=time_item, ad1=death)  # Arrow - 1, Bullet - 1, Grim Reaper - 1 Time + Human = Corpse
corpse3 = Craft(death, human, corpse, aa7=human, aa1=blade, ab1=explosion, ac1=time_item, ad1=death)  # Arrow - 1, Bullet - 1, Grim Reaper - 1 Death + Human = Corpse
corpse_blood = Craft(blade, human, corpse, blood, aa7=human, aa1=blade, ab1=explosion, ac1=time_item, ad1=death, ba1=blade, bb1=human, bc1=sword)  # Arrow - 1, Bullet - 1, Grim Reaper - 1, Warrior - B1 Blade + Human = Corpse and Blood
death1 = Craft(corpse, philosophy, death, aa4=philosophy, aa1=corpse, ab1=life, ac1=time_item)  # Grave - 1, Graveyard - 1, Skeleton - 1 Corpse + Philosophy = Death
death2 = Craft(life, time_item, death, aa4=philosophy, aa1=corpse, ab1=life, ac1=time_item)  # Grave - 1, Graveyard - 1, Skeleton - 1 Life + Time = Death
phoenix1 = Craft(death, fire, aa4=fire, aa1=death, ab1=life, ac1=egg)  # Bird - 1 Death + Fire = Phoenix
phoenix2 = Craft(life, fire, aa4=fire, aa1=death, ab1=life, ac1=egg)  # Bird - 1 Life + Fire = Phoenix
phoenix_omelette = Craft(egg, fire, phoenix, omelette, aa4=fire, aa1=death, ab1=life, ac1=egg, ba3=egg, ba1=fire, bb1=heat, bc1=tool)  # Bird - 1 Egg + Fire = Phoenix and Omelette
egg1 = Craft(phoenix, phoenix, egg, aa1=phoenix, ab1=life, ac1=fish)  # Container - 1, Ant - 1, Bee - 1, Bird - 1, Butterfly - 1, Chameleon - 1, Chicken - 1, Crow - 1, Dinosaur - 1, Dragon - 1, Duck - 1, Eagle - 1, Flying Fish - 1, Frog - 1, Hummingbird - 1, Lizard - 1, Moth - 1, Ostrich - 1, Owl - 1, Parrot - 1, Peacock - 1, Penguin - 1, Pigeon - 1, Piranha - 1, Pterodactyl - 1, Scorpion - 1, Seagull - 1, Snake - 1, Spider - 1, Turtle - 1, T-Rex - 1, Vulture - 1, Woodpecker - 1 Phoenix x2 = Egg
egg2 = Craft(fish, fish, egg, aa1=phoenix, ab1=life, ac1=fish)  # Container - 1, Ant - 1, Bee - 1, Bird - 1, Butterfly - 1, Chameleon - 1, Chicken - 1, Crow - 1, Dinosaur - 1, Dragon - 1, Duck - 1, Eagle - 1, Flying Fish - 1, Frog - 1, Hummingbird - 1, Lizard - 1, Moth - 1, Ostrich - 1, Owl - 1, Parrot - 1, Peacock - 1, Penguin - 1, Pigeon - 1, Piranha - 1, Pterodactyl - 1, Scorpion - 1, Seagull - 1, Snake - 1, Spider - 1, Turtle - 1, T-Rex - 1, Vulture - 1, Woodpecker - 1 Fish x2 = Egg
omelette1 = Craft(egg, heat, omelette, aa3=egg, aa1=fire, ab1=heat, ac1=tool)  # Egg + Heat = Omelette
omelette2 = Craft(egg, tool, omelette, aa3=egg, aa1=fire, ab1=heat, ac1=tool)  # Egg + Tool = Omelette
fish1 = Craft(animal, lake, fish, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water)  # Animal + Lake = Fish
fish2 = Craft(animal, ocean, fish, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water)  # Animal + Ocean = Fish
fish3 = Craft(animal, sea, fish, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water)  # Animal + Sea = Fish
fish4 = Craft(animal, water, fish, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water)  # Animal + Water = Fish
fish_roe = Craft(egg, lake, fish, roe, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water, ba6=egg, ba1=water, bb1=fish, bc1=lake, bd1=ocean, be1=sea)  # Egg + Lake = Fish and Roe
fish_roe2 = Craft(egg, ocean, fish, roe, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water, ba6=egg, ba1=water, bb1=fish, bc1=lake, bd1=ocean, be1=sea)  # Egg + Ocean = Fish and Roe
fish_roe3 = Craft(egg, sea, fish, roe, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water, ba6=egg, ba1=water, bb1=fish, bc1=lake, bd1=ocean, be1=sea)  # Egg + Sea = Fish and Roe
fish_roe4 = Craft(egg, water, fish, roe, aa4=animal, ab4=egg, aa2=lake, ab2=ocean, ac2=sea, ad2=water, ba6=egg, ba1=water, bb1=fish, bc1=lake, bd1=ocean, be1=sea)  # Flying Fish - 1 Egg + Water = Fish and Roe
roe1 = Craft(egg, fish, roe, aa6=egg, aa1=water, ab1=fish, ac1=lake, ad1=ocean, ae1=sea)  # Flying Fish - 1 Egg + Fish = Roe
fishingrod1 = Craft(fish, wood, fishing_rod, aa4=fish, aa3=tool, ab3=wood)  # Piranha - 4, Swordfish - 4, Thread - 3, Wire - 3 Fish + Wood = Fishing Rod
rainbow1 = Craft(cloud, light, rainbow, aa4=light, aa3=sun, aa2=water, ab2=rain, aa1=cloud)  # Prism - 2 Cloud + Light = Rainbow
rainbow2 = Craft(rain, light, rainbow, aa4=light, aa3=sun, aa2=water, ab2=rain, aa1=cloud)  # Prism - 2 Rain + Light = Rainbow
rainbow3 = Craft(water, light, rainbow, aa4=light, aa3=sun, aa2=water, ab2=rain, aa1=cloud)  # Prism - 2 Water + Light = Rainbow
rainbow4 = Craft(rain, sun, rainbow, aa4=light, aa3=sun, aa2=water, ab2=rain, aa1=cloud)  # Prism - 2 Rain + Sun = Rainbow
rainbow5 = Craft(water, sun, rainbow, aa4=light, aa3=sun, aa2=water, ab2=rain, aa1=cloud)  # Prism - 2 Water + Sun = Rainbow
magic1 = Craft(life, rainbow, magic, aa2=life, ab2=energy, aa1=rainbow, ab1=wizard)  # Double Rainbow - 1, Witch - 1 Life + Rainbow = Magic
magic2 = Craft(wizard, energy, magic, aa2=life, ab2=energy, aa1=rainbow, ab1=wizard)  # Double Rainbow - 1, Witch - 1 Wizard + Energy = Magic
wizard1 = Craft(human, magic, wizard, aa4=human, aa1=magic, ab1=rainbow)  # Double Rainbow - 1, Unicorn - 1 Human + Magic = Wizard
wizard2 = Craft(human, rainbow, wizard, aa4=human, aa1=magic, ab1=rainbow)  # Double Rainbow - 1, Unicorn - 1 Human + Rainbow = Wizard
wand1 = Craft(wizard, sword, wand, aa4=wizard, aa1=sword, ab1=tool, ac1=wood, ad1=pencil)  # Wizard + Sword = Wand
wand2 = Craft(wizard, tool, wand, aa4=wizard, aa1=sword, ab1=tool, ac1=wood, ad1=pencil)  # Wizard + Tool = Wand
wand3 = Craft(wizard, wood, wand, aa4=wizard, aa1=sword, ab1=tool, ac1=wood, ad1=pencil)  # Wizard + Wood = Wand
wand4 = Craft(wizard, pencil, wand, aa4=wizard, aa1=sword, ab1=tool, ac1=wood, ad1=pencil)  # Wizard + Pencil = Wand
pencil1 = Craft(wood, charcoal, pencil, aa2=wood, aa1=charcoal, ab1=coal)  # Wood + Charcoal = Pencil
pencil2 = Craft(wood, coal, pencil, aa2=wood, aa1=charcoal, ab1=coal)  # Wood + Coal = Pencil
crafts = [steam1, steam2, steam3, steam_obsidian, pressure1, pressure2, pressure3, pressure4, pressure5, geyser1, geyser2, puddle1, puddle2, pond1, pond2, pond3, pond4, lake1, lake2, lake3, lake4, sea1, sea2, sea3,
          sea4, ocean1, ocean2, ocean3, land1, land2, land3, land4, land5, continent1, continent2, continent3, planet1, planet2, planet3, planet4, planet_horizon, solarsystem1, solarsystem2, galaxy1,
          galaxy2, galaxy3, galaxycluster1, universe1, energy1, energy2, energy3, energy_heat, heat1, heat2, heat3, lava1, lava2, stone1, stone2, metal1, metal2, mud1, mud2, clay1, clay2, clay3, clay4, clay5, primordialsoup1,
          primordialsoup2, primordialsoup3, primordialsoup4, primordialsoup5, primordialsoup6, life1, life2, life3, life4, life5, life6, life7, life8, life9, life10, life11, life12, human1, human_meat, human_sloth,
          tool1, tool2, tool3, tool4, tool5, tool6, tool7, tool_lumberjack, tool_axe, wheel1, wheel2, wheel3, wheel4, wheel5, science1, gas1, gas2, smoke1, smoke2, smoke_ash_tobacco, smoke_ash_charcoal, atmosphere1,
          atmosphere2, cloud1, cloud2, cloud3, cloud4, sky1, sky2, sky_aurora, sky_eclipse, sun1, sun2, sun3, sun4, obsidian1, mist1, mist2, mist3, horizon1, horizon2, horizon3, horizon4, horizon5, horizon6, space1,
          sand1, sand2, sand3, sand4, sand5, sand6, sand7, moon1, moon2, moon3, moon4, rain1, rain2, rain3, lightning1, lightning2, lightning3, lightning4, lightning5, lightning6, lightning_storm, electricity1,
          electricity2, electricity3, ozone1, ozone2, ozone3, storm1, storm2, storm_ozone_aurora, wind1, wind2, wind3, motion1, motion2, motion3, idea1, idea2, idea3, idea4, idea5, idea6, idea7, philosophy1, big1,
          big2, big3, big4, big5, big6, small1, small2, small3, gold1, gold2, gold3, gold4, gold5, gold6, gold_spotlight, gold_spotlight2, machine1, machine2, car1, car2, glass1, glass2, glass3, glass4, glasses1, glasses2,
          glasses_mirror, glasses_mirror2, mirror1, hacker1, hacker2, hacker3, computer1, computer2, computer3, internet1, animal_soil, soil1, soil2, soil_mineral, meat1, meat2, meat3, meat_fishingrod, plant1, plant2,
          ash1, dust1, dust2, dust3, field1, field2, field3, gunpowder1, gunpowder2, gunpowder3, gunpowder4, gunpowder5, explosion1, explosion2, explosion3, explosion_eruption, lightbulb1, light1, spotlight1,
          organicmatter1, organicmatter2, organicmatter3, mineral1, mineral2, mineral3, steel1, steel2, steel3, steel4, coal1, charcoal1, charcoal2, charcoal_smoke_campfire, tree1, tree2, tree3, oxygen1, oxygen_sunflower,
          wood1, wood2, wood3, wood4, lumberjack1, lumberjack2, axe1, axe2, axe_sword, pebble1, pebble2, pebble3, rock1, rock2, rock3, blade1, blade2, blade3, blade4, sword1, sword2, granite1, granite2, granite_eruption,
          eruption1, volcano1, boulder1, boulder2, boulder3, boulder4, boulder5, corpse1, corpse2, corpse3, corpse_blood, death1, death2, phoenix1, phoenix2, phoenix_omelette, egg1, egg2, omelette1, omelette2, fish1,
          fish2, fish3, fish4, fish_roe, fish_roe2, fish_roe3, fish_roe4, roe1, fishingrod1, rainbow1, rainbow2, rainbow3, rainbow4, rainbow5, magic1, magic2, wizard1, wizard2, wand1, wand2, wand3, wand4, pencil1, pencil2]
# GAME CODE:
inventory = [air, water, earth, fire]
items_crafted = 4
TOTAL_ITEMS = len(items)
fire.uses -= 3  # Air - 1, Fire - 2
mist.uses -= 1
heat.uses -= 2
# ice.uses -= 1
# snow.uses -= 1
coal.uses -= 1
# alcohol.uses -= 1
while items_crafted < TOTAL_ITEMS:  # The minus value is until we can get all items in the game at any one time.
    show_inventory()
    input_items()
    check_depleted()
    if not time_item.discovered and items_crafted >= 100:
        clear_console()
        print("You have created 100 items, GG! Have a free item:")
        print("")
        input("Press Enter to Continue: ")
        item_discovered(time_item)
print("You have made everything in the game!")
print("")
input("Press Enter to Quit: ")
