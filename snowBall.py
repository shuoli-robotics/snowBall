import pandas as pd
import numpy as np

class SnowBall():
    def __init__(self):
        path = '/Users/shuo/python_projects/SnowBall/data.xls'
        data_origin = pd.read_excel(path)
        self.data_origin = np.array(data_origin)

    def if_knock_out(self,start_index,date_length,ki,ko):
        result_date = self.data_origin[start_index+date_length,0]
        perid = date_length
        signal = "NULL"


        for i in range(start_index,start_index + date_length):
            ret = self.data_origin[i,1] / self.data_origin[start_index,1]
            if ret > ko:
                result_date = self.data_origin[i,0]
                period = i - start_index
                signal = "knock out"
                break

        if signal != "knock out":

            if data_origin[start_index + data_length-1,1] / data_origin[start_index,1] < 0.75:
                signal = 'knock in but no knock out'
            else:
                signal = "no knock out nor in"

        return (signal,period,result_date)

snowball = SnowBall()
signal,period,result_data = snowball.if_knock_out(0,252,0.75,1.03)
print(signal)
print(period)
print(result_data)


