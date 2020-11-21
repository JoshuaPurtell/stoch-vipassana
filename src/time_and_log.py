###fxns to time and log 

##imports
import pandas as pd
import numpy as np
import os
import time

def begin_session(path_to_csv,baseline,mean_fxn,var_fxn):
    if (os.path.isfile(path_to_csv)):
        history_df=pd.read_csv(path_to_csv)
        nr=history_df.shape[0]
    else:
        nr=0
    
    mu = mean_fxn(nr)
    sigma = var_fxn(nr,baseline)

    
    #sample from dist
    mins = baseline + max(-baseline+1,np.random.normal(mu,sigma))

    #Session
    os.system("say Begin Practice")
    print(mins)
    time.sleep(60*mins)
    os.system("say End Practice")

    #record stages
    stage = input("Which stage of meditation did you enter during this practice at its acme?")
    date = input("What is the date?")

    newrow = {"Date": [date], "Stage": [stage], "Duration": [mins]}
    if (nr==0):
        history_df = newrow
    else:
        history_df = history_df.append(newrow)

    pd.write_csv(history_df,path_to_csv)
    return

if __name__ == "__main__":
    path_to_csv = "~/documents/github/stoch-vipassana/data/session_record.csv"
    baseline=10
    def mean_fxn(x): return .5*x
    def var_fxn(x,y): return .33*(x+y)
    begin_session(path_to_csv,baseline,mean_fxn,var_fxn)
