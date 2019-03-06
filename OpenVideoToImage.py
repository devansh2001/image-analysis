import cv2
import skvideo.io
import json
import imageNumbers as imnums

FRAMES_PER_VIDEO = 6

def getNumberOfFrames():
    metadata = skvideo.io.ffprobe('myVid.mp4')
    json_data = json.dumps(metadata)
    json_data = json.loads(json_data)
    totalNumberOfFrames = (int)(json_data['video']['@nb_frames'])
    return totalNumberOfFrames

def convertImageToNums():
    video = cv2.VideoCapture('myVid.mp4')
    maxFrames = getNumberOfFrames()
    count = 0
    index = 0
    array = [[0 for i in range(0, 4)] for j in range(0, FRAMES_PER_VIDEO) ]
    for i in range(1, maxFrames):
        count = count + 1
        ret, frame = video.read()
        if count >= maxFrames / FRAMES_PER_VIDEO:
            count = 0
            cv2.imwrite('frame_%d.jpg' % index, frame)
            #print 'Done' + str(index)
            array[index] = imnums.getImageAnalysis('frame_%d.jpg' % index)
            index = index + 1
    for x in array:
        print x

def main():
    convertImageToNums()

if __name__ == '__main__':
    main()


