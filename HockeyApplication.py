import json 

class Statistics:
    def __init__(self, players: list) -> None:
        self.players = players
    
    def search_for_player(self,name: str):
        for player in self.players:
            if player["name"] == name:
                return player
    
    def teams_in_order(self):
        return sorted(list(set(map(lambda player: player["team"], self.players))))
    
    def countries_in_order(self):
        return sorted(list(set(map(lambda player: player["nationality"], self.players))))
    
    def players_by_team(self,team):
        return sorted([player for player in self.players if player["team"] == team],reverse=True,key= lambda player: player["goals"]+player["assists"])
    
    def players_by_country(self,country):
        return sorted([player for player in self.players if player["nationality"] == country],reverse=True,key= lambda player: player["goals"]+player["assists"])

    def most_points(self):
        return sorted(self.players,key=lambda player: player["goals"]+player["assists"],reverse=True)
    
    def most_goals(self):
        return sorted(self.players,key=lambda player: (player["goals"], -player["games"]),reverse=True)
        

class HockeyStatsApplication:
    def __init__(self) -> None:
        self.statistics = None
    
    def load_data(self):
        file = input("file: ")
        with open(file) as file:
            data = file.read()
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.statistics = Statistics(players)
    
    def print_player(self, player: dict):
        print(f"{player['name']:21}{player['team']}{player['goals']:4} +{player['assists']:3} ={player['goals']+player['assists']:4}")
        
    def search_for_player(self):
        name = input("name: ")
        print("")
        player = self.statistics.search_for_player(name)
        self.print_player(player)
    
    def teams_in_order(self):
        for team in self.statistics.teams_in_order():
            print(team)
    
    def countries_in_order(self):
        for country in self.statistics.countries_in_order():
            print(country)
    
    def player_by_team(self):
        team = input("team: ")
        print("")
        for player in self.statistics.players_by_team(team):
            self.print_player(player)

    def player_by_country(self):
        country = input("country: ")
        print("")
        for player in self.statistics.players_by_country(country):
            self.print_player(player)

    def most_points(self):
        n = int(input("how many players? "))
        for player in self.statistics.most_points()[0:n]:
            self.print_player(player)
    
    def most_goals(self):
        n = int(input("how many players? "))
        for player in self.statistics.most_goals()[0:n]:
            self.print_player(player)
    
    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 list all teams")
        print("3 list all countries")
        print("4 list players by team")
        print("5 list players by country")
        print("6 most points")
        print("7 most goals")

    
    def execute(self):
        self.load_data()
        print("")
        self.help()
        while True:
            print ("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()
            elif command == "2":
                self.teams_in_order()
            elif command == "3":
                self.countries_in_order()
            elif command == "4":
                self.player_by_team()
            elif command == "5":
                self.player_by_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()



application = HockeyStatsApplication()
application.execute()