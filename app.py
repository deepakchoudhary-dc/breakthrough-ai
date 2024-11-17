from flask import Flask, render_template, request, jsonify
from modules.data_loader import load_csv_data, load_google_sheet_data
from modules.query_generator import generate_query
from modules.web_search import perform_search
from modules.llm_processor import extract_information
from modules.data_output import save_to_csv, update_google_sheet

app = Flask(__name__)

# Route for the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle CSV file upload
@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    csv_file = request.files['csv_file']
    if csv_file:
        data = load_csv_data(csv_file)  # Assuming load_csv_data is modified to accept file objects
        return jsonify(data=data.head().to_dict()), 200
    return jsonify({"error": "No file uploaded"}), 400

# Route to handle Google Sheets connection
@app.route('/connect_google_sheet', methods=['POST'])
def connect_google_sheet():
    sheet_id = request.form['sheet_id']
    data = load_google_sheet_data(sheet_id, 'Sheet1!A1:Z10')  # Example range
    return jsonify(data=data), 200

# Route to handle query processing
@app.route('/process_query', methods=['POST'])
def process_query():
    template = request.form['query_template']
    entities = ['Google', 'Microsoft']  # Example entities, replace with dynamic data as needed
    results = []
    for entity in entities:
        query = generate_query(template, entity)
        search_results = perform_search(query)
        extracted_info = extract_information(search_results, entity, template)
        results.append({entity: extracted_info})
    return jsonify(results=results), 200

if __name__ == '__main__':
    app.run(debug=True)
