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
    retIndex = 0
    array = [[0 for i in range(0, 4)] for j in range(0, FRAMES_PER_VIDEO)]
    retArr = [[0] for i in range(0, FRAMES_PER_VIDEO)]
    for i in range(1, maxFrames):
        count = count + 1
        ret, frame = video.read()
        if count >= maxFrames / FRAMES_PER_VIDEO:
            count = 0
            cv2.imwrite('frame_%d.jpg' % index, frame)
            array[index] = imnums.getImageAnalysis('frame_%d.jpg' % index)
            framesProcessed += 1
            index = index + 1
            retArr[retIndex] = array
            retIndex = retIndex + 1
        if index == FRAMES_PER_VIDEO:
            break;
    for x in array:
        print x
    print 'Total Processed Frames: ' + str(framesProcessed)
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n'
    return retArr

def main():
    data = [[0] for i in range(0,3)]
    for i in range(1, 4):
        data[i - 1] = convertImageToNums('videos/Left/left%d.mp4' % i)
        print 'Done With Video : %d' % i
    print data

if __name__ == '__main__':
    main()


