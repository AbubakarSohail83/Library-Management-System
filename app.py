import profile
from typing import List
from flask_mail import Mail, Message
from sqlite3 import DatabaseError
from flask import Flask, render_template ,request,make_response,session
from model import db
from flask_restful import Api
from routes import initialize_routes
import os
from datetime import date, datetime, timedelta

app = Flask(__name__)
app.secret_key='zyx1234'
api=Api(app)
initialize_routes(api)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'pucitlibrary@gmail.com',
    MAIL_PASSWORD = 'edktjvrbhyvhwrlw',
))

mail = Mail(app)


# mail when your request is approved
def sendEmailOnRequestApprove(recieverEmail):
   msg = Message('Hello', sender = 'librarymanagementpucit@gmail.com', recipients = recieverEmail)
   msg.body = "Your Request for borrowing the book has been approved. Please collect the book from library tomorrow.. from Flask-Mail"
   mail.send(msg)
   print("Mail Sent")
   return "Sent"



# if session["username"]!="" and session["pwd"]!="":
#     dbb=db("localhost","root","abubakar786","libraryManagmen")
#     role=dbb.getRoleFromDataBase(session["username"],session["pwd"])
#     id=dbb.getIdByUserNamePassword(session["username"],session["pwd"])
#     if role[0]=="student":
#         bookIssueRecord=dbb.getBookIssueReturnDateById(id)
#         for returnDate in bookIssueRecord:
#             rD=date(returnDate)
#             print(rD)

        

        






def isUsernameAvaliable(username):
    try:
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        
        isTrue=dbb.checkIfusernameIsAvaliable(username)
        if isTrue:
            return True
        else:
            return False

    except Exception as e:
            print(str(e))

# if email found return false
def isemailAvaliable(email):
    try:
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        
        isTrue=dbb.checkIfemailAvaliable(email)
        if isTrue:
            return True
        else:
            return False

    except Exception as e:
            print(str(e))

# if email found return false
def checkIfQuantity0(quantity):
    try:
        if quantity==0 or quantity<0:
            return False

        elif quantity>=1:
            return True
    except Exception as e:
            print(str(e))

# a person can get total book of 5 time
def checkIfStudentHas5Books(stdid):
    try:
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        stdCount=0
        stdCount=dbb.studentCountInBookIssue(stdid)

        if stdCount >=5:
            return False
        elif stdCount <5:
            return True
    except Exception as e:
            print(str(e))        



# delete that request if the book is no approved 
# current date = expiry date
def deleteRecord():
    try:
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        
        data=dbb.tbl33333()
        i=0
        for p in range(len(data)):
            date = datetime.today()

            day=date.strftime('%d')
            date1=data[p][4].strftime('%d')
            if day==date1 and data[p][5]=="no":    
                # delete that record         
                dbb.deleteTbl3Record(data[p][0])
                print("record deleted")
    except Exception as e:
            print(str(e))
        




@app.route("/")
def home():
    
    session['username']="None"
    return render_template("home.html" )

# search book by name 
@app.route("/bksname" , methods=["POST"])
def bksname():
    bname=""
    
    if request.method == "POST":
        bname=request.form["bookname"]
        #to create connection
    
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBooksFromName(bname)
    return render_template("searchBookByName.html",books=books)

@app.route("/bkauthor" , methods=["POST"])
def bkauthor():
    aname=""
    
    if request.method == "POST":
        aname=request.form["aname"]
        #to create connection
    
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBooksFromAuthorName(aname)
    return render_template("searchBookByAuthor.html",books=books)


@app.route("/bkisbn" , methods=["POST"])
def bkisbn():
    isbn=""
    
    if request.method == "POST":
        isbn=request.form["isbn"]
        #to create connection
    
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getisbnbook(isbn)
    return render_template("searchBookByIsbn.html",books=books)


@app.route("/bksubject" , methods=["POST"])
def bksubject():
    subject=""
    
    if request.method == "POST":
        subject=request.form["subject"]
        #to create connection
    
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getbookbysubjectname(subject)
    return render_template("searchBookBySubject.html",books=books)




