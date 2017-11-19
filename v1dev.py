# -*- coding: utf-8 -*-
import LINETCR
import time
import sys
import datetime
import urllib

kokoa = LINETCR.LINE()
tino = LINETCR.LINE()
rize = LINETCR.LINE()
chiya = LINETCR.LINE()
syaro = LINETCR.LINE()
moka = LINETCR.LINE()
megu = LINETCR.LINE()

kokoa.login(token="EmMNxkESqtLLGdYimFx2.lCQlKffPrDvJ4C9I01fB4G.Mi9qkLaNGflBN5yHA7bBxM+zeW4zDyttagUtbJq73lQ=")
kokoa.loginResult()
tino.login(token="Emp1ze1uZVSmIb6R1JD4.nVVrGx/cv6f5b03ArGFU5a.FVXgKB5umtIsSaLX3wEd//9PQvSLfJ0hFQD5DSlUkzw=")
tino.loginResult()
rize.login(token="EmXghEnhwPcp05GrCJOf.2Ad+jSMK5L577woncnuh7W.2ypZiZCTMdgCQiCkMI77WJJWDgnJ+1b3xLpuZ2cUFnY=")
rize.loginResult()
chiya.login(token="EmQUsLtqrrg5dPDpk9R3.WYwUmPddvCwHomBR1CqRKW.KTi5YyuOFsP6+76NYf8Y9iz+rDks7sKzmtZ48q7QHVM=")
chiya.loginResult()
syaro.login(token="Emq4iaP5toSDPvY33GWd.2LoE6VMBQSoJV0xj2s8CRq.MdcwKXXf4/iGD73WBxmzDGajg02SAUH5y/Qm21ftvhs=")
syaro.loginResult()
moka.login(token="EmDgHCS2au797sJXV7l1.g6FOp0t4PxDBHY58MdDjSq.SOpvVx0ee2KZJVrF4CdJi3sCTYfke+wUrSi57/svigM=")
moka.loginResult()
megu.login(token="EmvEEvB0owIRu8VhK8n7.0PhcaDg6BmNNypOZPKzWPW.AwT+5Mc8Tiy4+vg5cBorBKUm3nV6KGA47vYWel/SG/k=")
megu.loginResult()

#blackList
b = ["u2c7f708769a2eb35d9ae9f73cd366e0b","u186cf7940c7de8f76a3cbc76405f5f5c"]
#admins
dp = ["u5f0e86fcdb62f7ce4f4394aa400983d0"]
rt = ["u5f0e86fcdb62f7ce4f4394aa400983d0","uf0383cc3d7ddcec7cd89cd855fe0ae4e","u56580388daf652254e4afc1dab9d2344","u79cb9ae7e629e9ee426ba565e413b251","ua057f8fe7e0486a9cb9f5d7c5e7dcd9a","ub390307c2e43a38138b555a923ee7b13","u08db961c53276824542d1e90e6242c9d","ufd18e9b10bf240f60e979d91d330eb9d"]
ad = ["u5f0e86fcdb62f7ce4f4394aa400983d0"]
ur = ["u5f0e86fcdb62f7ce4f4394aa400983d0"]

kg = dp + rt + ad + ur

#bots
c1 = kokoa.getProfile()
c2 = tino.getProfile()
c3 = rize.getProfile()
c4 = chiya.getProfile()
c5 = syaro.getProfile()
c6 = moka.getProfile()
c7 = megu.getProfile()
c8 = "%s"%(c1.mid)
c9 = "%s"%(c2.mid)
c10 = "%s"%(c3.mid)
c11 = "%s"%(c4.mid)
c12 = "%s"%(c5.mid)
c13 = "%s"%(c6.mid)
c14 = "%s"%(c7.mid)

bots = [c8,c9,c10,c11,c12,c13,c14]

#today
todaydetail = datetime.datetime.today()
gurl = {}
kickp = {}
gnamep = {}
gname = {}
br = 0
ba = 0
blistuserbye = 0
data = 100000

