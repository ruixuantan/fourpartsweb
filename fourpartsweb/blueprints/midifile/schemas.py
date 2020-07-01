from marshmallow import fields, validate

from fourpartsweb.extensions import marshmallow


class MidifileSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'midistring', 'resultstring')


class UploadMidifileSchema(marshmallow.Schema):
    midistring = fields.Str(required=True)
    resultstring = fields.Str(required=True)


midifile_schema = MidifileSchema()
upload_midifile_schema = UploadMidifileSchema()
