import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if isinstance(event, MessageEvent):
        messages=event.message.text
        if messages == 'hi': #re.match('hi',message):
            line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://doqvf81n9htmm.cloudfront.net/data/crop_article/112964/52.jpg_1140x855.jpg',
                    title='台中北屯、南屯、西屯',
                    text='想看什麼地區的房子呢？',
                    actions=[
                        PostbackTemplateAction(
                            label='北屯',
                            text=answer=='hihi',
                            data='北屯',
                            
                        ),
                        PostbackTemplateAction(
                            label='西屯',
                            text='西屯',
                            data='西屯'
                    
                        ),
                        PostbackTemplateAction(
                            label='南屯',
                            text='南屯',
                            data='南屯'
                        )
                        ]
                        )
                )
            )

        elif event.message.text == "北屯" or "西屯" or "南屯":
                area=event.message.text
                line_bot_api.reply_message(
                    event.reply_token,
                            TemplateSendMessage(
                                alt_text='CarouselTemplate',
                                template=CarouselTemplate(
                                    columns=[
                     CarouselColumn(
                         thumbnail_image_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fdvblobcdnjp.azureedge.net%2F%2FContent%2FUpload%2FPopular%2FImages%2F2018-10%2Ffa132452-c08d-4ccc-b7f9-2ca3e1f0941b_m.jpg&imgrefurl=https%3A%2F%2Fdailyview.tw%2FPopular%2FDetail%2F3071&tbnid=biebrUdHNEWHiM&vet=12ahUKEwjolLf34qr4AhUE6ZQKHUH7BWQQMygMegUIARDRAQ..i&docid=b3EFFa4mCYjMyM&w=940&h=650&q=%E9%80%8F%E5%A4%A9%E5%8E%9D&ved=2ahUKEwjolLf34qr4AhUE6ZQKHUH7BWQQMygMegUIARDRAQ',
                         title='透天',
                         text=' ',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='拆解步驟詳細介紹安裝並使用Anaconda、Python、Spyder、VScode…'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=270'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fhousezong.com%2Fwp-content%2Fuploads%2F%25E5%259C%2596%25E7%2589%25871.jpg&imgrefurl=https%3A%2F%2Fhousezong.com%2Fhouse-selection-01%2F&tbnid=Z1LF3UscxqcuNM&vet=12ahUKEwjJ2LDjrKP4AhVNDd4KHSYZAX0QMygKegUIARDQAQ..i&docid=NF226hpUHw2G7M&w=560&h=420&q=%E9%9B%BB%E6%A2%AF%E5%A4%A7%E6%A8%93&ved=2ahUKEwjJ2LDjrKP4AhVNDd4KHSYZAX0QMygKegUIARDQAQ',
                         title='電梯大樓',
                         text=' ',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='Line Bot申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2532'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                         title='華廈',
                         text=' ',
                         actions=[
                             MessageAction(
                                 label='教學',
                                 text='Telegrame申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2648'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                         title='公寓',
                         text=' ',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='Telegrame申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2648'
                             )
                         ]
                     ),
                    CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                         title='未分類',
                         text=' ',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='Telegrame申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2648'
                             )
                         ]
                     )
                 ]
             )
         )
    )
