from crypt import methods
from flask import Flask,render_template,jsonify,request
from project import db
from project.models import Course,UdemyCourseList
from project.udemy.factory import Factory
import datetime
import psycopg2


@app.route('/')
def index():
    recentSearches=[]
    if Course.query.count()>=10:
        recentQuery=Course.query.order_by(Course.last_visit.desc()).limit(5).all()
        for row in recentQuery:
            recentSearches.append((row.udemy_courselist.name,row.udemy_courselist.link))
    return render_template('index.html',recentSearches=recentSearches)

@app.route('/update',methods=["GET","POST"])
def update():
    if request.method=='POST':
        #get current selected search result's link
        courseLink=request.form['link']
        courseLink=courseLink[21:]
    queryCourseRow=UdemyCourseList.query.filter_by(link=courseLink).first()
    syllabus=queryCourseRow.course.course_syllabus
    print(syllabus)
    return jsonify({'syllabus':syllabus})
