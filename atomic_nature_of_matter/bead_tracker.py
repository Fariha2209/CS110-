#importing necessary libraries
import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    #Reads command-line arguments and assigns them to the desginated variable
    pixel = int(sys.argv[1])                 
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frame = sys.argv[4:]
    
    #Finds the beads in the first picture
    bf = BlobFinder(Picture(frame[0]), tau )
    #Stores the beads from the frame
    prevBeads = bf.getBeads(pixel)
     
    #Goes through the rest of the pictures and gets beads from the current frame
    for i in range(1, len(frame)):

        bf = BlobFinder(Picture(frame[i]), tau )
        currBeads = bf.getBeads(pixel)
        
        #For each bead in the current frame, finds the closest bead from the previous frame
        for currBead in currBeads:
            min_dist = float('inf')
            for prevBead in prevBeads:
                d = currBead.distanceTo(prevBead)                
                if d <= delta and d < min_dist:
                    min_dist = d

            if min_dist != float('inf'):
                stdio.writeln('%.4f' % min_dist)

        stdio.writeln()
        
        #Sets current bead as previous beads for the next iteration
        prevBeads = currBeads

if __name__ == "__main__":
    main()
