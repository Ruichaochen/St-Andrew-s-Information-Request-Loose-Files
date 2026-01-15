from roblox import Roblox
from hypixel import Hypixel
from time_conversion import since_ms
from time import sleep
from webhook import post_roblox
presences = {}
users = [] # list of roblox userids
while True:
    for user_id in users:
        print(presences)
        player_data = Roblox(user_id)
        current_presence = player_data.presence
        
        print(current_presence)
        
        previous_presence = presences.get(user_id, None)
        if player_data.isPrivate:
            new_presence = current_presence
        else:
            new_presence = current_presence + player_data.launch_link if current_presence == "InGame" else current_presence
        
        if previous_presence == new_presence:
            print("Presence is the same. Passing")
        else:
            post_roblox(player_data)
            presences[user_id] = new_presence
    sleep(10)
#months, days, hours, minutes, seconds = since_ms(Hypixel("Ruichao").lastLogout.time)
#print("Last seen {} months, {} days, {} hours ago".format(months,days,hours))
