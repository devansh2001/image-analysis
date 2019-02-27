from PIL import Image


def getImageAnalysis(imgName):
    # Use PIL to access image data
    img = Image.open(imgName).convert(mode='L', dither=Image.NONE)


    # Get image dimensions
    width, height = img.size
    print width
    print height

    # Get width, height of each unit of the 16-images
    xMax = width / 4
    yMax = height / 4

    # Get numerical data from the image
    data = list(img.getdata())
    data = [data[offset:offset + width] for offset in range(0, width * height, width)]

    # Initialize 4x4 array to store final values with 0
    matrix = [[0 for i in xrange(4)] for i in xrange(4)]

    # Find average of final
    for i in xrange(0,4):
        for j in xrange(0,4):
            mySum = 0
            for x in xrange(yMax * i, yMax * (i + 1)):
                for y in xrange(xMax * j, xMax * (j + 1)):
                    mySum += data[x][y]
            avg = mySum / (xMax * yMax)
            matrix[i][j] = avg
            avg = 0

    # Display results
    for x in xrange(0, 4):
        print matrix[x]


    # count = 0
    # row = 0
    # col = 0
    # for a in matrix:
    #     for b in a:
    #         print "Element[%d][%d]: %d" %(row, col, b)
    #         col += 1
    #         count += 1
    #     row += 1
    #     col = 0

def main():
    getImageAnalysis('redHand.png')

if __name__ == '__main__':
    main()
