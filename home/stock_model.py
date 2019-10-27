import os
import pandas as pd
from sklearn import linear_model
from nsetools import Nse
import pathlib
import joblib

nse = Nse()

def nse_data(stock_name):
    '''input stock_name : str
    output : list = output,high,low'''
    data = nse.get_quote(stock_name)
    current = [data['open'],data['dayHigh'],data['dayLow']]
    return current

def model_check(stock_name):
    '''checking if model exits or not;
    input stock_name str
    return true or false'''
    model_path = pathlib.Path(os.getcwd()+"\\nse_data\\saved_model\\"+stock_name+'.pkl')
    if model_path.exists():
        return True
    else:
        return False

def any_stock(stock_name):
    '''function to predict any stock values
    stock_name == str; today_value= list,[open,high,low]
    '''
    try:
        if model_check(stock_name) == False:
            data_path = os.getcwd()+"\\home\\nse_data\\HISTORICAL_DATA\\"
            df = pd.read_csv(data_path + stock_name + '_data.csv')
            df.fillna(df.mean(),inplace=True)
            X = df.iloc[:,[1,2,3]]
            y = df.iloc[:,[4]]

            reg = linear_model.LinearRegression()
            reg.fit(X,y)
            y_today = reg.predict([nse_data(stock_name)])
            
            model_path_one = os.getcwd()+"\\home\\nse_data\\saved_model\\"
            joblib_file = model_path_one + stock_name+ ".pkl"
            joblib.dump(reg, joblib_file)
            print('model creation')
            return y_today[0][0]
        else:
            print('model loading')
            model_path_one = os.getcwd()+"\\home\\nse_data\\saved_model\\"
            joblib_file = model_path_one + stock_name+ ".pkl"
            model = joblib.load(joblib_file)
            y_today = model.predict([nse_data(stock_name)])
            
            return y_today
    except:
        return (" internal error")



  


# try:
#     print(any_stock('SBIN'))
# except IndexError:
#     print('index error')
# except FileNotFoundError:
#     print("no file")

