#!/usr/bin/python
import pandas as pd
from bs4 import BeautifulSoup
import argparse

# Function to extract table data and save to CSV
def extract_table_to_csv(html_file_path, output_csv_path):
    # Read the HTML content from the file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract table header
    headers = ["Title", "CRN", "Subject", "Course Number", "Section", "Credit Units", "Campus", "Meeting Times", "Instructor", "Availability", "Reserved Seats", "Schedule Type", "Attribute", "Linked Sections"]

    # Extract table rows
    rows = soup.find_all('tr')

    # Prepare data for DataFrame
    data = []

    for row in rows:
        row_data = []
        for header in headers:
            cell = row.find('td', {'data-content': header})
            if cell:
                row_data.append(cell.get_text(strip=True))
            else:
                row_data.append('')  # If the cell is missing, append an empty string
        data.append(row_data)

    # Create a DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Save DataFrame to CSV
    df.to_csv(output_csv_path, index=False)
    print(f"Data has been successfully extracted to '{output_csv_path}'")

# Main function to parse arguments and call the extraction function
def main():
    parser = argparse.ArgumentParser(description='Extract table data from HTML file to CSV')
    parser.add_argument('html_file', help='Path to the HTML file')
    parser.add_argument('csv_file', help='Path to the output CSV file')

    args = parser.parse_args()

    extract_table_to_csv(args.html_file, args.csv_file)

if __name__ == '__main__':
    main()

