import tkinter as tk
import requests
import json
from tkinter import *

window=tk.Tk()

num_label=tk.Label(window, text="Number : ")
num_label.grid(row=0)

num=tk.Entry(window)
num.grid(row=0, column=10)

m_label = tk.Label(window, text="Message : ")
m_label.grid(row=2)

t = tk.Text(window, height=6, width=25)
t.grid(row=2, column=10)


URL = 'https://www.way2sms.com/api/v1/sendCampaign'

#m=t.get(0.0,tk.END)
# print(m)
#n=num.get()
# print(n)

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  print(requests.post(reqUrl, req_params))

# get response
#response = sendPostRequest(URL, 'VILAAM3IWX4K242A89KWSDMH3E7QAF1N', 'IH1QL900W3HWJU6G', 'stage', , m)
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
#print(response.text)

btn=tk.Button(window, text="Send ", command = lambda: sendPostRequest('https://www.way2sms.com/api/v1/sendCampaign', '1WR8CL6I9C8B73OUD9ZKM24CD0CC1C10', 'Z0XQA7GY7H2YUGWU', 'stage', num.get(), "sender's mailid",t.get('1.0',END)))
btn.grid(row=4, column=10)

window.mainloop()

