import csv
import re

input_file = "input.csv"
output_file = "output.csv"

with open(output_file, "w") as input:
    input.write("Subject,Start Date,Start Time,End Date,End Time,Location,Description\n")
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            subj = row.get("Class Nbr")
            start_date = row.get("Start/End Date")[:6] + row.get("Start/End Date")[8:10]

            #start_time
            if int(re.sub("[^\w]", " ",  row.get("Days & Times")).split()[1]) < 10:
                start_time = "0" + re.sub(":[^\w]", " ",  row.get("Days & Times")).split()[1][:-2]
                if re.sub("[^\w]", " ",  row.get("Days & Times")).split()[2][2:5] == "PM":
                    start_time += " PM"
                else:
                    start_time += " AM"
            else:
                start_time = re.sub(":[^\w]", " ",  row.get("Days & Times")).split()[1][:-2]
                if re.sub("[^\w]", " ",  row.get("Days & Times")).split()[2][2:5] == "PM":
                    start_time += " PM"
                else:
                    start_time += " AM"
            
            end_date = re.sub("/[^\w]", " ",  row.get("Start/End Date")).split()[2][:6] + re.sub("/[^\w]", " ",  row.get("Start/End Date")).split()[2][8:10]
            end_time = re.sub("[^:\w]", " ",  row.get("Days & Times")).split()[2]

            #end_time
            if int(re.sub("[^\w]", " ",  row.get("Days & Times")).split()[3]) < 10:
                end_time = "0" + re.sub(":[^\w]", " ",  row.get("Days & Times")).split()[3][:-2]
                if re.sub("[^\w]", " ",  row.get("Days & Times")).split()[2][2:5] == "PM":
                    end_time += " PM"
                else:
                    end_time += " AM"
            else: 
                end_time = re.sub(":[^\w]", " ",  row.get("Days & Times")).split()[3][:-2]
                if re.sub("[^\w]", " ",  row.get("Days & Times")).split()[2][2:5] == "PM":
                    end_time += " PM"
                else:
                    end_time += " AM"
            
            loc = row.get("Room")
            desc = row.get("Component")
            input.write(subj + "," + start_date + "," + start_time + "," + end_date + "," + end_time + "," + loc + "," + desc + "\n")