Provience_table =filtered_df = df[df['province'] == 'Burgundy']

country_table = ['Argentina', 'Canada', 'South Africa', 'US', 'Chile', 'Peru', 'Australia', 'New Zealand', 'Brazil']

# Function to calculate statistics
def calculate_statistics(data, column_name):
    grouped_statistics = data.groupby('province')[column_name].describe()
    median_series = data.groupby('province')[column_name].median()

    grouped_statistics = grouped_statistics.reset_index()
    grouped_statistics['median'] = median_series.values

    grouped_statistics = grouped_statistics[[
        'province', 'count', 'mean', 'median', 'std', 'min', '25%', '50%', '75%', 'max']]
    
    # Print the grouped_statistics DataFrame to the console
    print(f"Statistics for {column_name}:\n")
    print(grouped_statistics)
    print('')
    return grouped_statistics
    
# Columns to process
columns_to_process = ['price','points']

# Initialize an empty DataFrame to store combined statistics
combined_statistics = None

# Loop through the columns and calculate statistics for each
for idx, column in enumerate(columns_to_process):
    statistics = calculate_statistics(Provience_table, column)
    
    if idx == 1:
        # Drop the 'Rater' column after the first output
        statistics = statistics.drop(columns=['province'])
    
    statistics.rename(columns={col: f'{column} {col}' for col in statistics.columns}, inplace=True)
    
    if combined_statistics is None:
        combined_statistics = statistics
    else:
        # Merge based on the index (no 'on' parameter) with a blank column separator
        combined_statistics = pd.concat([combined_statistics, pd.DataFrame(columns=['']), statistics], axis=1)

# Rename the first column from the 'columns_to_process' list to "Rater" after the final append
if combined_statistics is not None:
    combined_statistics.rename(columns={combined_statistics.columns.values[0]: 'province'}, inplace=True)

# Create an Excel writer object
output_file = current_directory + '/02-output/burgundy_stats/Q2D_Burgundy.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    combined_statistics.to_excel(writer, sheet_name='Combined Statistics', index=False)
    
    # Auto-adjust column width for the entire sheet
    worksheet = writer.sheets['Combined Statistics']
    for i, col in enumerate(combined_statistics.columns):
        max_len = max(combined_statistics[col].astype(str).str.len().max(), len(col))
        worksheet.set_column(i, i, max_len)  
    
    # Freeze the first column
    worksheet.freeze_panes(1, 1)
