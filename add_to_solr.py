import csv
import pysolr
import sys

# Read the input CSV file
input_csv = "../data/tsvOriginal/BFRO_final.csv"

json_docs = []
doc_id = 0

with open(input_csv, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        json_doc = {}
        # Add the phrase "This happens in the United States of America" to the text field
        text_content = "This happens in the United States of America. "
        # Concatenate the contents of multiple columns into the "text" field
        text_content += ' '.join([row[col] for col in ['Headline', 'State', 'County', 'Nearest Town', 'Location Details', 'Environment']])
        json_doc["text"] = text_content
        json_doc["id"] = str(doc_id)
        doc_id += 1
        json_docs.append(json_doc)

# Solr core name
core_name = 'BFROloc'

# Create a Solr client instance
solr = pysolr.Solr('http://localhost:8983/solr/' + core_name, always_commit=True, timeout=10)

# Add documents to Solr
solr.add(json_docs)

print("Data successfully added to Solr.")

