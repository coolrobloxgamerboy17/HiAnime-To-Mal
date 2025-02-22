# HiAnime-To-Mal

**How to Use**
1. Run `Main.py`.
2. Input your HiAnime "connect.sid" cookie (see below for instructions on how to obtain it).
3. Wait until the script finishes.
4. Wait for the script to retrieve Mal IDs (this might take about 5 minutes).
5. Input your "cURL (bash)" request (see below for instructions).
6. Wait for the script to add the anime to your Mal list.
7. All done!

<br>

**How to Obtain the Required Information**
- *connect.sid*
  1. Log in to HiAnime and go to the home page (you cannot be on an anime page, as it will redirect you).
  2. Right-click on the HiAnime page and select "Inspect Element."
  3. Go to "Application" at the top and click on it.
  4. In the left panel, click on the "Cookies" dropdown.
  5. In the dropdown menu, select "https://hianime.to."
  6. Find "connect.sid," copy it, and paste it into the `Main.py` terminal.

- *cURL*
  1. Log in to MyAnimeList (Mal).
  2. Go to a random anime that is not in your list (I like to use "One Piece").
  3. Right-click on the Mal anime page and select "Inspect Element."
  4. Wait for the page to fully load, then click the "(\)" icon next to the red icon, located just under the "Network" tab. If you hover over it for a couple of seconds, it should say "Clear network log - Ctrl+L."
  5. Click "Add to List" and check the "Inspect Element" panel again.
  6. There should be a new item with this icon -> " $\color{orange}{\lbrace;\rbrace}$ " It should be called "add.json" (see the next step).
  7. Right-click on it, hover over "Copy," and select "Copy as cURL (bash)."
  8. Paste it into the `Main.py` terminal (as one line).

<br>

**To-Do List**
- Add a terminal that opens to show the progress of long-running tasks.
- Add AniList support.
- Implement step-saving to avoid redoing tasks in case of mistakes.
- Add cURL validation to check if it is valid.
- Fix error codes 400 and 405; for the 405 errors, I need to address the "fixing."
- Enhance print statements for better visual appeal.
- Implement a check for lost anime.
- Display the name instead of the ID (and include the status).
- Add the Hawk Tuah girl rug-pulling her crypto coin while talking on Talk Tuah.

<br>

**Info**
- I would not recommend using this script right now, as it has some limitations. It can only handle about 120-140 requests before it breaks for some reason.
- If anyone wants to fork this or something similar, feel free to do so.
