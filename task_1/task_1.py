import sqlite3
import pandas as pd
import os


pd.set_option('display.max_column', None)

# Leave that code unchanged, it is required for the server check!
db = sqlite3.connect(os.environ.get("DB_PATH") or './dataset_1/database.sqlite')

# You may load the data from SQL table directly to the Pandas dataframe as
player_data = pd.read_sql("SELECT * FROM Player;", db)

player_data.head()

# TODO Task 1 (0.25 point). Calculate the number of players with a height between 180 and 190 inclusive
players_180_190 = player_data[player_data["height"].between(170, 190, 'both')].shape[0]  # Your code here
assert(isinstance(players_180_190, int))

# TODO Task 2 (0.25 point). Calculate the number of players born in 1980.
# Hint: you may want to cast your 'birthday' column to DateTime type by pandas.to_datetime
players_1980 = list(pd.DatetimeIndex(player_data["birthday"]).year).count(1980)  # Your code here
assert(isinstance(players_1980, int))

# TODO Task 3 (0.25 point). Make a list of the top 10 players with the highest weight sorted in descending order.
# If there are several players with the same weight put them in the lexicographic order by name.
highest_players = player_data.sort_values(by=["weight"], ascending=False)[0:10]  # Your code here
highest_players = sorted(highest_players["player_name"].values.tolist())

assert(len(highest_players) == 10)
assert(isinstance(highest_players, list))
for i in range(10):
    assert(isinstance(highest_players[i], str))

# TODO Task 4 (0.5 point). Make a list of tuples containing years along with the number of players born in that year
# from 1980 up to 1990. Structure example: [(1980, 123), (1981, 140) ..., (1990, 83)] ->
# There were born 123 players in 1980, there were born 140 players in 1981 and etc.
years_born_players = []
years = list(pd.DatetimeIndex(player_data["birthday"]).year)  # Your code here

for year in list(set(years)):
    if 1980 <= year <= 1990:
        years_born_players.append((year, years.count(year)))

assert(len(years_born_players) == 11)
assert(isinstance(years_born_players, list))
for i in range(10):
    assert(isinstance(years_born_players[i], tuple))
    assert(isinstance(years_born_players[i][0], int))
    assert(isinstance(years_born_players[i][1], int))


# TODO Task 5 (0.5 point). Calculate the mean and the standard deviation of the players' height with the name Adriano.
# Note: Name is represented by the first part of player_name.

adriano_mean, adriano_std = player_data.loc[player_data["player_name"] == "Adriano"]["height"].mean(), \
                            player_data.loc[player_data["player_name"] == "Adriano"]["height"].std()  # Your code here
assert(isinstance(adriano_mean, float))
assert(isinstance(adriano_std, float))

# TODO Task 6 (0.75 point). How many players were born on each day of the week?
# Find the day of the week with the minimum number of players born.
dow_with_min_players_born = list(pd.DatetimeIndex(player_data["birthday"]).weekday)  # Your code here
values = list(set(dow_with_min_players_born))
counts = []
for i in values:
    counts.append(dow_with_min_players_born.count(i))

if counts.index(min(counts)) == 6:
    dow_with_min_players_born = "Sunday"
if counts.index(min(counts)) == 5:
    dow_with_min_players_born = "Saturday"
if counts.index(min(counts)) == 4:
    dow_with_min_players_born = "Friday"
if counts.index(min(counts)) == 3:
    dow_with_min_players_born = "Thursday"
if counts.index(min(counts)) == 2:
    dow_with_min_players_born = "Wednesday"
if counts.index(min(counts)) == 1:
    dow_with_min_players_born = "Tuesday"
if counts.index(min(counts)) == 0:
    dow_with_min_players_born = "Monday"

assert(isinstance(dow_with_min_players_born, str))


# TODO Task 8 (1.25 point). Find a player who participated in the largest number of matches during the whole match history.
# Assign a player_name to the given variable

max_matches_player = '' # Your code here
assert(isinstance(max_matches_player, str))


# TODO Task 9 (1.5 point). List top-5 tuples of most correlated player's characteristics in the descending order of the
# absolute Pearson's coefficient value.

