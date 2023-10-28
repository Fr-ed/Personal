import pandas as pd

def clean_time_series(time_series):
    """
    Cleans the test time series data by converting it into proper date format.

    Parameters:
    - time_series: list
        A list of strings representing the time series data.

    Returns:
    - pd.Series:
        A pandas Series object with the cleaned time series data in proper date format.

    Raises:
    - ValueError:
        Raises an error if the input time series is empty or contains invalid date strings.
    """

    # Checking if the time series is empty
    if not time_series:
        raise ValueError("Input time series is empty.")

    # Converting the time series into a pandas Series object
    series = pd.Series(time_series)

    try:
        # Converting the series into datetime format
        series = pd.to_datetime(series)
    except ValueError as e:
        raise ValueError("Invalid date string found in the time series.") from e

    return series

# Example usage:

# Input time series data
time_series_data = ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04"]

# Clean the time series data
cleaned_series = clean_time_series(time_series_data)

# Print the cleaned time series
print(cleaned_series)
