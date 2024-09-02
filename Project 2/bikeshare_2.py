import time
import os
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_cities = ['chicago', 'new york', 'washington']
valid_filters = ['month', 'day', 'both', 'none']
valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
valid_restarts = ['yes', 'no']
day_int_conversion = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def valid_check(input_data, valid_range):
    result = False
    if input_data in valid_range:
        result = True
    return result

def valid_city_check():
    while True:
        city_input = input('Would you like to see data for Chicago, New York, or Washington?\n').strip().lower()
        result = valid_check(city_input, valid_cities)
        if result:
            return city_input
        else:
            print('Your previous entry is invalid, please re-enter!\n')

def valid_filter_check():
    while True:
        filter_input = input('Would you like to filter the data by month, day, or both?\n').strip().lower()
        result = valid_check(filter_input, valid_filters)
        if result:
            return filter_input
        else:
            print('Your previous entry is invalid, please re-enter!\n')

def valid_month_check():
    while True:
        month_input = input('Which month - January, Februry, March, April, May, June, or All?\n').strip().lower()
        result = valid_check(month_input, valid_months)
        if result:
            return month_input
        else:
            print('Your previous entry is invalid, please re-enter!\n')

def valid_day_check():
    while True:
        day_input = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All?\n').strip().lower()
        result = valid_check(day_input, valid_days)
        if result:
            return day_input
        else:
            print('Your previous entry is invalid, please re-enter!\n')

def valid_restart_check():
    while True:
        restart_input = input('Would you like to restart? Enter yes or no?\n').strip().lower()
        result = valid_check(restart_input, valid_restarts)
        if result:
            return restart_input
        else:
            print('Your previous entry is invalid, please re-enter!\n')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    city = valid_city_check()
    month = 'all'
    day = 'all'
    month_day_filter = valid_filter_check()
    if month_day_filter == 'all':
        month = valid_month_check()
        day = valid_day_check()
    elif month_day_filter == 'month':
        month = valid_month_check()
    elif month_day_filter == 'day':
        day = valid_day_check()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.weekday

    # filter month
    if month != 'all':
        month = valid_months.index(month) + 1
        df = df[df['Month'] == month]

    # filter day
    if day != 'all':
        df = df[df['Day_of_week'] == (day_int_conversion.index(day) + 1)]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_counts = df['Month'].value_counts()
    most_common_month = month_counts.idxmax()
    month_max_count = month_counts.max()
    print(f'Most commom month: {most_common_month}, Count: {month_max_count}\n')

    # display the most common day of week
    day_counts = df['Day_of_week'].value_counts()
    most_common_day = day_int_conversion[day_counts.idxmax() - 1]
    day_max_count = day_counts.max()
    print(f'Most common day: {most_common_day}, Count: {day_max_count}\n')

    # display the most common start hour
    df['Start_hour'] = df['Start Time'].dt.hour
    hour_counts = df['Start_hour'].value_counts()
    most_common_hour = hour_counts.idxmax()
    hour_max_count = hour_counts.max()
    print(f'Most common start hour: {most_common_hour}, Count: {hour_max_count}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_counts = df['Start Station'].value_counts()
    most_common_start_station = start_station_counts.idxmax()
    start_station_max_count = start_station_counts.max()
    print(f'Most commom start station: {most_common_start_station}, Count: {start_station_max_count}\n')

    # display most commonly used end station
    end_station_counts = df['End Station'].value_counts()
    most_common_end_station = end_station_counts.idxmax()
    end_station_max_count = end_station_counts.max()
    print(f'Most commom end station: {most_common_end_station}, Count: {end_station_max_count}\n')

    # display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' ==> ' + df['End Station']
    station_combination_counts = df['Station Combination'].value_counts()
    most_common_station_combination = station_combination_counts.idxmax()
    station_combination_max_count = station_combination_counts.max()
    print(f'Most commom station combination: {most_common_station_combination}, Count: {station_combination_max_count}\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_in_hour = total_travel_time/3600
    print(f'Total travel time: {total_travel_time}(s) ~ {total_travel_time_in_hour:.1f}(h)\n')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_travel_time:.1f}(s)\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'{user_types}\n')

    # Display counts of gender
    try:
        user_genders = df['Gender'].value_counts()
        print(f'{user_genders}\n')
    except:
        print('No data available for user genders!\n')

    # Display earliest, most recent, and most common year of birth
    try:
        user_birth_years = df['Birth Year'].value_counts()
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_year_birth = user_birth_years.idxmax()
        print(f'Eerliest year of birth: {int(earliest_birth_year)}\n')
        print(f'Most recent year of birth: {int(most_recent_birth_year)}\n')
        print(f'Most common year of birth: {int(most_common_year_birth)}\n')
    except:
        print('No data available for user birth years!\n')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    while True:
        clear_screen()
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = valid_restart_check()
        if restart != 'yes':
            clear_screen()
            break

if __name__ == "__main__":
	main()
