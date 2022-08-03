import urllib.request
import json
import sys


# 기상청 단기예보 조회서비스
# 단기예보 조회서비스 - (3) 단기예보조회 -> 해당 시각 + 해당 시각으로부터 3일 이내의 정보 제공(1시간 단위의 정보 제공)
# POP: 강수확률 / PTY: 강수형태 / PCP: 1시간 강수량 / REH: 습도
# SNO: 1시간 신적설 / SKY: 하늘상태 / TMP: 1시간 기온/ TMN: 일 최저기온 / TMX: 일 최고기온
# UUU: 풍속(동서성분) / VVV: 풍속(남북성분) / WAV: 파고 / VEC: 풍향 / WSD: 풍속
def api_3():
    encodingKey = ""

    # request url 정의
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?ServiceKey=" + encodingKey + "&pageNo=1&numOfRows=1000&dataType=JSON&base_date=20220803&base_time=1100&nx=60&ny=127"
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


api_3()