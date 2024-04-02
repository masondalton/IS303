# Mason Dalton
# 003

# This Project creates a Class for initating team objects. 
# Within the class is the method for returning qualification status
# Take Home team and number of games and play games for the season in a loop
# Then display season record and qualification status
import random

class soccerTeam : 
    # This is my custom constructor that will pass the needed values of each team on intiation
    def __init__ (self, teamName, totalWins, totalLosses, goalsScored, goalsAllowed) :
        self.team_name = teamName
        self.wins = totalWins
        self.losses = totalLosses
        self.goals_scored = goalsScored
        self.goals_allowed = goalsAllowed

    # Method to take calc winning ratio and return correct phrase
    def seasonStatus(self) :
        # Calc winning percentage
        fPercWon = self.wins / (self.wins + self.losses)

        # Return the status of team based on win percentage
        if (fPercWon >= .75) :
            return ( "\nQualified for the NCAA Women's Soccer Tournament" )
        elif (fPercWon >= .50) :
            return ( "\nYou had a good season" )
        else :
            return ( "\nYour team needs to practice!" )

# Get team name and total number of games in the season from the User
sHomeTeam = input( "Your team name: " )
iNumGames = int( input( "Enter number of games this season: " ) )

# Create object for the home team
oHomeTeam = soccerTeam(sHomeTeam, 0, 0, 0, 0)

for iCount in range(iNumGames) :
    # Get name of the opposing team for the current game
    iCurrAwayTeam = input( "Enter the name of away team for game " + str(iCount+1) + ": " )

    # Calculate both team's score for the game
    iAwayScore = random.randint(0, 12)
    iHomeScore = random.randint(0, 12)

    # Making sure there are no ties
    while iAwayScore == iHomeScore :
        iAwayScore = random.randint(0, 12)
        iHomeScore = random.randint(0, 12)

    # This tracks the scores allowed and scored by the home team
    oHomeTeam.goals_scored += iHomeScore
    oHomeTeam.goals_allowed += iAwayScore

    # Increment wins or losses based on the results of the current game
    if (iAwayScore < iHomeScore) :
        oHomeTeam.wins += 1
    else :
        oHomeTeam.losses += 1

    # Print Game results
    print(oHomeTeam.team_name + "'s score: " + str(iHomeScore) + " " + iCurrAwayTeam + "'s score: " + str(iAwayScore))

# This is the example output:
# Final Output Team Name: BYU
# Final season record: 2 - 1
# Total goals scored: 18 - Total goals allowed: 12
# You had a good season

print("Team Name: " + oHomeTeam.team_name + "\nFinal Season Record: " + str(oHomeTeam.wins) + " - " + str(oHomeTeam.losses) + "\nTotal Goals Scored: " + str(oHomeTeam.goals_scored) + " - " + "Total Goals Allowed: " + str(oHomeTeam.goals_allowed) + oHomeTeam.seasonStatus())
