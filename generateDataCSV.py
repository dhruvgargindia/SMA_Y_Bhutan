import os
import pandas as pd

# Function to generate image columns and save modified DataFrame to CSV
def process_data(path, image_links_path, output_file):
    # Load the CSV data
    df = pd.read_csv(path)
    image_links_df = pd.read_csv(image_links_path) 

    totalMediaCount = 0
    lastMediaCount = 0

    # Function to generate columns for image links based on media count and populate them from the image_links dataframe
    def generate_image_columns(row):
        nonlocal totalMediaCount, lastMediaCount  
        media_count = row["Media Count"]
        lastMediaCount = totalMediaCount
        totalMediaCount += media_count
        for i in range(1, media_count + 1):
            col_name = f"Image Link {i}"
            if lastMediaCount + i - 1 <= len(image_links_df) - 1:
                row[col_name] = image_links_df.loc[lastMediaCount + i - 1, "Image Path"]  
            else:
                row[col_name] = None  
        return row

    # Create the FinalData folder if it doesn't exist
    if not os.path.exists("FinalData"):
        os.makedirs("FinalData")

    # Save the modified DataFrame to a new CSV file in the FinalData folder
    output_path = os.path.join("FinalData", output_file)
    df.to_csv(output_path, index=False)

    # Display the modified DataFrame
    print(df)


# List of paths for CSV files and corresponding image link files
csv_paths = [
    '/workspaces/SMA_Y_Bhutan/data/analysis/csvs for other data/bode_posts.csv',
    '/workspaces/SMA_Y_Bhutan/data/analysis/csvs for other data/farmrio_posts.csv',
    '/workspaces/SMA_Y_Bhutan/data/analysis/csvs for other data/kelzangtextiles_posts.csv',
    '/workspaces/SMA_Y_Bhutan/data/analysis/csvs for other data/norlha_atelier_posts.csv'
    
]

image_links_paths = [
    '/workspaces/SMA_Y_Bhutan/image_paths_BODE IG Photos.csv',
    '/workspaces/SMA_Y_Bhutan/image_paths_FarmRio IG Photos.csv',
    '/workspaces/SMA_Y_Bhutan/image_paths_Kelzang Handicraft IG Photos.csv',
    '/workspaces/SMA_Y_Bhutan/image_paths_Norla Atelier IG Photos.csv'
]

output_files = ['data_bode.csv', 'data_farmrio.csv', 'data_kelzang.csv', 'data_norlha.csv']

# Process data for each pair of CSV and image link files
for csv_path, image_links_path, output_file in zip(csv_paths, image_links_paths, output_files):
    process_data(csv_path, image_links_path, output_file)
