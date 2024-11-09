import math
import matplotlib.pyplot as plt



def car_data(data):

    speed_ms = []
    time_s = []

    latitudes = []
    longitudes = []

    #  Skip header
    next(data)

    for line in data:
        split_data = line.split(',')

        speed_ms.append(float(split_data[6]))

        date, time = split_data[0].split(' ')
        hours, minutes, seconds = time.split(':')
        time_s.append( int(hours) * 3600 + int(minutes) * 60 + float(seconds) )


        latitudes.append(float(split_data[3]))
        longitudes.append(float(split_data[4]))

    return speed_ms, time_s, latitudes, longitudes


def plot_speed_vs_time(time_s, speed_kmh):

    plt.plot(time_s, speed_kmh, label='Speed (km/h)', color='blue', linewidth=2)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Speed (km/h)')
    plt.title('Car Speed vs. Time')
    plt.show()

def estimate_total_distance(time_s, speed_ms):

    total_distance_m = 0.0

    for i in range(1, len(time_s)):
        delta = time_s[i] - time_s[i - 1]
        average_speed = (speed_ms[i] + speed_ms[i - 1]) / 2
        distance = average_speed * delta
        total_distance_m += distance

    total_distance_km = total_distance_m
    return total_distance_km


def plot_route(latitudes, longitudes, speeds_kmh, speed_threshold_kmh=50):

    plt.title('Car Route')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    for i in range(1, len(latitudes)):
        lat_start = latitudes[i - 1]
        lon_start = longitudes[i - 1]
        lat_end = latitudes[i]
        lon_end = longitudes[i]
        speed = speeds_kmh[i]

        # Determine color based on speed
        if speed > speed_threshold_kmh:
            color = 'green'
        else:
            color = 'red'

        plt.plot([lon_start, lon_end], [lat_start, lat_end], color=color, linewidth=2)



    plt.show()


input_file = open('CarRideData.csv', 'r')
speed_ms, time_s, latitudes, longitudes = car_data(input_file)
input_file.close()

speed_kmh = [s * 3.6 for s in speed_ms]

plot_speed_vs_time(time_s, speed_kmh)
print(estimate_total_distance(time_s, speed_ms))
plot_route(latitudes, longitudes, speed_kmh)
