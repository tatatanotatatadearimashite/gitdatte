import sqlite3

from flask import Flask , render_template , request , redirect ,session

import datetime

import random


app = Flask(__name__)

app.secret_key = 'sunabako'




@app.route("/")
def index():
        return render_template("seisaku.html")



@app.route ("/login" , methods=["GET"])
def login_get():
        if "user_id" in session :
                return render_template("enterpage.html")
        else:
                return render_template("login.html")



@app.route("/login" , methods=["POST"])
def login_post():
        # user_id = session["user_id"]
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect("seisaku.db")
        c = conn.cursor()
        c.execute("select id from user where name = ? and password = ?" , (name,password))
        user_id = c.fetchone()
        conn.close()
        if user_id is None :
                return render_template("login.html")
        else:
                session["user_id"] = user_id[0]
                return render_template("enterpage.html")



@app.route('/logout')
def logout():
        session.pop("user_id", None)
        return redirect('/login')



@app.route("/regist" , methods =["GET"])
def regist_get():
        if "user_id" in session:
                return render_template("enterpage.html")
        else :
                return render_template("regist.html")



@app.route("/regist" , methods=["POST"])
def regist_post():
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect("seisaku.db")
        c = conn.cursor()
        c.execute("INSERT INTO user values(null,?,?)" , (name,password))
        conn.commit()
        conn.close()
        return redirect("/login")



@app.route("/regist" , methods=["POST"])
def regist2_post():
        # name = request.form.get("name")
        # password = request.form.get("password")
        conn = sqlite3.connect("seisaku.db")
        c = conn.cursor()
        # c.execute("INSERT INTO holiday (lunch, walk, movie, shopping, hiking, game, read, homemovie, clean, relax) values(0,0,0,0,0,0,0,0,0,0)")
        c.execute("INSERT INTO holiday values(0,0,0,0,0,0,0,0,0,0)" , (lunch, walk, movie, shopping, hiking, game, read, homemovie, clean, relax))
        # c.execute("INSERT INTO holiday values(null,0,0,0,0,0,0,0,0,0,0)")
        conn.commit()
        conn.close()
        return redirect("/login")




# @app.route('/keijiban',methods=["POST"])
# def keijiban_post():

# @app.route("/history")
# def history():
#         return render_template('/history.html')



@app.route("/outside",methods = ["GET","POST"])
def outside():
        # x = ["食事","散歩","映画","買い物" ,"ハイキング" ,"sunabacoへ行く"]
        x = ["https://cdn.discordapp.com/attachments/654119593803251745/656323410380455948/18e85da701a2ff6c.png","https://cdn.discordapp.com/attachments/654119593803251745/656323412544847872/7c8c9bd64e3544ee.png","https://cdn.discordapp.com/attachments/654119593803251745/656323408115793930/72149bd2977ff92f.png","https://cdn.discordapp.com/attachments/654119593803251745/656323405687029771/018f582e29a39db8.png" ,"https://cdn.discordapp.com/attachments/654119593803251745/656323416491556894/ef2857b7c610c996.png" ,"https://cdn.discordapp.com/attachments/654119593803251745/655948175454240768/SUNABACO.png"]
        y = random.choice(x)
        k = random.choice(x)
        l = random.choice(x)
        m = random.choice(x)
        if y == "食事":
                n = '/lunch' 
        
        elif y == "散歩":
                n = '/walk' 
        
        elif y == "映画":
                n = '/movie' 
        
        elif y == "買い物":
                n = '/shopping' 
        
        elif y == "ハイキング":
                n = '/hiking' 
        
        # elif y == "sunabacoへ行く":
        elif y == "https://cdn.discordapp.com/attachments/654119593803251745/655948175454240768/SUNABACO.png":
                n = '/sunabaco' 
        




        if k == "食事":
                o = '/lunch' 
        
        elif k == "散歩":
                o = '/walk' 
        
        elif k == "映画":
                o = '/movie' 
        
        elif k == "買い物":
                o = '/shopping' 
        
        elif k == "ハイキング":
                o = '/hiking' 
        
        elif k == "sunabacoへ行く":
                o = '/sunabaco' 
        


        if l == "食事":
                p = '/lunch' 
        
        elif l == "散歩":
                p = '/walk' 
        
        elif l == "映画":
                p = '/movie' 
        
        elif l == "買い物":
                p = '/shopping' 
        
        elif l == "ハイキング":
                p = '/hiking' 
        
        elif l == "sunabacoへ行く":
                p = '/sunabaco' 
        


        if m == "食事":
                q = '/lunch' 
        
        elif m == "散歩":
                q = '/walk' 
        
        elif m == "映画":
                q = '/movie' 
        
        elif m == "買い物":
                q = '/shopping' 
        
        elif m == "ハイキング":
                q = '/hiking' 
        
        elif m == "sunabacoへ行く":
                q = '/sunabaco' 
        
        return render_template('/outside.html',y = y,k = k,l = l,m = m,n = n,o = o,p = p, q = q)



