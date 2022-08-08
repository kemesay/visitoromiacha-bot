# import pandas as pd
# import os
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# import pickle
# import requests
# import json
# from flask import Flask
# # def DataStore(name,mobile_number,email,occupation):
# #     if os.path.isfile("user_data.xlsx"):
# #         df=pd.read_excel("user_data.xlsx")
# #         df=df.append(pd.DataFrame([[name,mobile_number,email,occupation]],
# #                         columns=["name","mobile_number","email","occupation"]))
# #         df.to_excel("user_data.xlsx",index=False)
# #     else:
# #         df=pd.DataFrame([[name,mobile_number,email,occupation]],
# #                         columns=["name","mobile_number","email","occupation"])
# #         df.to_excel("user_data.xlsx",index=False)
# #     return []

# # def FetchData(column,occupation):

# #     if os.path.isfile("user_data.xlsx"):
# #         df=pd.read_excel("user_data.xlsx")
# #         data=df[column][df["occupation"]==occupation]
# #         return data.to_list()
# #     else:
# #         return ["There is no data. "]
# # Folder Path
# path = "eexampless\static"
  
# # Change the directory
# os.chdir(path)
  
# # Read text File
  

# def FetchData(file_path):
#     with open(file_path, 'r') as f:
#         return f.read()
#         #print(f.read())
  
  
# # iterate through all file
# for file in os.listdir():
#     # Check whether file is in image format or not
#     if file.endswith(".jpj"):
#         file_path = f"{path}\{file}"
  
#         # call read text file function
#         FetchData(file_path)