@app.route("/home")
def home1():
    return render_template("home.html")

#show book search page
@app.route("/booksearchbyname")
def booksearchbyname():
   
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBookstFromDataBase()
    return render_template("searchBookByName.html",books=books)

@app.route("/booksearchbyauthor")
def booksearchbyauthor():
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBookstFromDataBase()
    return render_template("searchBookByAuthor.html",books=books)

@app.route("/booksearchbyisbn")
def booksearchbyisbn():
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBookstFromDataBase()
    return render_template("searchBookByIsbn.html",books=books)


@app.route("/booksearchsubject")
def booksearchsubject():
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBookstFromDataBase()
    return render_template("searchBookBySubject.html",books=books)



#search book by author name
@app.route("/searchBookByAuthor", methods=["POST"])
def searchBookByAuthor():
    aname=""
    if request.method == "POST":
        aname=request.form["authorname"]
        #to create connection

    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBooksFromAuthorName(aname)
    return render_template("searchBookByAuthor.html",books=books)

#search book by isbn
@app.route("/booksearchisbn", methods=["POST"])
def booksearchisbn():
    isbn=""
    if request.method=="POST":
        isbn=request.form["isbn"]
        #to create connection

    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBooksbyisbn(isbn)
    return render_template("searchBookbyIsbn.html",books=books)

# route if studnet register a book
@app.route("/studentregister", methods=["POST"])
def studentregister():
    #print("hello user register book")
    if request.method =="POST":
        bookid=""
        bookid=request.form["bname"]
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        bookQuantity1=""
        bookQuantity=dbb.getbookquantity(bookid)
        print("The book quantity is ",bookQuantity)
        username=session["username"]
        bookQuantity1=bookQuantity[0]
        
        bquantity=int(bookQuantity1)
        bquantity-=1

        #get id form the username
        stdid=dbb.getstdidfromusername(username)
        
        #for datetime    
        date = datetime.today()
        newDate = date + timedelta(hours=24)
        bookQuantity1=str(bquantity)
        #adding data into the bookissue table;
        # here id is the bookid
        dbb.insertUserDataIntoDb(stdid,bookid,date,newDate)
        dbb.udpateBookQuantity(bookQuantity1,bookid)
        # print("the id of book is ",id)
    return render_template("studentHome.html")

#route for librarian to show requests
@app.route('/showRequest')
def showRequest():
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    data=()
    data=dbb.getlibRequestRecords()
    return render_template("librarianShowRequests.html",data=data)




    # here we will get data from table2
    # from here we will send name bname
    # button will be there from where we will aprove request.


#route for librarian if he press approve button
@app.route('/librarianApprove', methods=["POST"])
def librarianApprove():
    deleteRecord()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    username=session["username"]
    tbl3id=""
    if request.method == "POST":

        tbl3id=request.form["tbl3id"]
        #print("the value of tbl3id is ",tbl3id)    
    
    librarianid=dbb.getstdidfromusername(username)
    date = datetime.today()
    lastestExpiryDate = date + timedelta(days = 7)    
    data=dbb.getBookIssueById(tbl3id)
    stdId=data[1]
    tempEmail=dbb.getEmailFromId(stdId)
    stdEmail=[]
    stdEmail=list(tempEmail)
    sendEmailOnRequestApprove(stdEmail)
    # here we update the updated data
    dbb.udpatewhenadminpressapprove(data[0],lastestExpiryDate,"yes",librarianid,"0","false")

    return render_template("librarianhome.html")

# show login
@app.route("/showlogin")
def showlogin():
    return render_template("login.html" )
# show signup
@app.route("/showSignUp")
def showSignUp():
    return render_template("signup.html")

# show book on books link in navbar
@app.route("/bookshow")
def bookshow():
    
    username=session["username"]
    print(username)
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=()
    books=dbb.getBookstFromDataBase()
    
    if username=="None":
        return render_template("firstTimeBook.html",books=books)

    if username!="None":
        return render_template("books.html" , books=books)

    
