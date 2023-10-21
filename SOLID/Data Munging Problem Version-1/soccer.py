import sys
from dry_fusion import data_match

smallest_difference = sys.maxsize
team = None
for i,line in enumerate(data_match):
    if(i==0):
        continue
    runs_scored = int(line[6])
    runs_left = int(line[7])
    if abs(runs_scored-runs_left) < smallest_difference:
        smallest_difference = abs(runs_scored-runs_left)
        team = line[1]

print(team)