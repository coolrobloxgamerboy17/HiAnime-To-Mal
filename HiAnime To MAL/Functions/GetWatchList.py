from bs4 import BeautifulSoup
from sys import exit as Stop
import requests
import json
import os

HiAnime = json.loads(os.environ.get("YouAreEls"))["HiAnime"]["Base"]
ListLink = json.loads(os.environ.get("YouAreEls"))["HiAnime"]["Watch"]

Statuses = {
    "watching": 1,
    "on_hold": 2,
    "plan_to_watch": 3,
    "dropped": 4,
    "completed": 5,
}


def IsValidCookie(Cookies) -> bool:
    response = requests.get(HiAnime + ListLink, cookies=Cookies)
    Soup = BeautifulSoup(response.content, "html.parser")
    return Soup.title.string != "HiAnime Free Anime Streaming Homepage"


def Main(Cookies):
    if not IsValidCookie(Cookies):
        return [False, "Cookie invalid."]

    with requests.Session() as Session:
        List: list[dict] = []
        for Status, StatusId in Statuses.items():
            Page = 1
            while True:
                response = Session.get(
                    HiAnime + ListLink,
                    params={"type": StatusId, "page": Page},
                    cookies=Cookies,
                )
                soup = BeautifulSoup(response.content, "html.parser")

                Titles = soup.find_all("a", class_="dynamic-name")
                if not Titles:
                    break

                for Title in Titles:
                    List.append(
                        {
                            "Title": Title.text.strip(),
                            "Href": Title["href"],
                            "Status": Status,
                        }
                    )
                Page += 1

    return [True, "Returned list.", List]
