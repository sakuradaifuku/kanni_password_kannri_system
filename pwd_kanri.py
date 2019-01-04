#! python3
#パスワード管理プログラム（簡易版のため脆弱性あり）
import sqlite3
import sys
import pyperclip
con = sqlite3.connect('pwd.db')
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE data_set(account, pwd)")
except:
    pass

cursor.execute('SELECT * FROM data_set')
try:
    PASSWORDS = dict(cursor.fetchall())
except:
    PASSWORDS = {'':''}


if len(sys.argv) < 2:
    print('使い方： python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします\n')
    print('追加する場合は： python pw.py [追加アカウント名]　を入力し、表示される指示に従って打ち込んでください\n')
    print('保持しているパスワードを確認したい場合： python pw.py all　を入力してください')
    con.close()
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
    con.close()
elif account == 'all':
    print('アカウントとパスワード'.center(21, '-') + '\n')
    for k, v in PASSWORDS.items():
        print(' ' + k.ljust(15) + str(v).rjust(6))
else:
    print(account + 'というアカウント名はありません')
    print(account + 'のパスワードを追加しますか？（追加する場合はyes、しない場合はEnterを押してください')
    te = input()
    if (te == 'yes'):
        print(account + 'のパスワードを入力してください：', end='')
        pwd = input()
        in_data = (account, pwd)
        cursor.execute("INSERT INTO data_set(account, pwd) VALUES(?, ?)", in_data)
        con.commit()
        con.close()
    else:
        con.close()
        sys.exit()
