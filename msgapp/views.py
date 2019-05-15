from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.


def msgproc(request):
    dataline = []
    if request.method == "POST":
        user_a = request.POST.get("userA", None)
        user_b = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}--\n".format(user_b, user_a, msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        user_c = request.GET.get("userC", None)
        if user_c is not None:
            with open("msgdata.txt", 'r') as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == user_c:
                        cnt += 1
                        d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3], }
                        dataline.append(d)
                    if cnt >= 10:
                        break
    return render(request, "MsgSingleWeb.html", {"data": dataline})


def homeproc(request):
    response = HttpResponse()
    response.write("<br>")
    response.write("<h1>这是首页，请点击<a href='./msggate'>这里</a>继续访问</h1>")
    response.write("<br>")
    response.write("<h1><em>亮亮</em>的第一个网页</h1>")
    response.write("<br>")
    response.write("<p> ---- 站点管理者：<strong>徐亮亮</strong></p>")
    response.write("管理员请点击<a href='./admin'>这里</a>")
    response.write("<br>")
    response.write("<h1>青春</h1>")
    response.write("<p> 青春不是年华，而是心境；青春不是桃面、丹唇、柔膝，而是深沉的意志、恢宏的想像、炽热的感情；青春是生命的深泉涌流。"
                   "<br>青春气贯长虹，勇锐盖过怯弱，进取压倒苟安。如此锐气，二十后生有之，六旬男子则更多见。年岁有加，并非垂老；理想丢弃，方堕暮年。"
                   "<br>岁月悠悠，衰微只及肌肤；热忱抛却，颓唐必致灵魂。忧烦、惶恐、丧失自信，定使心灵扭曲，意气如灰。"
                   "<br>无论年届花甲，抑或二八芳龄，心中皆有生命之欢乐，奇迹之诱惑，孩童般天真久盛不衰。人的心灵应如浩淼瀚海，只有不断接纳美好、希望、欢乐、勇气和力量的百川，才能青春永驻、风华长存。"
                   "<br>一旦心海枯竭，锐气便被冰雪覆盖，玩世不恭、自暴自弃油然而生，即使年方二十，实已垂垂老矣；然则只要虚怀若谷，让喜悦、达观、仁爱充盈其间，你就有望在八十高龄告别尘寰时仍觉年轻。</p>")
    response.write("<br><p>----作者：<strong>塞缪尔·厄尔曼</strong></p>")
    return response
    # return HttpResponse("<h1>这是首页，请点击<a href='./msggate'>这里</a>继续访问</h1>")
