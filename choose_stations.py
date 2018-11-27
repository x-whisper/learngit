stations = {'kone': {'id', 'ut', 'nv'}, 'ktwo': {'id', 'wa', 'mt'}, 'kthree': {'or', 'ca', 'nv'}, 'kfour': {'ut', 'nv'}, 'kfive': {'az', 'ca'}}
states_needed = {'id', 'az', 'nv', 'or', 'wa', 'mt', 'ca', 'ut'}
stations_choosed = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station in stations.keys():
        covered = stations[station] & states_needed
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    stations_choosed.add(best_station)
    states_needed -= states_covered

print(stations_choosed)