"""Iterate over seven notes in each of five octaves."""
class MusicNotes:
    def __init__(self):
        self._base = (55, 61.74, 65.41, 73.42, 82.41, 87.31, 98)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 35:
            raise StopIteration
        octave, note = divmod(self._index, 7)
        self._index += 1
        return round(self._base[note] * 2 ** octave, 2)


if __name__ == '__main__':
    notes_iter = iter(MusicNotes())
    for frequency in notes_iter:
        print(frequency)
