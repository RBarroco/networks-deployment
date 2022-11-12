import joblib
import pandas as pd
from pathlib import Path
from joblib import load

BASE_DIR="/finalized_model.sav"
# import will be a row for example from a dataframe

def predict(input):
    model_file = Path(BASE_DIR)
    if not model_file.exists():
        return False

    # input = pd.DataFrame(input)
    input = pd.DataFrame(input)
    loaded_model = joblib.load(model_file)
    output = loaded_model.predict(input)
    
#    model.plot(forecast).savefig(f"{ticker}_plot.png")
#    model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")

    return output

def converts(output):
    if output == 0:
        return "Blackhole"
    elif output == 1:
        return "Diversion"
    elif output == 2:
        return "Normal"
    elif output == 3:
        return "Overflow"
    elif output == 4:
        return "PortScan"
    elif output == 5:
        return "TCP-SYN"

output = converts(predict(input))

print(output)
# tasks:
# 1) Check best way to save a xgboost model
# 2) make that model.py file is working well
# 3) Requirements.txt
# 4) 