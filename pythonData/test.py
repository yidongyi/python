#-*-coding:utf8-*-
import numpy as np;
import pandas as pd;
data = np.array([[1,2],
              [3,4]]);
print data*10;
print  data.shape;
print data.dtype;

#切片索引：
print "---------切片索引:---------";
arr = np.array([0,1,2,3,4,5,6,7,8,9]);
print arr[1:6];#[1 2 3 4 5]
print arr[:9];#[0 1 2 3 4 5 6 7 8]
print arr[0:]#[0 1 2 3 4 5 6 7 8 9]
print arr[:]#[0 1 2 3 4 5 6 7 8 9]
print data[:];#[[1 2]
              #[3 4]]
print data[:1]#[[1 2]]
print data[:2,1:]#[[2]
                 #[4]]
print data[1,:2] #[3 4]

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe']);
data = np.random.randn(7,4);
print names;
print data;
print data[names=='Bob']