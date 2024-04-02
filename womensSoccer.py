# Mason Dalton
# Section 003

# Program that asks about a home women’s soccer team, how many games they played in a season
# Then displays the scores of each game as well as the overall record of the home team for the season.
import random

# Take User input and declare variables
sTeamName = input("Enter your home team name (e.g. BYU): ")

# Here I take input for total games. I also practiced excpetion handling
bMoveOn = False
while (bMoveOn == False) :
    try:
        iNumGames = int( input("Enter number of games this season: ") )
        bMoveOn = True
    except:
        print("Please enter a whole number")

# Declare this variable to iterate on it in the loop
iGamesWon = 0

# Loop for all games. We take away team name, calc the score for each team during the game (no ties), 
# and then output winner
for iCount in range(iNumGames):
    iCurrAwayTeam = input("Enter the name of away team for game " + str(iCount+1) + ": ")

    iAwayScore = random.randint(0, 12)
    iHomeScore = random.randint(0, 12)

    # Making sure there are no ties
    while iAwayScore == iHomeScore :
        iAwayScore = random.randint(0, 12)
        iHomeScore = random.randint(0, 12)

    # Increment winning record to calc winning percentage at the end
    if (iAwayScore < iHomeScore) :
        iGamesWon += 1

    # Print Game results
    print(sTeamName + "'s score: " + str(iHomeScore) + " " + iCurrAwayTeam + "'s score: " + str(iAwayScore))

# Calc win/loss record and display it
iGamesLost = iNumGames - iGamesWon
print("Final Season Record: " + sTeamName + " " + str(iGamesWon) + "-" + str(iGamesLost))

# Find ratio and print out if they qualified for tourny
fPercWon = iGamesWon / iNumGames

# This is the logic for deciding if they qualify for the tourny based on winning percentage
if (fPercWon >= .75) :
    print("Qualified for the NCAA Women's Soccer Tournament")
elif (fPercWon >= .50) :
    print("You had a good season")
else :
    print("Your team needs to practice!")



'''
First version: I left this here for my own notes/learning

iTotalGames = iNumGames
lstAwayTeam = list()

# Get names of way teams based on total games for this season
while iNumGames != 0 :
    iCurrAwayTeam = input("Enter the name of away team for game " + str(iCount) + ": ")
    lstAwayTeam.append(iCurrAwayTeam)
    iCount += 1
    iNumGames -= 1

# Get team scores by randomizaiton and print who won
for team in lstAwayTeam :
    iAwayScore = random.randint(0, 12)
    iHomeScore = random.randint(0, 12)

    # Making sure there are no ties
    while iAwayScore == iHomeScore :
        iAwayScore = random.randint(0, 12)
        iHomeScore = random.randint(0, 12)

    # Increment winning record
    if (iAwayScore < iHomeScore) :
        iGamesWon += 1

    # Print Game results
    print(sTeamName + "'s score: " + str(iHomeScore) + " " + team + "'s score: " + str(iAwayScore))
'''
