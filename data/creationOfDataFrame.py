import pandas as pd
import cv2

from hairColorDetection import hairColorDetection
from parsing import Downloader


# Read json data
womanPhotos = pd.read_json(r'data\tinderData.json')
    
womans = dict() # Dict with urls for woman photos

for womanNumber, woman in enumerate(womanPhotos['photos']):
    for photoNumber, variable in enumerate(woman): # variable - Dictionary with photoraphy parameters (photos are available in various resolutions)
        womans['woman' + str(womanNumber) + 'photo' + str(photoNumber)] = variable['photo'][1]['url']

# Creation of DataFrame
colorNames = ['brown-haired', 'light brown', 'blond', 'red hair', 'black']
colors = pd.DataFrame({color: [29] for color in colorNames})

# Fill DF
for woman in womans:
    img = Downloader(womans[woman]).getPhoto()
    
    # Check
    if img is None:
        continue
    
    detector = hairColorDetection(img)
    rectangle = detector.findFace()

    # Check face
    if rectangle is None:
        continue
    
    try:    
        result = detector.getColorRatio(detector.getFaceAndHair(rectangle))
        result = pd.DataFrame(result, index=[woman])
    except cv2.error:
        continue
    else:
        colors = pd.concat([colors, result], axis=0)
        
colors.to_csv('data/hairColorsTrainData.csv')
