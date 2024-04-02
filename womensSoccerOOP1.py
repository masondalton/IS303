# Mason Dalton
# 003

# This Project creates a Class for initating team objects.
# Within the class is the method for returning qualification status based on win percentage
class soccerTeam : 
    # This is my custom constructor that will pass the needed values of each team on intiation
    def __init__ (self, team_name, wins, losses, goals_scored, goals_allowed) :
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_allowed = goals_allowed

    # Method to take calc winning ratio and return correct phrase
    def seasonStatus(self) :
        # Calc winning percentage
        fPercWon = self.wins / (self.wins + self.losses)

        # Return the status of team based on win percentage
        if (fPercWon >= .75) :
            return ( "Qualified for the NCAA Women's Soccer Tournament" )
        elif (fPercWon >= .50) :
            return ( "You had a good season" )
        else :
            return ( "Your team needs to practice!" )

# Declare team object
oTeam = soccerTeam("BYU", 12, 8, 21, 17)

# Output the season record for the team
print(oTeam.seasonStatus())