@app.route("/inside",methods = ["GET","POST"])
def inside():
        a = ["ゲーム","読書","家で映画鑑賞","掃除、片付け" ,"ダラダラ" ]

        b = random.choice(a)
        c = random.choice(a)
        d = random.choice(a)
        e = random.choice(a)
        # f = random.choice(a)
        
        # if b == "ゲーム":
        #         c = "スクリーンショット (50).png"

        if b == "ゲーム":
                bb = '/game' 
        
        elif b == "読書":
                bb = '/read' 
        
        elif b == "家で映画鑑賞":
                bb = '/homemovie' 
        
        elif b == "掃除、片付け":
                bb = '/clean' 
        
        elif b == "ダラダラ":
                bb = '/relax' 
        




        if c == "ゲーム":
                cc = '/game' 
        
        elif c == "読書":
                cc = '/read' 
        
        elif c == "家で映画鑑賞":
                cc = '/homemovie' 
        
        elif c == "掃除、片付け":
                cc = '/clean' 
        
        elif c == "ダラダラ":
                cc = '/relax' 




        if d == "ゲーム":
                dd = '/game' 
        
        elif d == "読書":
                dd = '/read' 
        
        elif d == "家で映画鑑賞":
                dd = '/homemovie' 
        
        elif d == "掃除、片付け":
                dd = '/clean' 
        
        elif d == "ダラダラ":
                dd = '/relax' 


                
        if e == "ゲーム":
                ee = '/game' 
        
        elif e == "読書":
                ee = '/read' 
        
        elif e == "家で映画鑑賞":
                ee = '/homemovie' 
        
        elif e == "掃除、片付け":
                ee = '/clean' 
        
        elif e == "ダラダラ":
                ee = '/relax' 


                
        # if f == "ゲーム":
        #         ff = '/game' 
        
        # elif f == "読書":
        #         ff = '/read' 
        
        # elif f == "家で映画鑑賞":
        #         ff = '/homemovie' 
        
        # elif f == "掃除、片付け":
        #         ff = '/clean' 
        
        # elif f == "ダラダラ":
        #         ff = '/relax' 


        
        return render_template('/inside.html',b = b,c = c,d = d,e = e,bb = bb,cc = cc,dd = dd,ee = ee)
        # return render_template('/inside.html',b = b,)



@app.route ("/history")
def history():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("SELECT IFNULL(lunch,0), IFNULL(walk,0), IFNULL(movie,0), IFNULL(shopping,0), IFNULL(hiking,0), IFNULL(sunabaco,0), IFNULL(game,0)game, IFNULL(read,0), IFNULL(homemovie,0), IFNULL(clean,0), IFNULL(relax,0) from holiday")
        # c.execute("SELECT lunch, walk, movie, shopping, hiking, game, read, homemovie, clean, relax from holiday")
        task_list = []
        for row in c.fetchall():
                task_list.append({"lunch":row[0],"walk":row[1],"movie":row[2],"shopping":row[3],"hiking":row[4],"sunabaco":row[5],"game":row[6],"read":row[7],"homemovie":row[8],"clean":row[9],"relax":row[10]})
        c.close()
        return render_template("history.html", task_list = task_list)

        # if lunch == null:
        #         lunch = 0
        # if "lunch" ==null:
        #         "lunch" = 0
        # return render_template("history.html", task_list = task_list)





@app.route("/reset1")
def reset1():
        conn = sqlite3.connect("seisaku.db")
        c = conn.cursor()
        # c.execute("DELETE lunch, walk, movie, shopping, hiking from holiday")
        c.execute("UPDATE holiday SET lunch = null, walk = null, movie = null, shopping = null, hiking = null")
        conn.commit()
        conn.close()
        return redirect("/history")





@app.route("/reset2")
# def reset2(id):
def reset2():
        conn = sqlite3.connect("seisaku.db")
        c = conn.cursor()
        c.execute("UPDATE holiday SET game = null, read = null, homemovie = null, clean = null, relax = null")
        # c.execute("DELETE game, read, homemovie, clean, relax FROM holiday")
        # c.execute("DELETE FROM holiday")
        # c.execute("DELETE FROM holiday WHERE game, read, homemovie, clean, relax")
        conn.commit()
        conn.close()
        return redirect("/history")




