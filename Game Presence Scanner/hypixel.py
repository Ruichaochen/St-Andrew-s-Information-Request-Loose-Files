from requests import post
from requests import get
from datetime import datetime, timezone
from re import match

api_key = ""
get_uuid_api = "https://api.mojang.com/users/profiles/minecraft/"# get uuid
uuid_to_user = "https://sessionserver.mojang.com/session/minecraft/profile/"# get username
pattern = "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"
        
class UUID:
    def __init__(self, uuid_string):
        if match(pattern, uuid_string):
            self.uuid = uuid_string
        elif len(uuid_string) == 32 and uuid_string.isalnum():
            formatted_uuid = "-".join([uuid_string[0:8],uuid_string[8:12], uuid_string[12:16], uuid_string[16:20], uuid_string[20:32]])
            self.uuid = formatted_uuid
        else:
            raise ValueError("UUID not valid")
    def __str__(self):
        return "<Object UUID with value '" + self.uuid + "'>"

class Player:
    def __init__(self, username, uuid = ""):
        if len(uuid) == 32 and uuid.isalnum() and username == "":
            data = get(uuid_to_user + uuid).json()
            if data.get("error"):
                raise ValueError("No such player found from UUID")
            else:
                self.username == data["name"]
                self.uuid = UUID(uuid)
        elif uuid == "" and username != "":
            data = get(get_uuid_api + username).json()
            if data.get("errorMessage"):
                raise ValueError("No such player found for value username " + username)
            else:
                self.username = data["name"]
                self.uuid = UUID(data["id"])
        else:
            raise ValueError("Please provide either a value uuid or username")
                
class Epoch():
    def __init__(self, time):
        if type(time) == int:
            if time >= 0:
                self.time = time/1000
            else:
                raise ValueError("Epoch must not be negative")
        elif (type(time) == str and time.isnum()):
            time = int(time)
            if time >= 0:
                self.time = int(time)/1000
            else:
                raise ValueError("Epoch is an invalid string")
        else:
             raise ValueError("Please provide a valid epoch")
        
    def toTimestamp(self):
        return datetime.fromtimestamp(self.time, timezone.utc)
    
    def __str__(self):
        return str(self.time)
        
        
            
class Hypixel:
    def __init__(self,username = "", uuid = ""):
        player = Player(username = username, uuid = uuid)
        player_data = get("https://api.hypixel.net/v2/player?uuid=" + player.uuid.uuid, headers = {
            "content_type" : "application/json",
            "API-Key" : api_key
            }).json()["player"]
        self.username = player.username
        self.displayname = player_data["displayname"]
        self.rank = player_data["newPackageRank"]
        self.lastLogin = Epoch(player_data["lastLogin"])
        self.lastLogout = Epoch(player_data["lastLogout"])
        if self.lastLogin.time > self.lastLogout.time:
            self.online = True
        else:
            self.online = False
