import cv2
import skvideo.io
import json

FRAMES_PER_VIDEO = 6

def getNumberOfFrames():
    metadata = skvideo.io.ffprobe('myVid.mp4')
    json_data = json.dumps(metadata)
    json_data = json.loads(json_data)
    totalNumberOfFrames = (int)(json_data['video']['@nb_frames'])
    return totalNumberOfFrames

def main():
    video = cv2.VideoCapture('myVid.mp4')
    maxFrames = getNumberOfFrames()
    count = 0
    index = 0
    for i in range(1, maxFrames):
        count = count + 1
        ret, frame = video.read()
        if count >= maxFrames / FRAMES_PER_VIDEO:
            count = 0
            cv2.imwrite('frame_%d.jpg' % index, frame)
            index = index + 1
            print 'Done' + str(index)


if __name__ == '__main__':
    main()


