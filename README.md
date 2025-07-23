참고자료
- https://wikidocs.net/book/8078
- https://dash.plotly.com/installation
- https://gits.gg.go.kr/gtdb/web/trafficDb/visualization/data/list.do
- https://www.data.go.kr/data/15040660/fileData.do?recommendDataYn=Y
- https://www.data.go.kr/data/15067528/fileData.do

데이터 소스 기관: 공공데이터포털, 행정표준코드관리시스템, 지오서비스, 경기버스정보

데이터
- 시도코드
  - url: https://sgis.kostat.go.kr/developer/html/openApi/api/dataCode/SidoCode.html
  - 출처: https://sgis.kostat.go.kr/developer/
- 법정동코드목록조회
  - url: https://www.code.go.kr/stdcode/regCodeL.do
  - 출처: 행정표준코드관리시스템
- 경기부동산포털 법정동 코드
  - url: https://data.gg.go.kr/portal/data/service/selectServicePage.do?infId=567Y42F7T84YIEBN9KAC33794182&infSeq=1
  - 출처: 경기데이터드림
- 대한민국 최신 행정구역(SHP)
   - url: http://www.gisdeveloper.co.kr/?p=2332
   - 출처: 지오서비스
- 경기버스 정보
   - 위치: bus_stop_loc/
   - url: https://www.gbis.go.kr/
   - 출처: 경기버스정보
- 전국 버스 정류장 위치 정보
  - url: https://www.data.go.kr/data/15067528/fileData.do
  - 출처: 공공데이터포털
- 국토교통부_버스노선
  - url: https://www.data.go.kr/data/15142030/openapi.do?recommendDataYn=Y
  - 출처: 공공데이터포털
- 국토교통부_(TAGO)_버스노선정보
  - url: https://www.data.go.kr/data/15098529/openapi.do?recommendDataYn=Y
  - 출처: 공공데이터포털


1. app.py
   - Flask 애플리케이션의 진입점
   - Flask 인스턴스를 생성하고, 필요한 블루프린트(views), 설정(config), 확장(ORM 등)을 등록
2. models.py
    - 데이터베이스의 테이블 구조와 데이터를 정의
3. forms.py
   - 웹 폼(입력 폼) 구조와 유효성 검사를 정의
   - 