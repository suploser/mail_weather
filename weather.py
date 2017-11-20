#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jinja2
import json
import requests


LOCATION='beijing'
ORIGINAL_URL='https://free-api.heweather.com/s6/weather/forecast'

#获取天气数据
def get_data():
    new_data=[]
    paraments={
        'location':LOCATION,
        'key':'febf0d8002514b4191f9447419d6b71b',
        'lang':'zh',
        'unit':'m'
    }
    try:
        response=requests.get(ORIGINAL_URL,params=paraments)
       # r=json.loads(json.dumps(response.text,ensure_ascii=False,indent=1))
        r=json.loads(response.text)
    except Exception as err:
        print(err)
    
    weather_forecast=r['HeWeather6'][0]['daily_forecast']
    for data in weather_forecast:
        
        new_obj={}
        new_obj['date']=data['date']
        new_obj['sr']=data['sr']
        new_obj['ss']=data['ss']
        new_obj['tmp_max']=data['tmp_max']
        new_obj['tmp_min']=data['tmp_min']
        new_obj['wind_sc']=data['wind_sc']
        new_obj['pop']=data['pop']
        new_data.append(new_obj)
    
    return new_data

#渲染模板，传递数据
def render_email(data):
    env=jinja2.Environment(loader=jinja2.FileSystemLoader('./template'))
    return env.get_template('hefentianqi.html').render({'data':data})

#print(render_email(get_data()))
