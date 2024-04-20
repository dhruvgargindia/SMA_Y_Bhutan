import os
import csv

def extract_image_paths(directory):
    image_paths = []
    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file is an image (you can add more extensions if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Construct the full path of the image file
                image_path = os.path.join(root, file)
                image_paths.append(image_path)
    return image_paths

def write_paths_to_csv(image_paths, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Image Path'])
        # Write image paths
        for path in image_paths:
            writer.writerow([path])

if __name__ == "__main__":
    # Directory containing the images
    directory = '/workspaces/SMA_Y_Bhutan/data/analysis/BODE IG Photos'
    # CSV filename
    csv_filename = 'image_paths_BODE.csv'
    
    # Extract image paths
    image_paths = extract_image_paths(directory)
    
    # Write image paths to CSV
    write_paths_to_csv(image_paths, csv_filename)
