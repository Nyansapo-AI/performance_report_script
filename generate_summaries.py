import pandas as pd
import os
import glob

# Define input and output folders
input_folder = "data"
output_folder = "summary"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all CSV files in the data folder
csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

# Function to process a single file
def process_file(file_path):
    try:
        # Load CSV file
        df = pd.read_csv(file_path)

        # Clean the data by setting correct headers and removing metadata rows
        df_cleaned = df.iloc[3:].reset_index(drop=True)
        df_cleaned.columns = [
            "Index", "No", "Name", "Grade", "Gender",
            "Beginner (Lit)", "Letter", "Word", "Paragraph", "Story", "Above (Lit)",
            "Beginner (Num)", "Count", "Number Rec.", "Addition", "Subtraction", 
            "Multiplication", "Division", "Above (Num)", "Extra"
        ]

        # Drop unnecessary columns
        df_cleaned = df_cleaned.drop(columns=["Index", "No", "Extra"])

        # Standardize Gender Column
        df_cleaned["Gender"] = df_cleaned["Gender"].map({"M": "Male", "F": "Female"}).fillna("Unspecified")

        # Convert assessment columns to numeric values
        assessment_columns = df_cleaned.columns[3:]
        df_cleaned[assessment_columns] = df_cleaned[assessment_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

        # Function to extract a child's literacy and numeracy level
        def get_level(row, categories):
            for category in categories:
                if row[category] == 1:
                    return category
            return "Unspecified"

        # Define categories
        literacy_categories = ["Beginner (Lit)", "Letter", "Word", "Paragraph", "Story", "Above (Lit)"]
        numeracy_categories = ["Beginner (Num)", "Count", "Number Rec.", "Addition", "Subtraction", "Multiplication", "Division", "Above (Num)"]

        # Apply function to extract levels
        df_cleaned["Literacy Level"] = df_cleaned.apply(lambda row: get_level(row, literacy_categories), axis=1)
        df_cleaned["Numeracy Level"] = df_cleaned.apply(lambda row: get_level(row, numeracy_categories), axis=1)

        # Select relevant columns for the summary
        summary_df = df_cleaned[["Name", "Grade", "Gender", "Literacy Level", "Numeracy Level"]]

        # Generate summary filename
        base_name = os.path.basename(file_path).replace(".csv", "")
        summary_file_path = os.path.join(output_folder, f"{base_name}_summary.csv")

        # Save summary to CSV
        summary_df.to_csv(summary_file_path, index=False)
        print(f"✅ Summary saved: {summary_file_path}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

# Process all CSV files found
if not csv_files:
    print("❌ No CSV files found in the 'data' folder.")
else:
    for file in csv_files:
        process_file(file)
