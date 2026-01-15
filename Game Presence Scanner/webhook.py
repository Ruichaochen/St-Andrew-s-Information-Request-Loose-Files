from requests import post
from requests import get
from datetime import datetime, timezone
webhook_url = ""
def post_roblox(player_data):
    name, profile = player_data.name, player_data.profile
    if player_data.presence == "InGame":
        is_private = player_data.isPrivate
        if not is_private:
            place_url, place_name, launch_link, icon_url  = player_data.place_url, player_data.place_name, player_data.launch_link, player_data.game_icon_url
            post(webhook_url, json = {
                "embeds": [
                    {
                        "title": "Someone is Online!",
                        "color": 11346723,
                        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                        "url": profile,
                        "author": {
                            "url": "https://discord.com"
                        },
                        #"thumbnail": {
                        #    "url": "https://i.postimg.cc/DybY4MYD/minecraft-logo-icon-168974.png"
                        #},
                        "image": {
                            "url": icon_url
                        },
                        "footer": {
                            "text": "Presence scanner",
                            "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png"
                        },
                        "fields": [
                        {
                            "name": "Currently playing:",
                            "value": place_name,
                            "inline": False
                        },
                        {
                            "name": "Link:",
                            "value": place_url,
                            "inline": False
                        },
                        {
                            "name": "Direct Join Link:",
                            "value": launch_link,
                            "inline": False
                        }
                    ],
                        "description": f"{name} is Online on Roblox"
                    }
                ]
            })
        else:
                        post(webhook_url, json = {
                "embeds": [
                    {
                        "title": "Someone is Online!",
                        "color": 11346723,
                        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                        "url": profile,
                        "author": {
                            "url": "https://discord.com"
                        },
                        #"thumbnail": {
                        #    "url": "https://i.postimg.cc/DybY4MYD/minecraft-logo-icon-168974.png"
                        #},
                        "footer": {
                            "text": "Presence scanner",
                            "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png"
                        },
                        "fields": [
                        {
                            "name": "Their activity is private.",
                            "value": "",
                            "inline": False
                        },
                    ],
                        "description": f"{name} is Online on Roblox"
                    }
                ]
            })
    else:
        headshot = get("https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={}&size=420x420&format=Png&isCircular=false".format(player_data.user_id)).json()["data"][0]["imageUrl"]
        post(webhook_url, json = {
            "embeds": [
                {
                    "title": "Someone is Online!",
                    "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                    "color": 50175,
                    "url": profile,
                    "author": {
                        "url": "https://discord.com"
                    },
                    "footer": {
                        "text": "Presence scanner",
                        "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png"
                    },
                    "description": f"{name} is Online on Roblox",
                    "thumbnail": {
                        "url": headshot
                    }
                }
            ]
        })
def post_hypixel(name):
    post(webhook_url, json = {
        "embeds": [
            {
                "title": "Someone is Online!",
                "color": 4321431,
                "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "url": "https://discord.com",
                "author": {
                    "url": "https://discord.com"
                },
                "thumbnail": {
                    "url": "https://i.postimg.cc/DybY4MYD/minecraft-logo-icon-168974.png"
                },
                "footer": {
                    "text": "Presence scanner",
                    "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png"
                },
                "description": f"{name} is Online on Roblox"
            }
        ]
    })
