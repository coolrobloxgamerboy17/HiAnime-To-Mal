from bs4 import BeautifulSoup
from mal import AnimeSearch
import requests
import json
import os

HiAnime = json.loads(os.environ.get("YouAreEls", "{}"))["HiAnime"]["Base"]
FullList = []


def Main(List):
    Links = [(Item["Href"], Item["Title"], Item["Status"]) for Item in List]

    for Href, Title, Status in Links:
        Response = requests.get(HiAnime + Href)
        Soup = BeautifulSoup(Response.content, "html.parser")

        SyncScript = Soup.find("script", id="syncData")
        if SyncScript:
            JsonSync = json.loads(SyncScript.string)
            MalId = JsonSync.get("mal_id")

            if MalId:
                FullList.append({"Id": MalId, "Status": Status})
            else:
                Search = AnimeSearch(Title)
                if Search.results:
                    FullList.append({"Id": Search.results[0].mal_id, "Status": Status})
        else:
            Search = AnimeSearch(Title)
            if Search.results:
                FullList.append({"Id": Search.results[0].mal_id, "Status": Status})

    return [True, "Got all links.", FullList]
