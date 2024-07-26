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

### 清除 Git 倉庫中的所有已提交文件

1. **創建一個新的孤立分支**
   ```bash
   git checkout --orphan new_branch
   ```

2. **添加所有文件**
   ```bash
   git add -A
   ```

3. **提交更改**
   ```bash
   git commit -m "Initial commit with no history"
   ```

4. **刪除舊分支**
   ```bash
   git branch -D main
   ```

5. **重命名新分支**
   ```bash
   git branch -m main
   ```

6. **強制推送到遠程倉庫**
   ```bash
   git push -f origin main
   ```