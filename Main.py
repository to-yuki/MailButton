import tkinter as tk
from tkinter import messagebox as messagebox
import tkinter.font as font
import datetime as datetime
import gmail as gmail


def ordering(label):
    send_gmain()
    now_date = str(datetime.datetime.now())
    label['text'] = '前回発注日時：' + now_date
    print('前回発注日時：' + now_date)
    messagebox.showinfo('MailSended!', now_date+'\n発注メールが送信されました')

def send_gmain():
    # Gmailアカウント情報
    sendUsername = '' #'from_user@gmail.com'
    sendUserPassword = '' #'from_user_password'

    # メール送信パラメータ
    subject = 'テスト'
    toAddr = '' #'to_user@gmail.com'
    body = 'テスト'

    # メールサーバに接続して、ログインとメール送信
    try:
        print('メール送信開始')

        # Gmailへのログインとメール送信
        client = gmail.GMail(sendUsername, sendUserPassword)
        message = gmail.Message(subject=subject,to=toAddr,text=body)
        client.send(message)
        client.close()
        print('メール送信完了!')
        
    except Exception as e:
    # メール送信エラー時の対処
        try:
            client.close()
        except:
            print('メール送信エラーです。')
        print(e)
        print('メール送信エラーです。')


def main():

    # Component Variables
    root = None
    label = None
    history_label = None
    button = None

    root = tk.Tk()
    # Main Window Title
    root.title('Iwashi Dash! Mail Button')

    # Main Window SIze
    root.geometry('540x280')

    # Font Objects Create
    buttonFont = font.Font(family='メイリオ', size=24, weight='bold')
    labelFont = font.Font(family='メイリオ', size=12)
    #print(font.families())

    # Label Create
    label = tk.Label(root, text='水の発注依頼',font=labelFont)
    label.pack()

    # Button Create
    button = tk.Button(root, text='水の発注依頼\nメール',font=buttonFont,width=20,height=3,command= lambda : ordering(history_label))
    button.pack()

    # Label2 Create
    history_label = tk.Label(root, text='',font=labelFont)
    history_label.pack()

    # Main Window Loop(NonClosing Process)
    root.mainloop()

# -- Main function Define--#
if __name__ == '__main__':
	main()
