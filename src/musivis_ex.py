from chord_player import ChordPlayer, player
from chord_plotter import ChordPlotter
from scale import Scale
from chord import Chord

from util import INTERVALS
from scale import TWELVE_TET_220, TWELVE_TET_440, TWELVE_TJT_220, TWELVE_TJT_440


# Example usage

def plot_some_chords():
    a_maj9 = Chord.maj7(TWELVE_TET_220, name="Amaj9").add_extension(INTERVALS.MAJ_NINTH)
    ChordPlotter(a_maj9)

    a_tri_multi = Chord(TWELVE_TET_220, [INTERVALS.TONIC, INTERVALS.TRITONE, INTERVALS.TRITONE.value*2, INTERVALS.TRITONE.value*3, INTERVALS.TRITONE.value*4], name="Quad Tritone")
    ChordPlotter(a_tri_multi)

    a5 = Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.PRF_FFTH], name="A5 JT")
    ChordPlotter(a5, 2)

    a_tri = Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.TRITONE], name="Tritone JT")
    ChordPlotter(a_tri, 2)

    majthrd =  Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.MAJ_THRD], name="M3")
    ChordPlotter(majthrd, 2)

    minthrd =  Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.MIN_THRD], name="m3")
    ChordPlotter(minthrd, 2)

    stacked_majsevenths = Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.MAJ_SVTH.value, INTERVALS.MAJ_SVTH.value*2])
    ChordPlotter(stacked_majsevenths, 2)

def sound_some_chords():
    a_maj = Chord.maj(TWELVE_TJT_220)
    player.play_chord(a_maj)

    a_min = Chord.min(Scale.twelve_tet(220))
    player.play_chord(a_min)

    a_maj7 = Chord.maj7(TWELVE_TET_220)
    a_maj7.invert(1)
    player.play_arpeggio(a_maj7)

    a_maj9 = Chord.maj7(TWELVE_TJT_220).add_extension(INTERVALS.MAJ_NINTH)
    player.play_chord(a_maj9)

    a_maj9 = Chord.maj7(TWELVE_TET_220).add_extension(INTERVALS.MAJ_NINTH)
    player.play_chord(a_maj9)

    a_dim = Chord.dim(TWELVE_TET_220).add_extension(INTERVALS.MAJ_SXTH).add_extension(INTERVALS.OCTAVE).add_extension(INTERVALS.MIN_TENTH)
    player.play_arpeggio(a_dim)

    a_tri = Chord(TWELVE_TET_220, [INTERVALS.TONIC, INTERVALS.TRITONE, INTERVALS.TRITONE.value*2, INTERVALS.TRITONE.value*3, INTERVALS.TRITONE.value*4])
    player.play_chord(a_tri)

    up = Chord(TWELVE_TET_220, [INTERVALS.PRF_FFTH, INTERVALS.PRF_FFTH.value+2])
    player.play_arpeggio(up, dur=0.25)

    a_maj13 = Chord(TWELVE_TJT_220, [INTERVALS.TONIC, INTERVALS.MAJ_THRD, INTERVALS.MAJ_SVTH, INTERVALS.MAJ_NINTH, INTERVALS.MAJ_FRTN])
    player.play_chord(a_maj13)


def play_giant_steps():
    Bmaj7 = Chord.maj7(TWELVE_TET_220, INTERVALS.MAJ_SCND)
    D7    = Chord.dom7(TWELVE_TET_220, INTERVALS.PRF_FRTH).invert(1)
    Gmaj7 = Chord.maj7(TWELVE_TET_220, INTERVALS.MIN_SVTH)
    Bb7   = Chord.dom7(TWELVE_TET_220, INTERVALS.MIN_SCND)
    Ebmaj7 = Chord.maj7(TWELVE_TET_220, INTERVALS.DIM_FFTH)
    Am7 = Chord.min7(TWELVE_TET_220)
    Fs7   = Chord.dom7(TWELVE_TET_220, INTERVALS.MAJ_SXTH)
    Fm7  = Chord.min7(TWELVE_TET_220, INTERVALS.MIN_SXTH)
    Cm7 = Chord.min7(TWELVE_TET_220, INTERVALS.MIN_THRD)
    Csm7 = Chord.min7(TWELVE_TET_220, INTERVALS.MAJ_THRD)

    player.play_chord(Bmaj7, dur=0.25)
    player.play_chord(D7, dur=0.25)
    player.play_chord(Gmaj7, dur=0.25)
    player.play_chord(Bb7, dur=0.25)
    player.play_chord(Ebmaj7, dur=0.50)

    player.play_chord(Am7, dur=0.25)
    player.play_chord(D7, dur=0.30)

    player.play_chord(Gmaj7, dur=0.25)
    player.play_chord(Bb7, dur=0.25)
    player.play_chord(Ebmaj7, dur=0.25)
    player.play_chord(Fs7, dur=0.20)
    player.play_chord(Bmaj7, dur=0.5)

    player.play_chord(Fm7, dur=0.25)
    player.play_chord(Bb7, dur=0.25)
    player.play_chord(Ebmaj7, dur=0.5)

    player.play_chord(Am7, dur=0.25)
    player.play_chord(D7, dur=0.25)
    player.play_chord(Gmaj7, dur=0.5)

    player.play_chord(Cm7, dur=0.25)
    player.play_chord(Fs7, dur=0.25)
    player.play_chord(Bmaj7, dur=0.5)

    player.play_chord(Fm7, dur=0.25)
    player.play_chord(Bb7, dur=0.25)
    player.play_chord(Ebmaj7, dur=0.5)

    player.play_chord(Csm7, dur=0.20)
    player.play_chord(Fs7, dur=0.20)

play_giant_steps()
        
