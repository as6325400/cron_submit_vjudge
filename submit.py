import os
import json
import base64
import urllib.parse
import cloudscraper
from dotenv import load_dotenv

# 讀取 .env
load_dotenv()

USERNAME = os.getenv("VJUDGE_USERNAME")
PASSWORD = os.getenv("VJUDGE_PASSWORD")
CONTEST_ID = os.getenv("CONTEST_ID")
print(os.getenv("PROBLEMS"))
PROBLEMS = json.loads(os.getenv("PROBLEMS"))
print(PROBLEMS)

# 建立 VJudge Session
scraper = cloudscraper.create_scraper()

# 1️⃣ 登入 VJudge
login_url = "https://vjudge.net/user/login"
login_data = {"username": USERNAME, "password": PASSWORD}
login_response = scraper.post(login_url, data=login_data)

if "success" not in login_response.text:
    print("❌ 登入失敗，請檢查帳號密碼")
    exit()

print("✅ 登入成功")

# 2️⃣ 取得 `JSESSIONID`
cookies = scraper.cookies.get_dict()
if "JSESSIONID" not in cookies:
    print("❌ 無法獲取 JSESSIONID，登入可能失敗")
    exit()

print(f"✅ 獲取 JSESSIONID: {cookies['JSESSIONID']}")

# 3️⃣ 遍歷要提交的題目
for problem, info in PROBLEMS.items():
    language = info["language"]
    file_path = info["file"]

    if not os.path.exists(file_path):
        print(f"❌ {problem} 題程式碼檔案 {file_path} 不存在，跳過")
        continue

    # 讀取程式碼
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    # URL + Base64 編碼
    encoded_source = base64.b64encode(urllib.parse.quote(source_code).encode()).decode()

    # 4️⃣ 發送提交請求
    submit_url = f"https://vjudge.net/contest/submit/{CONTEST_ID}/{problem}"
    submit_data = {
        "method": "0",
        "language": language,
        "open": "1",
        "source": encoded_source,
        "password": ""  # 比賽無密碼則留空
    }

    response = scraper.post(submit_url, data=submit_data, cookies=cookies)

    # 5️⃣ 確認提交成功
    if response.status_code == 200 and "success" in response.text:
        print(f"✅ 題目 {problem} 提交成功！")
    else:
        print(f"❌ 題目 {problem} 提交失敗")
        print(response.text)
