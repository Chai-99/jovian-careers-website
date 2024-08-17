from flask import Flask, render_template,jsonify
app=Flask(__name__)

JOBS=[
  {
  
    'id':1,
    'title':'Data Analyst',
    'Location':'Hyderabad',
    'Salary': '23,0000 Rs' 
  
  },
  {
    'id':2,
    'title':'Software Engineering',
    'Location':'Indor',
    'Salary': '190000 Rs',

    
    
  },
  {
    'id':3,
    'title':'Cybersecurity',
    'Location':'Pune',
    

    
  },
  {
    'id':4,
    'title':'AI Engineer',
    'Location':'Chennai',
    'Salary': '1000000 Rs',

    
  },
  {'id':5,
    'title':'Fullstack Developer',
    'Location':'Bangalore',
    'Salary': '1000000 Rs',

    
    
  }

      ]


@app.route("/")
def hello():
  return render_template("home.html",
                         jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)

if __name__=="__main__":
   app.run(host="0.0.0.0",debug=True)
