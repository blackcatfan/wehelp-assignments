from flask import Flask #載入Flask
from flask import request #載入request 物件
from flask import redirect #載入redirect 函式
from flask import render_template #載入render template 函式
from flask import session #載入session 工具
import json
app=Flask(
    __name__,
    static_folder="public",#靜態檔案資料夾名稱
    static_url_path="/",#靜態檔案,網址路徑
)# 建立application 物件
#建立首頁&使用template連結至index.html
app.secret_key="blackcatisbest" #設定session的密鑰

@app.route("/")#連線到首頁或建立回應對應路徑
def index():#回應網站首頁連線的函式
    return render_template("index.html") #套入板模至html
@app.route("/signin", methods=["GET","POST"]) #導入登入驗證頁面
def signin():#登入驗證函式
    message=()
    NameInput=request.form["AccountName"]#採用request.form 指令取表單資訊-帳號
    PasswordInput=request.form["AccountPassword"]#採用request.form 指令取表單資訊-密碼
    session["AccountNameInSession"]=request.form["AccountName"] #將登入帳號放入session紀錄登入狀態
    if NameInput == "test" and PasswordInput =="test":#兩欄位輸入正確資訊,導入登入成功頁面
        return redirect("/member/")
    elif len(NameInput) ==0 or len(PasswordInput) == 0:   
        return redirect("/error/?message=請輸入帳號、密碼")#若任一欄位無輸入, 則資料長度為空, 提示再輸入訊息
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")#若兩欄位都輸入且錯誤, 提示輸入不正確
@app.route("/member/") #登入成功頁面
def member():   
    if "AccountNameInSession" in session: #若session有寫入登入資訊, 則帶出本page內容
        return render_template("member.html")
    else:
        return redirect("/")#若session為空, 則導回登入頁面         
@app.route("/error/") #登入失敗頁面
def error():
    ErrorMessage=request.args.get("message") #根據失敗帶入不同的message
    return "<h1>失敗頁面<br></h1>{}".format(ErrorMessage)
@app.route("/signout") #登出頁面
def signout():#再登入畫面按登出鍵後導入此頁
    session.clear() #登出後清空cookie內的sessuon
    return redirect("/")
#啟動網站伺服器, terminal 要跑..http://127.0.0.1:5000/才會有資料, 否則出現錯誤
app.run(port=3000)#改變埠號from 5000 to 3000 