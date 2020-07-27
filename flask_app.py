import json
import math
import os
import random
import secrets
import shutil
from datetime import datetime
from random import randint

import pymysql
import pyqrcode
from flask import (
    Flask, flash, redirect, render_template, request, send_file, session)
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
from werkzeug.utils import secure_filename

pymysql.install_as_MySQLdb()

#Initiating the newline character for Mails!
newline = "\n"

#Opening of config.json file
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'config.json')

with open(my_file, 'r') as c:
    params = json.load(c)["params"]

#Initilising Server (Local)
local_server = True

"""
pip install Flask
pip install Flask-mail
pip install Flask-SQLAlchemy
pip install wheel
pip install pymysql
pip install pyqrcode[PIL]
pip install qrcode[PIL]
pip install pypng
"""

#Upload Location
UPLOAD_FOLDER = params['upload_location']

#Allowed Extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','pdf','html','mp4','mp3','js','txt','docx','doc','css'}

#Initialising Flask App
app = Flask(__name__)

#The rest work
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = secrets.token_urlsafe(randint(30,10000))  #The Secrect Key

#For mail
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)

#Initialising the mail app
mail = Mail(app)
mail.init_app(app)

#Connecting to database
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


#######################################################
#The Class for SQL Table



#######################################################

#Contacts

#Offers

#AboutUs

#Menu

#Client

#Menu

#QrCode

#PasswordTracker

#######################################################



#Contacts
class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    subject = db.Column(db.String(250), unique=False, nullable=True)
    msg = db.Column(db.String(250), unique=False, nullable=False)
    dt_time = db.Column(db.String(120), unique=True, nullable=True)

#Offers
class Offers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    month = db.Column(db.Integer, unique=False, nullable=False)
    date = db.Column(db.Integer, unique=False, nullable=False)
    body = db.Column(db.String(250), unique=False, nullable=False)
    slug = db.Column(db.String(250), nullable=False)
    img_file = db.Column(db.String(250), unique=False, nullable=False)

#AboutUs
class Aboutus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about_left = db.Column(db.String(600), unique=False, nullable=False)
    about_right = db.Column(db.String(600), unique=False, nullable=False)
    pizza = db.Column(db.Integer, unique=False, nullable=True)
    pasta = db.Column(db.Integer, unique=False, nullable=False)
    salad = db.Column(db.Integer, unique=False, nullable=False)
    chef = db.Column(db.Integer, unique=False, nullable=False)

#Client
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    body = db.Column(db.String(300), unique=False, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    ocup = db.Column(db.String(250), unique=False, nullable=True)

#Menu
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part = db.Column(db.String(600), unique=False, nullable=False)
    name = db.Column(db.String(600), unique=False, nullable=False)
    body = db.Column(db.String(250), unique=False, nullable=True)
    size1 = db.Column(db.String(250), unique=False, nullable=True)
    price = db.Column(db.String, unique=False, nullable=True)
    size2 = db.Column(db.String(250), unique=False, nullable=True)
    price1 = db.Column(db.String, unique=False, nullable=True)
    img_file = db.Column(db.String(250), unique=False, nullable=False)
    best = db.Column(db.String(250), unique=False, nullable=True)
    partname = db.Column(db.String(600), unique=False, nullable=False)
    indexin = db.Column(db.String(3), unique=False, nullable=False)
    menuin = db.Column(db.String(3), unique=False, nullable=False)
    pricesym = db.Column(db.String(3), unique=False, nullable=True)
    price1sym = db.Column(db.String(3), unique=False, nullable=True)
    availability = db.Column(db.String(3), unique=False, nullable=True)
    active  = db.Column(db.String(3), unique=False, nullable=True)

#QrCode
class Qrcode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2000), unique=False, nullable=False)
    qrcode = db.Column(db.String(300), unique=False, nullable=False)
    endpoint = db.Column(db.String(250), nullable=False)
    stime = db.Column(db.String(250), unique=False, nullable=True)

#PasswordTracker
class Passwordtracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    dt_time = db.Column(db.String(120), unique=False, nullable=False)
    ip_address = db.Column(db.String(250), unique=False, nullable=False)


#Ends
#######################################################



active = lambda : db.engine.execute('UPDATE menu SET menu.active="active" WHERE menu.part IN (SELECT * FROM(SELECT menu.part FROM menu HAVING MIN(menu.id))tblTmp )')




#######################################################
#The Client Page Functions


#######################################################


#Main Index File

#About Us

