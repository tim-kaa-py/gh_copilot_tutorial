GitHub Copilot Hands-On Tutorial
==============================================================

*   **Objective**: Learn to use GitHub Copilot in your projects with a simple Python example. You will write it regardless of whether you have experience with Python or not. Address all your questions to GitHub Copilot. Try to rely solely on the windows of your Integrated Development Environment (IDE).

*   **Prequisites**:
    * IDE with GitHub Copilot (recommended: `Mircosoft VSC Code`)
    * Github Copilot subscription
    * Familiarize yourself with the functionality of GitHub Copilot by watching the following [5 minute introduction video](https://www.youtube.com/watch?v=jXp5D5ZnxGM)

*   **How to use this repository?**
    * Simply follow the instructions below and code
    * If you got trouble check out the branch `tim_solution` which contains an example solution including a file `prompts.txt` in the home directory showing all the prompts I used to generate the code
    * Don't forget to create your own branch, because you can **not** commit into the main branch 


Programming task: Python Data Processing Project
---------

Develop a Python program to automate data processing for a bank by extracting and transforming data from a CSV file, identifying potential targets for insurance offers based on loan data, and exporting the results to an Excel file. **Insurance Offer Criteria:** Interest rate > 5%, Loan duration > 5 years.

### Input file

*  **The CSV File `customer_loan_data.csv`:** Contains mock data for banking customers with columns: `CustomerID`, `Name`, `LoanAmount`, `LoanType`, `InterestRate`, `LoanDuration`, `InsuranceOptIn`.

### Detailed Instructions

#### Step 1: Initialize Project Structure

*   **Open VSC Code** and clone this repo to a new directory for your project
*   **Create a new branch**  with a creative name representing your group
*   **Activate GitHub Copilot** by signing in to your GitHub account within VSC Code
*   **Open the GitHub Copilot's chat function** and request  a complete standard Python project structure for a python code without any modules. The main file is called `process_loans.py`. The customer data is saved in a file `customer_loan_data.csv` in the folder data/input. The output is called `processed_loan_data.xlsx`.
+   **Generate suggested folders and files**, if you need help address your questions to the chat window 

#### Step 2: Environment Setup

*   Find out how to create a virtual python environment called: `gh_copilot`
*   And associate it with your project
*   And finally find out  how to install necessary packages: which may be `pandas` and `openpyxl`

#### Step 3: Script Creation (`process_loans.py`)

*   Use copilot to genereate the following functions
*   *Hint:* Start with the inline chat and if you are not happy with the reuslts highligh te produced code and use the chat window to refine it

*   **Function Definitions:**
    
    1.  `load_csv_data(filepath)`: Loads CSV data into a DataFrame
        
    2.  `calculate_total_loan_cost(df)`: Adds a `TotalLoanCost` column to the DataFrame
        
    3.  `identify_insurance_targets(df, interest_rate_threshold, loan_duration_threshold)`: Adds an `InsuranceOffer` boolean column based on defined thresholds, should be true if: `InterestRate` > `interest_rate_threshold`and `LoanDuration` > `loan_duration_threshold5 years` (**Insurance Offer Criteria**)
        
    4.  `export_to_excel(df, filepath)`: Exports the DataFrame to an Excel file named `customer_insurance_offers.xlsx`

    5.  `main()`: Function where you call all functions above
        

#### Step 4: Run the code

*   If you get errors debug the code by copying error messages to the chat window. If you know which code lines are the issue highlight them in the editor, if not highlight everything (to give it as context to the Chat Window)


#### Optional Step 5: Testing

*  Use the Copilot feature `Generate Tests` to create a test for `calculate_total_loan_cost(df)`
*  For that right click on the function then, select `Copilot` and `Generate Tests`
*  Check how you should run the created test file, using the chat window
*  If tests fail verify if the suggested results are corrcect! Ask Copilot for help but it will probably refuse to help x.X

#### Optional Step 6: Debugging

*  Finally, we want to highlight the header row of our Excel File in yellow.
*  Copy the following function and call it last in your main(). Then try to run it, you will encounter 2-3 issues.
*  Copy the terminal errors to the Chat window with the function `format_excel_header` highlighted in the editor to debug the errors
*  *Hint:* inspect the Excel file to check if the code does what you expect

```python
def format_excel_header(filepath):
    # Load the Excel file into an openpyxl workbook
    workbook = openpyxl.load_file(filepath)
    sheet = workbook.active
    
    # Apply yellow fill to the header row
    yellow_fill = openpyxl.styles.PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
    
    for cell in sheet["2:2"]:
        cell.fill = yellow_fill
    
    # Save the changes to the file
    workbook.save(filepath)
```

#### Step 7: Final Steps
*   Highlight all code in each source file (main script and possibly testing script) you generated and ask Copilot to reformat and comment the code in a professional manner
*   *Hint:* in our example we can do it for the complete code, in more complex projects you may have to do it in multiple steps because the context window (the length of the text that can be processed at once) is limited
*   If you haven't already genereate a `requirements.txt` file listing the python packages you used

#### Step 8: GitHub and VSC Code

*   Use VSC Code for version control and GitHub to commit and share the project



#### Step 9: Wow, still got time?

*   Wanna see how bug fixing and even programming will work in the near future? Watch this [20 minute](https://www.youtube.com/watch?v=RJ6NN8Y-xok) video showing how the open-source [SWE agent](https://swe-agent.com) solves bugs all by itself.
