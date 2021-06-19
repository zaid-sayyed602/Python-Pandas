'''1. Group by the team and display all teams
2. Print all Riders teams Details
3. Print The maximum Points of Year 2014
4. Print all rank 1 teams
5. Print Each Teams Highest Points
6. Print Each Teams average Points'''


import pandas as pd
import numpy as np
df=pd.read_csv("Teams.csv")

print("QUESTION NO 1\n\n")
team=df.groupby("Team")
print(team.get_group("Riders"))
print(team.get_group("Devils"))
print(team.get_group(" Kings"))
print(team.get_group(" kings"))
print(team.get_group("Royals"))

print("\n\nQUESTION NO 2\n\n")
print(team.get_group("Riders"))

print("\n\nQUESTION NO 3\n\n")
year=df.groupby("Year")
a=year.get_group(2014)
print(a["Points"].agg(np.max))

print("\n\nQUESTION NO 4\n\n")
rank=df.groupby("Rank")
print(rank.get_group(1))

print("\n\nQUESTION NO 5\n\n")
team=df.groupby("Team")
print(team["Points"].agg(np.max))

print("\n\nQUESTION NO 6\n\n")
print(team["Points"].agg(np.mean))
