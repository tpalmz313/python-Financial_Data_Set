import csv 
from pathlib import Path

filepath = Path("/Users/thomaspalmisano/Desktop/FinTech_ASU/Python_HW/python-Financial_Data_Set/PyBank/budget_data.csv")
#filepath
#with open(filepath, 'r') as text_File:
 #   content_file = text_File.read()
    
#Define all variables 

total = 0
tot_change = 0
change = 0 
count = 0
curr_month = 0
prev_month = 0
great_loss = 0
great_prof = 0
m_date = ' '
great_loss_date = ' '
greate_prof_date = ' '
write_file = 'PyBankDataPull.csv'
text_file = 'Financial Analysis'

#reading the csv file
with open(filepath, 'r') as text_File, open(write_file, 'w') as new_file: 
    reader = csv.DictReader(text_File)
    writer = csv.writer(new_file, delimiter = ',')
    
    #checkpoint 
#print(content_file) 

#the goal is to create a loop with conditions that will keep count of the dates, 

    for row in reader: 
        count+=1
        m_date = row['Date']
        curr_month = int(row['Profit/Losses'])
        writer.writerow((m_date, curr_month))
        total += curr_month


    
        if count >1:
            change = curr_month - prev_month
        
            if change == 0:
                great_loss = change
                great_prof = change
                great_loss_date = m_date
                great_prof_date = m_date
            
            elif change < great_loss:
                great_loss = change
                great_loss_date = m_date
            
            if change > great_prof:
                great_prof = change
                great_prof_date = m_date
            
        tot_change += change
    
        prev_month = curr_month
    
avg = round(tot_change / (count-1), 2)
    
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {great_prof_date} ${great_prof}")
print(f"Greatest Decrease in Profits: {great_loss_date} ${great_loss}")


with open(text_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------\n")
    file.write(f"Total Months: {count}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${avg}\n")
    file.write(f"Greatest Increase in Profits: {great_prof_date} ${great_prof}\n")
    file.write(f"Greatest Decrease in Profits: {great_loss_date} ${great_loss}\n")