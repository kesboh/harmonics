import sys
import numpy as np
import matplotlib.pyplot as plt
import math

from scipy import signal

from chord import Chord
from scale import Scale, TWELVE_TET_220, TWELVE_TJT_220, TWELVE_TET_440, TWELVE_TJT_440
from chord_player import ChordPlayer
from util import INTERVALS, W_SAW_FNC, W_SINE_FNC, W_SQUARE_FNC

class ChordPlotter(object):

    def __init__(self, chord, num_periods=1, wave_fnc=W_SINE_FNC):

        fig, ax = plt.subplots(nrows=len(chord.intervals)+1, ncols=1, figsize=(20,10), sharex=True, sharey=True)

        # Scale our waveform so that the plot covers num_periods periods. The chord might be in inversion,
        # so locate the lowest-frequency interval in the chord as it might not be its root
        lowest = sys.maxsize
        for interval in chord.intervals:
            if interval > lowest:
                lowest = interval

        cut = (len(ChordPlayer.chord_as_wave(chord)) / chord.scale.fund_hz) * num_periods

        period = (1.0/chord.scale.fund_hz)
        x = np.linspace(0, period, cut)

        ax[0].plot(x, ChordPlayer.chord_as_wave(chord, wave_fnc)[:cut], color="b", lw=2)
        ax[0].grid(True)

        if (not chord.name is None):
            ax[0].title.set_text(chord.name)
        else:
            ax[0].title.set_text("Chord and constituent intervals")

        for i in range(1, len(ax)):
            ax[i].plot(x, ChordPlayer.interval_as_sine(chord.intervals[i-1], wave_fnc)[:cut], color="r", lw=2)
            ax[i].set_xticklabels(())
            ax[i].grid(True)
            
            txt = "$f_{" + str(i) + "} = " + str(chord.intervals[i-1]) + "Hz$"
            ax[i].title.set_text(txt)

        fig.tight_layout()
        plt.xlim(0, period)
        plt.show()



# a_maj9 = Chord.maj7(TWELVE_TET_220, name="Amaj9").add_extension(INTERVALS.MAJ_NINTH)
# ChordPlotter(a_maj9)

# a_tri = Chord(TWELVE_TET_220, [INTERVALS.TONIC, INTERVALS.TRITONE, INTERVALS.TRITONE.value*2, INTERVALS.TRITONE.value*3, INTERVALS.TRITONE.value*4], name="Quad Tritone")
# ChordPlotter(a_tri)

# a5 = Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.PRF_FFTH], name="A5 JT")
# ChordPlotter(a5, 2)

# a_tri = Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.TRITONE], name="Tritone JT")
# ChordPlotter(a_tri, 2)

# majthrd =  Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.MAJ_THRD], name="M3")
# ChordPlotter(majthrd, 2)

# minthrd =  Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.MIN_THRD], name="m3")
# ChordPlotter(minthrd, 2)

stacked_majsevenths = Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.MAJ_SVTH.value, INTERVALS.MAJ_SVTH.value*2])
ChordPlotter(stacked_majsevenths, 2)   
        
