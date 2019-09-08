import time

from contextlib import contextmanager
import sys, os

import pyaudio
import numpy as np

from chord import Chord
from scale import Scale, TWELVE_TET_220, TWELVE_TJT_220, TWELVE_TET_440, TWELVE_TJT_440
from musivis_consts import *
from util import INTERVALS


class ChordPlayer(object):


    def __init__(self):
        self.player = pyaudio.PyAudio()


    @staticmethod
    def chord_as_wave(chord):
        """ Takes as input a chord and returns a wave consisting of the superpositions of
        the frequencies of its constituent intervals """
        wave = 0

        #Combine the intervals of the chord; normalizing to avoid clipping
        for interval in chord.intervals:
            wave += (ChordPlayer.interval_as_sine(interval) / (len(chord.intervals)))

        return wave.astype(np.float32)

    @staticmethod
    def interval_as_sine(freq):
        """ Takes as input a frequency and returns a sine wave of said frequency """
        return np.sin(2*np.pi*np.arange(F_SAMPLE*LEN_S*LEN_SCALE_FACTOR)*freq/F_SAMPLE).astype(np.float32)



    def play_chord(self, chord, volume=1):
        """ Plays an audio-representation of the given chord """
        if volume > 1.0 or volume < 0.0:
            volume = 1

        stream = self.player.open(format=pyaudio.paFloat32, channels=1, rate=F_SAMPLE,
                input=False, output=True)

        chord_as_wave = ChordPlayer.chord_as_wave(chord)
        stream.write(volume*chord_as_wave)
        stream.stop_stream()
        stream.close()

    def play_arpeggio(self, chord, volume=1):
        """ Plays an audio-representation of the given chord """
        if volume > 1.0 or volume < 0.0:
            volume = 1

        for interval in chord.intervals:
            stream = self.player.open(format=pyaudio.paFloat32, channels=1, rate=F_SAMPLE,
                    input=False,output=True)

            #Shorten the samples so that playing all intervals take as long as playing the chord would
            smpls = ChordPlayer.interval_as_sine(interval)
            stream.write(volume*smpls[:len(smpls)/len(chord.intervals)])
            stream.stop_stream()
            
        stream.close()


    
player = ChordPlayer()

# A major in just temperament
# a_maj = Chord.maj(Scale.twelve_tjt(220))
# player.play_chord(ChordPlayer.chord_as_wave(a_maj))

# A minor in equal temperament
# a_min = Chord.min(Scale.twelve_tet(220), INTERVALS.MIN_THRD)
# player.play_chord(ChordPlayer.chord_as_wave(a_min))

# a_maj7 in just temperament, first inversion
# a_maj7 = Chord.maj7(TWELVE_TET_220)
# player.play_arpeggio(a_maj7)

# Big a_dim chord
# a_dim = Chord.dim(TWELVE_TET_220).add_extension(INTERVALS.MAJ_SXTH).add_extension(INTERVALS.OCTAVE).add_extension(INTERVALS.MIN_TENTH)
# player.play_arpeggio(a_dim)

# #Build chord manually from arbitrary intervals
# a_min = Chord(TWELVE_TJT_220, [INTERVALS.TONIC,  INTERVALS.MAJ_THRD], INTERVALS.TRITONE)
# player.play_chord(ChordPlayer.chord_as_wave(a_min))







