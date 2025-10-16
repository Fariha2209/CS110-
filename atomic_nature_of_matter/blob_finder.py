#importing necessary libraries
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        self._blobs = []                                                      #initializes an empty list
        self._marked = stdarray.create2D(pic.width(), pic.height(), False)    #creates a 2D list with the dimension of the picture
        
        #Goes through every pixel in the picture
        for i in range(pic.width()):
            for j in range(pic.height()):
                if not self._marked[i][j]:           #Checks if the pixel has been checked yet or not
                    if (pic.get(i, j)).luminance() >= tau:
                        blob = Blob()
                        self._findBlob(pic, tau, i, j, self._marked, blob)
                        if blob.mass() > 0:
                            self._blobs.append(blob)


    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):

        beads = []
        for i in range(len(self._blobs)):
            if self._blobs[i].mass() >= pixels:
                beads.append(self._blobs[i])
        return beads

    # Identifies a blob using depth-first search. The parameters are the picture (pic), luminance
    # threshold (tau), pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob
    # being identified (blob).
    def _findBlob(self, pic, tau, i, j, marked, blob):
        if i < 0 or i >= pic.width():
            return
        
        if j < 0 or j >= pic.height():
            return
        
        if marked[i][j]:
            return
        
        if pic.get(i, j).luminance() < tau:           
            return
        
        marked[i][j] = True                                 #Marks the pixel
        blob.add(i, j)                                      #adds the pixel to the current blob

        self._findBlob(pic, tau, i + 1, j, marked, blob)     #right
        self._findBlob(pic, tau, i - 1, j, marked, blob)     #left
        self._findBlob(pic, tau, i, j + 1, marked, blob)     #down
        self._findBlob(pic, tau, i, j - 1, marked, blob)     #up



# Unit tests the data type [DO NOT EDIT].
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef("%d Beads:\n", len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef("%d Blobs:\n", len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == "__main__":
    _main()
