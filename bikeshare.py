import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input ('Enter the city for which you want to analyze data either for Chicago or New York City or Washington:  ').lower()
      if city not in CITY_DATA:
        print('Please check again and chooce a speciic city from CITY DATA')
      else:
        break
    # get user input for month (all, january, february, ... , june)
    while True:
     month = input('Enter a month from January, February, March, April, May, June or enter "All" for all months: ').lower()
     months = ['january', 'february', 'march', 'april', 'may', 'june']
     if month != 'all' and month not in months:
        print('Please check again and chooce a correct month name')
     else:
        break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter a day of a week or enter all days to analyze data on all days: ').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != 'all' and  day not in days:
          print('Please check again and chooce a correct day name')
        else:
          break
    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print(' Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(' Most Common Used Start Station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(' Most Common Used End Station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = df.groupby(['Start Station','End Station']).count().idxmax()[0]
    print('Most Frequent Combination of Start Station and End Station Trip:',combination_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Counts Of User Types:',counts_of_user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
      counts_of_gender = df['Gender'].value_counts()
      print('Counts Of Gender:', counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
      earliest_year_of_birth = df['Birth Year'].min()
      print('Earliest year of Birth:', earliest_year_of_birth)

      most_common_year_of_birth = df['Birth Year'].mode()[0]
      print('Most Common year of Birth:', most_common_year_of_birth)

      most_recent_year_of_birth = df['Birth Year'].max()
      print('Most Recent year of Birth:', most_recent_year_of_birth)

      print("\nThis took %s seconds." % (time.time() - start_time))
      print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # To prompt the user whether they would like want to see the raw data
        user_data = ['yes', 'no']
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')

        while view_data.lower() not in user_data:
             view_data = input('Please enter yes or no: \n')
             view_data = view_data.lower()
        start_loc = 0
        while True:
             if view_data.lower() == 'yes':
                 print(df.iloc[start_loc: start_loc + 5])
                 start_loc += 5
                 view_data = input("Do you wish to continue?: ").lower()
                 while view_data.lower() not in user_data:
                    view_data = input('Please enter Yes or No:\n')
                    view_data = view_data.lower()
             else:
                  break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
