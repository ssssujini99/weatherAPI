import urllib.request
import json
import sys


# 기상청 중기예보 조회서비스
# 중기예보 조회서비스 - (3) 중기기온조회 -> 일 2회(6:00, 18:00)회 생성되며 예보일로부터 3~10일까지의 최저/최고기온 정보 제공
def api_5():
    encodingKey = ""

    # request url 정의
    url = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa?serviceKey=" + encodingKey + "&pageNo=1&numOfRows=10&dataType=JSON&regId=11B10101&tmFc=202208030600"
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


api_5()