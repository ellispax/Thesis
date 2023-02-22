import datetime as dt

#check farm status
#get sensor values
#send to db
#compare
#irrigate if necessary 
#repeat



def get_stamp():
    yy = dt.datetime.today().year
    mm = dt.datetime.today().month
    dd = dt.datetime.today().day
    hh = dt.datetime.today().hour
    m = dt.datetime.today().minute
    ss = dt.datetime.today().second
    #print(str(yy), str(mm), str(dd), str(hh), str(m), str(ss))
    Tstamp = (str(yy)+str(mm)+str(dd)+str(hh)+str(m)+str(ss))
    return Tstamp

def check_status():
    pass

def get_values():
    pass