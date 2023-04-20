import asyncio
from pyrogram import Client, filters
import pyrogram
from datetime import datetime
import time
import os
from pyrogram.errors import FloodWait







api_id = 15292568
api_hash = "ae509244400baf31bcb8c368e8e727ad"
autoactivate = True
send_to_channel = True
to_channel_base = -100169043008684123

app = Client('my_account', api_id,api_hash)



used_checks = []

def check_checks(link):
       global used_checks
       FINDED = False
       i_i=0
       # print(len(used_checks))
       if len(used_checks) != 0:
              while i_i != len(used_checks):
                     aa = used_checks[i_i].find(link)
                     # print(f"find;{aa} , link:{used_checks[i_i]} , lengh:{len(used_checks)}")
                     # print(used_checks)
                     if aa > -1:
                            i_i = len(used_checks)
                            # print("NAYDENO--------------")
                            FINDED = True
                     else:
                            i_i = i_i + 1  
       if FINDED == False:
              return False
       else:
              return True


def send_to_channel_func(chat_id,msg_id,link):
       global used_checks
       global to_channel_base
       if send_to_channel == True:
              if check_checks(link) == False:
                     app.forward_messages(to_channel_base, chat_id, msg_id).reply_text(f'С чата(fromchat): https://t.me/{app.get_chat(chat_id).username}/{str(msg_id)}')
                     used_checks.insert(0, link)
              else:
                     print('Yzeuzali')
       else:
              pass

def send_to_bot_wallet(link):
       global used_checks
       global autoactivate
       if autoactivate == True:

              if check_checks(link) == False:
                     app.send_message("wallet",f"/start {link.split('=')[1]}")
                     used_checks.insert(0, link)
              else:
                     print('Yzeuzali')


# def send_to_bot_crypto(link):
#        global autoactivate
#        if autoactivate == True:
#               # test = "/start " + link.split('=')[1]
#               app.send_message("CryptoBot",f"/start {link.split('=')[1]}")

def send_to_bot_crypto(link):
       global autoactivate
       if autoactivate == True:
              if check_checks(link) == False:
                     # test = "/start " + link.split('=')[1]
                     aaaa = app.send_message("CryptoBot", f"/start {link.split('=')[1]}").id + 1
                     
                     # print(app.get_messages("CryptoBot", aaaa))
                     timing = 100
                     iiii = 0
                     while iiii < timing:
                            if app.get_messages("CryptoBot", aaaa).empty == True:
                                   iiii = iiii + 1
                            else:
                                   iiii = timing + 1
                     # print(app.get_messages("CryptoBot", aaaa))
                     arara = app.get_messages("CryptoBot", aaaa).text.find("получили")
                     brbrb = app.get_messages("CryptoBot", aaaa).text.find("подпишитесь")
                     if arara >= 0:
                            print(app.get_messages("CryptoBot", aaaa).text)
                     elif brbrb >= 0:
                            print('brbrbr')
                            iii = 0
                            while app.get_messages("CryptoBot", aaaa).reply_markup.inline_keyboard[iii][0].url != None:
                                   print(iii,app.get_messages("CryptoBot", aaaa).reply_markup.inline_keyboard[iii][0].url)
                                   try:
                                          app.join_chat(app.get_messages("CryptoBot", aaaa).reply_markup.inline_keyboard[iii][0].url)
                                   except Exception as e:
                                          print(e)
                                   iii = iii + 1
                            time.sleep(2)
                            app.send_message("CryptoBot", f"/start {link.split('=')[1]}")
                            # send_to_bot_crypto(link)
                     else:
                            pass
              else:
                     print('Yzeuzali')



