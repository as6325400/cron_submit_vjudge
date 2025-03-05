import os
import json
import base64
import urllib.parse
import cloudscraper
from dotenv import load_dotenv

# Load .env
load_dotenv()

USERNAME = os.getenv("VJUDGE_USERNAME")
PASSWORD = os.getenv("VJUDGE_PASSWORD")
CONTEST_ID = os.getenv("CONTEST_ID")
print(os.getenv("PROBLEMS"))
PROBLEMS = json.loads(os.getenv("PROBLEMS"))
print(PROBLEMS)

# Create VJudge session
scraper = cloudscraper.create_scraper()

# 1️⃣ Log in to VJudge
login_url = "https://vjudge.net/user/login"
login_data = {"username": USERNAME, "password": PASSWORD}
login_response = scraper.post(login_url, data=login_data)

if "success" not in login_response.text:
    print("❌ Login failed. Please check your username and password.")
    exit()

print("✅ Login successful.")

# 2️⃣ Retrieve `JSESSIONID`
cookies = scraper.cookies.get_dict()
if "JSESSIONID" not in cookies:
    print("❌ Failed to retrieve JSESSIONID. Login may have failed.")
    exit()

print(f"✅ JSESSIONID retrieved: {cookies['JSESSIONID']}")

# 3️⃣ Iterate over problems to submit
for problem, info in PROBLEMS.items():
    language = info["language"]
    file_path = info["file"]

    if not os.path.exists(file_path):
        print(f"❌ Code file {file_path} for problem {problem} does not exist. Skipping.")
        continue

    # Read source code
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    # URL + Base64 encode
    encoded_source = base64.b64encode(urllib.parse.quote(source_code).encode()).decode()

    # 4️⃣ Send submission request
    submit_url = f"https://vjudge.net/contest/submit/{CONTEST_ID}/{problem}"
    submit_data = {
        "method": "0",
        "language": language,
        "open": "1",
        "source": encoded_source,
        "password": ""  # Leave empty if the contest has no password
    }

    response = scraper.post(submit_url, data=submit_data, cookies=cookies)

    # 5️⃣ Verify submission success
    if response.status_code == 200 and "success" in response.text:
        print(f"✅ Problem {problem} submitted successfully!")
    else:
        print(f"❌ Submission failed for problem {problem}.")
        print(response.text)
