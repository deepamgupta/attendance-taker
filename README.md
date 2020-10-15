# Attendance Taker 

A python script which takes names of students present in class and provide their attendance.
Currently it contains hard-coded list of students of CSA IET-DAVV 4th year.
So, it can take attedance of only these fellas as of now.

To get an idea, I have made a short 3 min video. You can watch the `Demo.mp4` clip. 

The idea is that while taking any online class on any platform esp. Google meet, there are extensions which help to generate a list of names of students present in class. But at the end teacher needs to make the entries in a spreadsheet. This process becomes redundant and cumbersome. 

This app will take the names of student present in class and provide attendance on form of 'P's roll no. wise:

``` 
P

P
P
P

P

P
```

Only task remaining is to copy this and paste it in the spreadsheet.

`EASY PEASY` 😎

Pre-requisite to use the "CSA_Attendance_Taker_App":

1. Use must have a Linux system.
2. You need to have list of students of my class.(Can take it from me)

# How to operate the app?

1. Clone the repo.
2. There is a folder `working apps` , just open it.

 - Now, there are two versions of the app - `v1 - strict` and `v2 - flexible` , both work differently.

3. Make an `input.csv` file in the same directory.
4. List down the name of students who were present in today's class.

 - for `strict` :  one student in each line in the input.csv file.
 - for `flexible` : no formatting required in the input.csv file, just the students who were present should be mentioned.

5. Double click the version, whichever you are using.
6. An output.csv file will be automatically get generated.

The `output.csv` file contains the attendance of students ( `P` for present and `empty-line` for absent).

Copy the content of whole file and use it in excel sheet😄
