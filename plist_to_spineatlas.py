import sys
import plistlib


def readPlistFileyWithPath(plitPath):
    print 'read plist file With:' + plitPath
    return plistlib.readPlist(plitPath)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "arg error not plist path"
        exit(1)
    info = readPlistFileyWithPath(sys.argv[1])
    atlasStr = ''
    metadata = info['metadata']
    textureName = metadata['textureFileName']
    sizeStr = metadata['size']
    sizeStr = sizeStr[1:len(sizeStr) - 1]
    atlasStr = textureName + '\n' + 'size:' + sizeStr + \
        '\nforamt:RGBA8888\nfilter:Linear,Linear\nrepeat:none\n'
    texFormat = metadata['format']
    framesDic = info['frames']
    for frameKey in framesDic.keys():
        frame = framesDic[frameKey]
        frameStr = frameKey[0:len(frameKey) - 4]
        if texFormat == 2:
            rotate = frame['rotated']
            frameRectStr = frame['frame']
            xyPosEnd = frameRectStr.index('}')
            xy = frameRectStr[2:xyPosEnd]
            frameSize = frameRectStr[xyPosEnd + 3:len(frameRectStr) - 2]
            originSize = frame['sourceSize']
            originSize = originSize[1:len(originSize) - 1]
            offset = frame['offset']
            offset = offset[1:len(offset) - 1]
            frameStr += '\n' + '  rotate:' + ('true' if rotate else 'false')
            frameStr += '\n' + '  xy:' + xy
            frameStr += '\n' + '  size:' + frameSize
            frameStr += '\n' + '  orig:' + originSize
            frameStr += '\n' + '  offset:' + offset
            frameStr += '\n' + '  index:-1'
            atlasStr += '\n' + frameStr
    #print atlasStr
    savePath = sys.argv[1] + '.atlas'
    output = open(savePath, 'w')
    output.write(atlasStr)
    output.close()
    print 'plist to spine atlas finish at path:' + savePath
