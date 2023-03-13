import pymysql


class db:
    def __init__(self,host,user,pwd,db):
        self.host=host
        self.user=user
        self.db=db
        self.pwd=pwd
        try:
            self.connection=pymysql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db)
        except Exception as e:
            print(str(e))
    #insert user data into the database
    def insertUserDataIntoDb2(self,name,email,rollno,username,pwd,role):
        try:
            cursor=self.connection.cursor()
            query="INSERT INTO users (name,email,rollno,username,password,role) VALUES (%s, %s,%s, %s,%s, %s)"
            val=(name,email,rollno,username,pwd,role)
            cursor.execute(query,val)
            self.connection.commit()

            print(cursor.rowcount, "record inserted.")
        except Exception as e:
            print(str(e))  

    def insertbook(self,bname,author,isbn,description,quantity,link):
        try:
            cursor=self.connection.cursor()
            
            query="INSERT INTO book(bname,author,isbn,description,quantity,pdflink) VALUES (%s, %s,%s, %s,%s,%s)"
           
            val=(bname,author,isbn,description,quantity,link)
            cursor.execute(query,val)
            print("adding books") 
            self.connection.commit()
            
            print(cursor.rowcount, "book inserted.")
        except Exception as e:
            print(str(e)) 

    # studentpress register button
    #insert button
    def insertUserDataIntoDb(self,stdid,bookid,date,date1):
        try:
            cursor=self.connection.cursor()
            query="INSERT INTO bookIssue(student_id, book_id, issuedate, expirydate, approved, librarian_id, fine, returnStatus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(stdid,bookid,date,date1,"no",-5,"0","false")
            
            cursor.execute(query,val)
            
            self.connection.commit()

            print(cursor.rowcount, "record inserted.")
        except Exception as e:
            print(str(e)) 

    #after admin press aprove button
    def udpatewhenadminpressapprove(self,iid,expirydate, approved,librarian_id,fine,returnStatus):
        try:
            cursor=self.connection.cursor()
            query="UPDATE bookIssue SET expirydate=%s, approved=%s,librarian_id=%s,fine=%s,returnStatus=%s WHERE iid=%s"
            val=(expirydate,approved,librarian_id,fine,returnStatus,iid)
            
            cursor.execute(query,val)
            
            self.connection.commit()

            print(cursor.rowcount, "record inserted.")
        except Exception as e:
            print(str(e)) 


    
    def udpateBookQuantity(self,bookQuantity,bid):
        try:
            cursor=self.connection.cursor()
            query="UPDATE book SET quantity=%s WHERE bid=%s"
            val=(bookQuantity,bid)
            
            cursor.execute(query,val)
            
            self.connection.commit()

            print(cursor.rowcount, "record udpated.")
        except Exception as e:
            print(str(e)) 


    # select student form the username
    def getstdidfromusername(self,username):
        try:
            row = ()
            cursor=self.connection.cursor()
            query="select id from users where username=%s "
            val=(username)
            cursor.execute(query,val)
            row=cursor.fetchone()
            
            return row

        except Exception as e:
            print(str(e))


    def getBookIssueById(self,id):
        try:
            row = ()
            cursor=self.connection.cursor()
            query="select * from bookIssue where iid=%s "
            val=(id)
            cursor.execute(query,val)
            row=cursor.fetchone()
            #print(row)
            return row

        except Exception as e:
            print(str(e))
    
    def getBookIssueReturnDateById(self,id):
        try:
            row = ()
            cursor=self.connection.cursor()
            query="select expirydate from bookIssue where student_id=%s "
            val=(id)
            cursor.execute(query,val)
            row=cursor.fetchall()
            #print(row)
            return row

        except Exception as e:
            print(str(e))

    def getIdByUserNamePassword(self,username,pwd):
        try:
            row = ()
            cursor=self.connection.cursor()
            query="select id from users where username=%s, password=%s "
            val=(username,pwd)
            cursor.execute(query,val)
            row=cursor.fetchone()
            #print(row)
            return row

        except Exception as e:
            print(str(e))

    # this function is to get table 3 data form db.
    def getlibRequestRecords(self):
        try:
            row = ()
            cursor=self.connection.cursor()
            query="select * from bookIssue where approved=%s "
            val=("no")
            cursor.execute(query,val)
            row=cursor.fetchall()
            print(row)
            return row

        except Exception as e:
            print(str(e))

    # librarian side approve request
    # this will add issuedate , expirydate,          



    def addRecordInIssueBook(self,bname,author,isbn,description,quantity):
        try:
            cursor=self.connection.cursor()
            
            query="INSERT INTO book(bname,author,isbn,description,quantity) VALUES (%s, %s,%s, %s,%s)"
           
            val=(bname,author,isbn,description,quantity)
            cursor.execute(query,val)
            print("adding books") 
            self.connection.commit()
            
            print(cursor.rowcount, "book inserted.")
        except Exception as e:
            print(str(e))


    def getDataFromDataBase(self,name,password):
        try:
            row = ()
            cursor=self.connection.cursor()
            query="select username,password from users where username=%s and password=%s "
            val=(name,password)
            cursor.execute(query,val)
            row=cursor.fetchone()
            print(row)
            return row

        except Exception as e:
            print(str(e))              


    def getRoleFromDataBase(self,username,password):
        try:
            cursor=self.connection.cursor()
            query="select role from users where username=%s and password=%s "
            val=(username,password)
            cursor.execute(query,val)
            row=cursor.fetchone()
            return row

        except Exception as e:
            print(str(e))                       


    def getisbnbook(self,isbn):
        try:
            cursor=self.connection.cursor()
            query="select *  from book where isbn=%s"
            val=(isbn)
            cursor.execute(query,val)
            row=cursor.fetchall()
           
            return row

        except Exception as e:
            print(str(e))

    
    def getbookbysubjectname(self,subject):
        try:
            cursor=self.connection.cursor()
            query="select *  from book where bname like %s"
            val=(subject)
            cursor.execute(query,val)
            row=cursor.fetchall()
            print(row)
            return row

        except Exception as e:
            print(str(e))


    def getBookstFromDataBase(self):
        try:
            cursor=self.connection.cursor()
            query="select *  from book"
            cursor.execute(query)
            row=cursor.fetchall()
           
            return row

        except Exception as e:
            print(str(e))

    def getBooksFromName(self,name):
        try:
            cursor=self.connection.cursor()
            query="select *  from book where bname=%s"
            val=(name)
            cursor.execute(query,val)
            row=cursor.fetchall()
           
            return row

        except Exception as e:
            print(str(e))  

    def getbookquantity(self,id):
        try:
            cursor=self.connection.cursor()
            query="select quantity from book where bid=%s"
            val=(id)
            cursor.execute(query,val)
            row=cursor.fetchone()
            
            return row

        except Exception as e:
            print(str(e)) 



    def getBooksFromAuthorName(self,aname):
        try:
            cursor=self.connection.cursor()
            query="select *  from book where author=%s"
            val=(aname)
            cursor.execute(query,val)
            row=cursor.fetchall()
           
            return row

        except Exception as e:
            print(str(e))    


    # bookIssue details whose return status is false;
    def getDataWhenReturnStatusIsFalse(self):
        try:
            cursor=self.connection.cursor()
            query="select * from bookIssue where returnStatus=%s and approved=%s"
            val=("false","yes")
            cursor.execute(query,val)
            row=cursor.fetchall()
           
            return row

        except Exception as e:
            print(str(e))

    def gettbl3recordById(self,stdid):
        try:
            cursor=self.connection.cursor()
            query="select * from bookIssue where student_id=%s and approved=%s and returnStatus=%s"
            val=(stdid,"yes","false")
            cursor.execute(query,val)
            row=cursor.fetchall()
            print(row)
            return row

        except Exception as e:
            print(str(e))

    def stdidbyuname(self,username):
        try:
            cursor=self.connection.cursor()
            query="select id from users where username=%s"
            val=(username)
            cursor.execute(query,val)
            row=cursor.fetchone()
            print(row)
            return row

        except Exception as e:
            print(str(e))
    
    
    def bookInHoldByStd(self,stdid):
        try:
            cursor=self.connection.cursor()
            query="select * from bookIssue where student_id=%s and approved=%s and returnStatus=%s"
            val=(stdid,"yes","false")
            cursor.execute(query,val)
            row=cursor.fetchall()
            print(row)
            return row

        except Exception as e:
            print(str(e))
        


    def updatetbl3lastcol(self,returnStatus,iid):
        try:
            cursor=self.connection.cursor()
            query="UPDATE bookIssue SET returnStatus=%s WHERE iid=%s"
            val=(returnStatus,iid)
            
            cursor.execute(query,val)
            
            self.connection.commit()

            print(cursor.rowcount, "record inserted.")

        except Exception as e:
            print(str(e))


    def getBooksbyisbn(self,isbn):
        try:
            cursor=self.connection.cursor()
            query="select *  from book where isbn=%s"
            val=(isbn)
            cursor.execute(query,val)
            row=cursor.fetchall()
           
            return row

        except Exception as e:
            print(str(e))

    # this will search book by subject name
    def getBooksbysubject(self,isbn):
        try:
            cursor=self.connection.cursor()
            query="select *  from book where isbn=%s"
            val=(isbn)
            cursor.execute(query,val)
            row=cursor.fetchall()
           
            return row

        except Exception as e:
            print(str(e))


    def insertintotbl4(self,tbl3id,expiry):
        try:
            cursor=self.connection.cursor()
            query="INSERT INTO requesttime(iid,expirydate) VALUES (%s,%s)"
            val=(tbl3id,expiry)
            
            cursor.execute(query,val)
            
            self.connection.commit()

            print(cursor.rowcount, "record inserted.")
        except Exception as e:
            print(str(e))

    def getidBystudentid(self,stdid):
        try:
            cursor=self.connection.cursor()
            query="select * from bookIssue where student_id=%s and approved=%s"
            val=(stdid,"no")
            
            cursor.execute(query,val)
            
            row=cursor.fetchone()
           
            return row
        except Exception as e:
            print(str(e))

    def tbl3(self,stdid):
        try:
            cursor=self.connection.cursor()
            query="select * from bookIssue "
            
            cursor.execute(query)
            
            row=cursor.fetchall()
           
            return row
        except Exception as e:
            print(str(e))

    def tbl33333(self):
        try:
            cursor=self.connection.cursor()
            query="select * from bookIssue "
            
            cursor.execute(query)
            
            row=cursor.fetchall()
           
            return row
        except Exception as e:
            print(str(e))



    def deleteTbl3Record(self,id):
        try:
            mycursor=self.connection.cursor()
            sql = "DELETE FROM bookIssue WHERE iid=%s"
            val=(id)
            mycursor.execute(sql,val)

            self.connection.commit()

            print(mycursor.rowcount, "record(s) deleted")
        except Exception as e:
            print(str(e))
        
    # check if username is avaliable
    def checkIfusernameIsAvaliable(self,username):
        try:
            cursor=self.connection.cursor()
            query="select * from users where username=%s"
            val=(username)
            cursor.execute(query,val)
            
            row=cursor.fetchone()
            if row==():
                return True
            else:
                return row
        except Exception as e:
            print(str(e))

    # check if username is avaliable
    def isemailAvaliable(self,email):
        try:
            cursor=self.connection.cursor()
            query="select * from users where email=%s"
            val=(email)
            cursor.execute(query,val)
            
            row=cursor.fetchone()
            if row==():
                return True
            else:
                return row
        except Exception as e:
            print(str(e))


    def studentCountInBookIssue(self,stdid):
        try:
            cursor=self.connection.cursor()
            query="select * from bookIssue where student_id=%s and approved=%s and returnStatus=%s"
            val=(stdid,"yes","false")
            cursor.execute(query,val)
            
            row=cursor.fetchall()
            records=int(len(row))
        except Exception as e:
            print(str(e))






