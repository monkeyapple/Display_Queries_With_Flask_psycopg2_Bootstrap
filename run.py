from flask import Flask,render_template
from config import config
import psycopg2
app=Flask(__name__)


###########################################
        #Route
#########################################

@app.route('/')
def index():
    conn=None
    rowResults=None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur=conn.cursor()
        order_statement='SELECT * FROM game ORDER BY last_visit DESC LIMIT 5;'
        cur.execute(order_statement)
        rowResults=cur.fetchall()
        
    except(Exception, psycopg2.Error) as error:
        print(error)

    finally:
        if conn is not None: 
            cur.close()
            conn.close()
            print("database connection is now closed")
    return render_template('index.html',recentRecords=rowResults)
    
if __name__=='__main__':
    app.run(debug=True)
