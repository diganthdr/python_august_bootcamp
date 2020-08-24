from report.covid_statewise_stats import get_total_cases
from subs.sub_data import get_subs_data

def generate_user_report(subscription_data ,data):
    print("Generating user report..")

    subscriber_mail_map = {}

    for mailid, list_of_states in subscription_data.items():
        tmp_list = []
        for state_name in list_of_states:
            total_cases = get_total_cases(state_name, data) #optimisation: pre calculate and keep statewise count
            sub_map = {state_name: total_cases}
            tmp_list.append(sub_map)
        sub_map = {mailid:tmp_list}
        subscriber_mail_map.update(sub_map)

    dashline = "--------------------------------"
    print(dashline)
    print(subscriber_mail_map)
    for k,v in subscriber_mail_map.items():
        print(k, "-->", v)
    print(dashline)
    return subscriber_mail_map

    #Hardcode