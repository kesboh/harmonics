from scale import Scale
from util import INTERVALS, rotate_list_left

class Chord(object):

    #TODO: Perhaps couple an interval to its corresponding scale degree more closely

    def __init__(self, scale, intervals, root_degree=INTERVALS.TONIC.value, name=None):
        """ A chord is an object consisting of one or more scale degrees
        of a given scale, with its tonic on the root degree
        """

        if isinstance(root_degree, INTERVALS):
            root_degree = root_degree.value

        if not isinstance(intervals, list):
            intervals = [intervals]


        self.scale = scale
        self.intervals = []
        self.root_degree = root_degree
        self.name = name
        
        for interval in intervals:
            if (isinstance(interval, INTERVALS)):
                interval = interval.value

            if interval > len(scale.intervals):
                raise ValueError("Chord intervals cant exceed intervals of given scale")

            self.intervals.append(scale.intervals[interval+root_degree])

    def invert(self, n=1):
        """ Inverts this chord by n degrees, e.g:
        invert(1): 1 3 5 -> 3 5 1+octave
        invert(2): 1 3 5 -> 5 (1+octave) (3+octave)
        """
        if n > len(self.intervals):
            raise ValueError("invert(self,n): n must be an integer smaller than len(self.intervals)")

        ri = rotate_list_left(self.intervals, n)
        for i in range(len(ri)-n, len(ri)):
            ri[i] = ri[i]*2

        self.intervals = ri
        return self

    def add_extension(self, interval_extension):
        """ Add an extension to this chord. The extension may be of the INTERVALS enum type, or
        a number representing the scale degree
        """
        if isinstance(interval_extension, INTERVALS):
            interval_extension = interval_extension.value
        else:
            interval_extension = interval_extension
        
        self.intervals.append(self.scale.intervals[interval_extension+self.root_degree])
        return self

    """
    All static methods below assume that the given scale divides an octave into 12 semitones.
    Methods that add extensions past the seventh degree do not add previous degrees (e.g maj9()
    does not return a chord including the major seventh); these may be added via add_extension()
    """

    @staticmethod
    def triad(scale, is_maj, root_degree=INTERVALS.TONIC, name=None):
        """ Return a chord of the simple triad type """
        third = INTERVALS.MAJ_THRD if is_maj else INTERVALS.MIN_THRD

        return Chord(scale, [INTERVALS.TONIC, third, INTERVALS.PRF_FFTH], root_degree, name)

    @staticmethod
    def maj(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a simple major triad """
        return Chord.triad(scale, True, root_degree, name)

    @staticmethod
    def maj7(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a maj7 chord """
        return Chord.maj(scale, root_degree, name).add_extension(INTERVALS.MAJ_SVTH)

    @staticmethod
    def maj9(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a maj9 chord """
        return (Chord.maj(scale, root_degree, name).add_extension(INTERVALS.MAJ_SVTH)
                .add_extension(INTERVALS.OCTAVE + INTERVALS.MAJ_SCND))

    @staticmethod
    def dom7(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a dominant 7th chord """
        return Chord.maj(scale, root_degree, name).add_extension(INTERVALS.MIN_SVTH)

    @staticmethod
    def min(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a simple minor triad chord """
        return Chord.triad(scale, False, root_degree, name)

    @staticmethod
    def min7(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a min7 chord """
        return Chord.triad(scale, False, root_degree, name).add_extension(INTERVALS.MIN_SVTH)

    @staticmethod
    def min9(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a min7 chord """
        return (Chord.triad(scale, False, root_degree, name).add_extension(INTERVALS.MIN_SVTH)
                .add_extension(INTERVALS.OCTAVE + INTERVALS.MAJ_SCND))

    @staticmethod
    def min_maj7(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a minor major seventh chord """
        return Chord.triad(scale, root_degree, name).add_extension(INTERVALS.MAJ_SVTH)

    @staticmethod
    def aug(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return an augmented triad """
        return Chord(scale, [INTERVALS.TONIC, INTERVALS.MAJ_THRD, INTERVALS.MIN_SXTH], root_degree, name)

    @staticmethod
    def dim(scale, root_degree=INTERVALS.TONIC, name=None):
        """ Return a diminished triad """
        return Chord(scale, [INTERVALS.TONIC, INTERVALS.MIN_THRD, INTERVALS.DIM_FFTH], root_degree, name)


