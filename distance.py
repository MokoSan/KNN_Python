import math

class IDistance( object ):
    '''
    Interface for all Distance functions.
    '''
    def compute( distance_context ):
        raise NotImplementedError

class EuclideanDistanceContext( object ):
    '''
    Context of the Euclidean Distance Class. 
    '''
    def __init__( self, item_a, item_b ):
        assert( len( item_a ) == len( item_b ))
        self.item_a  = item_a
        self.item_b  = item_b
        self.length = len( item_a )

class EuclideanDistance( IDistance ):
    '''
    Class responsible for computing the Euclidean distance.
    '''
    def compute( self, distance_context ):
        distance = 0
        for i in range( distance_context.length ):
            distance += pow( distance_context.item_a[ i ] - distance_context.item_b[ i ], 2 )
        return math.sqrt( distance )