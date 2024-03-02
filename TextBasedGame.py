#Jack Crish
import time


def main():
  
  # modify game visualzations, sleep timers, etc.
  configuration = {
    'mini_game':{
      'column_width' : 20
    },
    'main_game':{
      'column_width': 30
    },
    'sleep':{
      'heading': 0.4,
      'intro': 1.0,
      'movement': 0.8,
      'exit': 0.9
    },
    'viz':{
      'width': 30
    }
  }

  inventory_loadout = {
    "Tablet": False,
    "Stone of Fire": False,
    "Angel Wing": False,
    "Dolphin Tooth": False,
    "Marble Eye": False,
    "Giza Stone": False
  }

  #A dictionary for the simplified dragon text game
  #The dictionary links a room to other rooms.
  rooms = {
    'Library': {
      'South': 'Reflections Studio',
      'item': "Tablet"
    },
    'Reflections Studio': {
      'North': 'Library', 
      'South': 'Room of Repentance',
      'West': 'Great Dining Hall',
      'item': "Stone of Fire"
    },
    'Room of Repentance': {
      'North': 'Reflections Studio', 
      'South': 'Pool of Sacred Tears',
      'West': 'Great Dining Hall',
      'East': 'Library',
      'item': 'Angel Wing'
    },
    'Pool of Sacred Tears':{
      'North': 'Room of Repentance',
      'South': 'Studio of Revelations',
      'West': 'Great Dining Hall',
      'East': 'Library',
      'item': 'Dolphin Tooth'
    },
    'Studio of Revelations':{
      'North': 'Room of Repentance',
      'South': 'Hall of Destiny',
      'West': 'Great Dining Hall',
      'item': 'Marble Eye'
    }, 
    'Hall of Destiny': {
      'North': 'Studio of Revelations',
      'South': 'Great Dining Hall',
      'East': 'Room of Repentance',
      'item': 'Giza Stone'
    },
    'Great Dining Hall':{
      'East': 'Lounge',
      'West': 'Great Dining Hall',
      'item': 'Check your inventory'
    },
    'Lounge':{
      'East': 'Studio of Revelations',
      'South': 'Fight'
    }
  }

  # Combine rooms and inventory
  artifact_location = zip(rooms, inventory_loadout)

  # TODO: reveal inventory 
  def reveal_inventory() -> dict: 
    for i in inventory_loadout:
      if inventory_loadout[i] is True:
        print(i)
    return inventory_loadout

  # visuals
  def print_main_headings(text) -> None:
    configured_width = configuration['viz']['width']
    print("")
    print("#" * configured_width)
    
    print(f"{text:-^{configured_width}}")
    
    print("#" * configured_width)

    time.sleep(configuration['sleep']['heading'])

  # print instructions
  def print_instructions() -> None:
    configured_width = configuration['main_game']['column_width']
    instructions = {
      #print a main menu and the commands
      1: "Dragon Text Adventure Game",
      2: "Collect 6 items to win the game by the time you reach the lounge, or be eaten by the dragon.",
      3: "Move commands: 'South', 'North', 'East', 'West'",
      4: "Add to Inventory: get 'item name'", 
      5: "Type 'exit' or 'quit' to exit game at any time",
    }

    print(f"{'Instructions:':*^{configured_width}}")

    for i in instructions:
      print( f"{i} {instructions[i]}" )

    print("*" * configured_width)

  #probably needs broken down into smaller functions
  def capture_artifact(item, store_loadout={}) -> dict:
    configured_width = configuration['mini_game']['column_width']

    if item == 'Check your inventory':
      print_main_headings('PREPARE TO FIGHT')
    elif store_loadout[item] == False:
      print(f" # Adding {item} to inventory...")
      store_loadout[item] = True
    else:
      print(" I don't know what happened")

    item_str = ""
    item_captured = ""
    numbered_items = ""
    
    #could use enumerate but no need to make it too complicated. Just for visuals anyway
    for i in range(1,7):
      numbered_items += f"{i:^{configured_width}}"
    for key in store_loadout:
      item_str += f"{key:^{configured_width}}"
      item_captured += f"{str(inventory_loadout[key]):^{configured_width}}"
    
    print(f"""
{numbered_items:>{configured_width}} - 
{item_str:>{configured_width}} -
{item_captured:>{configured_width}} - 
""")
    
    return store_loadout

  # artifact collection and ordering
  def check_inventory(backpack = inventory_loadout, damage = 0) -> dict:
    print_main_headings("# Did you collect all necessary artifacts to defeat the dragon?")
    print(" # Current Inventory: ") 

    # Check that all artifacts were captured
    all_items_captured = list(filter(lambda item: item is False, backpack))
    print(f"Checking your inventory...")
    time.sleep(0.8)
    if len(all_items_captured) == 0:
      print(" You may begin the fight")
      time.sleep(0.2)
      print("Good First Strike")
      time.sleep(1.2)
      print("...")
      print("Good defense")
      time.sleep(0.4)
      print("...")
      print("Good defense")
      time.sleep(0.4)
      print_main_headings("You won the fight")
      return True
    else:
      # This has a return value of inventory_loadout but is not stored in memory so we use a closure as state management.
      # This is called 'technical debt' because I'm building myself into a corner. lol
      print(f" You have not collected all the artifacts and the dragon has taken {'s' if damage > 1 else ' '}/3{damage} of your life.")
      print(f" You cannot enter The Lounge until you have all the artifacts ")
      damage += 1
  
    return backpack, damage
  
  # global exit
  def exit_room() -> None: 
    print_main_headings("Thank you for playing")
    return

  # Display welcome message
  def display_intro() -> None:
    configured_time = configuration['sleep']['intro']
    print_main_headings("DECEPTION DRAGON")
    print_instructions()
    time.sleep(configured_time)

  # Show Current Rooms 
  def show_current_room(room) -> str:
    configured_width = configuration['viz']['width']

    #Display Rooms
    print_main_headings(f"# You are in the: \n {room:^{configured_width}} ")
    
    #reveal movement options to player
    print("You Can Move")      
    for i in rooms[room]:      
      if i != 'item':
        print(f"  {'-'} {i:<7} {'to the '} {rooms[room][i]:<20}  {'-':>10}")
    
    print("#" * configured_width)
  
  # Direction Input
  def get_next_move() -> str:
    configured_time = configuration['sleep']['movement']
    user_defined_direction:str = input(f"# Which direction would you like to go? \n  -> ")
    print(f"{'# Moving you:  '} {user_defined_direction}")
    time.sleep(configured_time)
    return user_defined_direction

  # Validate Move Error Checking
  def validate_move(move, room):
    configured_time: int = configuration['sleep']['exit']
    options_table = ['exit', 'quit', 'Check your inventory'] #, 'inventory']

    if move not in options_table:
      try:        
        collected_item = rooms[room]['item']
        new_room = rooms[room][move]
        print(f"# You collected the {collected_item}")        
        return collected_item, new_room
      except TypeError as e:
        print(f"{e} \n ### Please enter a string not a number")
      except KeyError as e:
        print(f"Incorrect Entry. Please review the list of available rooms")
        print(f"{e} is not a valid entry")          
      except:
        print(" You've found a trapdoor to escape! Goodbye! ")
        exit_room()
    elif move == 'Check your inventory':
      reveal_inventory()
    else:
      print("Exit Heard ")
      time.sleep(configured_time)
      exit_room()
    
  ################################
  ### Main Game Recursive Loop ###
  ################################
  def game_loop(room, current_inventory):
    
    won_the_fight = False
    show_current_room(room)
    move: str = get_next_move()

    if room != 'Lounge':
      new_item, new_room = validate_move(move, room)
      loop_inventory: str = capture_artifact(new_item, current_inventory)
    else: 
      won_the_fight = check_inventory(current_inventory, 0)
    
    
    if won_the_fight == False:
      game_loop(new_room, loop_inventory)
    else:
      print_main_headings("WINNER")
      return
    

  # Begin the game
  display_intro()
  game_loop("Library", inventory_loadout)

if __name__ == "__main__": 
    main()
