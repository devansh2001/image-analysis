import cv2
import skvideo.io
import json
import imageNumbers as imnums

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
    retArr = [[0 for i in range(0,16)] for i in range(0, FRAMES_PER_VIDEO)]
    for i in range(1, maxFrames):
        count = count + 1
        ret, frame = video.read()
        if count >= maxFrames / FRAMES_PER_VIDEO:
            count = 0
            cv2.imwrite('frame_%d.jpg' % index, frame)
            matrix = imnums.getImageAnalysis('frame_%d.jpg' % index)
            array = matrix.flatten()
            framesProcessed += 1
            retArr[index] = array
            index = index + 1
        if index == FRAMES_PER_VIDEO:
            break;
    print 'Total Processed Frames: ' + str(framesProcessed)
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n'
    return retArr

def main():
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
    print data

    count = 0
    for item in data:
        count = count + 1
        print count
        print item
        for smallArray in item:
            print smallArray

if __name__ == '__main__':
    main()
