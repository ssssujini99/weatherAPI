import urllib.request
import json
import sys


# 기상청 중기예보 조회서비스
# 중기예보 조회서비스 - (2) 중기육상예보조회 -> 일 2회(6:00, 18:00)회 생성되며 예보일로부터 3~10일까지의 육상날씨정보 제공
# 제공 정보: 제공 시간대는 오전/오후로 나뉘며, (강수 확률)과 (날씨 정보) 두 가지 제공
def api_4():
    encodingKey = ""

    # request url 정의
    url = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst?serviceKey=" + encodingKey + "&pageNo=1&numOfRows=10&dataType=JSON&regId=11B00000&tmFc=202208030600"
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


api_4()