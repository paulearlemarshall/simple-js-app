# Business Process Analyzer Web App

This web application allows users to input a company name and a number 'N'. It then (currently, via a mock service) identifies the top N business processes for that company, associated Key Performance Indicators (KPIs) for each process, and the potential beneficial impact of intelligent automation on those KPIs.

## Features

- User-friendly web interface to input company name and number of processes.
- Displays structured results showing business processes, KPIs, and automation impacts.
- Basic input validation.

## Setup and Installation

1.  **Prerequisites:**
    *   Python 3.7+

2.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4.  **Install dependencies:**
    The application requires Flask. These can be installed using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Start the Flask development server:**
    ```bash
    python app.py
    ```

2.  **Access the application:**
    Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

-   `app.py`: The main Flask application file containing the backend logic and routes.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `templates/`: Contains HTML templates.
    -   `index.html`: The main page with the input form.
    -   `results.html`: The page to display the analysis results.
-   `static/`: (Currently unused) Intended for static files like CSS or JavaScript.
-   `README.md`: This file.

## Note on LLM Integration

The current version of this application uses a **mock LLM response** for demonstration purposes. The `query_llm` function in `app.py` simulates the behavior of an LLM call.

To integrate a real Large Language Model (LLM):
- You would need to replace the mock implementation in the `query_llm` function with actual API calls to your chosen LLM provider.
- Ensure you handle API keys and potential errors from the LLM API appropriately.
