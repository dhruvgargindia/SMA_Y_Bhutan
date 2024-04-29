import os
import csv

def get_file_paths(directory):
    files = sorted(os.listdir(directory))
    file_paths = [os.path.join(directory, filename) for filename in files]
    return file_paths

def write_paths_to_csv(image_paths, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image Path'])
        for path in image_paths:
            writer.writerow([path])

if __name__ == "__main__":
    # Directories containing the images
    directories = [
        '/workspaces/SMA_Y_Bhutan/data/analysis/BODE IG Photos',
        '/workspaces/SMA_Y_Bhutan/data/analysis/FarmRio IG Photos',
        '/workspaces/SMA_Y_Bhutan/data/analysis/Kelzang Handicraft IG Photos',
        '/workspaces/SMA_Y_Bhutan/data/analysis/Norla Atelier IG Photos'
    ]

    for directory in directories:
        # Extract image paths
        image_paths = get_file_paths(directory)
        image_paths.reverse()

        csv_filename = f'image_paths_{os.path.basename(os.path.normpath(directory))}.csv'

        # Write image paths to CSV
        write_paths_to_csv(image_paths, csv_filename)
