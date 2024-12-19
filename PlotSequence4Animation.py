import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Load the csv file into a pandas dataframe
data = pd.read_csv("20240911 area mean velocity in mm per sec.csv")

# Create the output folder if it does not exist
if not os.path.exists('plot_output'):
    os.makedirs('plot_output')

# Loop through the rows of the dataframe and create a plot for each row
# for i in range(5):
for i in range(data.shape[0]):
    # Extract the columns for the current plot
    print(f'Current progress: {i+1} / {data.shape[0]}')
    x = data.iloc[0:i + 1, 0]  # Time (sec) column from first row to current row
    yA = data.iloc[0:i + 1, 1]  # A column from first row to current row
    yB = data.iloc[0:i + 1, 2]  # B column from first row to current row
    yC = data.iloc[0:i + 1, 3]  # C column from first row to current row
    yD = data.iloc[0:i + 1, 4]  # D column from first row to current row
    # yE = data.iloc[0:i + 1, 5]  # E column from first row to current row

    # Create a line plot with matplotlib
    plt.plot(x, yA, label='100 SCCM (2.0 kV, liquid anode)', color='blue', linewidth=3)
    plt.plot(x, yB, label='100 SCCM (NO power applied)', color='red', linewidth=3)
    plt.plot(x, yC, label='200 SCCM (NO power applied)', color='orange', linewidth=3)
    plt.plot(x, yD, label='300 SCCM (NO power applied)', color='green', linewidth=3)
    # plt.plot(x, yE, label='[KBr] = 10⁻³ M', color='purple', linewidth=3)
    plt.xlabel('Time (s)', fontsize=14)
    plt.ylabel('Area mean velocity (mm/s)', fontsize=14)
    plt.xlim(-2, 30)  # Set the range of x-axis
    plt.ylim(0, 15)  # Set the range of y-axis
    plt.title(f"Current time: {-2 + i / 10:05.2f} s")  # Set the title of the plot
    plt.legend(loc='upper left', fontsize=12)
    plt.savefig(f"plot_output/plot_{i + 1:04d}.png")  # Save the plot as a png file in the output folder
    plt.clf()  # Clear the figure to start a new plot

# # Get the list of image files in the output folder
# image_files = sorted([f"output/{f}" for f in os.listdir('output') if f.endswith('.png')])
#
# # Set the video dimensions based on the first image file
# img = cv2.imread(image_files[0])
# height, width, _ = img.shape
# size = (width,height)
#
# # Set the video codec and create the video writer object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4V codec for .mp4 files
# video_writer = cv2.VideoWriter('output/video.mp4', fourcc, 25, size)
#
# # Loop through the image files and add them to the video
# for i, image_file in enumerate(image_files):
#     img = cv2.imread(image_file)
#     video_writer.write(img)
#     print(f"Added frame {i+1}/{len(image_files)} to the video")
#
# # Release the video writer object and display a message
# video_writer.release()
# print("Video created successfully!")