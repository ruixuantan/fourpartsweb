from utils.utils import get_time_string


def _generate_hashed_filenames(filename):
    """Generates the hashed filenames of the midifile and results csv files. 
    
    Parameters
    ----------
    filename : str
        Original .mid filename. It should end with the suffix: '.mid'.

    Returns
    -------
    tuple of str
        The hashed filenames of the midi and csv files.
    """

    if filename[:-4] == '.mid':
        filename = filename[:-4]

    hashed_filename = str(hash(filename + get_time_string()))
    hashed_mid = hashed_filename + '.mid'
    hashed_parallels_csv = hashed_filename + '_parallels.csv'
    hashed_chords_csv = hashed_filename + '_chords.csv'

    return hashed_mid, hashed_parallels_csv, hashed_chords_csv


class FileCollection:
    """A DataStructure that holds the midifile and 
    its associated analysed result files.

    Parameters
    ----------
    midifile, parallels_result, chords_result : str
        The directory strings.
    """

    def __init__(self, midifile, parallels_result, chords_result,
                 midi_path, parallels_path, chords_path):
        """
        Attributes
        ----------
        midifile, parallels_result, chords_result : str
            Filenames.
        midi_path, parallels_path, chords_path : str
            Concatenated directory and filenames to the associated file.
        """

        self.midifile = midifile
        self.parallels_result = parallels_result
        self.chords_result = chords_result
        self.midi_path = midi_path
        self.parallels_path = parallels_path
        self.chords_path = chords_path

    @classmethod
    def generate_file_collection(cls, midifile, 
                                 midi_path, parallels_path, chords_path):
        """Constructor method for FileCollection.

        Parameters
        ----------
        midi_path : str
            Path intended to save the midifile.
        parallels_path : str
            Path intended to save the generated parallel results.
        chords_path : str
            Path intended to save the generated chord results.
        midifile : str
            Name of the midifile.

        Returns
        -------
        FileCollection
        """

        hashed_mid, hashed_parallels_csv, hashed_chords_csv = \
            _generate_hashed_filenames(midifile)

        return cls(hashed_mid,
                   hashed_parallels_csv,
                   hashed_chords_csv,
                   midi_path + hashed_mid,
                   parallels_path + hashed_parallels_csv,
                   chords_path + hashed_chords_csv)

