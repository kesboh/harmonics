from util import INTERVALS, NOTES_JUST, NOTES_EQUAL

class Scale(object):

    def __init__(self, fund_hz, intervals, octave_extend_n=None):
        """ Returns a scale based on the given fundamental, consisting of the given
        intervals, and extended by octave_extend_n number of octaves """

        self.intervals = intervals
        self.fund_hz = fund_hz
        self.num_intervals = len(self.intervals)

        if (octave_extend_n == None):
            octave_extend_n = 2

        k = 2
        while k < octave_extend_n*2:
            tmp_h = [x * k for x in self.intervals[1:self.num_intervals]]
            #tmp_l = [x / k for x in self.intervals[1:self.num_intervals]]
            self.intervals = self.intervals + tmp_h
            #self.intervals = tmp_l + self.intervals #Annoying to keep track of indexes (tonic) when we do this
            k = k*2

        self.fund_hz_index = self.intervals.index(fund_hz)



    def print_freqs(self):
        """ Print the frequencies of this scale """
        for i in range(0, len(self.intervals)):
            print(self.intervals[i])

    def print_ratios(self):
        """ Print the ratios of the intervals in this scale """
        for i in range(1, len(self.intervals)):
            print(self.intervals[i] / self.intervals[i-1])

    @staticmethod
    def twelve_tjt(fund_hz):
        """ Returns a scale of the just intonation type, based on the
        provided fundamental
        """
        intervals = []
        r = [1.0, 25.0/24.0, 9.0/8.0, 6.0/5.0, 5.0/4.0, 4.0/3.0, 45.0/32.0, 3.0/2.0, 8.0/5.0,
            5.0/3.0, 9.0/5.0, 15.0/8.0, 2.0]

        for ratio in r:
            intervals.append(fund_hz*ratio)

        return Scale(fund_hz, intervals)

    @staticmethod
    def tet(fund_hz, num_steps):
        """ Return a scale of the TET type, based on the provided
        provided fundamental and with num_steps number of intervals
        """
        intervals = [fund_hz]

        for i in range(1, num_steps+1):
            intervals.append(intervals[i-1]*(2**(1/12.0)))

        return Scale(fund_hz, intervals)

    @staticmethod
    def twelve_tet(fund_hz):
        """ Returns a scale of the 12TET type """
        return Scale.tet(fund_hz, 12)


#Useful
TWELVE_TET_220 = Scale.twelve_tet(220)
TWELVE_TJT_220 = Scale.twelve_tjt(220)
TWELVE_TET_440 = Scale.twelve_tet(440)
TWELVE_TJT_440 = Scale.twelve_tjt(440)
