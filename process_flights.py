import pandas as pd


# Function to calculate time difference in minutes
def time_diff_in_minutes(arrival, departure):
    return (departure - arrival).total_seconds() / 60


# Load the CSV and process it
def load_and_process_csv(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # Strip extra spaces from column names
    df.columns = df.columns.str.strip()

    # Strip spaces from Arrival and Departure times
    df['Arrival'] = df['Arrival'].astype(str).str.strip()
    df['Departure'] = df['Departure'].astype(str).str.strip()

    # Convert Arrival and Departure to datetime
    df['Arrival'] = pd.to_datetime(df['Arrival'], format='%H:%M', errors='coerce')
    df['Departure'] = pd.to_datetime(df['Departure'], format='%H:%M', errors='coerce')

    # Sort by arrival time
    df = df.sort_values('Arrival')

    calculate_success(df)

    # Convert Arrival and Departure back to string format with only time
    df['Arrival'] = df['Arrival'].dt.strftime('%H:%M')
    df['Departure'] = df['Departure'].dt.strftime('%H:%M')

    return df


def calculate_success(df):
    # Initialize success_count
    success_count = 0
    # Calculate the success column
    for i, row in df.iterrows():
        time_diff = time_diff_in_minutes(row['Arrival'], row['Departure'])
        if time_diff >= 180 and success_count < 20:
            df.at[i, 'success'] = 'success'
            success_count += 1
        else:
            df.at[i, 'success'] = 'fail'


# Save the processed CSV by overwriting the same file
def save_csv(df, file_path):
    df.to_csv(file_path, index=False)  # Overwrite the original file


# Example usage (if needed to run standalone):
if __name__ == '__main__':
    input_file = 'flights.csv'
    output_file = 'flights.csv'  # Overwrite the same file
    updated_file = load_and_process_csv(input_file)
    save_csv(updated_file, output_file)
