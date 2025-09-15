import seaborn as sns
import pandas as pd


# update/add code below ...

def fibonacci(n):
    """Return the nth Fibonacci number."""
    # Handle base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Iteratively compute Fibonacci numbers
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def to_binary(n):
    """Convert an integer to its binary representation"""
    #n must be positive
    if n < 0:
        return "Input cannot be a negative integer."
    #convert integer to binary
    else:
        x = bin(n)
        #isolate 1s and 0s
        binary_num = x[2:]
        return binary_num


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    """Return a list of columns, sorted such that first column has least missing values"""
    s = df_bellevue.copy()
    #change the genders that are not M or W to missing values
    s['gender'].fillna('?', inplace=True)
    s['gender'].fillna('g', inplace=True)
    s['gender'].fillna('h', inplace=True)
    #identify number of missing values
    id_missing = s.isna().sum()
    #sort the missing values
    sort_id_missing = id_missing.sort_values()
    #turn into a list and return final product
    return sort_id_missing.index.tolist()

def task_2():
    """Return a DataFrame with two columns: year and total number of immigrant admissions"""
    s = df_bellevue.copy()
    # Ensure 'date_in' is datetime and extract year
    s['date_in'] = pd.to_datetime(s['date_in'])
    s['year'] = s['date_in'].dt.year
    # Group by year and count admissions
    admissions = s.groupby('year').size().reset_index(name='total_admissions')
    return admissions

def task_3():
    """Return a series with index for each gender and values is average age for each gender"""
    s = df_bellevue.copy()
    # Only use valid genders ('m', 'w'), ignore others if present
    valid_genders = ['m', 'w']
    #Filter out non 'valid' genders
    filtered = s[s['gender'].str.lower().isin(valid_genders)]
    # Group by gender and calculate average age
    avg_age = filtered.groupby('gender')['age'].mean()
    return avg_age

def task_4():
    """5 most common professions"""
    s = df_bellevue.copy()
    #Count all professions
    common_profs = s['profession'].value_counts()
    #Isolate the top 5
    top_5 = common_profs.head(5)
    return top_5