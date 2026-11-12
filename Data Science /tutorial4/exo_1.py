import numpy as np


# 1. Create the array T 
T = np.array([
    [22, 25, 20],
    [24, 27, 21],
    [19, 20, 22],
    [25, 29, 28],
    [26, 30, 27],
    [21, 21, 23],
    [20, 26, 25],
])
cities = ["Alger", "Annaba", "Oran"]
print("T =\n", T)
 
# 2. Maxima
max_per_city = T.max(axis=0)      # one value per column (city)
max_per_day = T.max(axis=1)       # one value per row (day)
overall_max = T.max()
print("Max per city :", dict(zip(cities, max_per_city)))
print("Max per day  :", max_per_day)
print("Overall max  :", overall_max)


# 3. Day and city of maximum
day_idx, city_idx = np.unravel_index(np.argmax(T), T.shape)
print(f"Overall max = {T[day_idx, city_idx]} °C on day {day_idx + 1} in {cities[city_idx]}")


# 4. Higher temperature
higher_alger_oran = np.maximum(T[:, 0], T[:, 2])
print("max(Alger, Oran) per day :", higher_alger_oran)


# 5. Add a row with the average temperature of each city
avg_row = T.mean(axis=0)
T_with_avg = np.vstack((T, avg_row))      # result is float because of the means
print(np.round(T_with_avg, 2))
 
# 6. Days where Annaba was the hottest city
mask = (T[:, 1] > T[:, 0]) & (T[:, 1] > T[:, 2])
days = np.where(mask)[0] + 1              # +1 because days start at 1
print("Annaba hottest on days:", days)
