import glob
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define input and output folders
summary_folder = "summary"
report_folder = "reports-docs"
os.makedirs(report_folder, exist_ok=True)

def generate_graphs(file_path):
    df = pd.read_csv(file_path)
    school_file_name = os.path.basename(file_path).replace("_summary.csv", "")

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

    def categorize_performance(row, categories):
        for category, levels in categories.items():
            if row in levels:
                return category

    df['Literacy Performance'] = df['Literacy Level'].apply(lambda x: categorize_performance(x, literacy_categories))
    df['Numeracy Performance'] = df['Numeracy Level'].apply(lambda x: categorize_performance(x, numeracy_categories))

    # Count occurrences of each category per grade
    literacy_counts = df.groupby(['Grade', 'Literacy Performance']).size().unstack(fill_value=0)
    numeracy_counts = df.groupby(['Grade', 'Numeracy Performance']).size().unstack(fill_value=0)

    # Plot literacy graph with separate bars for each category
    fig, ax = plt.subplots(figsize=(8, 5))
    literacy_counts.plot(kind='bar', ax=ax, width=0.8)

    ax.set_title('Literacy Performance by Grade')
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')

    plt.xticks(rotation=0)
    plt.legend(title='Literacy Performance')
    plt.tight_layout()

    plt.savefig(os.path.join(report_folder, f"{school_file_name}_literacy_graph.png"))

    # Plot numeracy graph with separate bars for each category
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    numeracy_counts.plot(kind='bar', ax=ax1, width=0.8)

    ax1.set_title('Numeracy Performance by Grade')
    ax1.set_xlabel('Grade')
    ax1.set_ylabel('Number of Students')

    plt.xticks(rotation=0)
    plt.legend(title='Numeracy Performance')
    plt.tight_layout()

    plt.savefig(os.path.join(report_folder, f"{school_file_name}_numeracy_graph.png"))

summary_files = glob.glob(os.path.join(summary_folder, "*.csv"))
if not summary_files:
    print("❌ No summary files found in the 'summary' folder.")
else:
    for file in summary_files:
        generate_graphs(file)