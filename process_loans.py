import pandas as pd

def load_csv_data(filepath):
    df = pd.read_csv(filepath)
    return df


def calculate_total_loan_cost(df):
    df['TotalLoanCost'] = df['LoanAmount'] + (df['LoanAmount'] * df['InterestRate'] * df['LoanDuration'])
    return df


def identify_insurance_targets(df, interest_rate_threshold, loan_duration_threshold):
    # Create a new column for InsuranceOffer
    df['InsuranceOffer'] = False
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        interest_rate = row['InterestRate']
        loan_duration = row['LoanDuration']
        # Check if interest rate and loan duration meet the thresholds
        if interest_rate >= interest_rate_threshold and loan_duration >= loan_duration_threshold:
            df.at[index, 'InsuranceOffer'] = True
    return df


def export_to_excel(df, filepath):
    df.to_excel(filepath, index=False)



def main():
    # Load the data
    filepath = 'data/input/customer_loan_data.csv'
    df = load_csv_data(filepath)

    # Calculate total loan cost
    df = calculate_total_loan_cost(df)

    # Identify insurance targets
    interest_rate_threshold = 0.05  # 5%
    loan_duration_threshold = 5  # 10 years
    df = identify_insurance_targets(df, interest_rate_threshold, loan_duration_threshold)

    # Export the DataFrame to an Excel file
    output_filepath = 'data/output/processed_loan_data.xlsx'
    export_to_excel(df, output_filepath)

if __name__ == "__main__":
    main()