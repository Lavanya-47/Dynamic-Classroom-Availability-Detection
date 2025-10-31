from flask import Flask, render_template, request, jsonify
import mysql.connector
app = Flask(__name__)
con=mysql.connector.connect(user="root",password="",database="dynamic")
cur=con.cursor()
# Sample data for available classrooms
print("Connected")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_classrooms', methods=['POST'])
def find_classrooms():
    block = request.form.get('block')
    shift = request.form.get('shift')
    time = request.form.get('time')
    f = int(request.form.get('floor'))
    print(block)
    print(shift)
    print(time)
    print(f)
    floor=""
    if f==1:
        floor="Ground Floor"
    elif f==2:
        floor="First Floor"
    elif f==3:
        floor="Second Floor"
    elif f==4:
        floor="Third Floor"
    elif f==5:
        floor="Fourth Floor"
    elif f==6:
        floor="Fifth Floor"
    
    import datetime

# Get today's date
    today = datetime.date.today()

    # Get the day name
    day_name = today.strftime("%A")

    day=day_name[:3].upper()
    f=str(f)
    sql="select floor_number,day,roomschedule.room_number,shift_id,subject,slot from roomschedule,room where roomschedule.room_number= room.room_number and day='"+day+"' and shift_id="+shift[-1]+" and slot='"+time+"' and floor_number='"+f+"' and (subject like '%LAB%' or subject like '%SPORT%' or subject like '%LIB%' or subject='')"
    print("Sql is ",sql)
    cur.execute(sql)
    data=cur.fetchall()
    fdata=[]
    for x in data:
        x=list(x)
        x[0]=floor
        fdata.append(list(x))
    print('Data is ',fdata)
    occupied_rooms = [row[2] for row in fdata]  # index 2 is room_number

    # Filter the available ones
    #final_empty = [room for room in available_rooms if room not in occupied_rooms]

    return render_template('index.html', schedule_data=fdata)

if __name__ == '__main__':
    app.run(debug=True)