# after admin login 
@app.route("/adminaddlib")
def adminaddlib():
    return render_template("adminaddLibrarian.html")

# admin add librarina to db
@app.route("/adminaddlibrarian", methods=["POST"])
def adminaddlibrarian():
    nam=''
    email=''
    pwd=''
    rollno=''
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        username=request.form['username']
        pwd=request.form["password"]
        cpwd=request.form['confirmpassword']
        rollno=request.form["rollno"]
        #to create connection

    dbb=db("localhost","root","abubakar786","libraryManagmen")
    if cpwd==pwd:
        dbb.insertUserDataIntoDb2(name,email,rollno,username,pwd,'librarian')
        return render_template("adminaddLibrarian.html" )
             
    else:
        return render_template("adminaddLibrarian.html" )


# stduent show all the requests
# show books to the sudent which are in hold of the studnet
@app.route("/BookInHoldOfStd")
def BookInHoldOfStd():
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    data=()
    data=dbb.getDataWhenReturnStatusIsFalse()
    return render_template("librarianAcceptReturnBook.html",data=data)






# librarn page when he revieve books
@app.route("/showRequestToApprove")
def showRequestToApprove():
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    # show all the bookIssue feilds whose return status is false
    data=()
    data=dbb.getDataWhenReturnStatusIsFalse()
    return render_template("librarianAcceptReturnBook.html",data=data)

#search by student name in the route
@app.route("/searchByStudentName",methods=["POST"])
def searchByStudentName():
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    data=""
    stdid=""
    if request.method == "POST":
        stdid=request.form["stdid"]
    data=()
    data=dbb.gettbl3recordById(stdid,)
    return render_template("librarianAcceptReturnBook.html",data=data)

# do this work in api datatable
@app.route("/approveBooks",methods=["POST"])
def approveBooks():
    deleteRecord()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    tbl3id=""
    if request.method == "POST":
        tbl3id=request.form["tbl3id"]
    # now we will update the table3 with the id 
    dbb.updatetbl3lastcol("true",tbl3id)
    row=dbb.getBookIdfromtbl3(tbl3id)
    # on revieving back we will increment that book quantity by 1
    print("The value of row is ",row[2])
    bkid=row[2]
    qt=dbb.getbookquantity(bkid)
    
    qt1=qt[0][0]
    print("the qt is ",qt1)
    quantity1=int(qt1)
    quantity1+=1

    dbb.updateBookQuantity(str(quantity1),bkid)

    return render_template("librarianhome.html")

@app.route("/bookinhold")
def bookinhold():
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    data=()
    
    username=session["username"]
    stdid=dbb.stdidbyuname(username)
    data=dbb.bookInHoldByStd(stdid)
    return render_template("booksInHoldOfStd.html",data=data)


@app.route("/libaddbook")
def libaddbook():
    return render_template("librarainAddBook.html")




# after librarian login he can add books
@app.route("/addbooks",methods=["POST"])
def addbooks():
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    if request.method=="POST":
        bname=request.form["bname"]
        aname=request.form["aname"]
        isbn=request.form['isbn']
        desc=request.form["description"]
        qty=request.form["quantity"]
        link=request.form["piclink"]
    dbb.insertbook(bname,aname,isbn,desc,qty,link)
    
    return render_template("librarainAddBook.html" )


# route for admin home
@app.route("/adminhome")
def adminhome():
    return render_template("adminHome.html")

#route for studen home
@app.route("/studenthome")
def studenthome():
    return render_template("studentHome.html")

# route for librarainhome
@app.route("/librarianhome")
def librarianhome():
    deleteRecord()
    return render_template("librarianhome.html")






