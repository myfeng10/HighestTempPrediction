import os

def save_to_csv(df, filename, path):
    current_script_path = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the target directory, navigating one level up from the current script
    full_dir_path = os.path.join(current_script_path, '..', path)

    # Ensure the directory exists, if not, create it
    if not os.path.exists(full_dir_path):
        os.makedirs(full_dir_path)

    # Construct the full file path by appending the filename to the directory path
    full_file_path = os.path.join(full_dir_path, filename)

    # Check if the file exists to determine whether to include the header
    file_exists = os.path.isfile(full_file_path)

    # If the file exists, append the data without writing the header, otherwise, write the data with the header
    df.to_csv(full_file_path, mode='a' if file_exists else 'w', header=not file_exists, index=False)
