import pandas as pd
import pytest

from process_loans import calculate_total_loan_cost

def test_calculate_total_loan_cost():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'LoanAmount': [1000, 2000, 3000],
        'InterestRate': [0.05, 0.1, 0.15],
        'LoanDuration': [12, 24, 36]
    })

    # Calculate the total loan cost
    df_with_total_cost = calculate_total_loan_cost(df)

    # Check if the 'TotalLoanCost' column is added correctly
    assert 'TotalLoanCost' in df_with_total_cost.columns

    # Check the calculated total loan cost values
    assert df_with_total_cost['TotalLoanCost'].tolist() == [1600, 6800, 19200]

# Run the test using pytest
