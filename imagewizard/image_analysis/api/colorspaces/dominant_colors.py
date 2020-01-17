import cv2 as cv
from sklearn.cluster import KMeans

""" Class that uses sklearn kMeans clustering to find dominant colors in an Image. """
class DominantColors():
    CLUSTERS = None
    COLORS = None

    def __init__(self, no_of_colors: int = 3):
        """
        Params:
            no_of_colors: number of dominant colors to be returned
        """
        self.CLUSTERS = no_of_colors
    
    def dominant_colors(self, img):
        """
        Params:
            image: (numpy nd array - BGR)
        """       
        # convert to rgb from bgr
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        
        # reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))        
        
        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters = self.CLUSTERS, random_state=1)
        kmeans.fit(img)
        
        # cluster centers are the dominant colors
        self.COLORS = kmeans.cluster_centers_
        
        # convert cluster values to integer and return the RGB clusters
        return self.COLORS.astype(int)
