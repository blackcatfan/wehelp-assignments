from flask import Flask #載入Flask
from flask import request #載入request 物件
from flask import redirect #載入redirect 函式
from flask import render_template #載入render template 函式
from flask import session #載入session 工具
import json
import mysql.connector
from mysql.connector import Error

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

@app.route("/signup", methods=["GET","POST"]) #導入登入驗證頁面
def signup():#註冊驗證函式, 判斷輸入欲註冊帳號username是否已被使用, if yes 要求輸入其它username註冊, 若無則新增資料至資料庫
    message=()
    website_db = mysql.connector.connect(
    host='127.0.0.1',          # 主機名稱
    user='root',        # 帳號
    password='101@Taiwan',# 密碼
    database='website')

    NewNickNameInput=request.form["NewNickName"]#採用request.form 指令取表單資訊-使用者暱稱
    NewAccountNameInput=request.form["NewAccountName"]#採用request.form 指令取表單資訊-帳號
    NewPasswordInput=request.form["NewAccountPassword"]#採用request.form 指令取表單資訊-密碼    
    sql= "INSERT INTO member(name, username, password) VALUES (%s,%s,%s)" #寫入member 資料表指令
    val=(NewNickNameInput,NewAccountNameInput,NewPasswordInput)
    AccountNameCheck = website_db.cursor()
    AccountNameCheck.execute("SELECT COUNT(*) FROM member WHERE username=%s",(NewAccountNameInput,)) 
    AccountNameCheck_result= AccountNameCheck.fetchone()[0]# will be 1 if there is such a row, 0 if there is not

    if AccountNameCheck_result==1:
    # if AccountNameCheck_result==1:
        return redirect("/error/?message=此帳號已被註冊過了,請重新註冊")#重複的帳號, 不允許註冊

    else: #將此未曾註冊的member資訊, 寫入資料庫 https://www.itread01.com/content/1546822113.html

        try:
            sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s);"
            new_data = (NewNickNameInput, NewAccountNameInput, NewPasswordInput)
            cursor = website_db.cursor()
            cursor.execute(sql, new_data)

            # 確認資料有存入資料庫
            website_db.commit()
            website_db.close()
    
        except Error as e:
            print("資料庫連接失敗：", e)

        finally:
            if (website_db.is_connected()):
                cursor.close()
                website_db.close()
        return render_template("index.html") #按照指示導回首頁


@app.route("/signin", methods=["GET","POST"]) #導入登入驗證頁面
def signin():#登入驗證函式
    message=()
    website_db = mysql.connector.connect(
    host='127.0.0.1',          # 主機名稱
    user='root',        # 帳號
    password='101@Taiwan',# 密碼
    database='website')
    NameInput=request.form["AccountName"]#採用request.form 指令取表單資訊-帳號
    PasswordInput=request.form["AccountPassword"]#採用request.form 指令取表單資訊-密碼
    CheckCursor = website_db.cursor()
    CheckCursor.execute("SELECT COUNT(*) FROM member WHERE username=%s AND password=%s", (NameInput, PasswordInput)) 
    #用輸入的帳號密碼值是跑CheckCursor, 如果有找到相符的值, fetchone()[0]會有值=1 
    result = CheckCursor.fetchone()[0] # will be 1 if there is such a row, 0 if there is not

    
    if result == 1:#兩欄位輸入正確資訊,導入登入成功頁面
        session["AccountNameInSession"]=request.form["AccountName"] #將登入帳號放入session紀錄登入狀態
        GetName = website_db.cursor()
        GetName.execute("SELECT name FROM member WHERE username=%s AND password=%s", (NameInput, PasswordInput)) 
        GetName_result = CheckCursor.fetchone()[0]#取得登入會員的name
        GetName.close()
        website_db.close()
        return render_template("member.html",name=GetName_result) #把會員名稱帶入member.html
    
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
    return "<h1>失敗頁面<br><br></h1>{}".format(ErrorMessage)
    #return render_template("error.html",name=ErrorMessage)

@app.route("/signout") #登出頁面
def signout():#再登入畫面按登出鍵後導入此頁
    session.clear() #登出後清空cookie內的sessuon
    return redirect("/")
#啟動網站伺服器, terminal 要跑..http://127.0.0.1:5000/才會有資料, 否則出現錯誤
app.run(port=3000)#改變埠號from 5000 to 3000 