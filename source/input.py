import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64
import algos.fcfs as fcfs
import algos.sjf as sjf
import algos.srtf as srtf

algorithms=["FCFS - First come first serve","SJF - Shortest Job First", "SRTF - Shortest Remaining Time First"]

def input_form():
    st.markdown(f'<h1 style="text-align:center; padding:25px">{"Process Scheduling Visualiser"}</h1>',unsafe_allow_html=True)
    with st.form('input form'):
        algo=st.selectbox('Select Algorithm',algorithms)
        at=st.text_input('Arrival Time')
        bt=st.text_input('Burst Time')
        res=st.form_submit_button('Calculate')

    if at==''and  res:
        st.error("Input cannot be empty")

    elif bt=='' and res:
        st.error("Input cannot be empty")
    
    elif bt.split(" ").count('0')>0 and res:
        st.warning("Burst time cannot be zero")
    
    elif at!='' and bt!='' and len(list(map(int,at.split(" "))))!=len(list(map(int,bt.split(" ")))) and res==True:
        st.warning("Number of arrival times and burst times do not match")

    elif res==False:
        file_ = open("./assets/maths.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="">',unsafe_allow_html=True,)

    elif at!='' and bt!='' and res:
        at_list=list(map(int,at.split(" ")))
        bt_list=list(map(int,bt.split(" ")))
        # st.header('Result : ')
        st.markdown(f'<h1 style="color:green;font-weight:normal">{algo.split(" ")[0]}</h1>',unsafe_allow_html=True)
        if algo=="FCFS - First come first serve":
            result,wt,tat,ct=fcfs.fcfs(at_list,bt_list,len(at_list))
            df=pd.DataFrame(result,columns=["AT","BT","CT","WT","TAT"],index=[i for i in range(1,len(at_list)+1)])
            st.table(df)
            col1,col2=st.columns(2)
            text="Average Waiting Time = "+str(wt)+" / " +str(len(at_list))+" = "+str(round(wt/len(at_list),4))
            col1.markdown(f'<div style="color:Black;background-color:#ffdab9;border-radius:5px ;padding:16px; text-align:center;justify-content:center;opacity:0.7">{text}</div>',unsafe_allow_html=True)
            # col1.success("Average Waiting Time = "+str(wt)+" / " +str(len(at_list))+" = "+str(round(wt/len(at_list),4)))
            col2.info("Average TurnAround Time = "+str(tat)+" / " +str(len(at_list))+" = "+str(round(tat/len(at_list),4)))

        elif algo=="SJF - Shortest Job First":
            result,wt,tat,ct=sjf.sjf(at_list,bt_list,len(at_list))
            df=pd.DataFrame(result,columns=["AT","BT","CT","WT","TAT"],index=[i for i in range(1,len(at_list)+1)])
            st.table(df)
            col1,col2=st.columns(2)
            text="Average Waiting Time = "+str(wt)+" / " +str(len(at_list))+" = "+str(round(wt/len(at_list),4))
            col1.markdown(f'<div style="color:Black;background-color:#ffdab9;border-radius:5px ;padding:16px; text-align:center;justify-content:center;opacity:0.7">{text}</div>',unsafe_allow_html=True)
            # col1.success("Average Waiting Time = "+str(wt)+" / " +str(len(at_list))+" = "+str(round(wt/len(at_list),4)))
            col2.info("Average TurnAround Time = "+str(tat)+" / " +str(len(at_list))+" = "+str(round(tat/len(at_list),4)))
        else:
            result,wt,tat,ct=srtf.srtf(at_list,bt_list,len(at_list))
            df=pd.DataFrame(result,columns=["AT","BT","CT","WT","TAT"],index=[i for i in range(1,len(at_list)+1)])
            st.table(df)
            col1,col2=st.columns(2)
            text="Average Waiting Time = "+str(wt)+" / " +str(len(at_list))+" = "+str(round(wt/len(at_list),4))
            col1.markdown(f'<div style="color:Black;background-color:#ffdab9;border-radius:5px ;padding:16px; text-align:center;justify-content:center;opacity:0.7">{text}</div>',unsafe_allow_html=True)
            # col1.success("Average Waiting Time = "+str(wt)+" / " +str(len(at_list))+" = "+str(round(wt/len(at_list),4)))
            col2.info("Average TurnAround Time = "+str(tat)+" / " +str(len(at_list))+" = "+str(round(tat/len(at_list),4)))
            
