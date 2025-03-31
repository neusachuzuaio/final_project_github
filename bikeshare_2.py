import time
import pandas as pd
import numpy as np

df = pd.read_csv('chicago.csv')

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
    day=['sunday','monday','tuesday','wednesday','thurday',
      'friday','saturday','all']
    month=['january','february','march','april','may','june','all']
    print('Welcome to the US Bikeshare Program')
    print('Join us and let\'s explore some US bikeshare data!')
    print('Please add below the city, the month and the day that you would like to have some more information')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """Collect the city input and check if we have in our dataframe. Else, send an error message to the user."""
    while (True):
        city = input("1. Please choose a city (Options: chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Oh Oh! Invalid input. Please choose one of above options.")
     
    # TO DO: get user input for month (all, january, february, ... , june)
    
    """Collect the month input and check if we have in our dataframe. Else, send an error message to the user."""
    
    while (True):
        month_input = input("2. Please choose a month (Options:all or january to june): ").lower()
        if month_input in month:
            month = month_input
            break
        else:
            print("Oh Oh! Invalid input. Please choose a valid month (or 'all' to select all months).")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    """Collect the day input and check if we have in our dataframe. Else, send an error message to the user."""
    while (True):
        day_input = input("2. Please choose a day (Options: all or monday to sunday): ").lower()
        if day_input in day:
            day = day_input
            break
        else:
            print("Oh Oh! Invalid input. Please choose a valid day (or 'all' to select all days).")

    print('-'*40)
    print(f"You have selected - City: {city}, Month: {month}, Day: {day}")
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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    """Check if the DataFrame is empty to avoid errors"""
    if (df.empty):
        print("No data available for the selected filters. Please try again.")
        return pd.DataFrame()

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    """Check if the DataFrame is empty to avoid errors"""
    
    if df.empty:
        print("No data to calculate statistics. Please adjust your filters.")
        return

    # TO DO: display the most common month
    """Mode function to check the most common month"""
    
    popular_month=df['month'].mode()[0]
    months=['January', 'February', 'March', 'April', 'May', 'June']
    
    """We subtract one on the popular_month to have the right month on the list."""
    
    common_month=months[popular_month - 1]
    print('-The most common month is:',common_month)
   
    # TO DO: display the most common day of week
    """Mode function to check the most common day of the week"""
    
    popular_day = df['day_of_week'].mode()[0]
    print('-Most common day of the week is:',popular_day)

    # TO DO: display the most common start hour
    """Mode function to check the most common hour"""
    
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('-Most common start hour is:',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    """Conditional function to avoid errors when start station or end station is empty."""
    
    if ('Start Station' in df.columns):
        common_used_startstation = df['Start Station'].mode()[0]
        print('-Most commonly used start station is:',common_used_startstation)
    else:
        print('No Start Station available data. Please Try Again.')
    # TO DO: display most commonly used end station
    if ('End Station' in df.columns):
        common_used_endstation = df['End Station'].mode()[0]
        print('-Most commonly used end station is:',common_used_endstation)
    else:
         print('No End Station available data. Please Try Again.')
    # TO DO: display most frequent combination of start station and end station trip
    """We concatenate to check all the combinations"""
    
    df['Station End-Start'] = df['Start Station'] +'-'+ df['End Station']
    
    """Use mode function to see which combination is the most frequent."""
    
    most_start_end = df['Station End-Start'].mode()[0]
    print('-Most frequent combination of start and end stations is:',most_start_end)

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print(df.info())
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    """Sum all values on trip duration column"""
    
    total_travel_time=df['Trip Duration'].sum()
    print('\n-Total Travel Time:',total_travel_time)
    
    # TO DO: display mean travel time
    """Mean value of all values on trip duration column"""
    
    mean_travel_time=df['Trip Duration'].mean()
    print('\n-Total Travel Time:',mean_travel_time)

    print("\n-This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ## print value counts for each user type
    user_types=df['User Type'].value_counts()
    print('\n These are the User Types:-',user_types)
    # TO DO: Display counts of gender
    """Only Chicago collects birth and gender. So we have to check if gender column exists first."""
    
    if ('Gender' in df.columns):
        gender_count=df['Gender'].value_counts()
        print('\n These are the gender types:-',gender_count)
    else:
        print('\n This city does not record or classify individuals by gender.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df.columns):
        earliest=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        common_birth_year=df['Birth Year'].mode()[0]
        print('\n These is the earliest birth year:-',earliest)
        print('\n These is the most recent birth year:-',recent)
        print('\n These is the most common birth year:-',common_birth_year)
    else:
        print('\n This city does not check birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """Defining the new function to display raw data"""
    index=0 #row number
    
    """We are using a While loop and checking the row index to display the data continuously
       until the answer is 'no' or 'n'   
    """
    while True:
        choice = input("\nYou have see the statistical data, would you like to see 5 rows of raw data? Enter yes(y) or no(n): ").lower()
        if choice in ['yes', 'y']:
            print(df.iloc[index:index + 5])
            index += 5  
            
            """When all data in the dataframe is displayed"""
            
            if index >= len(df):
                print("\nNo more raw data to display.")
                break
                
            """If choice is 'no'"""
        elif choice in ['no', 'n']:
            print("\nReturning to the main program...")
            break
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes(y) or no(n).\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