while True:
    op = kokoa.stream()
    try:
        msg = op.message.text
    except:
        msg = "None"
    
    if op.type == 13:
        if op.param2 in kg:
            if op.param3 in bots:
                try:
                    kokoa.acceptGroupInvitation(op.param1)
                    gr = kokoa.getGroup(op.param1)
                    gr.preventJoinByTicket = False
                    kokoa.updateGroup(gr)
                    ur = kokoa.reissueGroupTicket(op.param1)
                    tino.acceptGroupInvitationByTicket(op.param1,ur)
                    rize.acceptGroupInvitationByTicket(op.param1,ur)
                    chiya.acceptGroupInvitationByTicket(op.param1,ur)
                    syaro.acceptGroupInvitationByTicket(op.param1,ur)
                    moka.acceptGroupInvitationByTicket(op.param1,ur)
                    megu.acceptGroupInvitationByTicket(op.param1,ur)
                    gr2 = tino.getGroup(op.param1)
                    gr2.preventJoinByTicket = True
                    tino.updateGroup(gr)
                    Group = kokoa.getGroup(op.param1)
                    hello = "( ｀・∀・´)ﾉﾖﾛｼｸです！\n製作者はLollipop(ELIF)(｢・ω・)｢ﾀﾞｵ!~"
                    kokoa.sendText(op.param1,hello)
                    text = "追加してね↓\nhttp://line.me/ti/p/%40ihf7284n"
                    kokoa.sendText(op.param1,text)
                except:
                    s2 = u"グループに入室時失敗しました"
                    print s2
    else:
        pass
    if op.type == 26:
        if op.message.toType == 2:
            try:
                if op.message.contentType == 13:
                    if data == 1:
                        try:
                            gtmid = op.message.contentMetadata.get("mid")
                            print gtmid
                            pr = kokoa.getContact(gtmid)
                            text = "[displayName]\n%s\n[mid]\n%s\n[statusMessage]\n%s\n[pictureStatus]\nhttp://dl.profile.line.naver.jp/%s"%(pr.displayName,pr.mid,pr.statusMessage,pr.pictureStatus)
                            kokoa.sendText(op.message.to,text)
                        except:
                            text = "情報の取得に失敗しました。"
                            kokoa.sendText(op.message.to,text)
                if msg[0:4] == "ggr:":
                    google = "http://www.google.co.jp/"
                    kensaku = "search?q="
                    goo = msg[4:]
                    gle = urllib.quote('%s'%(goo))
                    ss = google + kensaku + gle
                    kokoa.sendText(op.message.to,ss)
                if msg == "help":
                    text = """
[ELIFBot]ヘルプ(コマンド一覧)

※現在テスト動作中です。安定して動作しないことがあります。

-権限なしで使えるコマンド-
mid = midを送信します
gid = gidを送信します

ggr:(検索する言葉) = Google検索します
ggrks = ぐぐれかす
send:(言葉) = (言葉)を喋ります

権限 = 権限を持ってるかどうか調べます

召喚 = 作者を召喚します

-権限が必要なコマンド-

note:(文) = (文)をノートに書き込みます
キッカー　= kickerが参加してない場合参加します
Friend:(mid) = midからプロフィール情報を読み込みます

speed = 速度測定

gurl-on = グループ招待URL許可
gurl-off = グループ招待URL拒否
gurl-get = グループ招待URL生成

Ginfo = グループ情報、設定表示

kick-on = 蹴り保護オン
kick-off = 蹴り保護オフ

gname-on = 名前保護オン
gname-off = 名前保護オフ

kickInvitation-on = 蹴られた人を再招待します
kickInvitation-off = 蹴られた人を再招待しません

Invitation-on = 招待保護オン
Invitation-off = 招待保護オフ

All-on = 全部の設定をオンにします
All-off = 全部の設定をオフにします

b/a = ブラリス追加
b/d = ブラリス確認

b/b = ブラリス排除

b/b-on = ブラリス招待、排除を常に行う
b/b-off = ブラリス招待、排除を常に行わない

b/r = ブラリス解除

KK:(mid) = 該当するmidの人をキック
NK:(名前) = 該当する名前の人をキック
MK:(@メンション) = メンションした人をキック

Cancel = 全キャンセル

Leave = 退会します

-権限レベル4が必要なコマンド-
debug = 知らねぇよ
"""
                    kokoa.sendText(op.message.to,text)
                if msg == "mid":
                    text = "あなたのmidは\n%s\nです。"%(op.message.from_)
                    kokoa.sendText(op.message.to,text)
                if msg == "gid":
                    text = "このグループのidは\n%s\nです。"%(op.message.to)
                    kokoa.sendText(op.message.to,text)
                if msg == "getprofile":
                    try:
                        pr = kokoa.getContact(op.message.from_)
                        text = "[displayName]\n%s\n[mid]\n%s\n[statusMessage]\n%s\n[pictureStatus]\nhttp://dl.profile.line.naver.jp/%s"%(pr.displayName,pr.mid,pr.statusMessage,pr.pictureStatus)
                        kokoa.sendText(op.message.to,text)
                    except:
                        text = "情報の取得に失敗しました。"
                        cl.sendText(op.message.to,text)
                if msg == "権限":
                    if op.message.from_ in dp:
                        text = "あなたは権限レベル4を所持しています"
                    elif op.message.from_ in rt:
                        text = "あなたは権限レベル3を所持しています"
                    elif op.message.from_ in ad:
                        text = "あなたは権限レベル2を所持しています"
                    elif op.message.from_ in ur:
                        text = "あなたは権限レベル1を所持しています"
                    else:
                        text = "あなたは権限を所持していません"
                    kokoa.sendText(op.message.to,text)
                if msg == "ggrks":
                    t1 = 'インターネット上の電子掲示板やチャットにおいて、予め自分で調べることを全くorほとんどしないまま、初歩的なことをあれこれ質問するユーザに対して、「ググれカス（または"ググレカス"、"ggrks"）」と返答を浴びせるのが一般的な用法である。\n\n'
                    t2 = "ググレカスとは「それくらい自分でググれ※1、カス野郎」の略。\n\n"
                    t3 = "この事態に触発されたふたば☆ちゃんねるの住人がネタとして“ググレカス”というローマ時代の人物をでっち上げた。\n"
                    t4 = "その後、同様の発想による亜種が幾つも生み出されるほどの一大ムーブメントとなる。･･･と言われているが、真偽は定かではない。"
                    text = t1 + t2 + t3 + t4
                    kokoa.sendText(op.message.to,text)
                    text2 = "このくらいggrks\nリンク貼っておくから\n\nhttp://www.google.co.jp/search?q=ggrks"
                    kokoa.sendText(op.message.to,text2)
                
                if msg == "time":
                    todaydetail = datetime.datetime.today()
                    text = "現在時刻は\n%s\nです。\n※取得時の時間です。若干時間がずれていることがあります"%(todaydetail)
                    kokoa.sendText(op.message.to,text)
                if msg[0:4] == "send":
                    ms = msg[5:]
                    kokoa.sendText(op.message.to,ms)
            except:
                pass
                
                
    if op.type == 26:
        if op.message.toType == 2:
            if op.message.from_ in kg:
                try:
                    if msg[0:6] == "Friend":
                        getgetmid = msg[7:]
                        try:
                            pr = kokoa.getContact(getgetmid)
                            text = "[displayName]\n%s\n[mid]\n%s\n[statusMessage]\n%s\n[pictureStatus]\nhttp://dl.profile.line.naver.jp/%s"%(pr.displayName,pr.mid,pr.statusMessage,pr.pictureStatus)
                            kokoa.sendText(op.message.to,text)
                        except:
                            text = "情報の取得に失敗しました。"
                            kokoa.sendText(op.message.to,text)
                    if msg == "キッカー":
                        try:
                            gr = kokoa.getGroup(op.message.to)
                            gr.preventJoinByTicket = False
                            kokoa.updateGroup(gr)
                            ur = kokoa.reissueGroupTicket(op.message.to)
                            tino.acceptGroupInvitationByTicket(op.message.to,ur)
                            rize.acceptGroupInvitationByTicket(op.message.to,ur)
                            chiya.acceptGroupInvitationByTicket(op.message.to,ur)
                            syaro.acceptGroupInvitationByTicket(op.message.to,ur)
                            moka.acceptGroupInvitationByTicket(op.message.to,ur)
                            megu.acceptGroupInvitationByTicket(op.message.to,ur)
                            gr2 = tino.getGroup(op.message.to)
                            gr2.preventJoinByTicket = True
                            Group = kokoa.getGroup(op.message.to)
                            text = "完了しました。"
                            kokoa.sendText(op.message.to,text)
                        except:
                            text = "正常に完了できませんでした"
                            kokoa.sendText(op.message.to,text)
                    if msg == "check":
                        text = "ELIF"
                        kokoa.sendText(op.message.to,text)
                        tino.sendText(op.message.to,text)
                        rize.sendText(op.message.to,text)
                        chiya.sendText(op.message.to,text)
                        syaro.sendText(op.message.to,text)
                        moka.sendText(op.message.to,text)
                        megu.sendText(op.message.to,text)
                    if msg == "speed":
                        start_time = time.time()
                        text = "measurement..."
                        kokoa.sendText(op.message.to,text)
                        owari = time.time() - start_time
                        text = "かかった時間は\n%s[sec]\nです。"%(owari)
                        kokoa.sendText(op.message.to,text)
                    if msg == "gurl-on":
                        gurl["%s"%(op.message.to)] = 1
                        gr = kokoa.getGroup(op.message.to)
                        gr.preventJoinByTicket = False
                        kokoa.updateGroup(gr)
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if msg == "gurl-off":
                        gurl["%s"%(op.message.to)] = 0
                        gr = kokoa.getGroup(op.message.to)
                        gr.preventJoinByTicket = True
                        kokoa.updateGroup(gr)
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if  msg == "gurl-get":
                        try:
                            key = gurl["%s"%(op.message.to)]
                        except:
                            gurl["%s"%(op.message.to)] = 1
                            key = gurl["%s"%(op.message.to)]
                        if key == 1:
                            try:
                                gr = kokoa.getGroup(op.message.to)
                                kokoa.updateGroup(gr)
                                ur = kokoa.reissueGroupTicket(op.message.to)
                                text = "%sのURLを生成しました。\n今までに取得したURLは使えなくなりました。\nhttp://line.me/ti/g/%s"%(gr.name,ur)
                                kokoa.sendText(op.message.to,text)
                            except:
                                text = "生成に失敗しました。"
                                kokoa.sendText(op.message.to,text)
                        else:
                            text = "リンク招待が有効になっていないか正常に処理出来ませんでした"
                            kokoa.sendText(op.message.to,text)
                    if msg == "kick-on":
                        kickp["%s"%(op.message.to)] = 1
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if msg == "kick-off":
                        kickp["%s"%(op.message.to)] = 0
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if msg == "b/a":
                        text = "ブラックリストに登録する連絡先ormidを送信してください"
                        ba = 1
                        kokoa.sendText(op.message.to,text)
                    elif ba == 1:
                        if msg[0:1] == "u":
                            try:
                                b.append("%s"%(msg))
                                text = "完了しました"
                                kokoa.sendText(op.message.to,text)
                                ba = 0
                            except:
                                text = "失敗しました"
                                kokoa.sendText(op.message.to,text)
                                ba = 0
                    if msg == "b/d":
                        text = "ブラックリストに登録されているのは\n%s\nです。"%(b)
                        kokoa.sendText(op.message.to,text)
                    if msg == "b/r":
                        text = "ブラックリストから削除する連絡先ormidを送信してください"
                        br = 1
                        kokoa.sendText(op.message.to,text)
                    elif br == 1:
                        if msg[0:1] == "u":
                            try:
                                b.remove("%s"%(msg))
                                text = "完了しました"
                                kokoa.sendText(op.message.to,text)
                                br = 0
                            except:
                                text = "失敗しました"
                                kokoa.sendText(op.mesage.to,text)
                                br = 0
                    if msg == "b/b":
                        blistuserbye = 1
                        #for tg in b:
                            
                    if gurl == 0:
                        gr = kokoa.getGroup(op.message.to)
                        if gr.preventJoinByTicket == False:
                            gr.preventJoinByTicket = True
                            kokoa.updateGroup(gr)
                    if msg == "data-on":
                        data = 1
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if msg == "data-off":
                        data = 0
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if msg == "gname-on":
                        gnamep["%s"%(op.message.to)] = 1
                        gr = kokoa.getGroup(op.message.to)
                        nana = gr.name
                        gname["%s"%(op.message.to)] = "%s"%(nana)
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if msg == "gname-off":
                        gnamep["%s"%(op.message.to)] = 0
                        text = "完了しました"
                        kokoa.sendText(op.message.to,text)
                    if msg[-3:-1] == "MF":
                        if "@" in msg:
                            mf1 = op.message.contentMetadata
                            mf2 = mf1['MENTION']
                            index = mf2.find('"M":"u')
                            if index == -1:
                                pass
                            else:
                                index2 = index + 5
                                index3 = index2 + 33
                                target = mf2[index2:index3]
                                pr = kokoa.getContact(target)
                                dm = pr.displayName
                                text = "%sさんのmidは%sです。"%(dm,target)
                                kokoa.sendText(op.message.to,text)
                    if msg == "debug":
                        text = "%s\n%s\n%s\n%s"%(gurl,kickp,gnamep,gname)
                        kokoa.sendText(op.message.to,text)
                    if msg == "Leave":
                        text = "またね！"
                        kokoa.sendText(op.message.to,text)
                        kokoa.leaveGroup(op.message.to)
                        tino.leaveGroup(op.message.to)
                        rize.leaveGroup(op.message.to)
                        chiya.leaveGroup(op.message.to)
                        syaro.leaveGroup(op.message.to)
                        moka.leaveGroup(op.message.to)
                        megu.leaveGroup(op.message.to)
                except:
                    pass
    if op.type == 26:
        if op.message.toType == 2:
            if op.message.from_ in kg:
                if op.message.contentType == 13:
                    if ba == 1:
                        print "aaaaaaaa"
                        try:
                            gtmid = op.message.contentMetadata.get("mid")
                            print gtmid
                            b.append("%s"%(gtmid))
                            text = "完了しました"
                            kokoa.sendText(op.message.to,text)
                            ba = 0
                        except:
                            text = "失敗しました"
                            kokoa.sendText(op.message.to,text)
                            ba = 0
                    if br == 1:
                        try:
                            gtmid = op.message.contentMetadata.get("mid")
                            b.remove("%s"%(gtmid))
                            text = "完了しました"
                            kokoa.sendText(op.message.to,text)
                            br = 0
                        except:
                            text = "失敗しました"
                            kokoa.sendText(op.message.to,text)
                            br = 0
    if op.type == 19:
        if op.param3 in bots:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        tino.kickoutFromGroup(op.param1,[op.param2])
                                        gr = tino.getGroup(op.param1)
                                        gr.preventJoinByTicket = False
                                        tino.updateGroup(gr)
                                        ur = tino.reissueGroupTicket(op.param1)
                                        kokoa.acceptGroupInvitationByTicket(op.param1,ur)
                                        tino.acceptGroupInvitationByTicket(op.param1,ur)
                                        rize.acceptGroupInvitationByTicket(op.param1,ur)
                                        chiya.acceptGroupInvitationByTicket(op.param1,ur)
                                        syaro.acceptGroupInvitationByTicket(op.param1,ur)
                                        moka.acceptGroupInvitationByTicket(op.param1,ur)
                                        megu.acceptGroupInvitationByTicket(op.param1,ur)
                                        gr.preventJoinByTicket = True
                                        tino.updateGroup(gr)
                                    except:
                                        rize.kickoutFromGroup(op.param1,[op.param2])
                                        gr = rize.getGroup(op.param1)
                                        gr.preventJoinByTicket = False
                                        rize.updateGroup(gr)
                                        ur = rize.reissueGroupTicket(op.param1)
                                        kokoa.acceptGroupInvitationByTicket(op.param1,ur)
                                        tino.acceptGroupInvitationByTicket(op.param1,ur)
                                        rize.acceptGroupInvitationByTicket(op.param1,ur)
                                        chiya.acceptGroupInvitationByTicket(op.param1,ur)
                                        syaro.acceptGroupInvitationByTicket(op.param1,ur)
                                        moka.acceptGroupInvitationByTicket(op.param1,ur)
                                        megu.acceptGroupInvitationByTicket(op.param1,ur)
                                        gr.preventJoinByTicket = True
                                        tino.updateGroup(gr)
                                except:
                                    chiya.kickoutFromGroup(op.param1,[op.param2])
                                    gr = chiya.getGroup(op.param1)
                                    gr.preventJoinByTicket = False
                                    chiya.updateGroup(gr)
                                    ur = chiya.reissueGroupTicket(op.param1)
                                    kokoa.acceptGroupInvitationByTicket(op.param1,ur)
                                    tino.acceptGroupInvitationByTicket(op.param1,ur)
                                    rize.acceptGroupInvitationByTicket(op.param1,ur)
                                    chiya.acceptGroupInvitationByTicket(op.param1,ur)
                                    syaro.acceptGroupInvitationByTicket(op.param1,ur)
                                    moka.acceptGroupInvitationByTicket(op.param1,ur)
                                    megu.acceptGroupInvitationByTicket(op.param1,ur)
                                    gr.preventJoinByTicket = True
                                    chiya.updateGroup(gr)
                            except:
                                syaro.kickoutFromGroup(op.param1,[op.param2])
                                gr = syaro.getGroup(op.param1)
                                gr.preventJoinByTicket = False
                                syaro.updateGroup(gr)
                                ur = syaro.reissueGroupTicket(op.param1)
                                kokoa.acceptGroupInvitationByTicket(op.param1,ur)
                                tino.acceptGroupInvitationByTicket(op.param1,ur)
                                rize.acceptGroupInvitationByTicket(op.param1,ur)
                                syaro.acceptGroupInvitationByTicket(op.param1,ur)
                                syaro.acceptGroupInvitationByTicket(op.param1,ur)
                                moka.acceptGroupInvitationByTicket(op.param1,ur)
                                megu.acceptGroupInvitationByTicket(op.param1,ur)
                                gr.preventJoinByTicket = True
                                syaro.updateGroup(gr)
                        except:
                            moka.kickoutFromGroup(op.param1,[op.param2])
                            gr = moka.getGroup(op.param1)
                            gr.preventJoinByTicket = False
                            moka.updateGroup(gr)
                            ur = moka.reissueGroupTicket(op.param1)
                            kokoa.acceptGroupInvitationByTicket(op.param1,ur)
                            tino.acceptGroupInvitationByTicket(op.param1,ur)
                            rize.acceptGroupInvitationByTicket(op.param1,ur)
                            chiya.acceptGroupInvitationByTicket(op.param1,ur)
                            syaro.acceptGroupInvitationByTicket(op.param1,ur)
                            moka.acceptGroupInvitationByTicket(op.param1,ur)
                            megu.acceptGroupInvitationByTicket(op.param1,ur)
                            gr.preventJoinByTicket = True
                            moka.updateGroup(gr)
                    except:
                        megu.kickoutFromGroup(op.param1,[op.param2])
                        gr = megu.getGroup(op.param1)
                        gr.preventJoinByTicket = False
                        megu.updateGroup(gr)
                        ur = megu.reissueGroupTicket(op.param1)
                        kokoa.acceptGroupInvitationByTicket(op.param1,ur)
                        tino.acceptGroupInvitationByTicket(op.param1,ur)
                        rize.acceptGroupInvitationByTicket(op.param1,ur)
                        chiya.acceptGroupInvitationByTicket(op.param1,ur)
                        syaro.acceptGroupInvitationByTicket(op.param1,ur)
                        syaro.acceptGroupInvitationByTicket(op.param1,ur)
                        moka.acceptGroupInvitationByTicket(op.param1,ur)
                        megu.acceptGroupInvitationByTicket(op.param1,ur)
                        gr.preventJoinByTicket = True
                        megu.updateGroup(gr)
                except:
                    kokoa.kickoutFromGroup(op.param1,[op.param2])
                    gr = kokoa.getGroup(op.param1)
                    gr.preventJoinByTicket = False
                    kokoa.updateGroup(gr)
                    ur = kokoa.reissueGroupTicket(op.param1)
                    kokoa.acceptGroupInvitationByTicket(op.param1,ur)
                    tino.acceptGroupInvitationByTicket(op.param1,ur)
                    rize.acceptGroupInvitationByTicket(op.param1,ur)
                    chiya.acceptGroupInvitationByTicket(op.param1,ur)
                    syaro.acceptGroupInvitationByTicket(op.param1,ur)
                    moka.acceptGroupInvitationByTicket(op.param1,ur)
                    megu.acceptGroupInvitationByTicket(op.param1,ur)
                    gr.preventJoinByTicket = True
                    kokoa.updateGroup(gr)
            except:
                pass
    if op.type == 19:
        if op.param3 in bots:
            pass
        elif op.param2 in bots:
            pass
        else:
            try:
                kkey = kickp["%s"%(op.param1)]
            except:
                kickp["%s"%(op.param1)] = 1
                kkey = kickp["%s"%(op.param1)]
            if kkey == 1:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            try:
                                                tino.kickoutFromGroup(op.param1,[op.param2])
                                                text = "強制退会は禁止です"
                                                tino.sendText(op.param1,text)
                                            except:
                                                rize.kickoutFromGroup(op.param1,[op.param2])
                                                text = "強制退会は禁止です"
                                                rize.sendText(op.param1,text)
                                        except:
                                            chiya.kickoutFromGroup(op.param1,[op.param2])
                                            text = "強制退会は禁止です"
                                            chiya.sendText(op.param1,text)
                                    except:
                                        syaro.kickoutFromGroup(op.param1,[op.param2])
                                        text = "強制退会は禁止です"
                                        syaro.sendText(op.param1,text)
                                except:
                                    moka.kickoutFromGroup(op.param1,[op.param2])
                                    text = "強制退会は禁止です"
                                    moka.sendText(op.param1,text)
                            except:
                                megu.kickoutFromGroup(op.param1,[op.param2])
                                text = "強制退会は禁止です"
                                megu.sendText(op.param1,text)
                        except:
                            kokoa.kickoutFromGroup(op.param1,[op.param2])
                            text = "強制退会は禁止です"
                            kokoa.sendText(op.param1,text)
                    except:
                        text = "Error:\n[%s]"%(todaydetail)
                        kokoa.sendText(op.param1)
                except:
                    pass

                
    if op.type == 26:
        if op.message.from_ in rt:
            if op.message.toType == 2:
                try:
                    if msg[0:2] == "KK":
                        target = msg[3:]
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            tino.kickoutFromGroup(op.message.to,[target])
                                        except:
                                            rize.kickoutFromGroup(op.message.to,[target])
                                    except:
                                        chiya.kickoutFromGroup(op.message.to,[target])
                                except:
                                    kokoa.kickoutFromGroup(op.message.to,[target])
                            except:
                                text = "Error:1\n[%s]"%(todaydetail)
                                kokoa.sendText(op.message.to,text)
                        except:
                            text = "Error:2\n[%s]"%(todaydetail)
                            kokoa.sendText(op.message.to,text)
                    if msg[0:2] == "MK":
                        if "@" in msg:
                            mf1 = op.message.contentMetadata
                            mf2 = mf1['MENTION']
                            index = mf2.find('"M":"u')
                            if index == -1:
                                pass
                            else:
                                index2 = index + 5
                                index3 = index2 + 33
                                target = mf2[index2:index3]
                                try:
                                    try:
                                        try:
                                            try:
                                                try:
                                                    tino.kickoutFromGroup(op.message.to,[target])
                                                except:
                                                    rize.kickoutFromGroup(op.message.to,[target])
                                            except:
                                                chiya.kickoutFromGroup(op.message.to,[target])
                                        except:
                                            kokoa.kickoutFromGroup(op.message.to,[target])
                                    except:
                                        text = "Error:1\n[%s]"%(todaydetail)
                                        kokoa.sendText(op.message.to,text)
                                except:
                                    text = "Error:2\n[%s]"%(todaydetail)
                                    kokoa.sendText(op.message.to,text)
                    if msg[0:2] == "NK":
                        gr = kokoa.getGroup(op.message.to)
                        mm = gr.members
                        mn = len(mm)
                        kz = 0
                        for var in range(0, mn):
                            try:
                                kazu = gr.members[kz]
                                dn = kazu.displayName
                                if msg[3:] in dn:
                                    target = kazu.mid
                                    try:
                                        try:
                                            try:
                                                try:
                                                    try:
                                                        tino.kickoutFromGroup(op.message.to,[target])
                                                        time.sleep(0.8)
                                                        kz += 1
                                                    except:
                                                        rize.kickoutFromGroup(op.message.to,[target])
                                                        time.sleep(0.8)
                                                        kz += 1
                                                except:
                                                    chiya.kickoutFromGroup(op.message.to,[target])
                                                    time.sleep(0.8)
                                                    kz += 1
                                            except:
                                                kokoa.kickoutFromGroup(op.message.to,[target])
                                                time.sleep(0.8)
                                                kz += 1
                                        except:
                                            text = "Error:1\n[%s]"%(todaydetail)
                                            kokoa.sendText(op.message.to,text)
                                    except:
                                        text = "Error:2\n[%s]"%(todaydetail)
                                        kokoa.sendText(op.message.to,text)
                                else:
                                    kz += 1
                            except:
                                text = "target not found\n[%s]"%(todaydetail)
                                kokoa.sendText(op.message.to,text)
                except:
                    pass
    if op.type == 11:
        try:
            kkkey = gnamep["%s"%(op.param1)]
        except:
            gnamep["%s"%(op.param1)] = 0
            kkkey =gnamep["%s"%(op.param1)]
        if kkkey == 1:
            try:
                kkkkey = gname["%s"%(op.param1)]
            except:
                pass
            gr = kokoa.getGroup(op.param1)
            if kkkkey == gr.name:
                pass
            else:
                gr.name = "%s"%(kkkkey)
                kokoa.updateGroup(gr)
