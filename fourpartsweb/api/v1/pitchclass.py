from flask import jsonify, request

import fourparts as fp
from fourpartsweb.api.v1 import V1FlaskView


class PitchclassView(V1FlaskView):
    def post(self):

        data = request.get_json()

        if 'notes' not in data:
            return jsonify({'error': 'wrong request'}), 400

        pitches = [int(p) for p in data['notes']]
        try:
            pcs = fp.PitchClassSet.create_pitch_class_set(pitches)
        except Exception:
            return jsonify({'error': 'Only cardinality of 2 to 7 pitches are supported'}), 200

        response = {
            'pitches': pcs.pitches,
            'name': pcs.name
        }

        return jsonify(response), 200
