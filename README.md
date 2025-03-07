# 用處
自動定時一小時上傳一次 Code 到 Vjudge, 避免伺服器抖動所照成的影響

# 使用教學
## 設定環境變數

```
# VJudge 登入資訊
VJUDGE_USERNAME=your_username
VJUDGE_PASSWORD=your_password

# 比賽 ID
CONTEST_ID=698494

# 提交題目與程式碼位置 (使用 JSON 格式)
PROBLEMS={"A": {"language": "5", "file": "solutions/A.cpp"},"B": {"language": "5", "file": "solutions/B.cpp"},"C": {"language": "6", "file": "solutions/C.py"},"D": {"language": "6", "file": "solutions/D.py"}}
```

去 Setting -> Secret and variable 設定該 Repo 的環境變數, 範例如圖, 可以參考 example.env
![截圖 2025-03-07 晚上9 53 26](https://github.com/user-attachments/assets/e80d98af-36fe-42a9-8df3-fbc739de93e0)

### PROBLEMS 設定
其中在 PROBLEMS 裡面, "language" 這個所對應的數字可以從 Vjudge 看
![截圖 2025-03-07 晚上10 01 07](https://github.com/user-attachments/assets/58794f13-22e3-4110-94c7-3ab13536cd65)
像是 5 在這題對應的就是 C++ 11

而 "file" 比較好懂, 就是你在 Repo 中所儲存的路徑


## 打開 Github Action
![截圖 2025-03-07 晚上10 04 59](https://github.com/user-attachments/assets/9a94c0f3-81e9-4e28-aed0-18e7fde20d98)
在這個頁面
