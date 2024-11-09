import math
import matplotlib.pyplot as plt


def read_data(filename):

    dates = []
    temps = []

    with open(filename, 'r') as file:

        for line in file:
            line = line.strip()
            parts = line.split(',')

            if line and parts[0].isdigit():

                if not (int(parts[3].strip()) == -9999):

                    date_str = parts[2].strip()
                    year, month, day = date_str[0:4], date_str[4:6], date_str[6:8]

                    month_dict = {
                        '01': "January",
                        '02': "February",
                        '03': "March",
                        '04': "April",
                        '05': "May",
                        '06': "June",
                        '07': "July",
                        '08': "August",
                        '09': "September",
                        '10': "October",
                        '11': "November",
                        '12': "December"
                    }

                    date_list = [year, month_dict[month], day]
                    temp_int = int(parts[3].strip())

                    # Convert to degrees Celsius
                    temp_c = temp_int / 10

                    dates.append(date_list)
                    temps.append(temp_c)

    return dates, temps

def get_highest_temp(max_dates, max_temps):

    highest_index = 0
    highest_temp = max_temps[0]

    for i in range(len(max_temps)):
        if max_temps[i] > highest_temp:
            highest_index = i
            highest_temp = max_temps[i]

    return max_dates[highest_index], max_temps[highest_index]

def get_lowest_temp(min_dates, min_temps):

    lowest_index = 0
    lowest_temp = min_temps[0]

    for i in range(len(min_temps)):
        if min_temps[i] < lowest_temp:
            lowest_index = i
            lowest_temp = min_temps[i]

    return min_dates[lowest_index], min_temps[lowest_index]

def get_longest_freezing(max_dates, max_temps):

    max_length = 0
    max_end_date = None

    current_length = 0
    current_end_date = None

    for i in range(len(max_temps)):
        temp = max_temps[i]
        date = max_dates[i]

        if temp < 0:
            current_length += 1
            current_end_date = date
        else:
            if current_length > max_length:
                max_length = current_length
                max_end_date = current_end_date
            current_length = 0
            current_end_date = None

    # After loop ends, check if the last sequence is the max
    if current_length > max_length:
        max_length = current_length
        max_end_date = current_end_date

    return max_length, max_end_date

def count_seasons(max_dates, max_temps):

    summer_days_per_year = {}
    tropical_days_per_year = {}

    for date, temp in zip(max_dates, max_temps):
        year = date[0]

        if year not in summer_days_per_year:
            summer_days_per_year[year] = 0
        if year not in tropical_days_per_year:
            tropical_days_per_year[year] = 0

        if temp >= 25:
            summer_days_per_year[year] += 1



            if temp >= 30:
                tropical_days_per_year[year] += 1

    return summer_days_per_year, tropical_days_per_year

def plot_barchart(years, counts, title, xlabel, ylabel):

    plt.figure(figsize=(15, 6))
    plt.bar(years, counts, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    plt.show()

def get_first_heat_wave(max_dates, max_temps):

    window = []

    for date, temp in zip(max_dates, max_temps):
        if temp >= 25.0:
            window.append((date, temp))

            if len(window) == 5:

                tropical_days = sum(1 for d, t in window if t >= 30.0)

                if tropical_days >= 3:
                    heat_wave_year = window[-1][0][0]  # last -> date -> year
                    return heat_wave_year

                # Removing the oldest day
                window.pop(0)
        else:
            # Reset the window if the day is not a summer day
            window = []

    # If no heat wave found
    return None


max_dates, max_temps = read_data('DeBiltTempMaxOLD.csv')
min_dates, min_temps = read_data('DeBiltTempMinOLD.csv')

highest_temp_date, highest_temp = get_highest_temp(max_dates, max_temps)
lowest_temp_date, lowest_temp = get_lowest_temp(min_dates, min_temps)

longest_freezing_days, freezing_end_date = get_longest_freezing(max_dates, max_temps)

summer_days_per_year, tropical_days_per_year = count_seasons(max_dates, max_temps)
all_years = sorted(summer_days_per_year.keys())
summer_counts = [summer_days_per_year[year] for year in all_years]
tropical_counts = [tropical_days_per_year[year] for year in all_years]

heat_year = get_first_heat_wave(max_dates, max_temps)


print(f"The highest temperature was {highest_temp} degrees Celsius and was measured on {highest_temp_date[2]} {highest_temp_date[1]} {highest_temp_date[0]}.")
print(f"The lowest temperature was {lowest_temp} degrees Celsius and was measured on {lowest_temp_date[2]} {lowest_temp_date[1]} {lowest_temp_date[0]}.")
print(f"Longest freezing period: {longest_freezing_days} days. End date of the longest freezing period: {freezing_end_date[2]} {freezing_end_date[1]} {freezing_end_date[0]}.")
print(f"First year that a heatwave: {heat_year}")

plot_barchart(
    years=all_years,
    counts=summer_counts,
    title='Number of Summer Days per Year',
    xlabel='Year',
    ylabel='Number of Summer Days'
)

plot_barchart(
    years=all_years,
    counts=tropical_counts,
    title='Number of Tropical Days per Year',
    xlabel='Year',
    ylabel='Number of Tropical Days'
)
