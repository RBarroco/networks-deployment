import joblib
import pandas as pd
from pathlib import Path


BASE_DIR="finalized_model.sav"
# import will be a row for example from a dataframe
# value = pd.read_csv("../data/batch_load/preprocessed_data/X_batch_v2.csv")
input = {
  'Unnamed: 0': 0,
  'Received Packets': 132,
  'Received Bytes': 9181,
  'Sent Bytes': 6311853,
  'Sent Packets': 238,
  'Port alive Duration (S)': 46,
  'Delta Received Packets': 0,
  'Delta Received Bytes': 0,
  'Delta Sent Bytes': 280,
  'Delta Sent Packets': 2,
  'Delta Port alive Duration (S)': 5,
  'Connection Point': 1,
  'Total Load/Rate': 0,
  'Total Load/Latest': 0,
  'Active Flow Entries': 9,
  'Switch ID_of:0000000000000002': 0,
  'Switch ID_of:0000000000000003': 0,
  'Switch ID_of:0000000000000004': 0,
  'Switch ID_of:0000000000000005': 0,
  'Switch ID_of:0000000000000006': 0,
  'Switch ID_of:0000000000000007': 0,
  'Switch ID_of:0000000000000008': 0,
  'Switch ID_of:0000000000000009': 0,
  'Switch ID_of:000000000000000a': 0,
  'Switch ID_of:000000000000000b': 0,
  'Switch ID_of:000000000000000c': 1,
  'Port Number_Port#:2': 0,
  'Port Number_Port#:3': 0,
  'Port Number_Port#:4': 0}


def predict(input):
    model_file = Path(BASE_DIR)
    if not model_file.exists():
        return False

    input = pd.DataFrame.from_dict(input, orient ='index')
    input = input.T
    
    loaded_model = joblib.load(model_file)
    print(1)

    output = loaded_model.predict(input)
    print(1)
#    model.plot(forecast).savefig(f"{ticker}_plot.png")
#    model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")

    # converts = {
    #             0: "Blackhole",
    #             1: "Diversion",
    #             2: "Normal",
    #             3: "Overflow",
    #             4: "PortScan",
    #             5: "TCP-SYN" 
    #             }

    return output

output = predict(input)
print(output)
# def converts(output):
#     if output == 0:
#         return "Blackhole"
#     elif output == 1:
#         return "Diversion"
#     elif output == 2:
#         return "Normal"
#     elif output == 3:
#         return "Overflow"
#     elif output == 4:
#         return "PortScan"
#     elif output == 5:
#         return "TCP-SYN"

# 


# tasks:
# 1) Check best way to save a xgboost model
# 2) make that model.py file is working well
# 3) Requirements.txt
# 4) 