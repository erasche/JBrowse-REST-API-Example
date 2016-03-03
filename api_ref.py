from flask import Flask, request, jsonify
app = Flask(__name__)
import random
seq = [random.choice(list('ACTG')) for x in range(10000)]


@app.route('/RegionFeatureDensities/chrA')
def rfd_chra():
    data = {
        "bins":  [
            51, 50, 58, 63, 57, 57, 65, 66, 63, 61,
            56, 49, 50, 47, 39, 38, 54, 41, 50, 71,
            61, 44, 64, 60, 42
        ],
        "stats": {
            "basesPerBin": 200,
            "max": 88
        }
    }
    return jsonify(**data)

@app.route('/stats/global')
def stats_global():
    data = {
        "featureDensity": 0.02,
        "featureCount": 234235,
        "scoreMin": 87,
        "scoreMax": 87,
        "scoreMean": 42,
        "scoreStdDev": 2.1,
    }
    return jsonify(**data)

@app.route('/features/chrA')
def feats():
    if request.args.get('sequence') == 'true':
        start = int(request.args.get('start'))
        end = int(request.args.get('end'))

        data = {
            'features':[
                {
                    "seq": ''.join(seq[start:end]),
                    "start": start,
                    "end": end
                },
            ]
        }

    else:
        data = {
            "features": [
                {
                    "type": "gene", "start": 5975, "end": 9744, "score": 0.84, "strand": 1,
                    "name": "au9.g1002",
                    "uniqueID": "blargh",
                    "subfeatures": [
                        {
                            "type": "mRNA", "start": 5975, "end": 9744, "score": 0.84, "strand": 1,
                            "name": "au9.g1002.t1", "uniqueID": "globallyUniqueString3",
                            "subfeatures": [
                                { "type": "five_prime_UTR", "start": 5975, "end": 6109, "score": 0.98, "strand": 1 },
                                { "type": "start_codon", "start": 6110, "end": 6112, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 6110, "end": 6148, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 6615, "end": 6683, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 6758, "end": 7040, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 7142, "end": 7319, "score": 1, "strand": 1, "phase": 2 },
                                { "type": "CDS",         "start": 7411, "end": 7687, "score": 1, "strand": 1, "phase": 1 },
                                { "type": "CDS",         "start": 7748, "end": 7850, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 7953, "end": 8098, "score": 1, "strand": 1, "phase": 2 },
                                { "type": "CDS",         "start": 8166, "end": 8320, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 8419, "end": 8614, "score": 1, "strand": 1, "phase": 1 },
                                { "type": "CDS",         "start": 8708, "end": 8811, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 8927, "end": 9239, "score": 1, "strand": 1, "phase": 1 },
                                { "type": "CDS",         "start": 9414, "end": 9494, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "stop_codon",  "start": 9492, "end": 9494,             "strand": 1, "phase": 0 },
                                { "type": "three_prime_UTR", "start": 9495, "end": 9744, "score": 0.86, "strand": 1 }
                            ]
                        },
                        {
                            "type": "mRNA", "start": 5975, "end": 9744, "score": 0.84, "strand": 1,
                            "name": "au9.g1002.t2", "uniqueID": "globallyUniqueString4",
                            "subfeatures": [
                                { "type": "five_prime_UTR", "start": 5975, "end": 6109, "score": 0.98, "strand": 1 },
                                { "type": "start_codon", "start": 6110, "end": 6112, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 6110, "end": 6148, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 6615, "end": 6683, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 6758, "end": 7040, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 8166, "end": 8320, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 8419, "end": 8614, "score": 1, "strand": 1, "phase": 1 },
                                { "type": "CDS",         "start": 8708, "end": 8811, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "CDS",         "start": 8927, "end": 9239, "score": 1, "strand": 1, "phase": 1 },
                                { "type": "CDS",         "start": 9414, "end": 9494, "score": 1, "strand": 1, "phase": 0 },
                                { "type": "stop_codon",  "start": 9492, "end": 9494,             "strand": 1, "phase": 0 },
                                { "type": "three_prime_UTR", "start": 9495, "end": 9744, "score": 0.86, "strand": 1 }
                            ]
                        }
                    ]
                }
            ]
        }
    return jsonify(**data)

@app.route("/")
def hello():
    return "Hello World!"

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    return response

if __name__ == "__main__":
    app.run(debug=True)
