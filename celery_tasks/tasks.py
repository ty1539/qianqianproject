
#使用celery
from celery import Celery


#创建一个celery对象

broker='redis:49.234.190.164:22/8'
app=Celery('celery_tasks.tasks',broker=broker)

@app.task
def send_email(to_email):
    #发邮件去
    pass



#在需要发送邮件的地方
send_email.deley('邮件地址')
