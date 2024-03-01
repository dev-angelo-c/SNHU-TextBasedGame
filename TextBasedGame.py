#Jack Crish
import time


def main():
  
  # modify game visualzations, sleep timers, etc.
  configuration = {
    'mini_game':{
      'column_width' : 20
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
    "Stone of Fire": True,
    "Angel Wing": False,
    "Tooth": False,
    "Marble Eye": False,
    "Giza Stone": False
  }

  #A dictionary for the simplified dragon text game
  #The dictionary links a room to other rooms.
  rooms = {
    'Library': {
      'South': 'Reflections Studio'
    },
    'Reflections Studio': {
      'North': 'Library', 
      'South': 'Room of Repentance'
    },
    'Room of Repentance': {
      'North': 'Reflections Studio', 
      'South': 'Pool of Sacred Tears'
    },
    'Pool of Sacred Tears':{
      'North': 'Room of Repentance',
      'South': 'Studio of Revelations'
    },
    'Studio of Revelations':{
       'North': 'Room of Repentance',
       'South': 'Hall of Destiny'
    }, 
    'Hall of Destiny': {
       'North': 'Studio of Revalations',
       'South': 'Great Dining Area'
    },
    'Great Dining Area':{
       'East': 'Lounge'
    },
    'Lounge':{
       'East': "Exit"
    }
  }

  artifact_location = zip(rooms, inventory_loadout)

  for i in artifact_location:
    print(i)

  # visuals
  def print_main_headings(text):
    print("#" * configuration['viz']['width'])
    print(f"{text:-^{configuration['viz']['width']}}")
    print("#" * configuration['viz']['width'] + "\n")
    time.sleep(configuration['sleep']['heading'])

  # print instructions
  def print_instructions():

    instructions = {
      #print a main menu and the commands
      1: "Dragon Text Adventure Game",
      2: "Collect 6 items to win the game, or be eaten by the dragon.",
      3: "Move commands: go South, go North, go East, go West",
      4: "Add to Inventory: get 'item name'"
    }

    print(f"{'Instructions:':*^30}")

    for i in instructions:
      print( f"{i} {instructions[i]}" )

    print("*" * 30)

  #probably needs broken down into smaller functions
  def display_capture_artifact(item="Tablet"):

    if item in inventory_loadout and inventory_loadout[item] is False:
      print(f" # Adding {item} to inventory...")
      inventory_loadout[item] = True

    

    item_str = ""
    item_captured = ""
    numbered_items = ""
    
    #could use enumerate but no need to make it too complicated. Just for visuals anyway
    for i in range(1,7):
      numbered_items += f"{i:^{configuration['mini_game']['column_width']}}"
    for key in inventory_loadout:
      item_str += f"{key:^{configuration['mini_game']['column_width']}}"
      item_captured += f"{str(inventory_loadout[key]):^{configuration['mini_game']['column_width']}}"
    
    print(numbered_items, " - ")
    print(item_str, " - ")
    print(item_captured, " - ")

   # print("LOADOUT : ", loadout)
    #print("INVENTORY ", inventory_loadout)
    return inventory_loadout

  # artifact collection and ordering
  def mini_game():
    print("")
    print("#" * configuration['viz']['width'])
    print(" #Order the artifacts appropriately so you can defeat the dragon")
    print("#" * configuration['viz']['width'])
    print("")
    print(" # Current Inventory: ") 
    
    display_capture_artifact()
  
  # global exit
  def exit_room(): 
    print_main_headings("Thank you for playing")
    return

  # Display welcome message
  def display_intro():
    print_main_headings("DECEPTION DRAGON")
    print_instructions()
    time.sleep(configuration['sleep']['intro'])

  # Get user Direction Input
  def pick_direction(room):
      
      #Display Rooms
      print("")
      
      print("#" * configuration['viz']['width'])
      print(f"# You are in the: \n {room:^{configuration['viz']['width']}} ") 
      print("#" * configuration['viz']['width'])
      print(f"# You can move:")
      
      #reveal options to player
      for i in rooms[room]:
        print(f"  {'-'} {i:<7} {'to the '} {rooms[room][i]:<10} {'-':<10}")
      
      print("#" * configuration['viz']['width'])
      
      #Gather input
      user_defined_direction:str = input(f"# Which direction would you like to go? \n  -> ")

      print(f"{'# Moving you'.rjust(10)} {user_defined_direction}")
      time.sleep(configuration['sleep']['movement'])
      
      return user_defined_direction

  ################################
  ### Main Game Recursive Loop ###
  ################################
  def game_loop(room):
        
    # establish direction
    direction: str = pick_direction(room)
    
    # validation
    if direction != "exit":
      try:
        game_loop(rooms[room][direction])
      except KeyError as e:
        print(f"Incorrect Entry. Please review the list of available rooms")
        print(f"{e} is not a valid entry")          
        game_loop(room)
      except:
        print(" You've found a backdoor")
        exit_room()
    else:
      print("Exit Heard ")
      time.sleep(configuration['sleep']['exit'])
      exit_room()
      return

    # start Game

  # Begin the game
  display_intro()
  game_loop("Library")
  
  # initialize mini game for artifact collection and ordering
  # after main loop has exited
  mini_game()

if __name__ == "__main__": 
    main()
