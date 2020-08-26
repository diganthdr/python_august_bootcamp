import time
import datetime

from inputdata.parse_input import get_input_data
from news.news import get_news
from subs.sub_data import get_subs_data
from mail.mail import send_mail
from report.generate_user_report import generate_user_report
from report.generate_xls import generate_xlx_report
from db.dbhandle import insert_row, get_rows

def trigger():
    ''' aggregation of all modules here'''
    #1. get data
    input_data = get_input_data()

    #2 Extract news and process news into dictionary
    news_map = get_news()

    #2 XLS generate
    generate_xlx_report( input_data )

    #4
    subscription_data =  get_subs_data()

    #5, get user --> interested states
    user_state_info = generate_user_report(subscription_data,input_data)

    print("--------Mail content-------")
    print(news_map)
    print(user_state_info) 

    #format mail, just for readability
    TAB ='\t'
    NEWLINE = '\n'
    print("Processing data collected from NEWS module..")
    processed_news_text = '\n----- HEADLINES -----\n'
    for link, headline in news_map.items():
        #import pdb;pdb.set_trace()
        insert_row('news', (datetime.date.today().strftime('%Y-%m-%d'), link, headline))
        processed_news_text = processed_news_text + headline + TAB + link + NEWLINE

    print(processed_news_text)
    get_rows('news', '2020-08-26')
    #6. Send mail with above data. 
    #   1. user specific data.
    #   2. XLS, attachment
    #   3. News.
    dashline  = "----------------------------------"
    XLS_REPORT_FILENAME = 'statewise_covid_report.xls'
    for user, content in user_state_info.items(): #contenet is statename and numver
        mail_text = "Subscribed states:\n" + dashline + NEWLINE

        for state_data in content:
            for state, active_cases in state_data.items():
                mail_text = state + " : " + str(active_cases) + "\n"
        
        mail_text = mail_text + "\n" + dashline + "\n" + processed_news_text
        
        SIGNATURE = "\n\nRegards,\n Automated Mailservice"
        mail_text = mail_text + SIGNATURE + "\n"
        subject_line = "Python mini-project: COVID: Dashboard"

        print("Sending mail to: ", user) #, "with:", mail_text)
        #send_mail(user, subject_line, mail_text, attachment=XLS_REPORT_FILENAME)
