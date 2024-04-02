# Mason Dalton
# Section 3
# Description: Run the soccer season for a home team. 
# By taking the input about team names and number of games I will then calculate 
# the scores, win/loss pct, display how season went for home team


# needed to generate random scores
import random

class SoccerTeam():
    # constructor. Creates the soccerTeam object when called
    def __init__(self, team_name):
        self.team_name = team_name
        self.wins = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_allowed = 0

    # generates the score with the standard chance
    def generateScore(self):
        return random.randint(0, 4)
            
    def seasonStatus(self):
        # depending on the win rate, display different final messages.
        if self.wins / (self.wins + self.losses) >= .75:
            message = "Qualified for the NCAA Women's Soccer Tournament"
        elif self.wins / (self.wins + self.losses) >= .5:
            message = "You had a good season"
        else:
            message = "Your team needs to practice!"
        return message
    
# here create a class called SponsoredTeam that inherits from SoccerTeam.
# and a generateScore method and seasonStatus method
class SponsoredTeam(SoccerTeam):

    # Constructor that inherits from the team class
    def __init__(self, Sponsor, team_name):
        super().__init__(team_name)
        self.sponsor_name = Sponsor

    # Method to generate the score for a team during a game 
    def generateScore(self):
        return random.randint(1, 4)
    
    # Method to take the wins/losses to calc win pct and return the message and how the sponsor feels
    def seasonStatus(self):
        if self.wins / (self.wins + self.losses) >= .75:
            message = f"Qualified for the NCAA Women's Soccer Tournament. {self.sponsor_name} is very happy."
        elif self.wins / (self.wins + self.losses) >= .6:
            message = f"{self.sponsor_name} thinks you had a good season but hopes you can do better."
        else:
            message = f"You are in danger of {self.sponsor_name} dropping you"
        return message

# Game class with constructor that stores a home team, and an away team, 
# as well as a method for gameStatus to return the game score for both teams
class Game():
    def __init__(self, homeTeam, awayTeam, homeScore, awayScore) :
        self.home_team = homeTeam
        self.away_team = awayTeam
        self.home_score = homeScore
        self.away_score = awayScore

    def gameStatus(self) :
        return "The Home team " + self.home_team + " scored " + str(self.home_score) + ". The away team " + self.away_team + " scored " + str(self.away_score) + "."
    
# get the inputs
sHomeTeamName = input("Enter the name of your team (the home team): ")
sIsSponsoredTeam = input("If your team is sponsored, enter the name of the sponsor. Otherwise enter N: ")
iNumGamesPlayed = int(input("Enter the number of teams that " + sHomeTeamName + " will play (1-10): "))

# creates a soccerTeam object and stores it in the variable homeTeam
if sIsSponsoredTeam.upper() != "N":
    oHomeTeam = SponsoredTeam(sIsSponsoredTeam, sHomeTeamName)
else:
    oHomeTeam = SoccerTeam(sHomeTeamName)

# this is creating an empty list for the away teams and an empty list for the games.
opponentTeamsList = []
gamesList = []

# run the loop for however many games the user entered
for game in range(1, iNumGamesPlayed +1):

    # get away team name
    sAwayTeamName = input(f"Enter the name of the away team for game {game}: " )

    # make the away team object. make sure to randomly make the away team a sponsored or normal team (50% chance)
    # randomly make the team a sponsored team or not:
    iChance = random.randint(0,1)

    if iChance == 1 :
        oAwayTeam = SponsoredTeam("Enemy Sponsor", sAwayTeamName)
    else :
        oAwayTeam = SoccerTeam(sAwayTeamName)

    # generate scores for both teams by calling generateScore()
    iHomeScore = oHomeTeam.generateScore()
    iAwayScore = oAwayTeam.generateScore()

    # keep generating scores if they are the same
    while iHomeScore == iAwayScore :
        iHomeScore = oHomeTeam.generateScore()
        iAwayScore = oAwayTeam.generateScore()

    # record goals scored & goals allowed
    # For the home team
    oHomeTeam.goals_allowed += iAwayScore
    oHomeTeam.goals_scored += iHomeScore
    # For the away team
    oAwayTeam.goals_allowed += iHomeScore
    oAwayTeam.goals_scored += iAwayScore

    #keep track of wins and losses for the home team and away team (similar to the above code)
    if iHomeScore > iAwayScore :
        oHomeTeam.wins += 1
        oAwayTeam.losses += 1
    else :
        oHomeTeam.losses += 1
        oAwayTeam.wins += 1

    # display the score for this game
    print(f"{oHomeTeam.team_name}'s score: {iHomeScore} {sAwayTeamName}'s score: {iAwayScore}")
    
    # Append away team to the team list, and create a new game object:
    opponentTeamsList.append(oAwayTeam.team_name)
    gamesList.append(Game(oHomeTeam.team_name, oAwayTeam.team_name, iHomeScore, iAwayScore))

# Disply: team name, season record, goals score/allowed, and the season Status.
print(f"\nTeam Name: {oHomeTeam.team_name}")
print(f"Final season record: {oHomeTeam.wins} - {oHomeTeam.losses}")
print(f"Total goals scored: {oHomeTeam.goals_scored} - Total goals allowed: {oHomeTeam.goals_allowed}")
print(oHomeTeam.seasonStatus())

# This is a loop that will keep asking for a game number until you type exit.
gameSelector = 0
while gameSelector != "exit":
    gameSelector = input(f"\nEnter in a game number between 1 and {iNumGamesPlayed} to see the stats of that game. Otherwise type exit: ")

    if gameSelector.isdigit():
        gameSelector = int(gameSelector)
        selectedGame = gamesList[gameSelector-1]
        print(selectedGame.gameStatus())
