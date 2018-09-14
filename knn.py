import operator
from distance import EuclideanDistanceContext, EuclideanDistance

class TrainingIncompleteException( Exception ):
    def __init__(self):
        Exception.__init__( self, "Prediction before training is not allowed." )

class NegativeOrZeroKException( Exception ):
    def __init__(self, k):
        Exception.__init__(self, "The value of k is negative or zero: " + str( k ))

class KNNRegression( object ):
    '''
    Class responsible for the K-Nearest Neighbor Algorithm.
    '''
    def train( self, training_set, distance ):
        '''
        Training Set of KNN is simply the entire dataset.
        '''
        self.training_set = training_set
        self.distance     = distance
        self.__is_trained = True

    def __get_neighbors( self, data_point, k ):
        '''
        Helper method that grabs k nearest neighbors based on the training set and data point.
        '''

        if k > len( self.training_set ):
            k = len( self.training_set ) - 1

        distances = []
        for t in self.training_set:
            distance_context = EuclideanDistanceContext( data_point, t ) 
            distance = self.distance.compute( distance_context )
            distances.append(( distance,  t ))

        distances.sort( key = operator.itemgetter( 1 ))
        return distances[ : k ]

    def __average_neighbors( self, neighbors ):
        length = len( neighbors )
        sum_of_dimensions = len( neighbors[ 0 ][ 1 ]) * [ 0 ] 
        for i in range( length ):
            training_point = neighbors[ i ][ 1 ]
            for t in range( len( training_point )):
                sum_of_dimensions[ t ] += training_point[ t ]
        return [ s / len( neighbors ) for s in sum_of_dimensions ]

    def predict( self, data_point, k ):
        '''
        Prediction method for KNN 
        '''
        # Precondition checks. 
        if not self.__is_trained:
            raise TrainingIncompleteException()

        if k <= 0:
            raise NegativeOrZeroKException( k ) 

        nearest_neighbors = self.__get_neighbors( data_point, k )
        return self.__average_neighbors( nearest_neighbors )

if __name__ == '__main__':
    knn = KNNRegression()
    knn.train( [ [0,0,2], [ 3,4,5 ], [ 5, 5, 5 ]], EuclideanDistance() )
    print( knn.predict( [ 2, 3, 4 ], 3 ))
    print( "Successfully created KNN.")