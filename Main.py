import tkinter as tk
from tkinter import messagebox as messagebox
import tkinter.font as font
import datetime as datetime
import gmail as gmail
import json

def ordering(label):
    now_date = str(datetime.datetime.now())
    retunCode = send_gmain()
    if(retunCode == 0):
        label['text'] = '前回メール配信日時：' + now_date
        print('前回メール配信日時：' + now_date)
        messagebox.showinfo('MailSended!', now_date + '\nメールが送信されました')
        writeHistory('[INFO] : ' + now_date + ' : メールが送信されました\n')
    else:
        messagebox.showerror('MailSendedError!', now_date + '\nメール送信に失敗しました')

def send_gmain():

    msgs = loadProperties()

    # Gmailアカウント情報
    sendUsername = msgs['from'] #'from_user@gmail.com'
    sendUserPassword = msgs['mailpass'] #'from_user_password'

    # メール送信パラメータ
    subject = msgs['subject']
    toAddr = msgs['to'] #'to_user@gmail.com'
    cc =  msgs['cc'] #'to_user@gmail.com'
    body = loadBody()

    #print(msgs)

    # メールサーバに接続して、ログインとメール送信
    try:
        print('メール送信開始')

        # Gmailへのログインとメール送信
        client = gmail.GMail(sendUsername, sendUserPassword)
        message = gmail.Message(subject=subject,to=toAddr,cc=cc,text=body)
        client.send(message)
        client.close()
        print('メール送信完了!')

    except Exception as e:
    # メール送信エラー時の対処
        try:
            client.close()
        except:
            print('メール送信エラーです。')
            return -1
        now_date = str(datetime.datetime.now())
        writeHistory('[ERROR] : ' + now_date + ' : メール送信に失敗しました\n')
        writeHistory('          ' + str(e) + '\n')
        print('メール送信エラーです。')
        return -1
    return 0

def loadBody():
    body = ''
    try:
        with open('template/body.txt') as f:
            for line in f:
                body = body + line
    except:
        print('メールテンプレートファイル読み込みエラー')
    return body

def loadProperties():
    try:
        # 読み込む JSON ファイル
        json_file = open('properties.json','r')
        # JSON ファイルのロードと辞書型へ変換
        json_dict = json.load(json_file)
    except:
        print('プロパティファイル読み込みエラー')
    return json_dict

def writeHistory(msg):
    try:
        wfile = open('history.txt','a')
        wfile.write(msg)
        wfile.flush()
    except:
        print('FileProcessError')	
    finally:
        wfile.close()

def main():
    
    msgs = loadProperties()

    # Component Variables
    root = None
    label = None
    history_label = None
    button = None

    root = tk.Tk()
    # Main Window Title
    root.title(msgs['title'])

    # Main Window SIze
    root.geometry('540x280')

    # Font Objects Create
    buttonFont = font.Font(family='メイリオ', size=24, weight='bold')
    labelFont = font.Font(family='メイリオ', size=12)
    #print(font.families())

    # Label Create
    label = tk.Label(root, text=msgs['label'],font=labelFont)
    label.pack()

    # Button Create
    button = tk.Button(root, text=msgs['button'],font=buttonFont,width=20,height=3,command= lambda : ordering(history_label))
    button.pack()

    # Label2 Create
    history_label = tk.Label(root, text='',font=labelFont,bg="#0059b3")
    history_label.pack()

    # Main Window Loop(NonClosing Process)
    root.mainloop()

# -- Main function Define--#
if __name__ == '__main__':
	main()
