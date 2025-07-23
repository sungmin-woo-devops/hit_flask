import requests
url = 'http://apis.data.go.kr/1613000/BusRouteInfoInqireService/getCtyCodeList'
params = {
    'serviceKey': 'M4b1RJ9DzKhNVluQtxDKwnBZjluhh0A2A8LQRp7u6UCjfX6sdxRp+S5+S1ZxGG7fFAwXzr/B+91t96JdiulOkA==',
    '_type': 'json'
}
response = requests.get(url, params=params)
# content(바이트) → decode("utf-8")로 한글 변환
decoded = response.content.decode("utf-8")
print(decoded)