# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import math 

def SVD(UIinput,hiddenk = 10, epoch = 10 ):

    UImatrix = UIinput.copy()
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
        for u, i in np.argwhere(np.isnan(UImatrix) == False):
            r_ui = UImatrix[u,i]
                
                
            err = r_ui - np.dot(p[u], q[i])
            # print(err)
            # Update vectors p_u and q_i
            
            p_u = (alpha * err * q[i])
            q_u = (alpha * err * p[u])
            p[u] += + p_u
            q[i] += + q_u



    return((p, q))