# signup send data to db
@app.route("/signup",methods=["POST"])
def signup():
    nam=''
    email=''
    pwd=''
    rollno=''
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        username=request.form['username']
        pwd=request.form["password"]
        cpwd=request.form['confirmpassword']
        rollno=request.form["rollno"]
        #to create connection

    dbb=db("localhost","root","abubakar786","libraryManagmen")
    if cpwd==pwd:
        dbb.insertUserDataIntoDb2(name,email,rollno,username,pwd,'student')
        return render_template("login.html" )
             
    else:
        return render_template("signup.html" )

# login link send database to db
@app.route("/login",methods=["POST"])
def login1():
    nm=''
    pwd=''
    if request.method=="POST":
        nm=request.form["name"]
        pwd=request.form["pwd"]
    
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    tuple1=()
    
    tuple1=dbb.getDataFromDataBase(nm,pwd)
    
    roletuple1=()
    roletuple1=dbb.getRoleFromDataBase(nm,pwd)
    print(roletuple1)
    
    # if there in invlaid data for login
    if tuple1 != None:
        login=False
        if tuple1[0]==nm and tuple1[1]==pwd:
            login=True
        
        
        if login== True and (roletuple1[0]=='student' ):
            session["username"]=nm
            session["pwd"]=pwd
            print(nm)
            res=make_response(render_template("studentHome.html",name=nm))
            
        #student login
        if login== True and ( roletuple1[0]=='admin'):
            session["username"]=nm
            session["pwd"]=pwd
            res=make_response(render_template("adminHome.html",name=nm))
        elif login== True and roletuple1[0]=='librarian':
            session["username"]=nm
            session["pwd"]=pwd
            res=make_response(render_template("librarianhome.html",name=nm))
            deleteRecord()
        return res     
                
    else:
        print("kuch nai aya")
        return render_template("login.html" )





@app.route("/logout")
def logout():
    res=make_response(render_template("login.html"))
    res.set_cookie('username',expires=0)
    res.set_cookie('pwd',expires=0)
    return res

@app.route("/searchbookug")
def searchbookug():
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBookstFromDataBase()
    return render_template("searchbookbynameug.html",books=books)

@app.route("/bksnameug" , methods=["POST"])
def bksnameug():
    bname=""
    
    if request.method == "POST":
        bname=request.form["bookname"]
        #to create connection
    
    books=()
    dbb=db("localhost","root","abubakar786","libraryManagmen")
    books=dbb.getBooksFromName(bname)
    return render_template("searchbookbynameug.html",books=books)

# abubakar code

@app.route("/showStudents")
def showStudents():
    return(render_template('showStudentsforLibrarian.html'))



@app.route("/showstudentupdateProfileInfo")
def showstudentupdateProfileInfo():
    print("Session Information: ",session["username"],session["pwd"])

    if session["username"]!="":
        try:
            dbb=db("localhost","root","abubakar786","libraryManagmen")
            profileData=dbb.getProfileFromDataBase(session["username"],session["pwd"])
            if profileData!=None:
                return render_template ("studentprofile.html",ProfileName=profileData[0]+"'s Profile",existingEmail=profileData[3],existingName=profileData[0],existingUserName=profileData[1],existingRollNo=profileData[4],existingPassword=profileData[2])
            else:
                return render_template("studentprofile.html",error="Login First!")
        except Exception as e:
            print(e);  

@app.route("/showadminupdateProfileInfo")
def showadminupdateProfileInfo():
    print("Session Information: ",session["username"],session["pwd"])

    if session["username"]!="":
        try:
            dbb=db("localhost","root","abubakar786","libraryManagmen")
            profileData=dbb.getProfileFromDataBase(session["username"],session["pwd"])
            if profileData!=None:
                return render_template ("adminprofile.html",ProfileName=profileData[0]+"'s Profile",existingEmail=profileData[3],existingName=profileData[0],existingUserName=profileData[1],existingRollNo=profileData[4],existingPassword=profileData[2])
            else:
                return render_template("adminprofile.html",error="Login First!")
        except Exception as e:
            print(e);