def send_to_bot_rocket(link):
       global autoactivate
       if autoactivate == True:
              if check_checks(link) == False:
                     # test = "/start " + link.split('=')[1]
                     aaaa = app.send_message("TonRocketBot", f"/start {link.split('=')[1]}").id + 1
                     
                     # print(app.get_messages("TonRocketBot", aaaa))
                     timing = 100
                     iiii = 0
                     while iiii < timing:
                            if app.get_messages("TonRocketBot", aaaa).empty == True:
                                   iiii = iiii + 1
                            else:
                                   iiii = timing + 1
                     # print(app.get_messages("TonRocketBot", aaaa))
                     arara = app.get_messages("TonRocketBot", aaaa).text.find("получили")
                     brbrb = app.get_messages("TonRocketBot", aaaa).text.find("необходимо")
                     if arara >= 0:
                            print(app.get_messages("TonRocketBot", aaaa).text)
                     elif brbrb >= 0:
                            iii = 0
                            while app.get_messages("TonRocketBot", aaaa).reply_markup.inline_keyboard[iii][0].url != None:
                                   print(iii,app.get_messages("TonRocketBot", aaaa).reply_markup.inline_keyboard[iii][0].url)
                                   try:
                                          app.join_chat(app.get_messages("TonRocketBot", aaaa).reply_markup.inline_keyboard[iii][0].url.split('https://t.me/')[1])
                                   except Exception as e:
                                          print(e)
                                   iii = iii + 1
                            time.sleep(2)
                            app.send_message("TonRocketBot", f"/start {link.split('=')[1]}")
                            # send_to_bot_rocket(link)
                     else:
                            pass
              else:
                     print('Yzeuzali')





@app.on_message(filters.command('aa',prefixes='.')& filters.me)
def aa(_,msg):
       global autoactivate
       if autoactivate == True:
              autoactivate = False
              print('== AUT0 ACT1VATE 0FF ==')
       else:
              autoactivate = True
              print('== AUT0 ACT1VATE 0N ==')
       msg.delete()

@app.on_message(filters.command('sc',prefixes='.')& filters.me)
def sc(_,msg):
       global send_to_channel
       if send_to_channel == True:
              send_to_channel = False
              print('== SEND T0 CHANNEL 0FF ==')
       else:
              send_to_channel = True
              print('== SEND T0 CHANNEL 0N ==')
       msg.delete()



@app.on_message(filters.command('usedchecks',prefixes='.')& filters.me)
def usedchecks(_,msg):
       print(used_checks)




@app.on_message(filters.command('info',prefixes='.')& filters.me)
def info(_,msg):
       print(msg.reply_to_message)
       msg.delete()
       # print(msg.reply_to_message.reply_markup.inline_keyboard[0][0].url.find("t.me/CryptoBot?start=CQ"))

@app.on_message(filters.command('fromchatid',prefixes='.')& filters.me)
def fromchatid(_,msg):
       #print(msg.forward_from_chat.id)
       msg.edit(msg.reply_to_message.forward_from_chat.id)


# @app.on_message(filters.command('test',prefixes='.')& filters.me)
# def test(_,msg):
#        print(pytesseract.image_to_string('test.png'))
#        msg.delete()

try:
       print(f" START T1ME:{datetime.now()}\n",f"AUT0ACT1VATE:{autoactivate}\n",f"SEND T0 CHANNEL:{send_to_channel}")
except Exception as e:
       print(e)





