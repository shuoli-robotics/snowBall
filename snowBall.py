import pandas as pd
import numpy as np

class SnowBall():
    def __init__(self):
        # path = '/Users/shuo/python_projects/SnowBall/data.xls'
        data_origin = pd.read_excel('data.xls')
        self.data_origin = np.array(data_origin)
        self.date_length = 252
        self.data_length = self.data_origin.shape[0]
        self.result = []
        # print(self.data_length)

    def if_knock_out(self,start_index,ki,ko):
        result_date = self.data_origin[start_index+self.date_length,0]
        period = self.date_length
        signal = "NULL"


        for i in range(start_index,start_index + self.date_length):
            ret = self.data_origin[i,1] / self.data_origin[start_index,1]
            if ret > ko:
                result_date = self.data_origin[i,0]
                period = i - start_index
                signal = "knock out"
                break

        if signal != "knock out":

            if self.data_origin[start_index + self.date_length-1,1] / self.data_origin[start_index,1] < 0.75:
                signal = 'knock in but no knock out'
            else:
                signal = "no knock out nor in"

        return (signal,period,result_date)

    def calc_everyday(self):
        for i in range(0,self.data_length-self.date_length):
            if self.data_origin[i,2] < 10 or self.data_origin[i,2] >20:
                continue

            signal,period,result_data =  self.if_knock_out(i,0.75,1.03)
            self.result.append([signal,period,result_data])

            print(signal)
            print(period)
            print(result_data)

        ret = pd.DataFrame(self.result)
        ret.to_excel("result.xls")
        

snowball = SnowBall()
signal,period,result_data = snowball.if_knock_out(0,0.75,1.03)

snowball.calc_everyday()


