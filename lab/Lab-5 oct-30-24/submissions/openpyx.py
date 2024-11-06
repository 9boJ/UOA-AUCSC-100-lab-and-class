from openpyxl import load_workbook 
workbook = load_workbook("Monthly_Expenses.xlsx") 
sheet = workbook.active  # Access the first sheet

"""Exercise 1: Write a  script that loads Monthly_Expenses.xlsx, and reads and prints out all item names and amounts."""

items = sheet["A"] # Grabs all the Items in row A

amounts = sheet["D"] # Grabs all the Amounts in row D

listcell = ['D0','D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13','D14','D15','D16'] 

for i in range(2,len(items)+1): # Loop through rows, starting from the second row
    print(sheet["A"+str(i)].value,":$",sheet[listcell[i]].value) # Print item name and amount
            
"""Exercise 2: Add a new column titled "Discounted Price" where each value is 90% of the original price in the Amount column."""

sheet["E1"].value = "Discounted Price" # Set header for the new column in cell E1

listcellE = ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16']

for i in range(2,len(items)+1): # Loop through each amount, calculate 90% of the original price, and write to column E
    DiscountedPrice = sheet[listcell[i]].value - sheet[listcell[i]].value*0.90 # Get the Discounted amount
    sheet[listcellE[i]].value = "$" + str(DiscountedPrice) # Write discounted price to column E

"""Exercise 3: Calculate the monthly total of all expenses and write the result in the cell below the last expense in the Amount column."""

sheet["A17"].value = "Total" # Set label "Total" in the first column after the last item

total = 0 # Sets the total value to 0

for i in range(2,len(items)+1):
    total = total + sheet[listcell[i]].value # Sum all values in the Amount column (D) from the second row to the last row with an expense
    
sheet["D17"].value = "$" + str(total)  # Write the total amount in the Amounts column

workbook.save("Monthly_Expenses.xlsx") # Save the changes to "Monthly_Expenses.xlsx"