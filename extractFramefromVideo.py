import cv2 
  
# Function to extract frames 
def FrameCapture(path): 
    folder = 'C:\\Users\\13418\\Desktop\\practice_place\\img\\'
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
    #cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    n = 2
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read()
        print(success)
        if success:
        # Saves the frames with frame-count 
            cv2.imwrite(folder + "frame%d.jpg" % count, image) 
            print("frame.shape:", image.shape)
        
            #frame = cv2.resize(image, (int(540/2), int(960/2) ))
            #cv2.imshow('video',frame)
            #cv2.imwrite('frame' + str(count) + '.jpg',image)
            #cv2.waitKey(500 * 1)
            count += 1

    print(count)
    return
# Driver Code 
if __name__ == '__main__': 
    # Calling the function 
    FrameCapture("C:\\Users\\13418\\Desktop\\practice_place\\hy.mp4") 
