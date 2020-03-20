from flask import Flask

app = Flask(__name__)

#Web  API 2개를 만들었다.
#주소에 대한
@app.route('/')
def index():
    return "this is my homepage!"
#/about 주소에 대한 요청이 들어오면 실행되는 함수
@app.route('/about')
def about():
    return "저는 geuno입니다."

# 플라스크 오브젝트의 런 메쏘드를 실행
if __name__ == '__main__':
    app.run()

