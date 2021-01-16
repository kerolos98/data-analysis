import time
import pandas as pd
import numpy as np
import statistics
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('select the city you want to analyze(chicago, new york city, washington):').lower().rstrip()
    while city not in ['chicago','new york city','washington']:
        print('not a valid city ')
        city=input('select the city you want to analyze(chicago, new york city, washington):').lower().rstrip()
    month=input('enter the specific month you want to analyze:if non enter all:-').lower().strip()
    day =input('enter the specific day week you want to analyze:if non enter all:-').lower().strip()
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower().strip()
    # TO DO: get user input for month (all, january, february, ... , june)
       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day,view_data


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
                   
    try:
        a=CITY_DATA[city]
        df=pd.read_csv(a)
        df['Start Time'] =pd.to_datetime(df['Start Time'])
 

        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name  
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month =months.index(month)+1 
            df =df[df['month']==month] 
        if day != 'all':
            df =df[df['day_of_week']==day.title()] 
          
    except ValueError as error:
           print('please enter a valid entry make sure you enter the right month or day and select from the cities givin to you')
    return df 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month:',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('the most common day :',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('the most common hour:',df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most popular starting station')
    print(df['Start Station'].mode()[0],'with count of:',df['Start Station'].value_counts()[0])
    print('the most popular ending station')

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0],'with count of:',df['End Station'].value_counts()[0])

    print('the most popular start station and end station trip')

    # TO DO: display most frequent combination of start station and end station trip
    print(statistics.mode(zip(df['Start Station'],df['End Station'])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('the total travel time ...')
    print(df['Trip Duration'].count())
    print('the average travel time ...')

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
       b=df['User Type'].value_counts()
       print('the count of user types')
       print(b)

    # TO DO: Display counts of gender
   
       c=df['Gender'].value_counts()   
       print('the count of genders')       
       print(c)

    # TO DO: Display earliest, most recent, and most common year of birth
       print('the earliest year of birth:',int(df['Birth Year'].min()),'the most recent year of birth:',int(df['Birth Year'].max()),'the most common year of birth:',int(df['Birth Year'].mode()[0]))
    except KeyError as error:
        print('sorry some info are unavailabe in the dataset')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(view_data,df):
    start = 0

    while view_data=='yes':
            print(df.iloc[0+start:5+start])
            start+=5
            view_data = input('Do you wish to continue viewing records?: yes or no >> ').lower().rstrip()


        

def main():
    while True:
        city, month, day,view_data = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(view_data,df)

                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
