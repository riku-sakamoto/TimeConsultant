from WorkVO import work_item
from enum import Enum

class WorkManager(object):
  def __init__(self):
    self.registered_work_items_dict = {}
    self.target_work = None
    self.work_status = WorkStatus.Stopped
  
  def register_work(self,work_name):
    if work_name not in self.registered_work_items_dict.keys():
      new_Work = work_item.Work(work_name)
      self.registered_work_items_dict.update({work_name:new_Work})
  
  def change_target_work(self,work_name):
    if work_name not in self.registered_work_items_dict.keys():
      raise Exception("Not registered")
    
    if self.work_status != WorkStatus.Stopped:
      self.target_work_stop()

    self.target_work = self.registered_work_items_dict.get(work_name)
  
  def target_work_start(self):
    self.target_work.start()
    self.work_status = WorkStatus.Progress
  
  def target_work_stop(self):
    self.target_work.stop()
    self.work_status = WorkStatus.Stopped
    

  
class WorkStatus(Enum):
  Progress = 0
  Stopped = 1
