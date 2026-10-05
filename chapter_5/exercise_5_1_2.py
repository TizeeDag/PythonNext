"""Play Yonatan Hakatan with an iterable of notes (Windows)."""
freqs = {'la': 220, 'si': 247, 'do': 261, 're': 293, 'mi': 329, 'fa': 349, 'sol': 392}
notes = 'sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500'


def play_song(beep=None):
    if beep is None:
        import winsound
        beep = winsound.Beep
    song = notes.split('-')
    print(type(song))
    print('__iter__' in dir(song))
    for note in song:
        name, duration = note.split(',')
        beep(freqs[name], int(duration))


if __name__ == '__main__':
    play_song()
