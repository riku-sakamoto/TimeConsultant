# -*- coding = utf-8 -*-

import tkinter as tk
from tkinter import ttk
import work_manager as work_manager

def work_start():
  Manager.target_work_start()

def work_stop():
  Manager.target_work_stop()
  change_time_status()

def work_change(label,comboBox):
  Manager.change_target_work(comboBox.get())
  label["text"] = "現在タスク : %s"%comboBox.get()

def register_default_works(WorkManager:work_manager.WorkManager):
  WorkManager.register_work("RESPサポート")
  WorkManager.register_work("RESP開発")
  WorkManager.register_work("勉強")
  WorkManager.register_work("雑件")

def change_time_status():
  work_name = combobox.get()
  label = labels_dict[work_name]
  time = Manager.registered_work_items_dict.get(work_name).get_total_seconds_of_working_time()
  label["text"] = "%s : %.2f[sec]"\
      %(work_name,time)



if __name__ == "__main__":
  # メインウィンドウ作成
  root = tk.Tk()
  Manager = work_manager.WorkManager()
  register_default_works(Manager)

  #メインウィンドウのタイトルを変更
  root.title("Clock Consultant")

  #メインウィンドウを640x480にする
  root.geometry("400x300")

  button_work_start = tk.Button(root, text="タスクスタート", command = lambda: work_start())
  # button_work_start.pack(fill = 'x', padx=20, side = 'left')
  button_work_start.grid(row =1,column=1,padx=2,sticky="w")

  button_work_stop = tk.Button(root, text="タスクストップ", command = lambda: work_stop())
  # button_work_stop.pack(fill = 'x', padx=20, side = 'left')
  button_work_stop.grid(row=1,column=2,padx=2,sticky="w")

  #Combobox生成
  combobox = ttk.Combobox(
        state = 'readonly', #編集不可
        values = list(Manager.registered_work_items_dict.keys())
        )
  #Combobox初期値設定
  combobox.current(0)
  combobox.grid(sticky="w")

  label_work_now = tk.Label(root, text="現在タスク : %s"%combobox.get(), font=(16))
  label_work_now.grid(sticky="w")
  work_change(label_work_now,combobox)
  
  button_work_change = tk.Button(root, text="作業変更", command = lambda: work_change(label_work_now,combobox))
  button_work_change.grid(sticky="w")


  label_work = tk.Label(root, text="本日の作業時間", font=(20))
  label_work.grid(sticky="w")

  labels_dict = {}
  for work_name in Manager.registered_work_items_dict.keys():
    label = tk.Label(root, text = "%s : %.2f[sec]"\
      %(work_name,Manager.registered_work_items_dict.get(work_name).get_total_seconds_of_working_time()),\
        font=(1))
    #表示する
    label.grid(sticky="w")
    labels_dict.update({work_name:label})


  #rootを表示し無限ループ
  root.mainloop()



