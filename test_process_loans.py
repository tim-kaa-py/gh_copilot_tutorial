import pandas as pd
import pytest
from process_loans import calculate_total_loan_cost

def test_calculate_total_loan_cost():
    """
    Test the function calculate_total_loan_cost to ensure it correctly calculates the total loan cost and adds it as a new column.
    """
    # Create a sample DataFrame with loan details
    df = pd.DataFrame({
        'LoanAmount': [1000, 2000, 3000],
        'InterestRate': [0.05, 0.1, 0.15],
        'LoanDuration': [12, 24, 36]
    })

    # Use the function to calculate the total loan cost and add it to the DataFrame
    df_with_total_cost = calculate_total_loan_cost(df)

    # Assert that the 'TotalLoanCost' column has been added to the DataFrame
    assert 'TotalLoanCost' in df_with_total_cost.columns, "TotalLoanCost column not found in the DataFrame."

    # Assert that the calculated total loan cost values are correct
    expected_values = [1600, 6800, 19200]
    assert df_with_total_cost['TotalLoanCost'].tolist() == expected_values, f"Expected values were {expected_values}, but got {df_with_total_cost['TotalLoanCost'].tolist()} instead."

# This test can be run using pytest by executing the command `pytest test_process_loans.py` in the terminal.