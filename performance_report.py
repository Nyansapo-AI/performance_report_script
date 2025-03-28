import glob
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define input and output folders
summary_folder = "summary"
report_folder = "reports-docs"

def generate_performance_graph(file_path, output_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Define performance categories
    literacy_categories = {
        "Below Expectations": ["Beginner (Lit)"],
        "Approaching Expectations": ["Letter", "Word"],
        "Meets Expectations": ["Paragraph"],
        "Above Expectations": ["Story", "Above (Lit)"]
    }
    numeracy_categories = {
        "Below Expectations": ["Beginner (Num)", "Count"],
        "Approaching Expectations": ["Number Rec.", "Addition"],
        "Meets Expectations": ["Subtraction", "Multiplication"],
        "Above Expectations": ["Division", "Above (Num)"]
    }

    # Function to categorize performance
    def categorize_performance(row, categories):
        for category, levels in categories.items():
            if row in levels:
                return category
        # return "Unspecified"

    # Apply categorization
    df['Literacy Performance'] = df['Literacy Level'].apply(lambda x: categorize_performance(x, literacy_categories))
    df['Numeracy Performance'] = df['Numeracy Level'].apply(lambda x: categorize_performance(x, numeracy_categories))

    # Filter out 'Unspecified' categories
    df = df[df['Literacy Performance'] != 'Unspecified']
    df = df[df['Numeracy Performance'] != 'Unspecified']

    # Group by grade and performance
    literacy_counts = df.groupby(['Grade', 'Literacy Performance']).size().unstack(fill_value=0)
    numeracy_counts = df.groupby(['Grade', 'Numeracy Performance']).size().unstack(fill_value=0)

    # Plot the graphs
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

    # Literacy Performance Graph
    literacy_counts.plot(kind='bar', stacked=True, ax=axes[0])
    axes[0].set_title('Literacy Performance by Grade')
    axes[0].set_xlabel('Grade')
    axes[0].set_ylabel('Number of Students')

    # Numeracy Performance Graph
    numeracy_counts.plot(kind='bar', stacked=True, ax=axes[1])
    axes[1].set_title('Numeracy Performance by Grade')
    axes[1].set_xlabel('Grade')
    axes[1].set_ylabel('Number of Students')

    # Save and show the plot
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()


summary_files = glob.glob(os.path.join(summary_folder, "*.csv"))
if not summary_files:
    print("❌ No summary files found in the 'summary' folder.")
else:
    for file in summary_files:
        school_name = os.path.basename(file).replace("_summary.csv", "")
        output_file = os.path.join(report_folder, os.path.basename(file).replace('_summary.csv', '_graph.png'))
        generate_performance_graph(file_path=file, output_path=output_file)
