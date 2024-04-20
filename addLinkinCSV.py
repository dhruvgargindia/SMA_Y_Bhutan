import pandas as pd

# Load the CSV data
df = pd.read_csv("/workspaces/SMA_Y_Bhutan/data/analysis/csvs for other data/bode_posts.csv")
image_links_df = pd.read_csv("/workspaces/SMA_Y_Bhutan/image_paths_BODE.csv") 

totalMediaCount = 0
lastMediaCount = 0

# Function to generate columns for image links based on media count and populate them from the image_links dataframe
def generate_image_columns(row):
    global totalMediaCount, lastMediaCount  
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

# Apply the function row-wise to add image link columns and populate them from the image_links dataframe
df = df.apply(generate_image_columns, axis=1)

# Save the modified DataFrame to a new CSV file
df.to_csv("modified_data.csv", index=False)

# Display the modified DataFrame
print(df)
