from flask.templating import render_template


def question(keyword_dic):
    if(keyword_dic.get("ok")=="socket open"):
        return render_template("main.html")
    elif("訂單" in keyword_dic.get("ok")):
        return render_template("order_board.html")
    elif("會員" in keyword_dic.get("ok")):
        return render_template("member_board.html")
    elif("退款" in keyword_dic.get('ok')):
        return render_template('refund.html')
    else:
        return "請問有甚麼問題呢"