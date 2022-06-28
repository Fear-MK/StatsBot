import requests
import json
from common import *

def api_request(ctx, args):
    name=[ctx.author.nick]

    if len(args) >= 2:
        if args[0].lower() in ladder_id:
            name, ladder=args[1:], ladder_id[args[0].lower()]
        else:
            name=args
            if ctx.channel.name[:2] in ladder_id:
                ladder = ladder_id[ctx.channel.name[:2]]
            else:
                ladder = ladder_id["rt"]
    elif len(args) == 1:
        if args[0].lower() in ladder_id and len(args) == 1:
            ladder = ladder_id[args[0].lower()]
        else:
            if ctx.channel.name[:2] in ladder_id:
                ladder = ladder_id[ctx.channel.name[:2]]
            else:
                ladder = ladder_id["rt"]
    elif len(args) == 0:
        ladder=ladder_id["rt"]

    if not isinstance(name, list):
        url=f"https://www.mkwlounge.gg/api/ladderplayer.php?player_name={name}&ladder_id={ladder}"
    else:
        url=f"https://www.mkwlounge.gg/api/ladderplayer.php?player_names={',%20'.join(name)}&ladder_id={ladder}"

    print(url)

    data=requests.get(url)

    try:
        if len(json.loads(str(data.text))["results"]) == 0:
            return False
    except KeyError:
        return False

    return json.loads(data.text)