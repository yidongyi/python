#coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_user='1329709650@qq.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_sender='2327819708@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量 gmlfdflygtrnecce  rrlwdujfvbzgecea
def mail():
    ret=True
    try:
        content='''爱上你我的脸上就有了笑容

                爱上你我的心空就布满了彩虹

                未来的岁月只愿与你牵手同行
                
                永远不忘爱你的海誓山盟
                
                无论是梨花枯萎

                还是桃花凋零
                
                永远不会改爱你的初衷
                
                爱上你我就找到了年少情梦
                
                爱上了你我的心海就百转柔情
                
                今后的时光只愿为你一人做梦
                
                心底永远荡漾着爱你的深情
                
                无论是海水干涸
                
                还是大地无楞
                
                心永远为你魂牵梦萦
                
                爱你一生不变
                
                你开心的时候
                
                我来欣赏你的笑容
                
                你难过的时候
                
                我来驱散你的愁容
                
                爱你一生不变
                
                你寂寞的时候
                
                我来点燃你的温情
                
                你孤独的时候
                
                我来抚慰你的心灵'''
        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["一个好人",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号 一个好人
        msg['To']=formataddr(["随心所欲",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号 随心所欲
        msg['Subject']="来自爱你的义" #邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com",465)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"gmlfdflygtrnecce")    #括号中对应的是发件人邮箱账号、邮箱密码  530860979 jdfzpmrcowtnbhfh
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception ,e:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
        print e
    return ret

ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed