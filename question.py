from flask.templating import render_template


def question(keyword_dic):
    if(keyword_dic.get("ok")=="socket open"):
        return "歡迎使用客服機器人"
    elif("訂單" in keyword_dic.get("ok")):
        return render_template("order_board.html")
    else:
        return "請問有甚麼問題呢"