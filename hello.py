from flask import Flask, escape, request, jsonify, Response

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name","World")
    return escape(name)

#주소를 반환하는 함수
def find_wellfares(wellfare_key) :
    wellfares={"종합건강검진":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506",
            "건강증진프로그램":"https://t1.daumcdn.net/cfile/tistory/99367A415E3B6B7C32",
            "상담":"https://t1.daumcdn.net/cfile/tistory/99E18A335E3B6B7C32",
            "직장어린이집":"https://t1.daumcdn.net/cfile/tistory/994344345E3B6B7B2D",
            "문화행사":"https://t1.daumcdn.net/cfile/tistory/99DADE3A5E3B6B7C2C",
            "기숙사":"https://t1.daumcdn.net/cfile/tistory/99786F4D5E3B6B7C2B",
            "직원할인":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506",
            "법인회원권":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506",
            "휴가비":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506",
            "통신비지원":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506",
            "자녀장학금":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506",
            "경조금":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506",
            "단체상해보험":"https://t1.daumcdn.net/cfile/tistory/99C43A485E3389E506"}
    print(wellfares[wellfare_key])
    return wellfares[wellfare_key]


@app.route('/check', methods=['POST'])
def check():
    
    #카카오 오픈빌더에서는 post를 통해서 넘겨주는 명령어가 이미 있음 request로 받으면 됨
    if request.is_json is True :  #validate json format / Content-Type : application/json
        print('json type in')
        content = request.get_json()
    else : 
        print('urlencoded type in') # x-www-form-urlendoded format / Content-Type : application
        content = request.form
    

    Params = content['action'].get('params')
    thumbnail_url = find_wellfares(Params.get('wellfare_benefits')) #주소로 환원하는 부분 위 find_wellfares 함수 부분 참조.
    print(Params)

    if Params is not None:
        wellfare_key = Params.get('wellfare_benefits')
    else : 
        wellfare_key = '복지키워드가 누락되었습니다.'
    
    print(wellfare_key)

    # user = {
    #     "version": "2.0",
    #     "template": {
    #         "outputs":[
    #             {
    #                 "simpleText":{
    #                     "text": "{}의 결과입니다.".format(escape(wellfare_key))
    #                 }
    #             }
    #         ]
    #     }
    # }
    # return user
    
    skill_result = {
        "version": "2.0",
        "template": {
            "outputs":[
                {
                    "basicCard":{
                        "title": "{}의 결과입니다.".format(escape(wellfare_key)),
                        "description":"{}와 관련된 복지내용은 뭐가있을까?".format(escape(wellfare_key)),
                        "thumbnail" : {
                            "imageUrl" : thumbnail_url
                        },
                        "profile":{
                            "imageUrl" : thumbnail_url,
                            "nickname" : "{}".format(escape(wellfare_key))
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "열어보기",
                            "messageText": "짜잔! 우리가 찾던 내용입니다"
                            },
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": thumbnail_url
                                }
                            ]
                        }
                    }
                ]
            }
        }
    return skill_result


if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000, debug=True)
