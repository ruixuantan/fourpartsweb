import fourparts as fp
import pandas as pd

from utils.utils import delete_file


def generate_parallels_result(chord_progression, path):
    """Check for parallels in chord_progression and saves to a csv file.

    Parameters
    ----------
    chord_progression : fp.ChordProgression
    path : str
        Path to where the csv file is to be saved.

    Returns
    -------
    bool
        True if the analysis is successful.
    """

    try:
        parallels = chord_progression.check_parallels()
        pd.DataFrame(parallels).to_csv(path)
    except Exception:
        return False

    return True


def generate_pitch_class_set(chord_progression, path):
    """Generates the pitch class set in chord_progression and saves to a csv file.

    Parameters
    ----------
    chord_progression : fp.ChordProgression
    path : str
        Path to where the csv file is to be saved.

    Returns
    -------
    bool
        True if the analysis is successful.
    """

    try:
        pitch_class_sets = chord_progression.get_pitch_class_sets()
        pd.DataFrame(pitch_class_sets).to_csv(path)
    except Exception:
        return False

    return True


def generate_results(midi_path, parallels_path, chords_path):
    """Generates results of the analysed midi file.

    Parameters
    ----------
    midi_path, parallels_path, chords_path : str
        The paths to the associated directories.

    Returns
    -------
    bool
        Returns True if the analysis is completed.
    """

    try:
        df = fp.midi_to_df(midi_path)
        chords = fp.PreProcessor(4).get_progression(df)
        chord_progression = fp.ChordProgression(chords)
    except Exception:
        delete_file(midi_path)
        return False

    if not generate_parallels_result(chord_progression,
                                     parallels_path):
        delete_file(midi_path)
        return False

    if not generate_pitch_class_set(chord_progression,
                                    chords_path):
        delete_file(midi_path)
        return False

    return True
