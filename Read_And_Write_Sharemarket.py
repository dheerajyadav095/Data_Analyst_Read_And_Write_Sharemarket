import threading
import time
import Final_Code_Stock_Market
import pandas as pd
import SQL_Connection as sqlcon

class shareDataThread(threading.Thread):

   def __init__(self, threadID, Type, url,sheet_name,total_file,cnt,settime,df,uploadedfile):
     
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.Type = Type
      self.url = url
      self.sheet_name = sheet_name
      self.total_file = total_file
      self.cnt= cnt
      self.dflist =df
      self.setTime = settime
      self.uploadedfile = uploadedfile

   def run(self):
      
      Final_Code_Stock_Market.Final_Code_StockMarket(self.threadID, self.Type, self.url,self.sheet_name,self.total_file,self.cnt,self.setTime,self.dflist,self.uploadedfile)

def export_file(Type,url,sheet_name):
        
    con = sqlcon.ConnectionManager().ConnectionString()
    cursor = con.cursor()

    df=''
    
    if Type == 'xlsx':
        df=pd.read_excel(url,sheet_name=sheet_name,engine='openpyxl')
    elif Type =='csv':
        df=pd.read_csv(url)
    elif Type =='sql':
        df = pd.read_sql(url, con)
        
    df.columns = ['DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE','NO. OF SHARES','NO. OF TRADES']
    
    return df
     
def UploadFileOption():
     
    num1 = int(input('How many documents will you be uploading?: '))
    
    uploadedfile = str(input('Enter uploaded file path: '))
    #uploadedfile ='Share_market_data\AllShareData.xlsx'

    cnt = 1
    etypeID= 0
    etype = ''
    url =''
    sheet_name =''
    
    for i in range(1,num1+1):
        
        settime = 0
        
        print('Which type of upload file Extension: ')
        print('1) .xlsx')
        print('2) .csv')
        print('3) sql Query')

        etypeID = int(input('Select option: '))
        
        strfilepath = ''
        strsheet_name='Save sheet name in the excel file: '
        
        if (etypeID == 1):
            
            etype='xlsx'

            strfilepath ='Enter excel file path: '
            
        elif (etypeID == 2):

            etype='csv'
            
            strfilepath ='Enter CSV file path: '

        elif (etypeID == 3):

            etype='sql'
           
            strfilepath = 'Enter SQL Query: '
            settime = 5

        url=str(input(strfilepath))
        sheet_name=str(input(strsheet_name))
    
        if (len(etype)>0 and len(url)>0):
            
            df =export_file(etype,url,sheet_name)
            thread = shareDataThread(i, etype,url,sheet_name,num1,cnt,settime,df,uploadedfile)

            time.sleep(3)
            thread.start()
            cnt =cnt + 1
  
if __name__ == "__main__":

    try:
        
        UploadFileOption()
        
        print ("Loading...")
        
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
        
        print("Press Enter to continue ...")
        input() 
