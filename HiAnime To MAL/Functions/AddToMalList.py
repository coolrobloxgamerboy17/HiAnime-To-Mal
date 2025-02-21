import requests
import shlex
import re
import json


def Main(Info, Curl):
    Statuses = {
        "plan_to_watch": 6,
        "dropped": 4,
        "on_hold": 3,
        "completed": 2,
        "watching": 1,
    }
    LostAnime = []

    for Item in Info:
        Tokens = shlex.split(Curl)
        CookieIndex = next(
            (
                Index
                for Index, Token in enumerate(Tokens)
                if Token.lower() == "-h"
                and Tokens[Index + 1].lower().startswith("cookie:")
            ),
            None,
        )

        Cookies = {}
        Tolkien = ""

        if CookieIndex is not None:
            CookieStr = Tokens[CookieIndex + 1][7:].strip()
            Cookies = dict(re.findall(r"([^=]+)=([^;]+)", CookieStr))

        Match = re.search(r'csrf_token":"([^"]+)"', Curl)
        if Match:
            Tolkien = Match.group(1)

        AniId = Item["Id"]
        Status = Statuses[Item["Status"]]
        Data = json.dumps(
            {
                "anime_id": int(AniId),
                "status": Status,
                "csrf_token": Tolkien,
            }
        )

        Response = requests.post(
            "https://myanimelist.net/ownlist/anime/add.json",
            cookies=Cookies,
            data=Data,
        )
        if Response.status_code == 200:
            print(
                f"Anime {AniId} has been added to your list with the status of {Status}."
            )
        elif Response.status_code == 405:
            LostAnime.append((AniId, Status))
            Curl = input(
                "Auth has become invalid. Please put in another (The Mal thing). "
            )
        else:
            LostAnime.append((AniId, Status))
            print(
                f"Something failed with adding anime to the list. Status code {Response.status_code}"
            )
    print(LostAnime)
    return LostAnime
