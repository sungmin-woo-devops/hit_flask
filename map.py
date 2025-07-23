import folium
import os
import pandas as pd

def create_map():
    """지도를 생성하고 static 폴더에 HTML 파일로 저장합니다."""
    # 현재 스크립트의 디렉토리를 기준으로 static 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir, "static")
    
    # static 디렉토리가 없으면 생성
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    # 수원시 중심에 기본 지도 생성
    m = folium.Map(
        location=[37.2636, 127.0286],  # 수원시 중심 좌표
        zoom_start=12,
        tiles="Cartodb dark_matter"
    )

    # 버스 정류장 데이터 로드
    try:
        bus_stops_file = os.path.join(current_dir, "data", "bus_stop_loc", "국토교통부_전국 버스정류장 위치정보_20241028.csv")
        df = pd.read_csv(bus_stops_file, encoding='utf-8')
        
        # 수원시 데이터만 필터링
        suwon_data = df[df["도시명"] == "경기도 수원시"]
        
        # 각 정류장을 지도에 점(CircleMarker)으로 추가
        for idx, row in suwon_data.iterrows():
            folium.CircleMarker(
                location=[row['위도'], row['경도']],
                radius=2,  # 점의 크기 (픽셀)
                color="blue",
                fill=True,
                fill_color="blue",
                fill_opacity=0.7,
                popup=row['정류장명']
            ).add_to(m)
        
        print(f"수원시 버스 정류장 {len(suwon_data)}개가 지도에 추가되었습니다.")
        
    except Exception as e:
        print(f"버스 정류장 데이터 로드 중 오류: {e}")
        # 기본 마커 추가
        folium.Marker(
            location=[37.2636, 127.0286],
            popup="수원시청",
            icon=folium.Icon(color="blue")
        ).add_to(m)

    # 지도를 HTML 파일로 저장 (static 폴더에)
    map_file_path = os.path.join(static_dir, "map.html")
    m.save(map_file_path)
    print(f"지도가 성공적으로 저장되었습니다: {map_file_path}")

if __name__ == "__main__":
    create_map()
