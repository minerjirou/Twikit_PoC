import csv
import asyncio
from twikit import Client

client = Client('ja-JP')

# 既存のCSVファイルからすでに保存されたユーザーIDを読み込む関数
def load_existing_user_ids(csv_file):
    existing_user_ids = set()
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # ヘッダーをスキップ
            for row in reader:
                existing_user_ids.add(row[0])  # ユーザーIDのカラムをセットに追加
    except FileNotFoundError:
        pass  # ファイルがない場合は新規作成として扱う
    return existing_user_ids

async def main():
    # cookies.json からログイン情報を読み込む
    client.load_cookies("cookies.json")

    # ツイートを検索 (recentで最新のツイートを取得)
    tweets = await client.search_tweet("#海外出稼ぎ", count=40, product='Latest')
    
    # 既存のCSVファイルからユーザーIDをロード
    existing_user_ids = load_existing_user_ids(filename)
    
    # 検索結果をCSVファイルに保存
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not existing_user_ids:  # 既存ファイルがなければヘッダーを書き込む
            writer.writerow(['User ID', 'User Name', 'Screen Name'])
        
        for tweet in tweets:
            if tweet.user.id not in existing_user_ids:  # ユーザーIDに重複がなければ書き込む
                writer.writerow([tweet.user.id, tweet.user.name, tweet.user.screen_name])
                existing_user_ids.add(tweet.user.id)  # 新しいユーザーIDをセットに追加

# 実行
filename = "tweet_data.csv"
asyncio.run(main())
