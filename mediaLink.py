import os
import csv

def get_file_paths(directory):
 

    files = sorted(os.listdir(directory)) 

    file_paths = [os.path.join(directory, filename) for filename in files]
    return file_paths

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
    bodeDirectory = '/workspaces/SMA_Y_Bhutan/data/analysis/BODE IG Photos'
    FarmDirectory = '/workspaces/SMA_Y_Bhutan/data/analysis/FarmRio IG Photos'
    kelzangDirectory = '/workspaces/SMA_Y_Bhutan/data/analysis/Kelzang Handicraft IG Photos'
    norlaDirectory = '/workspaces/SMA_Y_Bhutan/data/analysis/Norla Atelier IG Photos'

    directory = kelzangDirectory
    # CSV filename
    csv_filename = 'image_paths_kelzang.csv'
    
    # Extract image paths
    image_paths = get_file_paths(directory)
    
    # Write image paths to CSV
    write_paths_to_csv(image_paths, csv_filename)
