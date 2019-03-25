import cv2
import skvideo.io
import json
import imageNumbers as imnums
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np

FRAMES_PER_VIDEO = 5

def getNumberOfFrames(vidName):
    metadata = skvideo.io.ffprobe(vidName)
    json_data = json.dumps(metadata)
    json_data = json.loads(json_data)
    totalNumberOfFrames = (int)(json_data['video']['@nb_frames'])
    return totalNumberOfFrames

def convertImageToNums(vidName):
    framesProcessed = 0
    video = cv2.VideoCapture(vidName)
    maxFrames = getNumberOfFrames(vidName)
    count = 0
    index = 0
    array = [0 for i in range(0, 16)]
    retArr = [0 for i in range(0, 80)]
    retArrIndex = 0
    for i in range(1, maxFrames):
        count = count + 1
        ret, frame = video.read()
        if count >= maxFrames / FRAMES_PER_VIDEO:
            count = 0
            cv2.imwrite('frame_%d.jpg' % index, frame)
            matrix = imnums.getImageAnalysis('frame_%d.jpg' % index)
            for m in xrange(0,4):
                for n in xrange(0,4):
                    array[m * 4 + n] = matrix[m][n]
            #array = matrix.flatten()
            print array

            framesProcessed += 1
            for val in range(0, 16):
                retArr[retArrIndex * 16 + val] = array[val]
            retArrIndex = retArrIndex + 1
            index = index + 1
        if index == FRAMES_PER_VIDEO:
            break;
    print 'Total Processed Frames: ' + str(framesProcessed)
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n'
    print retArr
    return retArr

def runFiles():
    #runFiles()

    data = [0 for i in range(0, 49)]
    print 'Left'
    for i in range(1, 25):
        print 'doing ' + str(i) + '.mp4'
        data[i - 1] = convertImageToNums('videos/RH_Left/%d.mp4' % i)
        print 'Done With Video : %d' % i

    print 'Right'
    for i in range(1, 26):
        print 'doing ' + str(i) + '.mp4'
        data[i + 23] = convertImageToNums('videos/RH_Right/%d.mp4' % i)
        print 'Done With Video : %d' % i

    print 'Now printing prepared data'
    np.save('data.txt', data)
    return data

def trainAlgo(data):
    clf = svm.SVC(kernel = 'linear', gamma = 0.001, C = 100)
    target = ['' for i in range(0, 49)]
    for i in range(0, 24):
        target[i] = 'left'
    for i in range(24, 49):
        target[i] = 'right'
    print target

    trainData = data
    for i in range(0, 48):
        trainData[i] = data[i]

    testData = data[48]

    print 'Troubleshooting'
    print trainData
    print '**********'
    #print trainData.shape

    clf.fit(trainData, target)
    print clf.predict(testData)

def main():
    data = runFiles()
    trainAlgo(data)
    print data

if __name__ == '__main__':
    main()
