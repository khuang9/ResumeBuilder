import openai


import os

os.environ['OPENAI_API_KEY'] = "to be replaced"
#der = TextLoader(r"C:\Anaconda3\envs\WebDev\kprjs\media\measurements.txt")
from langchain.indexes import VectorstoreIndexCreator
#index = VectorstoreIndexCreator().from_loaders([loader])

from langchain.document_loaders.csv_loader import CSVLoader
csvloader = CSVLoader(file_path="C:\Prj\LLM\Hackathon\health_log\media\measurements.txt", source_column="measurement type")

def ai_answer(query):
  return '180 lbs'

  index = VectorstoreIndexCreator().from_loaders([csvloader])
  answer = index.query(query).strip()
  
  return answer
  

