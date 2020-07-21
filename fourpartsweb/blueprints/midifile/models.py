from fourpartsweb.extensions import db

class Midifile(db.Model):
    """No storing of midi file in database.
    Store a string instead, which points towards the
    midi file in the folder 'midifiles_storage'/.
    """

    __tablename__ = 'midifile'

    id = db.Column(db.Integer, primary_key=True)
    midi_string = db.Column(db.String(), unique=True)
    parallels_string = db.Column(db.String(), unique=True)
    chords_string = db.Column(db.String(), unique=True)

    def __repr__(self):
        return "<Midi: {0}, Csv: {1}>" \
                .format(self.midi_string, self.csv_string)
