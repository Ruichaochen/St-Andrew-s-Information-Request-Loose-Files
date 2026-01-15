from requests import post
from requests import get
from cookie import get_roblox_cookie

ROBLOSECURITY = get_roblox_cookie()

presence_types = ["Offline", "Online", "InGame", "InStudio", "Invisible"]

class Roblox:
    def __init__(self,userId):
        self.isPrivate = False
        presence = post('https://presence.roblox.com/v1/presence/users', json={'userIds': [userId]}, cookies = {'.ROBLOSECURITY': ROBLOSECURITY}).json()
        name = get("https://users.roblox.com/v1/users/{}".format(userId)).json()
        self.presence = presence_types[presence["userPresences"][0]["userPresenceType"]]
        self.lastOnline = presence["userPresences"][0]["lastOnline"]
        self.user_id = userId
        self.name = name["name"]
        self.displayName = name["displayName"]
        self.profile = "https://www.roblox.com/users/{}/profile".format(userId)
        if self.presence == "InGame":
            if presence["userPresences"][0]["placeId"] == None:
                self.isPrivate = True
            else:
                self.isPrivate = False
                self.place_name = presence["userPresences"][0]["lastLocation"]
                self.placeId = presence["userPresences"][0]["placeId"]
                self.place_url = "https://www.roblox.com/games/{}".format(self.placeId)
                self.gameId = presence["userPresences"][0]["gameId"]
                self.game_icon_url = get("https://thumbnails.roblox.com/v1/assets?assetIds={}&size=768x432&format=Png&isCircular=false".format(presence["userPresences"][0]["placeId"])).json()["data"][0]["imageUrl"]
                self.launch_link = "Roblox.GameLauncher.joinGameInstance({}, '{}')".format(self.placeId, self.gameId)
