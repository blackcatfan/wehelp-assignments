import  urllib.request as request
import json
import csv

weblink="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(weblink) as response:
  data=json.load(response) #利用json 模組處理json 資料格式, 這裡要用load非loads
  travel_list=data["result"]["results"] #觀光局的旅遊景點資訊

with open('data.csv', 'w', encoding="utf-8", newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=' ')  # 以空白分隔欄位，建立 CSV 檔寫入器
  for i in travel_list:
    area=i["address"][5:8]#從住址裡面取區域資訊
    image_getlink=i["file"]
    image_addcomma=image_getlink.replace('https', ',https')
    image_removefirstcomma=image_addcomma[1:]
    image_spiltstr=image_removefirstcomma.split(',')
    first_image=image_spiltstr[0]
    csvfile.write(i["stitle"]+","+area+","+i["longitude"]+","+i["latitude"]+","+first_image+"\n")