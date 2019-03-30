import cv2
import skvideo.io
import json
from sklearn.model_selection import cross_val_score, train_test_split
import seaborn as sns
import imageNumbers as imnums
import argparse
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np

sns.set_style('white')

FRAMES_PER_VIDEO = 5
dataIndex = 0
RH_Left = 24
RH_Right = 25
RH_PinchIn = 25
RH_PinchOut = 22

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

def runFiles(data_path=None):
    if data_path:
        return np.load(data_path)
    dataIndex = 0
    data = [0 for i in range(0, RH_Right + RH_Left + RH_PinchIn + RH_PinchOut)]
    print 'Left'
    for i in range(0, RH_Left):
        print 'doing ' + str(i) + '.mp4'
        data[dataIndex] = convertImageToNums('videos/RH_Left/%d.mp4' % (i + 1))
        dataIndex = dataIndex + 1
        print 'Done With Video : %d' % i

    print 'Right'
    for i in range(0, RH_Right):
        print 'doing ' + str(i) + '.mp4'
        data[dataIndex] = convertImageToNums('videos/RH_Right/%d.mp4' % (i + 1))
        dataIndex = dataIndex + 1
        print 'Done With Video : %d' % i

    print 'Pinch In'
    for i in range(0, RH_PinchIn):
        print 'doing ' + str(i) + '.mp4'
        data[dataIndex] = convertImageToNums('videos/RH_PinchIn/%d.mp4' % (i + 1))
        dataIndex = dataIndex + 1
        print 'Done With Video : %d' % i

    print 'Pinch Out'
    for i in range(0, RH_PinchOut):
        print 'doing ' + str(i) + '.mp4'
        data[dataIndex] = convertImageToNums('videos/RH_PinchOut/%d.mp4' % (i + 1))
        dataIndex = dataIndex + 1
        print 'Done With Video : %d' % i

    print len(data)

    # for i in range(1,2):
    #     print 'doing ' + str(i) + '.mp4'
    #     data[i + 47] = convertImageToNums('videos/Tests/%d.mp4' % i)
    #     print 'Done With Video : %d' % i

    print 'Now printing prepared data'
    np.save('data', data)
    return data

def trainAlgo(data):
    clf = svm.SVC(kernel = 'linear', gamma = 0.001, C = 100)
    target = ['left'] * RH_Left + ['right'] * RH_Right + ['pinch_in'] * RH_PinchIn + ['pinch_out'] * RH_PinchOut
    print target

    #trainData = data[:48]
    #testData = data[48].reshape(1, -1)

    #print 'Troubleshooting'
    #print trainData
    #print '**********'


    #clf.fit(trainData, target)

    # ------------- Testing -------------
    mySum = RH_Right + RH_Left + RH_PinchIn + RH_PinchOut


    # Test 1 ----> K Cross Validation Testing
    scores = cross_val_score(clf, data[:mySum], target, cv=12)

    # Test 2 ----> Test Split Testing
    # scores = []
    # for _ in range(1000):
    #     X_train, X_test, y_train, y_test = train_test_split(data[:mySum], target,
    #                                                         test_size=2, shuffle=True)
    #     clf.fit(X_train, y_train)
    #     scores.append(clf.score(X_test, y_test))

    print scores
    print len(scores)
    sns.distplot(scores)
    plt.show()


    #print clf.predict(testData)

def main():
    # To use existing data ---> use from 2nd execution
    #data = runFiles('data.npy')

    # To actually generate the data and store it inside data.npy ---> use for first run
    data = runFiles()

    trainAlgo(data)
    print data

if __name__ == '__main__':
    main()