#LoCATE uS

#Contact Us

#Menu

#Error Handler

#Offers

#Offers About


#######################################################



#Main Index File
@app.route("/")
def home():
    name1 = "| Home |"

    #Execution of lambda active function()
    active()

    #Required quering to database
    aboutus = Aboutus.query.all()
    menu = Menu.query.filter_by(indexin="YES", availability="YES").all()
    menu2 = db.engine.execute('SELECT DISTINCT part,partname,active FROM menu WHERE indexin="YES" AND availability="YES"')
    menu1 = Menu.query.filter(Menu.best.endswith('Yes')).filter_by(availability="YES").all()

    #Returing to the file
    return render_template('index.html', title = name1,params=params, aboutus=aboutus, menu=menu,menu2=menu2,menu1=menu1)


#About Us
@app.route("/about")
def about():
    name1 = "| About Us |"
    aboutus = Aboutus.query.all()
    client = Client.query.all()
    return render_template('about_us.html', title=name1, params=params, aboutus=aboutus, client=client)


#LoCATE uS
@app.route("/locateus")
def locateus():
    name1 = "| Locate Us |"
    return render_template('locateus.html', title=name1, params=params)


#Contact Us
@app.route("/contact", methods = ['GET','POST'])
def contact():
    if request.method=='POST':
        """ADD ENTRY TO DATABASE"""

        #Using Post request to get the form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        msg = request.form.get('msg')
        date = datetime.now()

        #Newline
        global newline

        #Commiting it to database
        entry = Contacts(name=name, email=email, subject=subject, msg=msg, dt_time=date)
        db.session.add(entry)
        db.session.commit()

        #Senind the mail
        mail.send_message('New message from ' + name +' given at 24 Ave Pizza',
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=f"Name: {name} {newline} Subject: {subject} {newline} Message of the user: {msg} {newline} Email-ID: {email}"
                          )
        flash('Your query has been submitted successfully')

    name1 = "| Contact Us |"
    return render_template('contact.html', title = name1,params=params)


#Menu
@app.route("/menu")
def menu():
    '''24 Ave Pizza menu'''
    name1 = "| Our Menu |"

    #Execution of lambda active function()
    active()
    
    #Quering it to database
    menu = Menu.query.filter_by(menuin="YES", availability="YES").all()
    menu2 = db.engine.execute('SELECT DISTINCT partname,part,active FROM menu WHERE menuin="YES" AND availability="YES"')
    

    #Returing to file
    return render_template('menu.html', title = name1,params=params,menu=menu,menu2=menu2)



#Error Handler
@app.errorhandler(404)
def page_not_found(e):
    '''Error 404 handler'''
    name1 = "| Url not Found |"
    # note that we set the 404 status explicitly
    return render_template('404.html', params=params, title=name1), 404



