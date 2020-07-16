import time
from contextlib import contextmanager

from enum import Enum

import pyaudio
import numpy as np
from scipy import signal

from chord import Chord
from scale import Scale, TWELVE_TET_220, TWELVE_TJT_220, TWELVE_TET_440, TWELVE_TJT_440
from musivis_consts import *
from util import INTERVALS, W_SAW_FNC, W_SINE_FNC, W_SQUARE_FNC


class ChordPlayer(object):

    def __init__(self):
        self.player = pyaudio.PyAudio()

    @staticmethod
    def chord_as_wave(chord, wave_fnc=W_SINE_FNC):
        """ Takes as input a chord and returns a wave consisting of the superpositions of
        the frequencies of its constituent intervals """
        wave = 0

        #Combine the intervals of the chord; normalizing to avoid clipping
        for interval in chord.intervals:
            wave += (ChordPlayer.interval_as_sine(interval, wave_fnc) / (len(chord.intervals)))

        return wave

    @staticmethod
    def interval_as_sine(freq, wave_fnc=W_SINE_FNC):
        """ Takes as input a frequency and returns a sine wave of said frequency """
        return wave_fnc(2*np.pi*np.arange(F_SAMPLE*LEN_S*LEN_SCALE_FACTOR)*freq/F_SAMPLE).astype(np.float32)

    def play_chord(self, chord, wave_fnc=W_SINE_FNC, volume=1, dur=1):
        """ Plays an audio-representation of the given chord """
        if volume > 1.0 or volume < 0.0:
            volume = 1

        if dur < 0.0:
            dur = 1

        stream = self.player.open(format=pyaudio.paFloat32, channels=1, rate=F_SAMPLE,
                input=False, output=True)

        chord_as_wave = ChordPlayer.chord_as_wave(chord, wave_fnc)
        stream.write(volume*chord_as_wave[:int(round(len(chord_as_wave)*dur))])
        stream.stop_stream()
        stream.close()

    def play_arpeggio(self, chord, volume=1, dur=1):
        """ Plays an audio-representation of the given chord """
        if volume > 1.0 or volume < 0.0:
            volume = 1

        if dur < 0.0:
            dur = 1

        for interval in chord.intervals:
            stream = self.player.open(format=pyaudio.paFloat32, channels=1, rate=F_SAMPLE,
                    input=False,output=True)

            #Shorten the samples so that playing all intervals take as long as playing the chord would
            smpls = ChordPlayer.interval_as_sine(interval)
            stream.write(volume*smpls[:int(round(len(smpls)*dur))/len(chord.intervals)])
            stream.stop_stream()
            
        stream.close()



player = ChordPlayer()



