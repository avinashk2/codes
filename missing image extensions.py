import os
import pandas as pd
from os import listdir
from os.path import isfile, join

# mypath is the path where you have saved all the images 
mypath = os.getcwd() +  '/images'
# CSV having details of the files needed header name has to be same as in the file provided to me "Picture ID"
csvpath = 'Master Inventory List - Sheet1.csv'
# headername is the header of the column which is having the 
headername = "Picture ID"
# list all types of files of images
filetypelist = ['.jpg','.jpeg','.png','.bmp','.gif',' .png']
df = pd.read_csv (csvpath)
onlyfilesimages = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def getafilename(filename, filetypes,onlyfilesimages1):
    remove_characters = ["&", "'", "%"]
    for character in remove_characters:
        filename = filename.replace(character, "_")
    out= ''
    if filename in onlyfilesimages1:
        out = filename
    else:
        for x in filetypes:
                if filename.split('.')[0]+x in onlyfilesimages1:
                    out = filename.split('.')[0]+x
                else:
                    if filename+x in onlyfilesimages1:
                        out = filename+x
    if out == "":
        out = 'noimage.jpg'
    return out
df[['realfile']] = df[headername].apply(lambda x: pd.Series(getafilename(x, filetypelist,onlyfilesimages))) 
df.to_csv(csvpath.split('.')[0]+'-updated.csv')