# Note 1: Players characteristics are all the columns in Player_Attributes table except
# [id, player_fifa_api_id, player_api_id, date, preferred_foot, attacking_work_rate, defensive_work_rate]).
# Note 2: Exclude duplicated pairs from the list. E.g. ('gk_handling', 'gk_reflexes') and
# ('gk_reflexes', 'gk_handling') are duplicates, leave just one of them in the resulting list.

# Hint: You may use dataframe.corr() for calculating pairwise Pearson correlation.

top_correlated_features = '' # Your code here
assert(len(top_correlated_features) == 5)
assert(isinstance(top_correlated_features, list))
for i in range(5):
    assert(isinstance(top_correlated_features[i], tuple))
    assert(isinstance(top_correlated_features[i][0], str))
    assert(isinstance(top_correlated_features[i][1], str))


# TODO Task 10 (2 points). Find top-5 most similar players to Neymar whose names are given.
# The similarity is measured as Euclidean distance between vectors of players' characteristics (described in the task above).
# Put their names in a vector in ascending order by Euclidean distance and sorted by player_name if the distance is the same
# Note 1: There are many records for some players in the Player_Attributes table.
# You need to take the freshest data (characteristics with the most recent date).
# Note 2: Use pure values of the characteristics even if you are aware of such preprocessing technics as normalization.
# Note 3: Please avoid using any built-in methods for calculating the Euclidean distance between vectors,
# think about implementing your own.

neymar_similarities = ''  # Your code here
assert(len(neymar_similarities) == 5)
assert(isinstance(neymar_similarities, list))
for i in range(5):
    assert(isinstance(neymar_similarities[i], str))


# TODO Task 11 (1 point). Calculate the number of home matches played by the Borussia Dortmund team in Germany 1.
# Bundesliga in season 2008/2009

borussia_bundesliga_2008_2009_matches = '' # Your code here
assert(isinstance(borussia_bundesliga_2008_2009_matches, int))


# Task 12 (1 point). Find a team having the most matches (both home and away!) in the Germany 1. Bundesliga in 2008/2009 season.
# Return number of matches.

team_most_matches_bundesliga_2008_2009 = '' # Your code here
assert(isinstance(team_most_matches_bundesliga_2008_2009, int))


# TODO Task 13 (1 point). Count total number of Arsenal matches (both home and away!) in the 2015/2016 season which they have won.

# Note: Winning a game means scoring more goals than an opponent.

arsenal_won_matches_2015_2016 = '' # Your code here
assert(isinstance(arsenal_won_matches_2015_2016, int))


# TODO Task 14 (2 points). Find a team with the highest win rate in the 2015/2016 season.
# Win rate means won matches / all matches. If there are several teams with the highest win rate return the first by name in lexical order

team_highest_winrate_2015_2016 = ''   # Your code here
assert(isinstance(team_highest_winrate_2015_2016, str))


# TODO Task 15 (2 points). Determine the team with the maximum days' gap between matches in England Premier League 2010/2011 season.
# Return number of days in that gap.
# Note: a gap means the number of days between two consecutive matches of the same team.

highest_gap_england_2010_2011 = '' # Your code here
assert(isinstance(highest_gap_england_2010_2011, int))


# Warning! Do not change anything in the area below
with open('student_answers.txt', 'w') as file:
    file.write(f"{players_180_190}\n")
    file.write(f"{players_1980}\n")
    file.write(f"{highest_players}\n")
    file.write(f"{years_born_players}\n")
    file.write(f"{round(adriano_mean, 3)} {round(adriano_std, 3)}\n")
    file.write(f"{dow_with_min_players_born}\n")
    file.write(f"{league_most_matches}\n")
    file.write(f"{max_matches_player}\n")
    file.write(f"{';'.join(['%s,%s' % tup for tup in top_correlated_features])};\n")
    file.write(f"{neymar_similarities}\n")
    file.write(f"{borussia_bundesliga_2008_2009_matches}\n")
    file.write(f"{team_most_matches_bundesliga_2008_2009}\n")
    file.write(f"{arsenal_won_matches_2015_2016}\n")
    file.write(f"{team_highest_winrate_2015_2016}\n")
    file.write(f"{highest_gap_england_2010_2011}\n")