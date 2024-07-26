# Docker 教學

Docker 是一個開源的平台，讓開發者可以在容器中打包、分發和運行應用程式。以下是 Docker 的基本教學。

## 1. 安裝 Docker

### Windows / Mac

1. 下載 [Docker Desktop](https://www.docker.com/products/docker-desktop)。
2. 安裝並啟動 Docker Desktop。

### Linux

使用以下命令安裝 Docker：

```bash
sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

## 2. 基本命令

### 確認安裝

```bash
docker --version
```

### 拉取鏡像

```bash
docker pull ubuntu
```

### 查看鏡像

```bash
docker images
```

### 啟動容器

```bash
docker run -it ubuntu
```

### 查看運行中的容器

```bash
docker ps
```

### 停止容器

```bash
docker stop <container_id>
```

### 刪除容器

```bash
docker rm <container_id>
```

### 刪除鏡像

```bash
docker rmi <image_id>
```

## 3. Dockerfile

你可以用 Dockerfile 來自動化構建鏡像。

### 範例 Dockerfile

```dockerfile
# 使用官方的 Node.js 鏡像
FROM node:14

# 設定工作目錄
WORKDIR /usr/src/app

# 複製 package.json 和 package-lock.json
COPY package*.json ./

# 安裝依賴
RUN npm install

# 複製應用程式的源代碼
COPY . .

# 暴露應用程式運行的端口
EXPOSE 3000

# 啟動應用程式
CMD ["node", "app.js"]
```

### 構建鏡像

```bash
docker build -t my-node-app .
```

## 4. Docker Compose

Docker Compose 允許你使用 YAML 文件來定義和運行多個容器。

### 範例 `docker-compose.yml`

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
```

### 啟動服務

```bash
docker-compose up
```

### 停止服務

```bash
docker-compose down
```

### 更新遠端 URL：

```bash
git remote set-url origin https://github.com/username/repository.git
```

或者：

```bash
git remote set-url origin git@github.com:username/repository.git
```

## 5. 常見問題

- **容器無法啟動**：檢查 Docker 日誌，使用 `docker logs <container_id>`。
- **端口衝突**：確保宿主機端口沒有被其他應用佔用。

## 6. 資源

- [Docker 官方文檔](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/) - 鏡像庫

這些基本概念和命令可以幫助你開始使用 Docker。如需深入學習，建議查看官方文檔和相關教程。