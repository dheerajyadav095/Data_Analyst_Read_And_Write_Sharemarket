# Data_Analyst_Read_And_Write_Sharemarket
I have created simple console application in python using multi-Threading. I have access xls file , csv file and sql data. I have calculation and adding data in this project. I will add more activity to implement in this project.

Follow steps:
1) Chack pakages :
    pip install openpyxl,
    pip install numpy,
    pip install pyodbc,
    pip install pandas,
2) 
   i) create table name is tbl_INE775A01035_1
   
   ii) column name is DATE	OPEN	HIGH	LOW	CLOSE	NO. OF SHARES	NO. OF TRADES
        ![image](https://user-images.githubusercontent.com/100525257/158029370-f75c0251-67ea-4a93-9f69-50421c9af179.png)
        
   iii) Insert into table data : ( enter sample data in excel . excel name is **AllShareData_All** and sheet name is **INE775A01035**)
   
3) 

  **SQL_Connection.py   line no 21**
  
  set your database server name ,userID and password 

  ex **Connection.__init__(self,'SQL Server', 'XYZ', 'DemoDatabase','sa','XYZ')**
  
3) Run project :

      How many documents will you be uploading?: **3**
      
      Enter uploaded file path: **Share_market_data\AllShareData.xlsx**
      
      Which type of upload file Extension:
      
      1) .xlsx
      
      2) .csv
       
      3) sql Query
      
      Select option: **1**
      
      Enter excel file path: **Share_market_data\AllShareData_All.xlsx**
      
      Save sheet name in the excel file: **INE155A01022**
      
      Which type of upload file Extension:
      
      1) .xlsx
      
      2) .csv
       
      3) sql Query
      
      Select option: **2**
      
      Enter CSV file path: **Share_market_data\INE417T01026.csv**
      
      Save sheet name in the excel file: **INE417T01026**
      
      Which type of upload file Extension:
      
      1) .xlsx
      
      2) .csv
       
      3) sql Query
      
      Select option: **3**
      
      Enter SQL Query: **SELECT * FROM tbl_INE775A01035_1**
      
      Save sheet name in the excel file: **INE775A01035**       
      
      *WAIT for 5 min After Watching *
    **Loading...
    
    **Upload file.
    
    **Press any key to continue . . .**
    
    **Output:**
    Open excel file 
    excel name is : AllShareData 
    
    
    

