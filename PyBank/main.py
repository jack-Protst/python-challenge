# Modules
import csv
# Prompt user for title lookup

# Set path for file
csvpath = r"PyBank\Resources\budget_data.csv"

# Initialize variables to store analysis results
total_months = 0
net_total = 0
previous_profit = 0
changes = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        # Extract date and profit/loss from the row
        date = row[0]
        profit = int(row[1])

        # Calculate total number of months
        total_months += 1

        # Calculate net total amount of profit/loss
        net_total += profit

        # Calculate change in profit/loss
        change = profit - previous_profit

        # Update greatest increase in profits
        if change > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change

        # Update greatest decrease in profits
        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change

        # Update previous profit for the next iteration
        previous_profit = profit

        # Save the change in the list
        changes.append(change)

# Calculate average change in profit
average_change = sum(changes)/len(changes)

# Display the analysis results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Define the path to the text file
output_file_path = r"PyBank\analysis\financial_analysis.txt"

# Save the results to the text file
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

print(f"\nResults saved to {output_file_path}")