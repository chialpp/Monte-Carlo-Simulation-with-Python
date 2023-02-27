import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


aaple=pd.read_csv(r"C:\Users\leilypour\Python-for-Finance-Repo-master\09-Python-Finance-Fundamentals\AAPL_CLOSE",index_col='Date',parse_dates=True)
cisco=pd.read_csv(r"C:\Users\leilypour\Python-for-Finance-Repo-master\09-Python-Finance-Fundamentals\CISCO_CLOSE",index_col='Date',parse_dates=True)
ibm=pd.read_csv(r"C:\Users\leilypour\Python-for-Finance-Repo-master\09-Python-Finance-Fundamentals\IBM_CLOSE",index_col='Date',parse_dates=True)
amzn=pd.read_csv(r"C:\Users\leilypour\Python-for-Finance-Repo-master\09-Python-Finance-Fundamentals\AMZN_CLOSE",index_col='Date',parse_dates=True)

stocks=pd.concat([aaple,cisco,ibm,amzn],axis=1)
stocks.columns=['Apple','cisco','ibm','amzn']

### Moshabeh in code stocks.pct_change(1)....Darsad Taghyir har roz nesbat be roze ghabl
log_ret=np.log(stocks/stocks.shift(1))


np.random.seed(101) #### Make sure that always we will have the same random number



num_ports=5000
All_weights=np.zeros((num_ports,len(stocks.columns))) ##Array of all weights
ret_arr=np.zeros(num_ports) ##Array of all returns for each etteration
vol_arr=np.zeros(num_ports) ##Array of all volitility for each etteration
sharpratio_arr=np.zeros(num_ports) ##Array of all sharp ratio for each etteration


for ind in range(num_ports):
   weights=np.array(np.random.random(4))  #### 4 random number between 0 and 1
   weights=weights/np.sum(weights) ### Transfer the weights to an array where the sum of them is equal to 1
   
   #Save Weights in the specific row
   All_weights[ind,:]=weights
   #Save expected return in the specific row
   ret_arr[ind]=np.sum(log_ret.mean()*weights*252)
   #Save volitility return in the specific row
   vol_arr[ind]=np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
   sharpratio_arr[ind]=ret_arr[ind]/vol_arr[ind]     ####Sharp ratio calculation



sharpratio_arr.max() ### maximum sharp ratio
sharpratio_arr.argmax() ### Adress of the max sharp ratio


max_sr_ret=ret_arr[1420]
max_sr_vol=vol_arr[1420]

plt.Figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr,c=sharpratio_arr,cmap='plasma')
plt.colorbar(label='Sharp ratio')
plt.xlabel('Volitility')
plt.ylabel('Return')
plt.scatter(max_sr_vol,max_sr_ret,c='red',s=50)
