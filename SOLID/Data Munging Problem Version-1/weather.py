from dry_fusion import data_weather

min_spread = float('inf')
min_spread_day = None
for i,line in enumerate(data_weather):
    if(i==0 or i==1):
        continue
    if(not line[0].isdigit()): continue
    day= int(line[0])
    max = float(line[1][:2]) 
    min = float(line[2][:2])
    difference = max - min  
    if(difference < min_spread):
        min_spread = difference
        min_spread_day = day

print(min_spread_day)