import pandas as pd
import folium

stop_data = pd.read_csv("busstop.csv")
color_data = pd.read_csv("info.csv")

busNumber = input('노선번호: ').strip()

center=[]
lines = []
for i in range(len(stop_data['노선명'])):
    if stop_data['노선명'][i] == busNumber:
        if len(center) == 0:
            center = [float(stop_data['Y좌표'][i]), float(stop_data['X좌표'][i])]
        lines.append([float(stop_data['Y좌표'][i]), float(stop_data['X좌표'][i])])
        
if len(lines) > 0:
    m=folium.Map(location=lines[len(lines)//4-1],zoom_start=14)

for i in range(len(stop_data['노선명'])):
    if stop_data['노선명'][i] == busNumber:
        folium.Marker(
            [float(stop_data['Y좌표'][i]), float(stop_data['X좌표'][i])],
            tooltip=f"[{stop_data['ARS_ID'][i]}] {stop_data['정류소명'][i]}",
            icon=folium.Icon(color='red', icon='star')
        ).add_to(m)
    
color = "#000000"
for i in range(len(color_data['유형'])):
    if color_data["노선번호"][i] == busNumber:
        color = color_data['유형'][i]

if len(lines) > 0:
    folium.Marker
    folium.PolyLine(locations=lines,color=color,).add_to(m)
    m.save(f"Route.html")
    print("노선도가 생성되었습니다.")
else: print("해당 노선이 조회되지 않습니다.")