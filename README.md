# Guide to export calendar

## Guide to export calendar

### Step 1:

Login to simconnect

### Step 2:

Go to My Apps > Self Service > Enrollment > My Timetable (List View: Class)

### Step 3:

Choose your term

### Step 4:

Copy Highlighted (Per Module) and paste into excel sheet

![files/Untitled.png](files/Untitled.png)

![files/Untitled%201.png](files/Untitled%201.png)

### Step 5:

Change **Class Nbr** Column into **Class** Column (Use data shown below) 

![files/Untitled%202.png](files/Untitled%202.png)

![files/Untitled%203.png](files/Untitled%203.png)

### Step 6:

fill up the blanks

![files/Untitled%204.png](files/Untitled%204.png)

### Step 7:

Save as input.csv and use python script. (Generates output.csv)
```
chmod +x SCtGC_convertor.py
python3 SCtGC_convertor.py
```

### Step 8:

Go to Google Calendar > Top Right Corner > Press the Gear > Settings

![files/Untitled%205.png](files/Untitled%205.png)

Go to Import & export

![files/Untitled%206.png](files/Untitled%206.png)

### Step 9:

Under Import > Select file from your computer > Select output.csv > Press Import
