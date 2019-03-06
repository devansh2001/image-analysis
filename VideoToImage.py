import skvideo.io
import skvideo.datasets
import json
import numpy as np

FRAMES_PER_VIDEO = 6

def getFrames():
    reader = skvideo.io.FFmpegReader(skvideo.datasets.bigbuckbunny())
    metadata = skvideo.io.ffprobe(skvideo.datasets.bigbuckbunny())
    json_data = json.dumps(metadata)
    json_data = json.loads(json_data)
    totalNumberOfFrames = (int)(json_data['video']['@nb_frames'])

    countFrame = 0
    for i in xrange(1, totalNumberOfFrames):
        countFrame = countFrame + 1
        reader.nextFrame()
        if countFrame >= totalNumberOfFrames / FRAMES_PER_VIDEO:
            countFrame = 0
            frame = reader.nextFrame()
            frame = np.array(frame)
            sums = np.sum(frame)
            print sums
            print i
            print frame

def main():
    getFrames()

if __name__ == '__main__':
    main()
