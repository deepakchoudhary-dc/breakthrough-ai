
# Dynamic Data Processor with Intelligent Query Resolution

This project is a Flask-based application that allows users to dynamically process data from CSV files or Google Sheets, retrieve web-based contextual information, and extract structured insights using Large Language Models (LLMs). With a user-friendly web dashboard, it automates the workflow of information retrieval and data enrichment.

### Key Features
- **Dynamic File Upload**: Upload and preview CSV files or connect to Google Sheets.
- **Custom Queries**: Define intelligent query templates tailored to your dataset.
- **Web Search Integration**: Automate data enrichment using web search APIs.
- **LLM-Powered Insights**: Extract meaningful information from web search results.
- **Structured Output**: Save results as JSON or CSV for further analysis.

  
2. Setup Instructions

### Setup Instructions

1. **Clone the Repository**:
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
  
2. **Create a Virtual Environment:**
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. **Install Dependencies:**
pip install -r requirements.txt
Set Up Environment Variables:

4. **Create a .env file in the root directory.**
Add API keys and credentials (see the "API Keys and Environment Variables" section below).

5. **Run the Application:**
python -m flask run
Access the app in browser at http://127.0.0.1:5000/.


#### 3. Usage Guide
### Usage Guide

1. **Upload a CSV File**:
   - On the dashboard, click "Upload CSV File" and select your file.
   - Preview the uploaded data and select a column to use for query processing.

2. **Connect to Google Sheets** (Optional):
   - Enter the Google Sheet ID and connect using the provided form.
   - Preview the loaded data in JSON format.

3. **Set Up a Query Template**:
   - Enter a query template (e.g., `Find the contact email for {company}`) where `{company}` dynamically replaces entities from the selected column.

4. **Run Query Processing**:
   - Submit the query form to initiate web searches and extract information.
   - View structured JSON results for each entity.

5. **Download Results**:
   - Save the extracted results as a CSV or update the connected Google Sheet.

     
4. **API Keys and Environment Variables**

### API Keys and Environment Variables

The application requires the following API keys and credentials:

1. **SerpAPI**: For web search functionality.
   - Sign up at [SerpAPI](https://serpapi.com/) and obtain your API key.
   - Add it to your `.env` file:
     ```
     SERPAPI_KEY=your-serpapi-key
     ```

2. **OpenAI**: For LLM-powered information extraction.
   - Sign up at [OpenAI](https://platform.openai.com/) and obtain your API key.
   - Add it to your `.env` file:
     ```
     OPENAI_API_KEY=your-openai-key
     ```

3. **Google Sheets API**: For Google Sheets integration.
   - Enable the Google Sheets API in Google Cloud Console.
   - Download the service account JSON file and save it in your project directory.
   - Update your `.env` file:
     ```
     GOOGLE_SERVICE_ACCOUNT_FILE=path-to-your-service-account.json
     ```

**Note**: Do not share your `.env` file publicly. Use `.gitignore` to exclude it from version control.


5. **Optional Features**:
### Optional Features

- **Google Sheets Output**: Update Google Sheets with the extracted information.
- **Error Handling**: Graceful fallback for missing or incomplete web search results.
- **Customizable Prompts**: Tailor query templates to suit specific datasets.


**Publishing Steps**
**Push to GitHub:**

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-repository.git
git push -u origin main
Add the Loom Video:


git tag v1.0
git push origin v1.0
Example Test Case
Run the application with:

python -m flask run
Upload a CSV File:

Use a sample file like:
csv

Company,Industry
Google,Technology
Microsoft,Software
Amazon,E-commerce
Set a Query Template:

Input:
plaintext

Find the contact email for {Company}.
Submit and View Results:

The app will perform searches and return structured JSON output with the extracted emails.
Download the Results:

Save the results as a CSV or update your Google Sheet.
This structure ensures your repository is well-documented, easy to set up, and appealing to potential collaborators or users. Let me know if you need further assi
