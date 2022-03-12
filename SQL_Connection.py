import pyodbc

class Connection:

  def __init__(self,DriverName, servername, dbname,uid,pwd):
   
    self.DriverName = DriverName
    self.servername = servername
    self.database = dbname
    self.uid = uid
    self.pwd = pwd

  def ConnectionString(self):
   
    con = pyodbc.connect('DRIVER={'+self.DriverName+'};SERVER='+self.servername+';DATABASE='+self.database+';UID='+self.uid+';PWD='+self.pwd)
    return con

class ConnectionManager(Connection):

  def __init__(self):
    Connection.__init__(self,'SQL Server', 'XYZ', 'DemoDatabase','sa','XYZ')

