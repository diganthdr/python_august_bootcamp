import time
import datetime
from report import covid_statewise_stats
from db.dbhandle import insert_row, get_rows

def generate_xlx_report( data ):
    if not isinstance(data, dict):
        print("API data is not in dictionary")
        return
        
    all_states = data.keys()
    state_stats_map = {}
    for state_name in all_states:
        total_cases = covid_statewise_stats.get_total_cases(state_name, data)
        state_stats_map.update({state_name: total_cases})

        #much easier to put in to DB here:
        insert_row('state_cases', (datetime.date.today().strftime('%Y-%m-%d'), state_name, total_cases))

    XLS_REPORT_FILENAME = 'statewise_covid_report.xls'
    create_xls(state_stats_map, XLS_REPORT_FILENAME )
    return XLS_REPORT_FILENAME


def create_xls(state_stats_map, xls_report_filename):
    print("create_xls..")
    import xlwt
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('All states')

    #first row, Header
    #takes, row, column and text ast arg
    worksheet.write(0,0,"STATE")
    worksheet.write(0,1,"ACTIVE")

    for row, (state, count) in enumerate(state_stats_map.items(), 1):
        col = 0
        worksheet.write(row, col, state)
        worksheet.write(row, col+1, count)
    workbook.save(xls_report_filename)