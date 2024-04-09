Python Data Processing Project: Banking and Insurance Scenario
==============================================================

Objective
---------

Develop a Python program to automate data processing for banking and insurance scenarios, demonstrating AI's ability to assist in coding by extracting and transforming data from a CSV file, identifying potential targets for insurance offers based on loan data, and exporting the results to an Excel file.

### Project Outline

1.  **The CSV File: `customer_loan_data.csv`**
    
    *   Contains mock data for banking customers with columns: `CustomerID`, `Name`, `LoanAmount`, `LoanType`, `InterestRate`, `LoanDuration`, `InsuranceOptIn`.
2.  **Program Objective:**
    
    *   Read the CSV, analyze loan data to identify insurance offer targets, and export results to an Excel file.

### Detailed Instructions

#### Step 1: Initialize Project Structure

*   **Open VSC Code** and clone this repo to a new directory for your project.
*   **Create branch** create a new branch with a creative name representing your group.
*   **Activate GitHub Copilot** by signing in to your GitHub account within VSC Code. Ensure you have a GitHub Copilot trial subscription.
*   **Open the GitHub Copilot's chat function** and request a basic Python project structure including directories for your source code (`src`), tests (`tests`), and a `requirements.txt` file for dependencies.

#### Step 2: Environment Setup

*   Open a terminal in VSC Code within your project directory.
*   Create a virtual environment: `python3 -m venv venv`.
*   Activate the virtual environment:
    *   On Windows, use `.\venv\Scripts\activate`.
    *   On Unix or MacOS, use `source venv/bin/activate`.
*   Install necessary packages: `pip install pandas openpyxl`.

#### Step 3: Script Creation (`process_loans.py`)

*   **Function Definitions:**
    
    1.  `load_csv_data(filepath)`: Loads CSV data into a DataFrame.
        
    2.  `calculate_total_loan_cost(df)`: Adds a `TotalLoanCost` column to the DataFrame.
        
    3.  `identify_insurance_targets(df, interest_rate_threshold, loan_duration_threshold)`: Adds an `InsuranceOffer` boolean column based on defined thresholds.
        
    4.  `export_to_excel(df, filepath)`: Exports the DataFrame to an Excel file named `customer_insurance_offers.xlsx`.
        
*   **Insurance Offer Criteria:** Interest rate > 5%, Loan duration > 10 years.
    

#### Step 4: Testing

*   Write unit tests for each function using `pytest`, emphasizing Test-Driven Development (TDD).

#### Step 5: GitHub and VSC Code

*   Use VSC Code for version control and GitHub to commit and share the project.

### Encouragement for Creativity

*   Explore different coding strategies and data transformations.
*   Refine the task with additional criteria for insurance offers or complex data transformations.

### Final Sharing

*   Commit your project to GitHub and share it with colleagues.
