# HiAnime-To-Mal

**How to use**
1. Run "Main.py"
2. Input your HiAnime "connect.sid" cookie (Look below to see how to get it)
3. Wait until it finishes
4. Wait again for the script to get Mal ids (might take like 5m)
5. Input your "cURL (bash)" request (Look below again to see how)
6. Wait for the script to add the anime to your Mal list
7. All Done<br><br>

**How to get the stuff**
- *connect.sid*
  1. Login to HiAnime and go the home page (You cannot be on a anime page. It will redirect you)
  2. Right click on HiAnime and press "Inspect element"
  3. Go to "Application" at the top and click on it
  4. On the left click on the "Cookies" dropdown button
  5. In the dropdown menu click on "https://hianime.to"
  6. Now find "connect.sid", copy it and then paste it in the "Main.py" terminal

- *cURL*
  1. Login to Mal
  2. Go to a random anime that is not in your list (I like to do "One Piece")
  3. Right click on the Mal anime page and press "Inspect element"
  4. Wait for the page to !fully! load and then press on the "(\)" icon next to the red icon. It should be just under network. If you hover over it for like 2 seconds it should say "Clear network log - Ctrl+L"
  5. Click on add to list and check in the "Inspect element" page again
  6. There should be a new item with this icon -> " $\color{orange}{\lbrace;\rbrace}$ ". It should be called "add.json" (next step below)
  7. Right click on it, hover over copy, and press "Copy as cURL (bash)"
  8. Paste it in the "Main.py" terminal
<br><br>
**To do list**
- Add a terminal that opens showing the progress of something that takes long.
- Add AniList also.
- Add the Hawk Tuah girl rugpulling her crypto coin
