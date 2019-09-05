import numpy as np
import matplotlib.pyplot as plt


note_dict = {
"A4": 440.,
"A#4": 466.16,
"B4": 493.88,
"C5": 523.25,
"C#5": 554.37,
"D5": 587.33,
"D#5": 622.25,
"E5": 659.25,
"F5": 622.25,
"F#5": 622.25,
"G5": 622.25,
"G#5": 622.25,
"A5": 880.00
}



def wave(omega, t, Amplitude=1):
    return Amplitude*np.cos(omega*t)

def frequency_to_omega(f):
    return 2*np.pi*f

def interval_superpos(omega, omega2, t, Amplitude=1, Amplitude2=1):
    return Amplitude*np.cos(omega*t) + Amplitude2*np.cos(omega2*t)

def chord_superpos(omega, omega2, omega3, t, Amplitude=1, Amplitude2=1, Amplitude3=1):
    return Amplitude*np.cos(omega*t) + Amplitude2*np.cos(omega2*t) + Amplitude3*np.cos(omega3*t)

def single_tone(note, t):
    '''Note = "A"   '''
    return wave(frequency_to_omega(note_dict[note]), t, Amplitude=1)

def interval(note1, note2, t):
    return interval_superpos(frequency_to_omega(note_dict[note1]), frequency_to_omega(note_dict[note2]), t)

def chord(note1, note2, note3, t):
    return chord_superpos(frequency_to_omega(note_dict[note1]), frequency_to_omega(note_dict[note2]), frequency_to_omega(note_dict[note3]) ,t)

def main():

    T_period = 1/note_dict["E5"]
    t = np.linspace(0,T_period*40,1000)

    nrows = 6
    ncols = 2
    f, ax = plt.subplots(nrows=nrows, ncols=ncols, sharey=False, sharex=True, figsize=(16,20))
    print(ax.shape)

    counter = 0
    keys = list(note_dict.keys())
    for y in range(ncols):
        for x in range(nrows):
            print(x,y)
            tone = keys[counter]
            ax[x][y].plot(t, interval("A4", tone, t))
            ax[x][y].set_title('A4 & %s' % tone)
            ax[x][y].grid()

            counter += 1


    '''
    ax[0][0].plot(t, single_tone("A4", t))
    ax[0][0].set_title('A4')
    ax[0][0].grid()

    ax[1][0].plot(t, interval("A4", "Asharp4", t))
    ax[1][0].set_title('A4 & A#4')
    ax[1][0].grid()

    ax[2][0].plot(t, interval("A4", "B4", t))
    ax[2][0].set_title('A4 & B4')
    ax[2][0].grid()

    ax[0][1].plot(t, interval("A4", "C5", t))
    ax[0][1].set_title('A4 & C5')
    ax[0][1].grid()

    ax[1][1].plot(t, interval("A4", "Csharp5", t))
    ax[1][1].set_title('A4 & C#5')
    ax[1][1].grid()

    ax[2][1].plot(t, interval("A4", "D5", t))
    ax[2][1].set_title('A4 & D5')
    ax[2][1].grid()
    '''

    plt.xlim(min(t), max(t))
    ax[5][0].set_xlabel('time [sec]')
    ax[5][1].set_xlabel('time [sec]')


    #plt.figure()
    #plt.plot(t, interval("A4", "A5", t))
    #plt.figure()
    #plt.plot(t, chord("A4", "E5", "Csharp5", t))
    #plt.figure()
    #plt.plot(t, chord("Csharp4", "E5", "A4", t))
    f.savefig("output/fig.pdf")
main()
#plt.show()
