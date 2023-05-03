import matplotlib.pyplot as plt

# Вибірка спостережень
# input_data = [
#     345.1, 261.8, 292.4, 326.4, 396.1, 307.7, 372.3,
#     260.1, 285.6, 224.4, 346.8, 280.5, 334.9, 348.5,
#     243.1, 341.7, 285.6, 249.9, 353.6, 331.5, 260.1,
#     328.1, 302.6, 275.4, 266.9, 387.6, 372.3, 212.5,
#     171.7, 358.7, 311.1, 249.9, 246.5, 307.7, 312.8,
#     236.3, 324.7, 314.5, 343.4, 404.6, 283.9, 346.8,
#     331.5, 292.4, 333.2, 234.6, 362.1, 297.5, 329.8,
#     302.6, 229.5, 302.6, 200.6, 316.2, 324.7, 331.5
# ]

input_data =[121.8, 92.4, 103.2, 115.2, 139.8, 108.6, 131.4, 91.8, 100.8, 79.2, 122.4, 99.0, 118.2, 123.0, 85.8, 120.6, 100.8, 88.2, 124.8, 117.0, 91.8, 115.8, 106.8, 97.2, 94.2, 136.8, 131.4, 75.0, 60.6, 126.6, 109.8, 88.2, 87.0, 108.6, 110.4, 83.4, 114.6, 111.0, 121.2, 142.8, 100.2, 122.4, 117.0, 103.2, 117.6, 106.8, 127.8, 105.0, 114.6, 117.0]

# Кількість інтервалів
intervals_count = 7

# Межі інтервалів
min_val = min(input_data)
max_val = max(input_data)
interval_width = (max_val - min_val) / intervals_count

intervals = []
for i in range(intervals_count):
    intervals.append([min_val + i * interval_width, min_val + (i + 1) * interval_width])


# Середина інтервалів 
intervals_mid = []
for interval in intervals:
    intervals_mid.append((interval[0] + interval[1]) / 2)
    

# Частота кожного інтервалу
frequencies = [0] * intervals_count
for val in input_data:
    for i in range(intervals_count):
        if val >= intervals[i][0] and val < intervals[i][1]:
            frequencies[i] += 1
            break
        
        
# Таблиця частот
print("Frequency table: ")
print("{:<20} {:<20} {:<20} {:<20}".format("Interval number", "Interval bounds", "Interval midpoint", "Frequency"))
for i in range(intervals_count):
    print("{:<20} [{:<8}, {:<8}]\t {:<20}\t {:<20}".format(i+1, intervals[i][0], intervals[i][1], intervals_mid[i], frequencies[i]))
    
    
# Графік полігону частот
plt.plot(intervals_mid, frequencies, 'o-', color="#ba181b")
plt.title("Frequency plot")
plt.xlabel("Intervals")
plt.ylabel("Frequency")
plt.xticks(intervals_mid)
plt.show()

