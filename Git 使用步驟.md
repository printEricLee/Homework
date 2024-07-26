Git 是一個分佈式版本控制系統，用於跟蹤文件的變更，協作開發等。以下是一些常用的 Git 指令及其簡單說明：

### 基本指令

1. **初始化 Git 倉庫**
   ```bash
   git init
   ```

2. **克隆倉庫**
   ```bash
   git clone <repository-url>
   ```

3. **檢查當前狀態**
   ```bash
   git status
   ```

4. **添加變更到暫存區**
   ```bash
   git add <file>
   # 或添加所有變更
   git add .
   ```

5. **提交變更**
   ```bash
   git commit -m "提交說明"
   ```

6. **查看提交歷史**
   ```bash
   git log
   ```

### 分支相關指令

1. **查看所有分支**
   ```bash
   git branch
   ```

2. **創建新分支**
   ```bash
   git branch <branch-name>
   ```

3. **切換到分支**
   ```bash
   git checkout <branch-name>
   ```

4. **合併分支**
   ```bash
   git merge <branch-name>
   ```

### 遠端操作

1. **查看遠端倉庫**
   ```bash
   git remote -v
   ```

2. **添加遠端倉庫**
   ```bash
   git remote add <name> <repository-url>
   ```

3. **推送到遠端倉庫**
   ```bash
   git push <remote-name> <branch-name>
   ```

4. **拉取遠端更新**
   ```bash
   git pull <remote-name> <branch-name>
   ```

### 其他有用指令

1. **顯示差異**
   ```bash
   git diff
   ```

2. **撤銷變更**
   ```bash
   git checkout -- <file>
   ```

3. **重置到某個提交**
   ```bash
   git reset --hard <commit-id>
   ```

這些指令能幫助你開始使用 Git 進行版本控制。如果有任何具體問題，歡迎隨時詢問！