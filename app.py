from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def query_llm(company_name, num_processes):
    """
    Simulates a call to an LLM.
    Returns a list of dictionaries, where each dictionary represents a business process.
    """
    processes = []
    for i in range(num_processes):
        process = {
            'process_name': f'Process {i+1} for {company_name}',
            'kpis': [
                {
                    'kpi_name': f'KPI A for Process {i+1}',
                    'automation_impact': 'Significant improvement in efficiency by automating data entry.'
                },
                {
                    'kpi_name': f'KPI B for Process {i+1}',
                    'automation_impact': 'Reduced error rates through automated validation.'
                }
            ]
        }
        processes.append(process)
    return processes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form.get('company_name')
        num_processes_str = request.form.get('num_processes')

        if not company_name:
            flash("Company name cannot be empty.")
            return redirect(url_for('index'))

        try:
            num_processes = int(num_processes_str)
            if num_processes < 1:
                flash("Number of processes must be a positive integer.")
                return redirect(url_for('index'))
        except ValueError:
            flash("Number of processes must be a positive integer.")
            return redirect(url_for('index'))

        llm_response = query_llm(company_name, num_processes)
        return render_template('results.html', data=llm_response, company_name=company_name)
    else: # GET request
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
