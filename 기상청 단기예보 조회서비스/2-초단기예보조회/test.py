import urllib.request
import json
import sys


# 기상청 단기예보 조회서비스
# 단기예보 조회서비스 - (2) 2-초단기예보조회 -> 해당 시각 + 6시간 이내까지의 정보를 제공
# T1H: 기온 / RN1: 1시간 강수량 / SKY: 하늘상태 / UUU: 동서바람성분 / VVV: 남북바람성분
# REH: 습도 / PTY: 강수형태 / LGT: 낙뢰 / VEC: 풍향 / WSD: 풍속
def api_2():
    encodingKey = ""

    # request url 정의
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?ServiceKey=" + encodingKey + "&pageNo=1&numOfRows=1000&dataType=JSON&base_date=20220803&base_time=1243&nx=60&ny=127"
    request = urllib.request.Request(url)

    # request 보내기
    response = urllib.request.urlopen(request)

    # 결과 코드 정의
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        response = json.loads(response_body)

        sys.stdout = open('test.json', 'w', encoding="UTF-8")
        print(json.dumps(response, ensure_ascii=False, indent=4))
        sys.stdout.close()
    else:
        print("Error Code:" + rescode)


api_2()

