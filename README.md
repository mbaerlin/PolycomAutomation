PolycomAutomation
=================

Project to automate polycom phone wall and test beds

Notes:
    1.  Every call should start from the home menu
    2.  Use a map for the softkeys so that new phones / firmware changes can be added later
    3.  Automate the phone to accept push and log to file
    4.  Need a state machine for soft keys

Found that I need to construct the authorization header each time or else it did not respond to the 401
Tried using session, but it did not work, still need to construct the AUTH each time
I can push curl commands using supprocess; very kludgy but works which is better than elegant and broken
The methods I use to construct the strings can be used with requests if I ever get it working