#----------------------------------------
    def updateProfileOnDatabase(self,name,email,uname,password,rollno,prId):
            try:
                cursor=self.connection.cursor()
                query="update users set name=%s,username=%s,password=%s,email=%s,rollno=%s where id=%s"
                val=(name,uname,password,email,rollno,prId)
                cursor.execute(query,val)
                self.connection.commit()
            except Exception as e:
                print(str(e))             




#------------------------
    def convertToListOfDicts(self,data):
        lis = []
        for prod in data:
            dicObj = {};
            dicObj["name"]=prod[0]
            dicObj["username"]=prod[1]
            dicObj["email"]=prod[2]
            dicObj["rollno"]=prod[3]
            lis.append(dicObj)
        return lis

    def showStudents(self):
        try:
            cursor=self.connection.cursor()
            query='select name,username,email,rollno from users where role=%s'
            args=("student")
            cursor.execute(query,args)
            data=cursor.fetchall()
            listOfDicts=self.convertToListOfDicts(data)
            return listOfDicts
        except Exception as e:
            raise Exception("show students nhi chal rha")

    def getProfileFromDataBase(self,uname,password):
            try:
                row = ()
                cursor=self.connection.cursor()
                query="select name,username,password,email,rollno,id from users where username=%s and password=%s "
                val=(uname,password)
                cursor.execute(query,val)
                row=cursor.fetchone()
                print(row)
                return row

            except Exception as e:
                print(str(e))    

    def getEmailFromId(self,id):
            try:
                row = ()
                cursor=self.connection.cursor()
                query="select email from users where id=%s"
                val=(id)
                cursor.execute(query,val)
                row=cursor.fetchone()
                print(row)
                return row

            except Exception as e:
                print(str(e))    



    def updateBook(self,id,name,autName,isb,desc,quant,link):
        try:
            cursor=self.connection.cursor()
            query='update book set bname=%s,author=%s,isbn=%s,description=%s,quantity=%s,pdflink=%s where bid=%s'
            args=(name,autName,isb,desc,quant,link,id);
            cursor.execute(query,args)
            self.connection.commit()
        except Exception as e:
            raise Exception("Book Update not working")      



    def convertBookTuplesToListOfDicts(self,data):
        lis = []
        for prod in data:
            dicObj = {}
            dicObj["id"]=prod[0]
            dicObj["bname"]=prod[1]
            dicObj["author"]=prod[2]
            dicObj["isbn"]=prod[3]
            dicObj["description"]=prod[4]
            dicObj["quantity"]=prod[5]
            dicObj["pdflink"]=prod[6]
            lis.append(dicObj)
        return lis
    def getlistOfBooks(self):
        try:
            cursor=self.connection.cursor()
            query="select *  from book"
            cursor.execute(query)
            row=cursor.fetchall()
            ls=self.convertBookTuplesToListOfDicts(row)
            return ls
        except Exception as e:
            raise Exception("Book Update not working")      


    def getBookIdfromtbl3(self,recordid):
        try:
            cursor=self.connection.cursor()
            query="select *  from bookIssue where iid=%s and approved=%s"
            val=(recordid,"yes")
            cursor.execute(query,val)
            row=cursor.fetchone()
            
            return row
        except Exception as e:
            raise Exception("Book Update not working")      



    def updateBookQuantity(self,quantity,bookid):
        try:
            cursor=self.connection.cursor()
            query="UPDATE book SET quantity=%s WHERE bid=%s"
            val=(quantity,bookid)
            
            cursor.execute(query,val)
            
            self.connection.commit()

            print(cursor.rowcount, "record inserted.")

        except Exception as e:
            print(str(e))