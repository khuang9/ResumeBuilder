# ResumeBuilder

ResumeBuilder is an AI-powered tool that helps students create personalised, high-quality resumes quickly and efficiently.

## Features

### User Accounts
* Accounts allow users to create, save, and download their own personalised resumes

### Chat-based Profile Creation
* Four main profile topics: __Education__, __Test/Competition Results__, __Courses__, and __Extracurriculars__
* Separate chat pages for each topic
* Questions will be tailored to specific topics
* User can choose to re-answer or skip questions using __"Backward"__ or __"Forward"__ buttons
* __"Unfinished questions"__ counter provides guideline on how many questions should be answered at the very least
* User answers are processed using ChatGPT API
* Chat history and GPT detail extraction overview are included as well

### AI Resume Generation
* Generate resumes based on your chats with the click of a button
* All important information and details will be compiled and formatted with ChatGPT
* Completed resumes can be downloaded as a __.TXT__, __.PDF__, or __.DOCX__ file
* Downloaded resumes can be found in the __*\ResumeBuilder\media*__ folder

### Q & A
* A page where the user can ask any questions they may have about the university they are applying to
* Questions will be processed and answered using LangChain Natural Language Processing
* Data used to answer questions will be stored in __*ApplicationKnowledge.csv*__ in the __*\ResumeBuilder\media*__ folder
* Users can edit the data in __*ApplicationKnowledge.csv*__ with the following code:

```python
import csv

# Obtain data through web scraping
data = [
    ["Your labels here", "your label 1", "your label 2", "etc."],
    ["Your data here", "your data 1", "your data 2", "etc."],
    ["Your data here", "your data 3", "your data 4", "etc."],
]

csv_file_name = "ApplicationKnowledge.csv"

"""Completely overwrite the existing data in the file"""
def overwrite(new_data):
  with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    for row in new_data:
      csv_writer.writerow(row)

#############################################################

def add_rows(new_data):
  with open(csv_file_name, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    for row in new_data:
      csv_writer.writerow(row)
  
def add_columns(new_data):
  data_index = 0
  
  with open(csv_file_name, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
      new_data[data_index] = row + new_data[data_index]
      data_index += 1
          
  overwrite(new_data)
  

"""Add new data to file without overwriting the old data"""
def append_data(new_data):
  with open(csv_file_name, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    labels = next(csv_reader)
    num_rows = sum(1 for row in csv_reader)
    
    data_rows = [["Not found"] * len(new_data[0]) for _ in range(num_rows)]
  
  for c in range(len(new_data[0])):
    if new_data[0][c] not in labels:
      labels.append(new_data[0][c])
      add_columns([[new_data[0][c]]] + [["Not found"] for _ in range(num_rows)])
      
    for r in range(1, len(new_data)):
      data_rows[r-1][labels.index(new_data[0][c])] = new_data[r][c]
      
  add_rows(data_rows)


"""Call either function to overwrite or append data as needed"""
# overwrite(data[:])
# append_data(data[:])
```
