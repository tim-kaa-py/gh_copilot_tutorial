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
*   **Open the GitHub Copilot's chat function** and request  a complete standard Python project structure for a python code without any modules. The main file is called `process_loans.py`. The customer data is saved in a file `customer_loan_data.csv` in the folder data/input. The output is called `processed_loan_data.xlsx`.
+   **Generate suggested folders and files**, if you need help address your questions to the chat window 

#### Step 2: Environment Setup

*   Find out how to create a virtual python environment called: `gh_copilot`.
*   and associate it with your project
*   and finally how to install necessary packages: which may be `pandas` and `openpyxl`.

#### Step 3: Script Creation (`process_loans.py`)

*   use copilot to genereate the following functions
*   Hint: Start with the inline chat and if you are not happy with the reuslts highligh te produced code and use the chat window to refine it

*   **Function Definitions:**
    
    1.  `load_csv_data(filepath)`: Loads CSV data into a DataFrame.
        
    2.  `calculate_total_loan_cost(df)`: Adds a `TotalLoanCost` column to the DataFrame.
        
    3.  `identify_insurance_targets(df, interest_rate_threshold, loan_duration_threshold)`: Adds an `InsuranceOffer` boolean column based on defined thresholds.
        
    4.  `export_to_excel(df, filepath)`: Exports the DataFrame to an Excel file named `customer_insurance_offers.xlsx`.
        
*   **Insurance Offer Criteria:** Interest rate > 5%, Loan duration > 5 years.

#### Step 4: Run the code

*   If you get errors debug the code copying error messages to the chat window. If you know which code lines are the issue highlight them in the editor

#### Optional Step 5: Testing

*  Use the Copilot feature `Generate Tests` to create a test for `calculate_total_loan_cost(df)` and `identify_insurance_targets(df, interest_rate_threshold, loan_duration_threshold)`
+   If tests fail verify if the suggested results are corrcect!

#### Optional Step 6: Plotting

*  Generate a plot for each person in the data showing how long from now it takes until their loan is paid back
*  Figure out yourself which packages to use and how many and what functions you need (ofc using the chat window :-D)
*  Save the plot as a PDF
*  Go the extra mile in the formatting and try to make the plot look beautiful

#### Step 7: GitHub and VSC Code

*   Use VSC Code for version control and GitHub to commit and share the project.
