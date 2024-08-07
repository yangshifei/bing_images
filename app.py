from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # 设置 Bing 壁纸 API 的 URL
    bing_api_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

    # 发送 HTTP 请求获取响应
    response = requests.get(bing_api_url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 JSON 响应
        data = response.json()

        # 检查是否包含图片信息
        if 'images' in data and len(data['images']) > 0:
            image_url = "https://www.bing.com" + data['images'][0]['url']
            return redirect(image_url)
        else:
            return "No image information found in the response.", 404
    else:
        return f"Failed to fetch Bing image. Status code: {response.status_code}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
