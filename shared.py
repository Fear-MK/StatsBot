import requests
import json
from common import *

def split_args(args):
    for x in range(len(args)):
        args[x:x+1]=args[x].split(",")
    args = list(filter(None, args))
    return args

def api_request(ctx, args):
    print(ctx.message.author.nick)
    if len(args) == 0:
        name=[ctx.author.display_name]
        if ctx.channel.name[:2] in ["rt", "ct"]:
            ladder = ctx.channel.name[:2]
        else:
            ladder = "rt"
    elif args[0].lower() in ["rt","ct"]:
        ladder = args[0].lower()
        if len(args) == 1:
            name=[ctx.author.display_name]
        else:
            name = args[1:]
    else:
        name = args
        if ctx.channel.name[:2] in ["rt", "ct"]:
            ladder = ctx.channel.name[:2]
        else:
            ladder = "rt"

    url=f"https://www.mkwlounge.gg/api/ladderplayer.php?player_names={',%20'.join(name)}&ladder_id={ladder_id[ladder]}"

    data=requests.get(url)

    try:
        if len(json.loads(str(data.text))["results"]) == 0:
            return "Failed", "Failed"
    except KeyError:
        return "Failed", "Failed"

    return json.loads(data.text)["results"], ladder