# -*- coding = utf-8 -*-

from datetime import datetime as dt

class Work(object):
  def __init__(self,name:str):
    self.name = name
    self.working_time=[]
  
    self.begin_time=0
    self.end_time=0
    
  def start(self):
    self.begin_time = dt.now()
  
  def stop(self):
    self.end_time = dt.now()
    self.working_time.append((self.begin_time,self.end_time))
    print("作業時間[sec]：%f"%(self.get_total_seconds_of_working_time()))
  
  def get_total_seconds_of_working_time(self) -> float:
    total_time = sum(delatdt.seconds for delatdt in (item[1]-item[0] for item in self.working_time))
    return total_time
    