@app.on_message(filters.channel | filters.group)
def test2222(_,msg):
       #tonrocket
       #link
       try:
              # web_page_finder = msg.web_page.url.find("https://t.me/tonRocketBot?start=mc")
              web_page_finder = msg.web_page.url.lower().find("https://t.me/tonrocketbot?start=mc")
              # print(web_page_finder)
              if web_page_finder >= 0:
                     send_to_bot_rocket(msg.web_page.url)
                     print(msg.web_page.url)
                     print(datetime.now(),web_page_finder,msg.web_page.url)
                     # app.send_message(to_channel_base, msg)
                     send_to_channel_func(msg.chat.id,msg.id,msg.web_page.url)
                     # app.forward_messages(to_channel_base, msg.chat.id, msg.id).reply_text(f'С чата(fromchat): https://t.me/{app.get_chat(msg.chat.id).username}/{str(msg.id)}')
                     
              # print(datetime.now())
              #button - 
       except:
              try:
                     # print(msg.reply_markup.inline_keyboard[0][0])
                     reply_markup_finder = msg.reply_markup.inline_keyboard[0][0].url.lower().find("https://t.me/tonrocketbot?start=mc")
                     if reply_markup_finder >= 0:
                            send_to_bot_rocket(msg.reply_markup.inline_keyboard[0][0].url)
                            print(datetime.now(),reply_markup_finder,msg.reply_markup.inline_keyboard[0][0].url)
                            send_to_channel_func(msg.chat.id,msg.id,msg.reply_markup.inline_keyboard[0][0].url)
                            
                            
                     # print(datetime.now())
              except Exception as e:
                     # print(e)
                     pass



       def autoact(code):
              print(code)
       try:
              # print('aaaa')
              web_page_finder = msg.web_page.url.find("t.me/CryptoBot?start=CQ")
              if web_page_finder >= 0:
                     if msg.text.lower().find('для') > -1 or msg.text.lower().find('может активировать') > -1 or msg.text.find('0.000') > -1:
                            pass
                     else:
                            if msg.text.find('0.000') > -1:
                                   print('var 1')
                            else:
                                   # send_to_bot_crypto(msg.web_page.url)
                                   send_to_bot_crypto(msg.web_page.url)
                            print(datetime.now(),web_page_finder,msg.web_page.url)
                            # app.send_message(to_channel_base, msg)
                            send_to_channel_func(msg.chat.id,msg.id,msg.web_page.url)
       except:
              try:
                     # print(msg.reply_markup.inline_keyboard[0][0])
                     reply_markup_finder = msg.reply_markup.inline_keyboard[0][0].url.find("t.me/CryptoBot?start=CQ")
                     if reply_markup_finder >= 0:
                            if msg.text.lower().find('для') > -1 or msg.text.lower().find('может активировать') > -1 or msg.text.find('0.000') > -1:
                                   pass
                            else:
                                   # print(msg.text)
                                   if msg.text.find('0.000') > -1:
                                          print('var 1')
                                   else:
                                          # send_to_bot_crypto(msg.reply_markup.inline_keyboard[0][0].url)
                                          send_to_bot_crypto(msg.reply_markup.inline_keyboard[0][0].url)
                                   print(datetime.now(),reply_markup_finder,msg.reply_markup.inline_keyboard[0][0].url)
                                   send_to_channel_func(msg.chat.id,msg.id,msg.reply_markup.inline_keyboard[0][0].url)

              except Exception as e:
                     # print(e)
                     pass

       try:
              # print('aaaa')
              web_page_finder = msg.web_page.url.find("t.me/wallet?start=C-")
              if web_page_finder >= 0:
                     send_to_bot_wallet(msg.web_page.url)
                     print(datetime.now(),web_page_finder,msg.web_page.url)
                     # app.send_message(to_channel_base, msg)
                     send_to_channel_func(msg.chat.id,msg.id,msg.web_page.url)
                     # send_to_bot(msg.web_page.url)
       except:
              try:
                     # print(msg.reply_markup.inline_keyboard[0][0])
                     reply_markup_finder = msg.reply_markup.inline_keyboard[0][0].url.find("t.me/wallet?start=C-")
                     if reply_markup_finder >= 0:
                            send_to_bot_wallet(msg.reply_markup.inline_keyboard[0][0].url)
                            print(datetime.now(),reply_markup_finder,msg.reply_markup.inline_keyboard[0][0].url)
                            send_to_channel_func(msg.chat.id,msg.id,msg.reply_markup.inline_keyboard[0][0].url)
                            # send_to_bot(msg.reply_markup.inline_keyboard[0][0].url)
              except Exception as e:
                     # print(e)
                     pass

       # sss_finder = msg
       # ssss_finder = sss_finder.find(url)
       # if ssss_finder >= 0:
       #        print("aaaaaaaaaa")



app.run()