#Offers
@app.route("/offers", methods=['GET'])
def offers_route():
    '''Offers'''

    #Query to database
    offers = Offers.query.filter_by().all()
    last = math.ceil(len(offers)/int(params['no_of_posts']))

    #pagination logic
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    offers = offers[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
    
    #First Pagination
    if last==1:
        page = 0
    if page == 0:
        prev="#"
        next="#"
    elif (page==1):
        prev = "#"
        next = "?page=" + str(page+1)
    
    #Last
    elif(page==last):
        next = "#"
        prev = "?page=" + str(page - 1)
    else:
        next = "?page=" + str(page + 1)
        prev = "?page=" + str(page - 1)

    name1 = "| Offers Available |"

    return render_template('offers.html', title = name1,params=params, offers=offers, prev=prev, next=next)



#Offers About
@app.route("/offers-about/<string:post_slug>", methods=['GET'])
def offers_about(post_slug):
    '''Offers About'''

    #Query to database
    offer = Offers.query.filter_by(slug=post_slug).first()
    name1 = "| Offers Available |"

    return render_template('offers-about.html', title = name1,params=params, offers=offer)


#Ends
#######################################################







#######################################################
#The Admin Page Functions



#######################################################

#Dashboard(offers/login page)
###View offers table Section
###Edit/Add offers
###Delete the offer

#View photo Section

#Client Sayings Section
###The client edit table
###Add / Edit Client
###Delete the client responses

#Edit/Add Menu section
###Edit menu
###Tables Menu
###To add/Edit menu
###To delete a menu

#Qr- Code Admin Section
###View the qrcode page table
###Generating the Qr-Code
###Deleting the QrCode

#Edit About Us

#Logout


#File manager
###File manager
###Delete File
###Delete Folder
###Create Folder
###Create File
###Rename

#Uploader
###Check the allowed files
###Uploader Route

#Password Tracker
###Password Tracker
###Delete Password
###Add Password

#Forgot Password

#Admin Contact Us
###Contact Us Admin
###Delete Contact Us User
###View Contact Us User
###Mail Contact Us User

#######################################################



#Dashboard and Login
#######################################################


#View offers table Section
@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    """For login page and dashboard page"""
    name1 = "| Welcome to Dashboard |"

    #Check if user has logged in
    if ('user' in session and session['user']==params['admin_email']):
        offers = Offers.query.all()
        return render_template('dashboard-admin.html', title=name1, params=params, offers=offers)
    
    #Post request for the login page
    if (request.method=='POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        #Validation
        if(username== params['admin_email'] and password==params['admin_password']):
            session['user'] = username
            offers = Offers.query.all()
            return render_template('dashboard-admin.html', title=name1, params=params, offers=offers)
        
        else: flash('Please enter the password or email correctly!')

    #If user not logged in then redirect to dashboard
    return render_template('login-admin.html', title = name1,params=params)



#Edit/add offers
@app.route("/edit/<string:id>", methods=['GET','POST'])
def edit(id):
    """To edit/add a offer"""
    name1 = " Add / Edit a offer "

    #Validating if the user is logged in
    if ('user' in session and session['user']==params['admin_email']):
        #When a post request is made
        if request.method == "POST":
            #Getting the form value via  post requests
            box_title = request.form.get('title')
            date = request.form.get('date')
            month = request.form.get('month')
            year = request.form.get('year')
            slug = request.form.get('slug')
            body = request.form.get('body')
            img_file = request.form.get('img_file')

            #If id is 0 then redirect user to the add offers page
            if id == '0':
                offers = Offers(title=box_title, date=date, month=month, year=year, body=body, img_file=img_file, slug=slug)
                db.session.add(offers)
                db.session.commit()

                #Flashing the success message
                flash('A offer has been successfully added to the database')
            
            #If the id is not 0 then goto edit offers working page
            else:
                #The query to database
                offers = Offers.query.filter_by(id=id).first()
                offers.title = box_title
                offers.date = date
                offers.month = month
                offers.year = year
                offers.body = body
                offers.img_file = img_file
                offers.slug = slug

                #Flashing the success message
                flash('The offer was successfully edited')
                db.session.commit()

                #Redirect
                return redirect('/edit/'+id)
            
    offers = Offers.query.filter_by(id=id).first()
    return render_template("edit-offers-admin.html",params=params, offers=offers,title=name1,id=id)



#Delete the offer
@app.route("/delete/<string:id>", methods=['GET','POST'])
def delete(id):
    """For deleting the offers"""

    #Validating if the user is logged in
    if ('user' in session and session['user']==params['admin_email']):
        #If id is 0 then redirect user to the add offers page
        if id == '0':
            return redirect('/edit/0')
        
        #If the id is not 0 then delete the respective offer
        else:
            offers = Offers.query.filter_by(id=id).first()
            db.session.delete(offers)

            #Flashing the success message
            flash("The offer has been deleted")
            db.session.commit()

    return redirect('/dashboard')

#Ends
#######################################################




#######################################################
#View photo Section

@app.route("/view-photo/<string:img_file>")
def viewphoto(img_file):
    """To view the offers photo"""

    #Validating if the user is logged in
    if ('user' in session and session['user']==params['admin_email']):
        name1 = " |View Photo|"

        #Then redirect to the view photo page to view the respective photo
        return render_template("view-photo-admin.html", title=name1, img_file=img_file)

#Ends
#######################################################





#######################################################
#Client Sayings Section

#The client edit table
@app.route("/edit-client")
def editclient(): return redirect(f"/edit-client/{secrets.token_urlsafe(randint(10,500))}/{request.remote_addr}")

@app.route("/edit-client/<path:id>/<string:ip>")
def editclientMain(id,ip):
    """To goto client edit table"""
    name1 = "| Edit the client Sayings |"

    #Check if user logged in
    if ('user' in session and session['user']==params['admin_email']):
        #Query from the database
        client = Client.query.all()

        #Return the Query into database
        return render_template('view-client-admin.html', title=name1, params=params, client=client)

    #If user not logged in then redirect to dashboard
    else: return redirect('/dashboard')




#Add / Edit Client
@app.route("/add-client/<string:id>", methods=['GET','POST'])
def addclient(id):
    """To add/edit a client in database"""
    name1 = "Edit/Add Client"

    #Check if the user logged in
    if ('user' in session and session['user']==params['admin_email']):
        #Get the query from the database
        client = Client.query.filter_by(id=id).first()

        #If post request is made
        if request.method=="POST":
            title = request.form.get('title')
            name = request.form.get('name')
            body = request.form.get('body')
            ocup = request.form.get('ocup')

            #If the id is 0 then add the client response
            if id == '0':
                #Get the query to database
                client = Client(title=title, ocup=ocup, body=body, name=name)

                #Add the client to database
                db.session.add(client)
                db.session.commit()

                #Flash the success message
                flash('A client has been successfully added to the database')

            #Else if the id is not 0 then edit the client according to its id
            else:
                #Get the data from the above post requests and then commit to the database
                client.title = title
                client.name = name
                client.body = body
                client.ocup = ocup
                db.session.commit()

                #Flash the success message
                flash('A client has been successfully edited')

        #Goto the add-client HTML file
        return render_template("add-client-admin.html", params=params, client=client, title=name1, id=id)

    #If user not logged in then redirect to dashboard
    else: return redirect('/dashboard')




#Delete the client responses
@app.route("/delete-client/<string:id>", methods=['GET','POST'])
def deleteclient(id):
    """For deleting the client responses"""

    #Check if the user logged in
    if ('user' in session and session['user']==params['admin_email']):
        #If id is 0 then goto add-client sitepont as there is no client response to be daleted
        if id == '0':
            return redirect('/add-client/0')
        
        #If id is not 0 then delete the client
        else:
            client = Client.query.filter_by(id=id).first()
            db.session.delete(client)

            #Flashing the success message
            flash("The client has been deleted")
            db.session.commit()
    
    #After the work is done then return to edit-client table
    return redirect('/edit-client')

#Ends
#######################################################




#######################################################
#Edit/Add Menu section

#Edit menu
@app.route("/edit-menu")
def editseemenu(): 
    #Execution of lambda active function()
    active()
    return redirect(f"/edit-menu/{secrets.token_urlsafe(randint(10,500))}/{request.remote_addr}")

@app.route("/edit-menu/<path:id>/<string:ip>")
def editseemenuMain(id,ip):
    """To edit menu table"""
    name1 = "Edit Menu"

    #Validation
    if ('user' in session and session['user'] == params['admin_email']):
        #Querying to the database
        menu = Menu.query.all()
        menu2 = db.engine.execute('SELECT DISTINCT part,partname,active from menu')

        return render_template('see-edit-menu-admin.html', title=name1, params=params, menu=menu, id=id,menu2=menu2)
    
    #If not admin then return to dashboard
    else: return redirect('/dashboard')



#Tables Menu
@app.route("/view-tables-menu-admin")
def enterViewTableAdmin(): return redirect(f"/view-tables-menu-admin/{secrets.token_urlsafe(randint(10,500))}/{request.remote_addr}")

@app.route("/view-tables-menu-admin/<path:id>/<string:ip>", methods=['GET','POST'])
def viewTableMenuAdmin(id,ip):
    name1 = "Availability Check of Menu"
    #Validation
    if ('user' in session and session['user']==params['admin_email']):
        menuavail = Menu.query.filter_by(availability = "YES").all()
        menuavailnot = Menu.query.filter_by(availability = "NO").all()
        return render_template("see-tables-menu-admin.html",params=params,title=name1, menuavail=menuavail,menuavailnot=menuavailnot)
    return redirect('/dashboard')


#To add/Edit menu
@app.route("/add-menu/<string:id>", methods=['GET','POST'])
def editmenu(id):
    """To add a menu"""
    name1 = "Edit/Add Menu"

    #Validation
    if ('user' in session and session['user']==params['admin_email']):
        #If post request is made
        if request.method == "POST":
            #Getting the forms value via post request
            title = request.form.get('title')
            name = request.form.get('name')
            partname = request.form.get('partname')
            price = request.form.get('price')
            size1 = request.form.get('size1')
            size2 = request.form.get('size2')
            price1 = request.form.get('price1')
            best = request.form.get('best')
            body = request.form.get('body')
            img_file = request.form.get('img_file')
            menuin = request.form.get('menuin')
            indexin = request.form.get('indexin')
            pricesym = ""
            price1sym = ""
            availability = request.form.get('availability')

            #Generating the partname
            part1 = str(partname)
            part2 = part1.split(' ')
            part = '-'.join(part2)

            #If and else for checkbox
            if str(best) != "YES": best="NO"

            if str(menuin) != "YES": menuin="NO"

            if str(indexin) != "YES": indexin="NO"

            if str(availability) != "YES": availability="NO"
            
            #If and else for prices in menu
            if str(price) == str(0) or str(price) == "" or str(price) == " " or str(price) == None: 
                price = ""
                size1 = ""
            else: pricesym = "bx bx-rupee"

            if str(price1) == str(0) or str(price1) == "" or str(price1) == " " or str(price1) == None: 
                price1 = ""
                size2 = ""
            else: price1sym = "bx bx-rupee"


            #If id is 0 then add it to the database
            if id == '0':
                #Getting values and quering it to database
                menu = Menu(part=part, name=name, body=body,menuin=menuin,indexin=indexin, img_file=img_file, price=price, size1=size1, price1=price1, size2=size2, best=best,partname=partname,pricesym=pricesym,price1sym=price1sym,availability=availability)
                db.session.add(menu)

                #Commiting it to database
                db.session.commit()

                #Flashing the success message
                flash('A dish has been successfully added to the database')
            
            #If id is not equal to 0 then goto edit menu option
            else:
                #Querying it to database
                menu = Menu.query.filter_by(id=id).first()

                #Commiting it to database
                img_file = request.form.get('img_file')
                menu.title = title
                menu.partname = partname
                menu.part = part
                menu.name = name
                menu.body = body
                menu.img_file = img_file
                menu.price = price
                menu.size1 = size1
                menu.price1 = price1
                menu.size2 = size2
                menu.best = best
                menu.menuin = menuin
                menu.indexin = indexin
                menu.pricesym = pricesym
                menu.price1sym = price1sym
                menu.availability = availability

                #Flashing the success message
                flash('The dish was successfully edited')
                db.session.commit()

                #Redirecting it to the required page
                return redirect('/add-menu/'+id)

    #Querying to database            
    menu = Menu.query.filter_by(id=id).first()
    menu_partname = db.engine.execute('SELECT DISTINCT partname FROM menu')
    return render_template("edit-menu-admin.html",params=params, menu=menu,title=name1,id=id, menu_partname=menu_partname)


#To delete a menu
@app.route("/delete-menu/<string:id>", methods=['GET','POST'])
def deletemenu(id):
    """For deleting the menu"""
    if ('user' in session and session['user']==params['admin_email']):
        if id == '0':
            return redirect('/add-menu/0')
        else:
            menu = Menu.query.filter_by(id=id).first()
            db.session.delete(menu)
            db.session.commit()
    return redirect('/edit-menu')

#Ends
#######################################################





#######################################################
#Qr- Code Admin Section

#View the qrcode page table
@app.route("/qr-code")
def qrcodeMain(): return redirect(f"/qr-code/{secrets.token_urlsafe(randint(10,500))}/{request.remote_addr}")

@app.route("/qr-code/<path:id>/<string:ip>")
def qrcode(id,ip):
    """For viewing QrCode section"""
    name1 = "| Generate  Qr Code Here | "

    #Check if the user logged in
    if ('user' in session and session['user'] == params['admin_email']):
        #Getting the query from the database
        qrcode = Qrcode.query.all()

        #Returning the query to file
        return render_template('qr-code-admin.html',title=name1, params=params,qrcode=qrcode)
    
    #If user not logged in then redirect to dashboard
    return redirect('/dashboard')


#Generating the Qr-Code
@app.route("/qr-code-gen/", methods=['GET','POST'])
def qrcodegen():
    """To generate Qr-Code"""
    name1 = "Generate Qr-Code"

    #Check if the user logged in
    if ('user' in session and session['user']==params['admin_email']):
        if request.method == "POST":
            #Getting the data
            title = request.form.get('title')
            endpoint = request.form.get('endpoint')

            #Getting the folder path
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            my_file = os.path.join(THIS_FOLDER, "static/images/", )
            filename = my_file + str(endpoint)+".png"

            stime = datetime.now()

            #Generate QrCode
            url = pyqrcode.QRCode(title, error='H')
            url.png(filename, scale=10)
            im = Image.open(filename)
            im = im.convert("RGBA")
            logo = Image.open(my_file+"logo.png")
            box = (135, 135, 235, 235)
            im.crop(box)
            region = logo
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            im.paste(region, box)

            #Naming the QrCode File
            qrcode = str(endpoint)+".png"

            #Add an entry to database
            qrcode3 = Qrcode(title=title, qrcode=qrcode,stime=stime,endpoint=endpoint)
            db.session.add(qrcode3)
            db.session.commit()

            #Flashing the success message
            flash('A qr code has been generated successfully')
            return redirect('/qr-code')

        #Return to the Qr-Code Generator page
        return render_template("qrcode-gen-admin.html",params=params,title=name1)
    
    #If user not logged in then redirect to dashboard
    return redirect('/dashboard')


#Deleting the QrCode
@app.route("/delete-qrcode/<string:id>", methods=['GET','POST'])
def deleteqrcode(id):
    """For deleting the generated QrCode"""

    #Check if the user logged in
    if ('user' in session and session['user']==params['admin_email']):
        id = str(id)

        #Getting QrCode for the database
        qrcode = Qrcode.query.filter_by(id=id).first()

        #Getting the file path
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(THIS_FOLDER, "static/images",qrcode.qrcode)

        #Removing / Deleting the QrCode
        os.remove(filename)
        db.session.delete(qrcode)
        db.session.commit()

        #Flashing the success message
        flash('The QR-CODE has been deleted successfully')
    
    #Then redirect to Qr-Code dashboard
    return redirect('/qr-code')

#Ends
#######################################################





#######################################################
#Edit About Us


@app.route("/edit-about", methods=['GET','POST'])
def editaboutMain():
    """For edit the about us section"""
    name1 = "| Edit the about us section here | "

    #Check if the user logged in
    if ('user' in session and session['user'] == params['admin_email']):
        #If the post request is made from the Admin Client Side
        if request.method == "POST":
            #Using the post request to get the data from the form
            about_left = request.form.get('about_left')
            about_right = request.form.get('about_right')
            pizza = request.form.get('pizza')
            pasta = request.form.get('pasta')
            salad = request.form.get('salad')
            chef = request.form.get('chef')

            #Query to database
            aboutus = Aboutus.query.first()

            #Commiting to the database
            aboutus.about_left = about_left
            aboutus.about_right = about_right
            aboutus.pizza = pizza
            aboutus.pasta = pasta
            aboutus.salad = salad
            aboutus.chef = chef
            db.session.commit()

            #Flashing the success message
            flash("Edited succesfully!")

        #Query to the database
        aboutus = Aboutus.query.first()
        return render_template('edit-about-us-admin.html',title=name1, params=params,about=aboutus)
    
    #If not logged then redirecting to the dashboard
    return redirect("/dashboard")

#Ends
#######################################################




#######################################################
#Logout

@app.route("/logout")
def logout():
    """For logout session"""
    try:
        session.pop('user')
    except KeyError as e:
        return redirect('/dashboard')
    return redirect('/dashboard')

#Ends
#######################################################



#######################################################
#File manager

@app.route('/filemanager', defaults={'req_path': ''})
@app.route('/filemanager/<path:req_path>')
def dir_listing(req_path):
    """File Manager"""
    name1 = "Dhruva Shaw ||Admin|| |Filenamanager|"
    if ('user' in session and session['user']==params['admin_email']):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        BASE_DIR = os.path.join(THIS_FOLDER, 'static')

        # Joining the base and the requested path
        abs_path = os.path.join(BASE_DIR, req_path)

        # Check if path is a file and serve
        if os.path.isfile(abs_path):
            return send_file(abs_path)

        # Show directory contents
        files = os.listdir(abs_path)
        return render_template('filemanager-admin.html', files=files, params=params,req_path=req_path, title=name1)
    return redirect("/dashboard")


#Delete File
@app.route("/delete-file/<path:id>", methods=['GET','POST'])
def deletefile(id):
    """For deleting the file"""
    if ('user' in session and session['user']==params['admin_email']):
        if request.method == "POST":
            #Getting the directory to file
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

            #Geting file from form at HTML form
            filename = request.form.get('inlineFormInputGroupUsername')

            #Joining the file
            my_file = os.path.join(THIS_FOLDER, "static", id, filename)

            #Deleting the file
            os.remove(str(my_file))

            #Flashing the message
            flash('The File has been deleted successfully')
    return redirect('/filemanager')

#Delete Folder
@app.route("/delete-folder/<path:id>", methods=['GET','POST'])
def deletefolder(id):
    """For deleting the folder"""
    if ('user' in session and session['user']==params['admin_email']):
        if request.method == "POST":
            #Getting the directory to folder
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

            #Joing the the folder location
            path = os.path.join(THIS_FOLDER, "static/", id)

            # Removing directory  
            shutil.rmtree(path) 
            flash('Folder has been deleted')
    return redirect("/filemanager")

#Create Folder
@app.route("/create-folder", methods=['GET','POST'])
def createfolder():
    """Create Folder"""
    if ('user' in session and session['user']==params['admin_email']):
        if request.method == "POST":
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            nameFolder = request.form.get('foldername')
            path = os.path.join(THIS_FOLDER, "static", nameFolder)
            try:  
                os.mkdir(path)  
            except OSError as error:  
                flash('A folder with same name already exists!')  
            flash('Folder has been created')
            return redirect("/filemanager")

#Create File
@app.route("/create-file/<path:id>", methods=['GET','POST'])
def createfile(id):
    """Create File"""
    if ('user' in session and session['user']==params['admin_email']):
        if request.method == "POST":
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            nameFile = request.form.get('filename')
            path = os.path.join(THIS_FOLDER, "static", id)
            with open(os.path.join(path, nameFile), 'w') as fp: 
                pass
            flash('The file has been created!')
            return redirect("/filemanager")


#################
#Uploader

#Check the allowed files
def allowed_file(filename):
    """To files allowed to be uploaded"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Uploader Route
@app.route("/upload/<path:id>", methods=['GET','POST'])
def upload(id):
    """Upload the files"""
    if ('user' in session and session['user']==params['admin_email']):
        if request.method == "POST":
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            UPLOAD_FOLDER = os.path.join(THIS_FOLDER, "static", id)
            path = request.form.get('path')

            if 'img_file' not in request.files:
                # check if the post request has the file part
                return redirect(request.url)
            
            file = request.files['img_file']

            # if user does not select file, browser also
            # submit an empty part without filename

            if file.filename == '':
                flash('No selected file')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                flash('File Uploaded')
            return redirect(path)

    return redirect("/filemanager")
#########


#Rename
@app.route("/rename/<path:id>", methods=['GET','POST'])
def rename(id):
    """To rename files"""
    if ('user' in session and session['user']==params['admin_email']):
        if request.method == "POST":
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            nameFileFolder = request.form.get('namefilefolder')
            renameFileFolder = request.form.get('renamefilefolder')

            source = os.path.join(THIS_FOLDER, "static/assets/", id, nameFileFolder)
            dest = os.path.join(THIS_FOLDER, "static/assets/", id, renameFileFolder)

            try : 
                os.rename(source, dest) 
                flash("Source path renamed to destination path successfully.") 
            
            # If Source is a file  
            # but destination is a directory 
            except IsADirectoryError: 
                flash("Source is a file but destination is a directory.") 
            
            # If source is a directory 
            # but destination is a file 
            except NotADirectoryError: 
                flash("Source is a directory but destination is a file.") 
            
            # For permission related errors 
            except PermissionError: 
                flash("Operation not permitted.") 
            
            # For other errors 
            except OSError as error: 
                flash(error)

    return redirect("/filemanager")

#File Mnager Code ends
#######################################################

#Ends
#######################################################





#######################################################
#Password Tracker

@app.route("/password-tracker")
def passwordtracker(): return redirect(f"/password-tracker/{secrets.token_urlsafe(randint(10,500))}/{request.remote_addr}")

@app.route("/password-tracker/<path:id>/<string:ip>")
def passwordtrackerMain(id,ip):
    if ('user' in session and session['user']==params['admin_email']):
        name1="Dhruva Shaw ||Admin|| |Password Tracker|"
        password = Passwordtracker.query.all()
        return render_template("password-tracker-admin.html",params=params, title=name1 ,password=password)
 
    return redirect("/dashboard")


#Delete Password
@app.route("/delete-password/<string:id>", methods=['GET','POST'])
def deletepassword(id):
    #Validating Iser
    if ('user' in session and session['user']==params['admin_email']):
        #Quering to database
        passwordtracker = Passwordtracker.query.filter_by(id=id).first()
        db.session.delete(passwordtracker)

        #Flashing success message
        flash("Password has been deleted")

        #commiting to database
        db.session.commit()
    return redirect("/password-tracker")



@app.route("/add-password", methods=['GET','POST'])
def addpassword():
    #Validating User
    if ('user' in session and session['user']==params['admin_email']):
        #Using post request to get the form the form data
        website = request.form.get('websiteadd')
        username = request.form.get('usernameadd')
        password = request.form.get('passwordadd')
        dt_time = datetime.now()
        ip_address = request.remote_addr

        #Commiting it to database
        passwordtracker = Passwordtracker(website=website, username=username, password=password, dt_time=dt_time, ip_address=ip_address)
        db.session.add(passwordtracker)

        #Flashing the success message
        flash('The password has been added to database sucessfully!')
        db.session.commit()

    return redirect("/password-tracker")
#Ends
#######################################################


#######################################################
#Forgot Password

@app.route("/forgot")
def forgot():
    global newline

    #Send mail
    mail.send_message('Forgot Your Password ? '+' ||24 Ave Pizza||',
                        sender='dhruvashaw@gmail.com',
                        recipients=[params['gmail-user'],"24avepizza@gmail.com"],
                        body = f"IP Address: {request.remote_addr} {newline} Date: {datetime.now()} {newline} The userId: {params['admin_email'] } {newline} The Password is: {params['admin_password']}"
                        )
    flash("The password has been sent to your email address")
    return redirect("/dashboard")

#Ends
#######################################################




#######################################################
#Admin Contact Us

#Contact Us Admin
@app.route("/contactus-admin")
def contactusadmin(): return redirect(f"/contactus-admin/{secrets.token_urlsafe(randint(10,500))}/{request.remote_addr}")

@app.route("/contactus-admin/<path:id>/<string:ip>")
def contactusadminMain(id,ip):
    """Admin Contact Us """
    name1 = "Dhruva Shaw ||Admin|| |Contact Us|"

    #Validating the user
    if ('user' in session and session['user']==params['admin_email']):
        #Quering it to data base
        contact = Contacts.query.all()

        return render_template("contactus-admin.html",params=params, title=name1, contact=contact)
    
    return redirect("/dashboard")


#Delete Contact Us User
@app.route("/delete-contactus-admin/<string:id>")
def deletecontactusadmin(id):
    """For deleting the contact us responses"""

    #Validating the user
    if ('user' in session and session['user']==params['admin_email']):
        #Querying to data database and commiting it!
        contact =Contacts.query.filter_by(id=id).first()
        db.session.delete(contact)
        db.session.commit()

        #FlASHING THE SUCCESS MESSAGE
        flash("The Contact user has been successfully deleted!")

    return redirect('/contactus-admin')


#View Contact Us User
@app.route("/view-contactus-admin/<string:id>")
def viewcontactusadmin(id):
    """For deleting the contact us responses"""
    name1 = "24avepizza || Admin ||  | View Contact Us |"

    #VALIDATING THE USER
    if ('user' in session and session['user']==params['admin_email']):
        #Querying to database
        contact =Contacts.query.filter_by(id=id).all()

        #Returning the appropriate file
        return render_template('view-contactus-admin.html', params=params, title=name1, contact=contact)


    return redirect("/contactus-admin")


#Mail Contact Us User
@app.route("/mail-contactus-admin/<string:id>", methods=['GET','POST'])
def mailcontactusadmin(id):
    """For deleting the contact us responses"""

    name1 = "24avepizza|| Admin ||  | Mail Contact Us |"

    #Validation
    if ('user' in session and session['user']==params['admin_email']):
        #Quering To database
        contact =Contacts.query.filter_by(id=id).first()

        #If Post Request Is Made
        if request.method=='POST':
            #Using Post Request to get form data
            name = request.form.get('name')
            email = request.form.get('email')
            subject = request.form.get('subject')
            msg = request.form.get('message')
            date = datetime.now()

            global newline
            
            #Sending Mail
            mail.send_message(subject,
                        sender=params['gmail-user'],
                        recipients=[str(email)],
                        body = f"Dear Customer, {newline} {name} {newline} {newline} Thanks for contacting Us! {str(msg)} {newline} {newline} Regards, {newline} 24 Ave Pizza {newline}{newline} Youtube: {params['youtube_url']} {newline} Instagram: {params['insta_url']}{newline} Twitter: {params['tweet_url']} {newline} Facebook: {params['fb_url']}" 
                        )

            #Flashing the suceess message
            flash("The mail has been sent!")
        return render_template('mail-contactus-admin.html', params=params, title=name1, contact=contact)
    
    return redirect("/contactus-admin")


#Ends
#######################################################




#Ends
#######################################################


#Running the whole main flask app
if __name__ == '__main__':
    app.run(debug=True)
