from midiutil.MidiFile import MIDIFile
import random
import os
def get_random_pitch():
    c3_note = 48
    c5_note = 72
    random_pitch = random.randint(c3_note, c5_note)
    return random_pitch
def generate_random_wavs(num):
    prefix = "midi_"
    for i in range(0, num):
        mf = MIDIFile(1)
        track = 0
        time = 0
        mf.addTrackName(track, time, "Sample Track")
        mf.addTempo(track, time, 120)
        channel = 0
        volume = 120
        t = 0
        num_notes = 20
        for x in range(0, num_notes):
            pitch = get_random_pitch()
            time = t
            add = random.randint(1, 3)
            duration = add
            t += add
            mf.addNote(track, channel, pitch, time, duration, volume)

        midi_filename = "midi/" + prefix + str(i) + ".mid"
        with open(midi_filename, 'wb') as outf:
            mf.writeFile(outf)
        my_file = midi_filename
        base=os.path.splitext(my_file)[0]
        os.rename(my_file, base + '.wav')



generate_random_wavs(20)

