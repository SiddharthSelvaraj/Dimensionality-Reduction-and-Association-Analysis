# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 19:18:35 2018

@author: Siddharth
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import matplotlib.cm as CM

# scatter plot function
def plotting(model,disease,text,xaxis,yaxis):
    labels=list(set(disease))
    # Color vector creation
    cvec=CM.brg(np.linspace(0,1,num=len(labels))) 
    legend_list=[]
    for i in range(len(labels)):
        plot_data = model[np.where(disease==labels[i])]
        x=plot_data[:,0]
        y=plot_data[:,1]
        legend_list.append(plt.scatter(x, y, c=cvec[i]))
           
    plt.legend(legend_list,labels,loc="best")
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(text,fontweight="bold") 
    plt.show() 
    
    
#TNSE
def tsne(attributes, disease, filename):
    tsne = TSNE(n_components=2, init='pca', learning_rate=100)
    final_tsne=tsne.fit_transform(attributes)
    text="TSNE: "+filename
    xaxis=""
    yaxis=""
    plotting(final_tsne,disease,text,xaxis,yaxis)
    
#SVD
def svd(attributes, disease, filename):
    u, s, vh = np.linalg.svd(attributes, full_matrices=True)
    new_svd = u[:,[0,1]]
    text="SVD: "+filename
    xaxis="Component 1"
    yaxis="Component 2"
    plotting(new_svd,disease,text,xaxis,yaxis)    

#PCA
def pca(attributes, disease, filename):
    mean = attributes.mean(axis=0)
    adj_attributes = attributes - mean
    covarience_mat = np.cov(adj_attributes, rowvar = False)
    evals, evecs = np.linalg.eig(covarience_mat)
    #sort eigen values in descending
    idx = np.argsort(evals)[::-1] 
    #top eigen vectors
    evecs = evecs[:,idx]  
    evals = evals[idx]
    pca_alg = np.dot(adj_attributes, evecs)
    text="PCA: "+filename
    xaxis="PC 1"
    yaxis="PC 2"
    plotting(pca_alg,disease,text,xaxis,yaxis)
    
#inputting the file
filename = input("Enter filename: ")
data = [line.strip().split('\t') for line in open(filename, 'r')] 
data = np.asarray(data)
attribute = data[:,0:data.shape[1]-1] #all columns except the last is taken as attributes
final_attribute = np.array(attribute, dtype=float)
disease = data[:,data.shape[1]-1]  #last column is taken as the disease

#calling the algorithms
pca(final_attribute, disease, filename)
tsne(final_attribute, disease, filename)
svd(final_attribute, disease, filename)