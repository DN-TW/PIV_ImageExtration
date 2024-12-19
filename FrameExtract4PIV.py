import cv2
import os
import shutil
import time
import csv
from tqdm import tqdm

videoList = []
startFrame = []
videoSource = []
outputNames = []

sourcedFolder = 'F:/High speed video file/20241104 discharge on silicone oil/'
frameInterval = 10
timeDuration = 30
timeB4zero = 2
totalFrame = (timeDuration + timeB4zero) / 0.01 / frameInterval
testMode = False

with open("./videoConfig.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        videoList.append(row)
    videoList.pop(0)

for item in videoList:
    # print(item)
    startFrame.append(item[3])
    videoSource.append(item[4] + '.avi')
    outputNames.append(item[4][:4] + item[1])

# Clear the extract folder if it exists
for folder in outputNames:
    if os.path.exists(folder):
        shutil.rmtree(folder)

    # Create the extract folder
    os.makedirs(folder)


def video_capturing(outputName, video_source, start_frame, frame_b=True):
    cap = cv2.VideoCapture(video_source)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame - 1)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'{outputName}/{outputName}_frame{start_frame:05d}_a.png', frame)
    if frame_b:
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'{outputName}/{outputName}_frame{start_frame:05d}_b.png', frame)
    cap.release()


tic = time.time()
RunningTime = 0

if testMode:
    R = 1
else:
    R = 1 + int(totalFrame)

for j in range(len(outputNames)):
    tic = time.time()
    for i in tqdm(range(R), desc=outputNames[j], unit=' frame'):
        # print('({:02d} / {:02d}) Start capturing ({:04d} / {:04d})'.format(j + 1, len(outputNames), i + 1, R))
        video_capturing(outputNames[j],
                        sourcedFolder + videoSource[j],
                        (int(startFrame[j]) - timeB4zero * 100) + i * frameInterval,
                        not testMode)

    toc = time.time()
    RunningTime += (toc - tic)
    # print(f'Running time of this Python code: {toc - tic:.2f} seconds.')

print(f'Frame extraction finished! Total running time: {RunningTime:.2f} seconds.')
