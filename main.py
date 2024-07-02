import requests

# リクエストURLとヘッダー
url = 'https://reserve.tokyodisneyresort.jp/hotel/api/queryHotelPriceStock/'
headers = {
    'User-Agent': 'PostmanRuntime/7.38.0'
}

# リクエストパラメータ
payload = {
    'commodityCD': 'HOTDHSCL0005N',
    'useDate': '20240901',
    'stayingDays': '1',
    'adultNum': '2',
    'childNum': '0',
    'roomsNum': '1',
    'stockQueryType': '3',
    'rrc3005ProcessingType': 'update'
}

# Line Notifyのトークン
line_notify_token = 'cvopaAfNZVxLf9wzZ0VhrPVF1z18a8n3g8moPx1npiG'
line_notify_url = 'https://notify-api.line.me/api/notify'

def check_hotel_availability():
    # ホテルの空き状況を問い合わせる
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        # レスポンスに'remainStockNum'が含まれているかどうかをチェック
        if 'remainStockNum' in response.text:
            # Line Notifyで通知する
            message = 'ディズニーのホテルに空きがあります！'
            line_notify_headers = {  # ここを修正
                'Authorization': f'Bearer {line_notify_token}'
            }
            data = {
                'message': message
            }
            requests.post(line_notify_url, headers=line_notify_headers, data=data)  # ここを修正
        else:
            print('空きはありませんでした。')
    else:
        print(f'リクエストが失敗しました。ステータスコード: {response.status_code}')
        
if __name__ == '__main__':
    check_hotel_availability()


