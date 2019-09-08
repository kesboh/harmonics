import sys
import numpy as np
import matplotlib.pyplot as plt
import math

from chord import Chord
from scale import Scale, TWELVE_TET_220, TWELVE_TJT_220, TWELVE_TET_440, TWELVE_TJT_440
from chord_player import ChordPlayer
from musivis_consts import *
from util import INTERVALS

class ChordPlotter(object):

    def __init__(self, chord):

        fig, ax = plt.subplots(nrows=len(chord.intervals)+1, ncols=1, figsize=(20,10), sharex=True, sharey=True)

        # Scale our waveform so that the plot covers 1 period. The chord might be in inversion,
        # so locate the lowest-frequency interval in the chord as it might not be its root
        lowest = sys.maxsize
        for interval in chord.intervals:
            if interval > lowest:
                lowest = interval

        cut = (len(ChordPlayer.chord_as_wave(chord)) / chord.scale.fund_hz)

        period = (1.0/chord.scale.fund_hz)
        x = np.linspace(0, period, cut)

        ax[0].plot(x, ChordPlayer.chord_as_wave(chord)[:cut], color="b", lw=2)
        ax[0].grid(True)
        if (not chord.name == None):
            ax[0].title.set_text(chord.name)
        else:
            ax[0].title.set_text("Chord and constituent intervals")

        for i in range(1, len(ax)):
            ax[i].plot(x, ChordPlayer.interval_as_sine(chord.intervals[i-1])[:cut], color="r", lw=2)
            ax[i].set_xticklabels(())
            ax[i].grid(True)
            ax[i].title.set_text(("f%u: %uHz\n" % (i, chord.intervals[i-1])))

        fig.tight_layout()
        plt.xlim(0, period)
        plt.show()



a_maj9 = Chord.maj7(TWELVE_TET_220).add_extension(INTERVALS.MAJ_NINTH)
a_maj9_plt = ChordPlotter(a_maj9)



        
        
