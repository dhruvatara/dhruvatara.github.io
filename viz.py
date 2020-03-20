import pandas as pd
import chart_studio
import plotly.express as px
username = "dhruvatara.b"
api_key = "DGQc7vukHHPMAwIqG7JT"
chart_studio.tools.set_credentials_file(username = username,api_key = api_key)
import chart_studio.plotly as py
import chart_studio.tools as tls

df = pd.DataFrame({'Skills':['Python','Java','C','C++','R','SQL','MongoDB','Realm'],'Proficiency on scale of 1-5':[3,4,3,4,4,2,3,1]})
#print(df)
fig = px.bar(df,x='Proficiency on scale of 1-5',y='Skills',orientation='h',width=600,height=600)
py.plot(fig,filename="skill_prof",auto_open=True)
