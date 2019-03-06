import skvideo.io
import skvideo.datasets
import json

FRAMES_PER_VIDEO = 5

def getFrames():
    reader = skvideo.io.FFmpegReader(skvideo.datasets.bigbuckbunny())
    metadata = skvideo.io.ffprobe(skvideo.datasets.bigbuckbunny())
    json_data = json.dumps(metadata)
    json_data = json.loads(json_data)
    totalNumberOfFrames = (int)(json_data['video']['@nb_frames'])




def main():
    getFrames()

if __name__ == '__main__':
    main()
