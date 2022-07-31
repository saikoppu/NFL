import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
teams = ["NE", "GB", "SF", "BAL", "PIT", "OAK", "DAL", "DEN", "WSH", "CAR", "PHI", "SEA", "JAG", "NYG", "IND", "MIA", "NYJ", "CHI", "BUF", "LAR", "TEN", "ARI", "NO", "MIN", "ATL", "LAC", "TB", "HOU", "KC", "CLE", "DET", "CIN"]
playoffwins = [37, 32, 35, 15, 36, 25, 35, 23, 23, 9, 23, 17, 7, 24, 23, 20, 12, 17, 14, 21, 17, 7, 9, 21, 10, 12, 6, 4, 13, 11, 7, 5]
graph = sns.barplot(playoffwins, teams, palette = "Reds_d")
graph.set(title = "NFL Playoff Wins", xlabel = "Teams", ylabel = "Number of Wins")
plt.savefig("bar.png")
plt.clf()