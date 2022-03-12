
import pandas as pd
import numpy as np
import SQL_Connection as sqlcon
import time
import openpyxl

class final_Code:

    def __init__(self,threadID, Type, url,sheet_name,total_file,cnt,setTime,dfList,uploadedfile):
       
       self.threadID = threadID
       self.Type = Type
       self.url= url
       self.sheet_name = sheet_name
       self.df = dfList
       self.total_file = total_file
       self.cnt = cnt
       self.setTime =setTime
       #self.dfList = dfList
       self.uploadedfile = uploadedfile

    def export_file(self):
        
        con = sqlcon.ConnectionManager().ConnectionString()
        cursor = con.cursor()

        if self.Type == 'xlsx':
            print("Loading Excel file")
            time.sleep(self.setTime)
            self.df=pd.read_excel(self.url,sheet_name=self.sheet_name,engine='openpyxl')
            print("Upload Excel file")
        elif self.Type =='csv':
            print("Loading csv file")
            time.sleep(self.setTime)
            self.df=pd.read_csv(self.url)
            print("Upload csv file")
        elif self.Type =='sql':
          
            print("Loading SQL table")
            self.df = pd.read_sql(self.url, con)
            time.sleep(self.setTime)
            print("Upload SQL table")

        self.df.columns = ['DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE','NO. OF SHARES','NO. OF TRADES']
    
    def add_newColumn_with_calculated(self):
        
        self.df['DATE'] = pd.to_datetime(self.df['DATE']).dt.date

        df = self.df.assign(
                    avg_Open_Close=lambda x: (x.OPEN + x.CLOSE) / 2,
                    per_Open_Close=lambda y:(y.OPEN + y.CLOSE)/100,
                    Profit_loss= ''
                    )

        for i in df.index:

            temp_open = df.iloc[i]['OPEN']
            temp_close = df.iloc[i]['CLOSE']
    
            if (temp_open <= temp_close):
                df.at[i,'Profit_loss'] = 'Profit'
            elif temp_open >= temp_close:
                df.at[i,'Profit_loss'] = 'Loss'
            else:
                df.at[i,'Profit_loss'] = np.nan

        self.df = df

        final_Code.unnamed_column(self)

    def unnamed_column(self):
        
        delete_col=[]

        for i in range(0,len(self.df.columns)):
            if (self.df.columns[i].lower() == ('unnamed: '+ str(i))):
                delete_col.append(self.df.columns[i])

        if len(delete_col) > 0:
            pd.concat([self.df.pop(x) for x in delete_col], axis=1)

    def save_data_in_excel(self):
        
        writer =''
        
        if self.cnt == 1 or self.total_file == 1:
            writer=pd.ExcelWriter(self.uploadedfile,mode='w',engine='openpyxl')
        else:
            writer=pd.ExcelWriter(self.uploadedfile,mode='a',engine='openpyxl')
        
        self.df.to_excel(writer, sheet_name=self.sheet_name,index =False)

        writer.save()

        if self.cnt == self.total_file:
            print("Upload file.")
                    
    def upload_file(self):
        
        #final_Code.export_file(self)
        final_Code.add_newColumn_with_calculated(self)
        final_Code.save_data_in_excel(self)

class Final_Code_StockMarket:

    def __init__(self,threadID, Type, url,sheet_name,total_file,cnt,setTime,df,uploadedfile):

       final_Code.__init__(self,threadID, Type, url,sheet_name,total_file,cnt,setTime,df,uploadedfile)
       final_Code.upload_file(self)
   