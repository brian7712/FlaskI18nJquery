from flask import Flask, render_template

# 創建Flask應用程序
app = Flask(__name__)


# 定義路由和視圖函數
@app.route('/')
def index():
    return render_template('index.html')


# 啟動Flask應用程序
if __name__ == '__main__':
    app.run(debug=True)
