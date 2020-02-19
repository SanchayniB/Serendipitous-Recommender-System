# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import math 

def SVD(UImatrix,hiddenk = 10, epoch = 10 ):

    n_factors = hiddenk
    n_epochs = epoch
    alpha = 0.1

    # Randomly initialize the user and item factors.
    n_users = UImatrix.shape[0]
    n_items = UImatrix.shape[1]
    p = np.random.normal(0, .1, (n_users, n_factors))
    q = np.random.normal(0, .1, (n_items,n_factors))

    # Gradient descent
    for _ in range(n_epochs):
        for u in range(n_users):
            for i in range(n_items):
                r_ui = UImatrix[u,i]
                if math.isnan(r_ui) == False:
                
                    err = r_ui - np.dot(p[u], q[i])
                    # print(err)
                    # Update vectors p_u and q_i
                    p[u] += alpha * err * q[i]
                    q[i] += alpha * err * p[u]
    


    return(np.dot(p, q))