# @app.reset("/reset")
# def reset():
#         conn = sqlite3.connect("seisaku.db")
#         c = conn.cursor()
#         c.execute("delete lunch, walk, movie, shopping, hiking, game, read, homemovie, clean, relax from holiday")
#         lunch, walk, movie, shopping, hiking, game, read, homemovie, clean, relax = c.fetchall()
#         conn.close()



        # if task is not None:

        #         task = task[0]
        # else:
        #         return"空っぽなのおお いやああん"
        # item = {"lunch" = lunch, "walk" = walk, "movie" = movie, "shopping" = shopping, hiking, game, read, homemovie, clean, relax}


        # return render_template("edit.html")



# @app.route("/lunch" , methods = ["POST"])

@app.route("/lunch")
def lunch():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET lunch = lunch + 1")
        conn.commit()
        conn.close()
        return render_template('/lunch.html')


@app.route("/walk")
def walk():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET walk = walk + 1")
        conn.commit()
        conn.close()
        return render_template('/walk.html')


@app.route("/movie")
def movie():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET movie = movie + 1")
        conn.commit()
        conn.close()
        return render_template('/movie.html')


@app.route("/shopping")
def shopping():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET shopping = shopping + 1")
        conn.commit()
        conn.close()
        return render_template('/shopping.html')


@app.route("/hiking")
def hiking():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET hiking = hiking + 1")
        conn.commit()
        conn.close()
        return render_template('/hiking.html')


@app.route("/sunabaco")
def sunabaco():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET sunabaco = sunabaco + 1")
        conn.commit()
        conn.close()
        return render_template('/sunabaco.html')




@app.route("/game")
def game():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET game = game + 1")
        conn.commit()
        conn.close()
        return render_template('/game.html')


@app.route("/read")
def read():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET read = read + 1")
        conn.commit()
        conn.close()
        return render_template('/read.html')


@app.route("/homemovie")
def homemovie():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET homemovie = homemovie + 1")
        conn.commit()
        conn.close()
        return render_template('/homemovie.html')


@app.route("/clean")
def clean():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET clean = clean + 1")
        conn.commit()
        conn.close()
        return render_template('/clean.html')


@app.route("/relax")
def relax():
        conn = sqlite3.connect('seisaku.db')
        c = conn.cursor()
        c.execute("UPDATE holiday SET relax = relax + 1")
        conn.commit()
        conn.close()
        return render_template('/relax.html')




# @app.route("/weeksum")
# def weeksum():
#         conn = sqlite3.connect('seisaku.db')
#         c = conn.cursor()
#         c.execute("SELECT MAX(SUM(lunch), SUM(walk) ,SUM(movie) ,SUM(shopping) ,SUM(hiking) ,SUM(sunabaco) ,SUM(game) ,SUM(read) ,SUM(homemovie) ,SUM(clean) ,SUM(relax)) from holiday WHERE create_date BETWEEN (CURDATE() - INTERVAL 7 DAY) AND (CURDATE() + INTERVAL 1 DAY)")
#         conn.commit()
#         conn.close()
#         if MAX == SUM(lunch):
#                 a1 = "今週はこれが人気です"
#         if MAX == SUM(walk):
#                 a1 = "今週はこれが人気です"
#         if MAX == SUM(movie):
#                 a1 = "今週はこれが人気です"
#         if MAX == SUM(shopping):
#                 a2 = "今週はこれが人気です"
#         if MAX == SUM(hiking):
#                 a3 = "今週はこれが人気です"
#         if MAX == SUM(sunabaco):
#                 a4 = "今週はこれが人気です"
#         if MAX == SUM(game):
#                 a5 = "今週はこれが人気です"
#         if MAX == SUM(read):
#                 a6 = "今週はこれが人気です"
#         if MAX == SUM(homemovie):
#                 a7 = "今週はこれが人気です"
#         if MAX == SUM(clean):
#                 a8 = "今週はこれが人気です"
#         if MAX == SUM(relax):
#                 a9 = "今週はこれが人気です"
#         return render_template('/outside.html')






@app.errorhandler(404)
def notfound(code):
        return "お探しのページは見つかりませんでした。入力ミスがないか確認して再度お試し下さい"




if __name__ == "__main__":
        app.run(debug = True)

