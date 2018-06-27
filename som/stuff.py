from root_numpy import root2array, tree2array, array2root
from root_numpy import testdata
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import datetime
from som import SOM

print(str(datetime.datetime.now())) # Print time, useful for determining how long it takes to train the self-organizing map
sig = root2array('/home/ptgroup/pacordova/code/bin/Training_Trees.root', 'TreeS') # path to sig rootfile
bg = root2array('/home/ptgroup/pacordova/code/bin/Training_Trees.root', 'TreeB') # path to bg rootfile
#sig = np.concatenate(sig[24],sig[29],sig[30],sig[31],sig[34], axis=1)
sig = np.array(sig.tolist()) # convert to np array
sig = sig[:10000,:] # cut the np array to preferred size
sasquatch_sig = sig[:,35] 
sig = sig[:,[24,25,26,29,30,31,32,34]]
#sig = sig[:,:37]
bg = np.array(bg.tolist())
bg = bg[:10000,:]
sasquatch_bg = bg[:,35]
bg = bg[:,[24,25,26,29,30,31,32,34]]
#bg = bg[,:37]
data = np.concatenate((sig,bg),axis=0)
sasquatch = np.concatenate((sasquatch_sig, sasquatch_bg), axis=0)
#Train a 10x10 SOM with 400 iterations, 8 is the number of variables in the data array
som = SOM(10, 10, 8, 400)
som.train(data)
print(str(datetime.datetime.now()))

# For 2 by 1 neural map, create two root files for each neuron
d0 = np.apply_along_axis(distance_n0, 1, data)
d1 = np.apply_along_axis(distance_n1, 1, data)
mapped = np.array(som.map_vects(data))
data = np.append(data,mapped,axis=1)
data = np.column_stack((data,sasquatch))
data = np.column_stack((data,d0))
data = np.column_stack((data,d1))
neuron1 = data[np.where(((data[:,8] < 10) | (data[:,9] > 14)) & (count[data[:,8].astype(int),data[:,9].astype(int)] > 100))]
neuron1.dtype = [('mm2', 'float64'),('me','float64'),('mp','float64'),('kps_m', 'float64'),('kp_me', 'float64'),('kp_mp', 'float64'),('kp_theta','float64'),('sigmazero_m', 'float64'),('flag1', 'float64'),('flag2', 'float64'),('sasquatch','float64'),('d0','float64'),('d1','float64')]
neuron1.dtype.names = ['mm2','me','mp','kps_m','kp_me','kp_mp','kp_theta','sigmazero_m','flag1','flag2','sasquatch','d0','d1']
neuron2 = data[np.where((data[:,8] > 10) | (data[:,9] < 14) & (count[data[:,8].astype(int),data[:,9].astype(int)] > 100))]
neuron2.dtype = [('mm2', 'float64'),('me','float64'),('mp','float64'),('kps_m', 'float64'),('kp_me', 'float64'),('kp_mp', 'float64'),('kp_theta','float64'),('sigmazero_m', 'float64'),('flag1', 'float64'),('flag2', 'float64'),('sasquatch','float64'),('d0','float64'),('d1','float64')]
neuron2.dtype.names = ['mm2','me','mp','kps_m','kp_me','kp_mp','kp_theta','sigmazero_m','flag1','flag2','sasquatch','d0','d1']
array2root(neuron1, '/home/ptgroup/pacordova/20by20_20k/neuron1.root', mode='recreate')
array2root(neuron2, '/home/ptgroup/pacordova/20by20_20k/neuron2.root', mode='recreate')

# get new data
sig2 = np.array(sigroot.tolist())
sig2 = sig2[15000:,:]
sasquatch_sig2 = sig2[:,35]
sig2 = sig2[:,[24,25,26,29,30,31,32,34]]
#sig = sig[:,:37]
bg2 = np.array(bgroot.tolist())
bg2 = bg2[15000:,:]
sasquatch_bg2 = bg2[:,35]
bg2 = bg2[:,[24,25,26,29,30,31,32,34]]
#bg = bg[,:37]
data2 = np.concatenate((sig2,bg2),axis=0)
sasquatch2 = np.concatenate((sasquatch_sig2, sasquatch_bg2), axis=0)
d02 = np.apply_along_axis(distance_n0, 1, data2)
d12 = np.apply_along_axis(distance_n1, 1, data2)
mapped2 = np.array(som.map_vects(data2))
data2 = np.append(data2,mapped2,axis=1)
data2 = np.column_stack((data2,sasquatch2))
data2 = np.column_stack((data2,d02))
data2 = np.column_stack((data2,d12))
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
df['coords'] = df2[8].astype('str') + df2[9].astype('str')
df2['coords'] = df2[8].astype('str') + df2[9].astype('str')

