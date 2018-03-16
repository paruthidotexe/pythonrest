import os
import urllib
import urllib.parse

def GetImagesUrlPath(path_to_search):
    files = os.listdir(path_to_search)
    #for curFile in files:
    #    print(urllib.parse.quote(curFile))
    if(files):
        imagesPath = [x for x in files if x.endswith(".jpg") or x.endswith(".png")]
        for curFile in imagesPath:
            print("\"" + path_to_search + urllib.parse.quote(curFile) + "\",")


def GetImagesStringPath(path_to_search):
    files = os.listdir(path_to_search)
    for curFile in files:
        print(path_to_search + curFile)


if __name__ == '__main__':
    GetImagesUrlPath("static/img/")
    #GetImagesStringPath("static/img/")

