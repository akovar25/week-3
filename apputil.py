import seaborn as sns
import pandas as pd


# update/add code below ...

def fibonacci(n):
    """
    Function to return the nth Fibonacci number.
    
    Parameters: 
    Input a positive integer.

    Return Value:
    The nth Fibonacci number (the sum of the n-1 and n-2 numbers within the Fibonacci series).

    """
    
    # Handle base cases#

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Iteratively compute Fibonacci numbers#
    
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def to_binary(n):
    """
    Function to convert an integer to its binary representation.

    Parameters:
    Input must be a positive integer.

    Return Value:
    The binary representation of the input integer.
    
    """
    
    # N must be positive#

    if n < 0:
        return "Input cannot be a negative integer."
    
    # Convert integer to binary#

    else:
        x = bin(n)
        #isolate 1s and 0s
        binary_num = x[2:]
        return binary_num


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    """
    Function that returns a list of columns, sorted such that first column has the least missing values and the last column has the most missing values.

    Parameters:
    No input parameters.

    Return value:
    A sorted list where the first column contains the least missing values and the last column has the most missing values.
    """
    s = df_bellevue.copy()

    # Change the genders that are not M or W to missing values#
    
    valid_genders = ['m', 'w']

    # Replace non valid genders with NAs#
    
    s.loc[~s['gender'].str.lower().isin(valid_genders), 'gender'] = pd.NA
    id_missing = s.isna().sum()
    
    # Sort the missing values#

    sort_id_missing = id_missing.sort_values()
    
    # Turn into a list and return final product#
    
    return sort_id_missing.index.tolist()

def task_2():
    """
    Function to return a DataFrame with two columns: year and total number of immigrant admissions per year.

    Parameters:
    No input parameters.

    Return Value:
    A DataFrame with columns, the year and the total number of immigrant admissions in that year.
    """
    s = df_bellevue.copy()
    
    # Ensure 'date_in' is datetime and extract year#
    
    s['date_in'] = pd.to_datetime(s['date_in'])
    s['year'] = s['date_in'].dt.year
    
    # Group by year and count admissions#
    
    admissions = s.groupby('year').size().reset_index(name='total_admissions')
    return admissions

def task_3():
    """
    Function to return a series with an index for each gender, where the values are the average age for each gender.
    
    Parameters:
    No input parameters.

    Return Value:
    A series, indexed for each gender, where the values are the average age for each gender.
    """
    s = df_bellevue.copy()

    # Only use valid genders ('m', 'w'), ignore others if present#
    
    valid_genders = ['m', 'w']

    # Filter out non 'valid' genders#
    
    filtered = s[s['gender'].str.lower().isin(valid_genders)]
    
    # Group by gender and calculate average age#
    
    avg_age = filtered.groupby('gender')['age'].mean()
    return avg_age

def task_4():
    """
    Function to identify the top 5 most common professions.

    Parameters:
    No input parameters.

    Return Value:
    A list of the top 5 most common professions in descending order.
    """
    s = df_bellevue.copy()

    # Count all professions#
    
    common_profs = s['profession'].value_counts()
    
    # Isolate the top 5#
    
    top_5 = common_profs.head(5)
    return top_5.index.tolist()