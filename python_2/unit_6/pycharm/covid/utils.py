def get_unique_values(df, col):
    """
    Return the number of unique values in the column `col`
        for the dataframe `df`.
    """
    return len(df[col].unique())


def get_max_cases(df):
    """
    Return the country with the maximum number of cases
        detected overall period.
    """
    sum_of_cases = df.groupby("countriesAndTerritories").sum()["cases"]
    m = sum_of_cases.max()
    c = sum_of_cases[sum_of_cases == m].index[0]
    return c, m


def get_max_deaths(df):
    """
    Return the country with the maximum number of cases
        detected overall period.
    """
    sum_of_deaths = df.groupby("countriesAndTerritories").sum()["deaths"]
    m = sum_of_deaths.max()
    c = sum_of_deaths[sum_of_deaths == m].index[0]
    return c, m

