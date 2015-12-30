from flask import Flask,render_template,request,make_response
from flask.ext.sqlalchemy import SQLAlchemy


# Init Flask Instance
app = Flask(__name__,static_url_path="/static")

# IN PRODUCTION,PLEASE TURN THIS OFF!!!
app.debug = True


SECRET_KEY = '$&^&B&*^*MN&*CDMN&*()B^&*()P^&_N*NM(P)*&D()&*^'

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:*******@localhost/ppro'
app.config['SECRET_KEY'] = 'faefea%$W#^TGVDSG'


# DB instance init
db = SQLAlchemy(app)


# Basic Contact Schema
class Contact(db.Model):

	id = db.Column(db.Integer, primary_key = True, autoincrement =True)
	
	name = db.Column(db.String(254))
	email = db.Column(db.String(254))
	number = db.Column(db.String(254))
	query = db.Column(db.Text)




@app.route('/')
def index():
	return render_template('index.html')


@app.route('/contact',methods=['GET','POST'])
def contact():

	if request.method == 'GET':
		return render_template('contact.html',success=False)

	# Process contact info
	elif request.method == 'POST':

		# Get form data form request obj.
		params = request.form
		
		# Init Conatact Object
		contact = Contact()
		
		# Populate Contact from form inputs 
		contact.name = params['name']
		contact.email = params['email']
		contact.query = params['query']
		contact.number = params['number']

		# commit to db
		db.session.add(contact)
		db.session.commit()

		# return template with success!
		return render_template('contact',success=True)	



@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')


if __name__ == '__main__':
	app.run('0.0.0.0')
