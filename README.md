Ontology Lookup Tool

The Ontology Lookup Tool is a web application built with Flask that allows users to search for ontology information using ontology IDs. It leverages the European Bioinformatics Institute (EBI) Ontology Lookup Service (OLS) API to retrieve details about specified ontologies.
Features:

    Search by Ontology ID: Users can input an ontology ID into the search field and retrieve detailed information about the ontology.
    Output Formats: Users can choose between human-readable and machine-readable formats for displaying ontology information.
    Error Handling: The application handles errors gracefully, providing user-friendly error messages when necessary.

Prerequisites

Before running this application, ensure you have the following prerequisites installed:

    Python (3.11.5 recommended)
    Flask
    Requests library (pip install requests)

Setup and Usage

    Clone the Repository:

    bash

    git clone <repository_url>
    cd into repository

Install Dependencies:

    bash

    pip install -r requirements.txt

Run the Application:

    bash

    python app.py

    The Flask application will start running locally on http://127.0.0.1:5000/.

    Access the Application:

    Open a web browser and navigate to http://127.0.0.1:5000/ to access the Ontology Lookup Tool.

Usage:
    
Enter an ontology ID into the search field.
Choose the desired output format (human-readable or machine-readable).
Click the "Submit" button to retrieve ontology information.
View the detailed ontology information on the results page.

Additional Notes:

This application relies on the EBI OLS API for ontology data. Ensure you have a stable internet connection to fetch ontology details.
Handle errors gracefully and provide meaningful error messages to the users for a better user experience.