from enum import Enum
from scipy import signal
import numpy as np

class INTERVALS(Enum):
    """ Enums representing the intervals of the chromatic scale in addition to
    the compound intervals of the second octave """
    TONIC     = 0
    MIN_SCND  = 1
    MAJ_SCND  = 2
    MIN_THRD  = 3
    MAJ_THRD  = 4
    PRF_FRTH  = 5
    DIM_FFTH  = 6
    AUG_FRTH  = 6
    TRITONE   = 6
    PRF_FFTH  = 7
    MIN_SXTH  = 8
    MAJ_SXTH  = 9
    MIN_SVTH  = 10
    MAJ_SVTH  = 11
    OCTAVE    = 12
    MIN_NINTH = 13
    MAJ_NINTH = 14
    MIN_TENTH = 15
    MAJ_TENTH = 16
    PERF_ELVTH= 17
    DBL_TRTN  = 18
    DIM_TWLFTH= 19
    MIN_THRTN = 20
    MAJ_THRTN = 21
    MIN_FRTN  = 22
    MAJ_FRTN  = 23
    DBL_OCT   = 24

class NOTES_JUST(Enum):
    """ Enums representing the notes of a chromatic scale in just temperament """
    A_4      = 440.00
    Asharp_4 = 466.16
    B_4      = 493.88
    C_5      = 523.25
    Csharp_5 = 554.37
    D_5      = 587.33
    Dsharp_5 = 622.25
    E_5      = 659.25
    F_5      = 622.25
    Fsharp_5 = 622.25
    G_5      = 622.25
    Gsharp_5 = 622.25
    A_5      = 880.00

class NOTES_EQUAL(Enum):
    """ Enums representing the notes of the chromatic scale in equal temperament """
    A_4      = 440.00
    Asharp_4 = A_4*(2.0**(1.0/12.0))
    B_4      = Asharp_4*(2.0**(1.0/12.0))
    C_5      = B_4*(2.0**(1.0/12.0))
    Csharp_5 = C_5*(2.0**(1.0/12.0))
    D_5      = Csharp_5*(2.0**(1.0/12.0))
    Dsharp_5 = D_5*(2.0**(1.0/12.0))
    E_5      = Dsharp_5*(2.0**(1.0/12.0))
    F_5      = E_5*(2.0**(1.0/12.0))
    Fsharp_5 = F_5*(2.0**(1.0/12.0))
    G_5      = Fsharp_5*(2.0**(1.0/12.0))
    Gsharp_5 = G_5*(2.0**(1.0/12.0))
    A_5      = Gsharp_5*(2.0**(1.0/12.0))


#Function aliases for generating the periodic signals
W_SINE_FNC   = np.sin
W_SQUARE_FNC = signal.square
W_SAW_FNC    = signal.sawtooth


def rotate_list_left(l, n):
    """ Helper method: rotate a list l n positions to the left """
    return l[n:] + l[:n]
