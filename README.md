使用 Flask 框架创建简单的 Web 应用程序，获取每日 Bing 图片的功能搭建的一个docker容器服务。
## 1. 拉取到本地直接，切换到目录中
## 2. 构建 Docker 镜像
     docker build -t bing-image-app .
## 3. 运行 Docker 容器
     docker run -d -p 5000:5000 bing-image-app
## 4. 访问服务
    启动容器后，打开浏览器并访问 http://localhost:5000/, 会直接看到每日 Bing 图片。
