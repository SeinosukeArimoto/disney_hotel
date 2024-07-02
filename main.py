import requests
import os

def check_availability():
    url = "https://reserve.tokyodisneyresort.jp/hotel/api/queryHotelPriceStock/"
    
    headers = {
        "User-Agent": "PostmanRuntime/7.38.0"
    }
    
    data = {
        "commodityCD": "HOTDHSCL0005N",
        "useDate": "20240901",
        "stayingDays": "1",
        "adultNum": "2",
        "childNum": "0",
        "roomsNum": "1",
        "stockQueryType": "3",
        "rrc3005ProcessingType": "update"
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if "remainStockNum" in response.text:
        send_line_notify("ディズニーホテルに空きが出ました！")
        return True
    return False

def send_line_notify(message):
    line_notify_token = os.environ.get('LINE_NOTIFY_TOKEN')
    if not line_notify_token:
        print("LINE_NOTIFY_TOKEN is not set")
        return
    
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": message}
    requests.post(line_notify_api, headers=headers, data=data)

if __name__ == "__main__":
    print("ディズニーホテル空き状況をチェックしています...")
    if check_availability():
        print("空きが見つかりました。LINE Notifyで通知を送信しました。")
    else:
        print("空きはありませんでした。")
