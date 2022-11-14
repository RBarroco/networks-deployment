import joblib
import pandas as pd
from pathlib import Path


BASE_DIR="../model-info/finalized_model.joblib"
# import will be a row for example from a dataframe

# input = 
# {'Received Packets': {24789: 4188},
#  'Received Bytes': {24789: 75785402},
#  'Sent Bytes': {24789: 137303965},
#  'Sent Packets': {24789: 417351},
#  'Port alive Duration (S)': {24789: 2027},
#  'Delta Received Packets': {24789: 0},
#  'Delta Received Bytes': {24789: 0},
#  'Delta Sent Bytes': {24789: 556},
#  'Delta Sent Packets': {24789: 4},
#  'Delta Port alive Duration (S)': {24789: 5},
#  'Connection Point': {24789: 2},
#  'Total Load/Rate': {24789: 0},
#  'Total Load/Latest': {24789: 0},
#  'Active Flow Entries': {24789: 4},
#  'Switch ID_of:0000000000000002': {24789: 0},
#  'Switch ID_of:0000000000000003': {24789: 1},
#  'Switch ID_of:0000000000000004': {24789: 0},
#  'Switch ID_of:0000000000000005': {24789: 0},
#  'Switch ID_of:0000000000000006': {24789: 0},
#  'Switch ID_of:0000000000000007': {24789: 0},
#  'Switch ID_of:0000000000000008': {24789: 0},
#  'Switch ID_of:0000000000000009': {24789: 0},
#  'Switch ID_of:000000000000000a': {24789: 0},
#  'Switch ID_of:000000000000000b': {24789: 0},
#  'Switch ID_of:000000000000000c': {24789: 0},
#  'Port Number_Port#:2': {24789: 1},
#  'Port Number_Port#:3': {24789: 0},
#  'Port Number_Port#:4': {24789: 0}}


def predict(input):
    model_file = Path(BASE_DIR)
    if not model_file.exists():
        return False

    input = pd.DataFrame.from_json(input)
    loaded_model = joblib.load(model_file)
    output = loaded_model.predict(input)[0]
    
    
#    model.plot(forecast).savefig(f"{ticker}_plot.png")
#    model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")

    converts = {
                0: "Blackhole",
                1: "Diversion",
                2: "Normal",
                3: "Overflow",
                4: "PortScan",
                5: "TCP-SYN" 
                }

    return converts[output]

# output = predict(input)
# print(output)


