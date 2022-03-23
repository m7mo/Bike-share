import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True :
        city = str(input('Enter the city please : ')).lower()
        if city in cities:
            break
        else:
            print('Invalid city, Try again')

    while True :
        month = str(input('Enter the month please : ')).lower()
        if month in months:
            break
        else:
            print('Invalid month, Try again')

    while True :
        day = str(input('Enter the day please : ')).lower()
        if day in days:
            break
        else:
            print('Invalid day, Try again')

    print('-'*40)
    return city, month, day

def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert stat time column from onject to datetime
    df['month'] = df['Start Time'].dt.month_name()  #extract month from start time column
    df['day_of_week'] = df['Start Time'].dt.day_name() #extract days from start time column
    df['hour'] = df['Start Time'].dt.hour # extract hours from start time column
    if month != 'all':
        df = df[df['month'] == month.title()] #filtering dataset by month


    if day != 'all':
        df = df[df['day_of_week'] == day.title()] #filtering dataset by day

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0] #getting most common month
    print('Most Popular Month:', most_month)
    # TO DO: display the most common day of week
    most_day = df['day_of_week'].mode()[0] #getting most common day
    print('\n Most Popular Day:', most_day)
    # TO DO: display the most common start hour
    most_hour = df['hour'].mode()[0] #getting most common day
    print('\n Most Popular Hour:', most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_st_station = df['Start Station'].mode()[0] #getting most common start station
    print('Most Popular Start Station:', most_st_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0] #getting most common end station
    print('\nMost Popular End Station:', most_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station'] #creating trip column
    most_trip = df['Trip'].mode()[0] #getting most common trip
    print('\nMost Popular Trip :', most_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time']) # convert end time column from onject to datetime
    df['Travel_Time'] = df['End Time'] - df['Start Time'] #creating travel time column
    total_trip = df['Travel_Time'].sum() # getting total trvel time
    print('The Total Trip Duration is: ', total_trip)
    # TO DO: display mean travel time
    average_trip = df['Travel_Time'].mean() # getting average trvel time
    print('\nThe Average Trip Duration is: ', average_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user = df['User Type'].value_counts().to_frame()
    print('Types of Users: ',user)


    try:
        #Display counts of gender
        gender_count = df['Gender'].value_counts().to_frame()
        print('\nBike riders : \n', gender_count)

        # Display earliest, most recent, and most common year of birth
        earl_birth = df['Birth Year'].min()
        most_rec_birth = df['Birth Year'].max()
        most_comm_birth = df['Birth Year'].mode()[0]
        print('\n Earliest birth year :  ',earl_birth)
        print('\n Most recent birth year :  ',  most_rec_birth)
        print('\n Most common birth year :  ',most_comm_birth)
       # dealing with Washington
    except KeyError:
        print('This data is invalid for Washington')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city):
    """Displaying raw data according to input city"""
    df = pd.read_csv(CITY_DATA[city])

    while True:
        out = input(' If you want To View raw data in 5 rows type: yes/no \n').lower()
        if out not in ['yes', 'no']:
            print('That\'s invalid input, pleas type yes or no')

        elif out == 'yes':
            print(df.head())


        elif out == 'no':
            print('\nExiting- - -')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
