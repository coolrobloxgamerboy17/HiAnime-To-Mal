from sys import exit as Stop
import json
import os

if __name__ == "__main__":
    os.environ["YouAreEls"] = json.dumps(
        {
            "HiAnime": {
                "Base": "https://hianime.to",
                "Watch": "/user/watch-list",
            },
            "MyAnimeList": {
                "Base": "https://myanimelist.net",
                "List": "/ownlist/anime/add.json",
            },
        }
    )
    MaxAnime = 0
    LostAni = [0, []]

    import Functions.GetWatchList as WatchList
    import Functions.AddToMalList as Import
    import Functions.GetMalAnime as GetAnime

    CookieResponse = input("What is your HiAnime cookie? ")
    if not CookieResponse.strip():
        print("Please enter a valid cookie nga!")
        Stop(0)

    print("Please wait a second.")
    HiWatchList = WatchList.Main({"connect.sid": CookieResponse})
    print(HiWatchList[1] + "\n")

    if HiWatchList[0] == True:
        MaxAnime = len(HiWatchList[2])

        print("Getting Mal links. This might take a while.")
        IdListStuff = GetAnime.Main(HiWatchList[2])
        if len(IdListStuff[2]) != MaxAnime:
            LostAni[0] = LostAni[0] + (MaxAnime - len(IdListStuff[2]))

        print("Dev", IdListStuff[2])

        print(IdListStuff[1] + "\n")
        Pasted = input("Paste your cURL thing. ")
        Losts = Import.Main(IdListStuff[2], Pasted)
        if len(Losts[2]) != MaxAnime:
            LostAni[0] = LostAni[0] + (MaxAnime - len(Losts[2]))
        LostAni[1].append((Losts[2]))
        print(LostAni[0], LostAni[1])

    else:
        Stop(0)
