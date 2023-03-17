# blackjack
Coding Temple Weekend Project #4
***

This is my fourth weekend project for Coding Temple. The assignment was to make a Blackjack program using **object-oriented programming** in  **Python**.

I used a hybrid approach rather than full OOP: there is a player class instantiated as Player and Dealer, but other gameplay functions exist outside of classes.

This project was much more complicated than I anticipated. As a result I wasn't able to spend as much time on user interface features like colors and timing. They can onnly be found in the title menu.

### installation/configuration/etc.
This program plays a game of Blackjack with the user. The computer plays the role of dealer. The deck tracks what cards have been played from hand to hand but is reshuffled at the beginning of any hand when less than 10 cards are left. The user is prompted for input when necessary.

This blackjack program requires no installation and has no configuration options short of editing the code directly. Simply navigate to the directory where it is saved and type '''python blackjack.py''' or '''python3 blackjack.py''' to run. Alternately, you may be able to run it by typing '''./blackjack.py''', but this will likely involve extra steps. Depending on your setup, you may need to edit the first line of the program so it points to where Python is installed in your system. In addition, it might be necessary to modify ownership and permissions on the file (via '''chmod 755''' or something similar). 