#data = np.hstack((data,sasquatch))
#neuron1 = data[np.where((data[:,8] < 10) | (data[:,9] > 14))]
neuron1 = data[np.where(((data[:,8] < 10) | (data[:,9] > 14)) & (count[data[:,8].astype(int),data[:,9].astype(int)] > 100))]
neuron1.dtype = [('mm2', 'float64'),('me','float64'),('mp','float64'),('kps_m', 'float64'),('kp_me', 'float64'),('kp_mp', 'float64'),('kp_theta','float64'),('sigmazero_m', 'float64'),('flag1', 'float64'),('flag2', 'float64'),('sasquatch','float64'),('d0','float64'),('d1','float64')]
neuron1.dtype.names = ['mm2','me','mp','kps_m','kp_me','kp_mp','kp_theta','sigmazero_m','flag1','flag2','sasquatch','d0','d1']
neuron2 = data[np.where((data[:,8] > 10) | (data[:,9] < 14) & (count[data[:,8].astype(int),data[:,9].astype(int)] > 100))]
neuron2.dtype = [('mm2', 'float64'),('me','float64'),('mp','float64'),('kps_m', 'float64'),('kp_me', 'float64'),('kp_mp', 'float64'),('kp_theta','float64'),('sigmazero_m', 'float64'),('flag1', 'float64'),('flag2', 'float64'),('sasquatch','float64'),('d0','float64'),('d1','float64')]
neuron2.dtype.names = ['mm2','me','mp','kps_m','kp_me','kp_mp','kp_theta','sigmazero_m','flag1','flag2','sasquatch','d0','d1']
array2root(neuron1, '/home/ptgroup/pacordova/20by20_20k/neuron1.root', mode='recreate')
array2root(neuron2, '/home/ptgroup/pacordova/20by20_20k/neuron2.root', mode='recreate')
print(str(datetime.datetime.now()))

dimx = 10
dimy = 10
count = np.empty([dimx,dimy])
count_sq = np.empty([dimx,dimy])
count_sq_bg = np.empty([dimx,dimy])

for i in range(dimx):
    for j in range(dimy):
        count[i,j] = data2[np.where((data2[:,8] == float(i)) & (data2[:,9] == float(j))),10].size

for i in range(dimx):
    for j in range(dimy):
        count_sq[i,j] = data2[np.where((data2[:,8] == float(i)) & (data2[:,9] == float(j))),10].sum().astype(int)/(count[i,j]+1)

for i in range(dimx):
    for j in range(dimy):
        count_sq_bg[i,j] = (count[i,j] - data2[np.where((data2[:,8] == float(i)) & (data2[:,9] == float(j))),10].sum().astype(int))/(count[i,j]+1)

for i in range(100):
    count[i,:] = data[np.where(data[:,8] == float(i)),10].size

for i in range(100):
    count_sq[i,:] = data[np.where(data[:,8] == float(i)),10].sum()/(count[i,j]+1)

heatmap = axis.pcolor(data, cmap='hot')
plt.colorbar(heatmap)

plt.imshow(count, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()

diff_sq = count_sq - count_sqi
diff_sq = abs(diff_sq)
changesq = np.divide(diff_sq,count_sqi+0.001)



count = np.empty([dimx,dimy])
count_sq = np.empty([dimx,dimy])
count_sq_bg = np.empty([dimx,dimy])

for i in range(dimx):
    for j in range(dimy):
        count[i,j] = data[np.where((data[:,8] == float(i)) & (data[:,9] == float(j))),10].size

for i in range(dimx):
    for j in range(dimy):
        count_sq[i,j] = data[np.where((data[:,8] == float(i)) & (data[:,9] == float(j))),10].sum().astype(int)/(count[i,j]+1)

for i in range(dimx):
    for j in range(dimy):
        count_sq_bg[i,j] = (count[i,j] - data[np.where((data[:,8] == float(i)) & (data[:,9] == float(j))),10].sum().astype(int))/(count[i,j]+1)


plt.hist(df[0], bins=50, weights=df['sig'], alpha=0.5, label='sig')
plt.hist(df[0], bins=50, weights=df['bg'], alpha=0.5, label='bg')
plt.legend(loc='upper right')
plt.show()
