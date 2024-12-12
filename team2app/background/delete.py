class database():
    # 既存のコード...

    def delete(self, post_id):
        """
        指定されたIDの投稿を削除する関数。
        """
        conn = sqlite3.connect(self.path)
        try:
            conn.execute("DELETE FROM entry WHERE id = ?;", (post_id,))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            conn.close()

# DB
db = database("entry.db")

def body(self, request, params):
    response = '<html><header><title>sample</title><link rel="stylesheet" href="https://cdn.rawgit.com/alexanderGugel/papier/master/dist/papier-1.0.0.min.css"></header><body class="bg-subtle"><div style="width:50%;margin:0 auto">'
    
    if request == "/get":
        # 投稿用フォームを挿入
        response += '<section class="panel"><header>Post form:</header><main><form method="GET" action="/post"><input type="text" name="message" placeholder="message"><input type="submit" value="送信"></form></main></section>'

        # 投稿内容を表示
        for e in sorted(db.get(), key=lambda e: e[2], reverse=True):
            response += '<section class="panel"><header>{0}</header><main>{1}</main>'.format(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(e[2])), e[1])
            response += '<form method="GET" action="/delete"><input type="hidden" name="id" value="{0}"><input type="submit" value="削除"></form></section>'.format(e[0])

    elif request == "/post":
        if not "message" in params:
            response += "<h1>Invalid Post</h1>"
        else:
            db.post(params["message"])
            response += '<meta http-equiv="REFRESH" content="1;URL=/get"><h1>Post Successful.</h1>'
    
    elif request == "/delete":
        if not "id" in params:
            response += "<h1>Invalid Delete Request</h1>"
        else:
            db.delete(params["id"])
            response += '<meta http-equiv="REFRESH" content="1;URL=/get"><h1>Delete Successful.</h1>'
    
    else:
        response += "<h1>Invalid Request</h1>"

    # フッター
    response += '</div></body></html>'
    return response.encode('utf-8')