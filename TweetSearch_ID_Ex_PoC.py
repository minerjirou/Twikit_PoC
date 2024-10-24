import csv
import asyncio
from twikit.client import Client

async def get_unique_user_ids_and_save_to_csv(query, filename):
    client = Client(language='en')
    await client.login(auth_info_1='your_username', password='your_password')

    # 検索結果を取得
    search_results = await client.search_tweet(query=query, product='Latest', count=100)
    
    # ユーザーIDをセットに保存 (重複を自動的に排除)
    unique_user_ids = {tweet.user_id for tweet in search_results}

    # CSVファイルに保存
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['User ID'])  # ヘッダー
        for user_id in unique_user_ids:
            writer.writerow([user_id])

    await client.logout()

# 実行
query = "特定のキーワード"
filename = "unique_user_ids.csv"
asyncio.run(get_unique_user_ids_and_save_to_csv(query, filename))
