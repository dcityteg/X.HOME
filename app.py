from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/lobe')
def lobe():
    return render_template('lobechat.html')

@app.route('/api')
def api():
    return render_template('oneapi.html')

if __name__ == '__main__':
    # 请注意：使用 sudo 运行下面的命令，确保有足够的权限
    app.run(debug=True, port=80)
