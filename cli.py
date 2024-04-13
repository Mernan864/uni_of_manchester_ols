import requests

BASE_URL = "http://127.0.0.1:5000"  # Update this with your Flask app's URL

class OntologyLookupClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_ontology_info(self, ontology_id):
        url = f"{self.base_url}/ontology/{ontology_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

def main():
    client = OntologyLookupClient(BASE_URL)
    ontology_id = input("Enter Ontology ID: ")

    ontology_info = client.get_ontology_info(ontology_id)

    if ontology_info:
        print("Ontology Information:")
        print(f"Title: {ontology_info['title']}")
        print(f"Description: {ontology_info['description']}")
        print(f"Number of Terms: {ontology_info['num_terms']}")
        print(f"Status: {ontology_info['status']}")
    else:
        print("Error: Ontology ID not recognized or service unavailable.")

if __name__ == "__main__":
    main()