@app.route("/showlibrarianupdateProfileInfo")
def showlibrarianupdateProfileInfo():
    print("Session Information: ",session["username"],session["pwd"])

    if session["username"]!="":
        try:
            dbb=db("localhost","root","abubakar786","libraryManagmen")
            profileData=dbb.getProfileFromDataBase(session["username"],session["pwd"])
            if profileData!=None:
                res=make_response(render_template("librarianprofile.html",ProfileName=profileData[0]+"'s Profile",existingEmail=profileData[3],existingName=profileData[0],existingUserName=profileData[1],existingRollNo=profileData[4],existingPassword=profileData[2]))
            else:
                res=make_response(render_template("librarianprofile.html",error="Login First!"))
            return res
        except Exception as e:
            print(e);            



@app.route("/studentupdateProfileInfoDB",methods=["POST"])
def studentupdateProfileInfoDB():
    try:
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        profileData=dbb.getProfileFromDataBase(session["username"],session["pwd"])
        profileId=profileData[5]
    except DatabaseError:
        print("Problem in updating profile!2")

    if request.method=="POST":
        newName=request.form.get("name")
        newEmail=request.form.get("email")
        newPassword=request.form.get("password")
        newUserName=request.form.get("username")
        newRollNo=request.form.get("rollno")
        
        try:
            dbb.updateProfileOnDatabase(newName,newEmail,newUserName,newPassword,newRollNo,profileId)

            session["username"]=newUserName
            session["pwd"]=newPassword

            print(newUserName,newName)
            

            return make_response(render_template ("studentprofile.html",ProfileName=newName+"'s Profile",existingEmail=newEmail,existingName=newName,existingUserName=newUserName,existingRollNo=newRollNo,existingPassword=newPassword))
        except DatabaseError:
            print("Error in updating profile 3")


@app.route("/adminupdateProfileInfoDB",methods=["POST"])
def adminupdateProfileInfoDB():
    try:
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        profileData=dbb.getProfileFromDataBase(session["username"],session["pwd"])
        profileId=profileData[5]
    except DatabaseError:
        print("Problem in updating profile!2")

    if request.method=="POST":
        newName=request.form.get("name")
        newEmail=request.form.get("email")
        newPassword=request.form.get("password")
        newUserName=request.form.get("username")
        newRollNo=request.form.get("rollno")
        
        try:
            dbb.updateProfileOnDatabase(newName,newEmail,newUserName,newPassword,newRollNo,profileId)

            session["username"]=newUserName
            session["pwd"]=newPassword

            print(newUserName,newName)
            

            return make_response(render_template ("adminprofile.html",ProfileName=newName+"'s Profile",existingEmail=newEmail,existingName=newName,existingUserName=newUserName,existingRollNo=newRollNo,existingPassword=newPassword))
        except DatabaseError:
            print("Error in updating profile 3")



@app.route("/librarianupdateProfileInfo",methods=["POST"])
def librarianupdateProfileInfo():
    try:
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        profileData=dbb.getProfileFromDataBase(session["username"],session["pwd"])
        profileId=profileData[5]
    except DatabaseError:
        print("Problem in updating profile!2")

    if request.method=="POST":
        newName=request.form.get("name")
        newEmail=request.form.get("email")
        newPassword=request.form.get("password")
        newUserName=request.form.get("username")
        newRollNo=request.form.get("rollno")
        
        try:
            dbb.updateProfileOnDatabase(newName,newEmail,newUserName,newPassword,newRollNo,profileId)

            session["username"]=newUserName
            session["pwd"]=newPassword

            print(newUserName,newName)
            

            return make_response(render_template ("librarianprofile.html",ProfileName=newName+"'s Profile",existingEmail=newEmail,existingName=newName,existingUserName=newUserName,existingRollNo=newRollNo,existingPassword=newPassword))
        except DatabaseError:
            print("Error in updating profile 3")






@app.route("/updateBooksInfo")
def updateBooksInfo():
    return render_template("showAllBooks.html")


if __name__ == '__main__':
    app.run(debug=True)

