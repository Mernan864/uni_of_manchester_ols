from flask import Flask, render_template, request, jsonify, abort
import requests

app = Flask(__name__, static_url_path='/static')

class OntologyLookupService:
    def __init__(self):
        self.base_url = "https://www.ebi.ac.uk/ols/api/ontologies/"

    def lowercase_after_first(self, s):
        return s[0].upper() + s[1:].lower()

    def fetch_ontology_details(self, ontology_id):
        url = f"{self.base_url}{ontology_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def get_ontology_info(self, ontology_id):
        ontology_data = self.fetch_ontology_details(ontology_id)

        if ontology_data:
            title = ontology_data.get('config', {}).get('title')
            description = ontology_data.get('config', {}).get('description')
            num_terms = ontology_data.get('numberOfTerms')
            status = ontology_data.get('status')

            return {
                "title": title,
                "description": description,
                "num_terms": num_terms,
                "status": self.lowercase_after_first(status)
            }
        else:
            return None
            
@app.route('/ontology/<ontology_id>', methods=['GET'])
def ontology_details(ontology_id):
    ols = OntologyLookupService()
    ontology_info = ols.get_ontology_info(ontology_id)

    if ontology_info:
        return jsonify(ontology_info)
    else:
        abort(404, description="Ontology ID not recognized or service unavailable.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ontology_id = request.form['ontology_id']
        output_format = request.form.get('output_format', 'human-readable')

        if not ontology_id:
            abort(400, description="Ontology ID is required.")
        
        ols = OntologyLookupService()
        ontology_info = ols.get_ontology_info(ontology_id)

        if ontology_info:
            if output_format == "human-readable":
                return render_template('ontology_info.html', ontology_info=ontology_info)
            elif output_format == "machine-readable":
                return jsonify(ontology_info)
            else:
                abort(400, description="Invalid output format specified.")
        else:
            abort(400, description="Ontology ID not recognized or service unavailable.")

    return render_template('index.html')

@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html', error=e.description), 400

if __name__ == '__main__':
    app.run(debug=True)
