# Create your views here.
from django import contrib
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime 
from firebase import firebase
from requests import post,get
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import SESSION_KEY, authenticate
from django.contrib.auth import logout,login
import pyrebase 
from pyrebase.pyrebase import Database
import firebase_admin
from firebase_admin import auth ,credentials, db
from datetime import date
from datetime import datetime 
import uuid
config = {    
    "apiKey": "AIzaSyDxtgOS-lNR5iHH-35xjs9r1gIwiLDW6E8",
    "authDomain": "neemeesh-trial.firebaseapp.com",
    "databaseURL": "https://neemeesh-trial-default-rtdb.firebaseio.com",
    "projectId": "neemeesh-trial",
    "storageBucket": "neemeesh-trial.appspot.com",
    "messagingSenderId": "608861234921",
    "appId": "1:608861234921:web:2792a40a8e9cf8611c7278",
    'measurementId': "G-67HDRQV9KN"
}
firebase = pyrebase.initialize_app(config) 
authe = firebase.auth() 
database = firebase.database()
cred = credentials.Certificate('neemeesh-trial-firebase-adminsdk-kl0a5-1cf2f25008.json')
firebase_admin.initialize_app(cred)
def index(request):
    #context = {"variable1": "Harry is great", "variable2": "Rohan is great"}
    #return HttpResponse("This is homepage")
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')    
def prelogin(request):
    return render(request,'prelogin.html')  
def adminlogin(request):
    return render(request,'adminlogin.html')    
def dispatchlogin(request):
    return render(request,'dispatchlogin.html')    
def mislogin(request):
    return render(request,'mislogin.html')    
def bookinglogin(request):
    return render(request,'bookinglogin.html')
def registeradmin (request) :
    return render(request , "registeradmin.html")    
def registerbooking (request) :
    return render(request , "registerbooking.html")    
def registerdispatch (request) :
    return render(request , "registerdispatch.html")    
def registermis (request) :
    return render(request , "registermis.html")    
def postregisteradmin (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registeradmin.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("Admin").push(data)
    print("User created")
    msg="You have successfully registered a new Admin!"
    return render(request,"registernewuser.html",{"msg":msg})
    # messages.success(request, 'Your have successfully registered!')
    # return render(request,"registernewuser.html")
def postregisterbooking (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registeradmin.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("Booking").push(data)
    print("User created")
    msg="You have successfully registered a new Booking User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postregistermis (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registeradmin.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("MIS").push(data)
    print("User created")
    msg="You have successfully registered a new MIS User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postregisterdispatch (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registeradmin.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("Dispatch").push(data)
    msg="You have successfully registered a new Dispatch User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postloginadmin (request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Admin', None) 
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['Email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'adminhome.html')
            except:
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"adminlogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"adminlogin.html",{"msg":msg}) 
def postloginbooking(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Booking', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['Email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'lh1.html')
            except :
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"bookinglogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"bookinglogin.html",{"msg":msg})
def postloginmis(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/MIS', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['Email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'lh2.html')
            except :
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"mislogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"mislogin.html",{"msg":msg})
def postlogindispatch(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Dispatch', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['Email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'lh3.html')
            except :
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"dispatchlogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:      
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"dispatchlogin.html",{"msg":msg})
def registernewuser(request):
    return render(request , "registernewuser.html")
def registernewproduct(request):
    return render(request , "registernewproduct.html")
def lh1(request):
     pass
def lh2(request):
     pass  
def lh3(request):
     messages.success(request, 'You have successfully logged in')  
     pass
def postresetbooking (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "bookingreset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "bookingreset.html", {"msg":message})
def postresetdispatch (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "postresetdispatch.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "postresetdispatch.html", {"msg":message})
def postresetmis (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "misreset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "misreset.html", {"msg":message})  
def postresetadmin (request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "postresetadmin.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "postresetadmin.html", {"msg":message})
def bookingforget (request) :
    return render (request ,"bookingreset.html")
def dispatchforget (request) :
    return render (request ,"dispatchreset.html")
def misforget (request) :
    return render (request ,"misreset.html")
def adminforget (request) :
    return render (request ,"postresetadmin.html")

def registernewcompany(request):
    return render(request , "registernewcompany.html")

def postregisternewcompany(request):
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    Data={
        'Company id': request.POST.get('compid'),
        'Company Name': request.POST.get('compname'),
        'Email id': request.POST.get('compmail'),
        'Contact Number 1': request.POST.get('compcont1'),
        'Contact Number 2': request.POST.get('compcont2'),
        'Address': request.POST.get('compadd'),
        'City': request.POST.get('compcity'),
        'Pincode' : request.POST.get('pincode'),
        'State': request.POST.get('compstate'),
    }
    firebase.post('/Data/Company/', Data)
    msg="Company is Registered Successfully!"
    return render(request,"registernewcompany.html",{"msg":msg})
def usertable (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    admindata=list(firebase.get("/Data/Signup/Admin",None).values())
    dispatchdata=list(firebase.get("/Data/Signup/Dispatch",None).values())
    bookingdata=list(firebase.get("/Data/Signup/Booking",None).values())
    misdata=list(firebase.get("/Data/Signup/MIS",None).values())
    #print(data[0]['address'])
    return render (request ,"usertable.html",{'admindata':admindata,'dispatchdata':dispatchdata,'bookingdata':bookingdata,'misdata':misdata,})
def checkuserupdate(request)  :
    return  render(request ,"checkuserupdate.html" )
def postcheckuserupdate (request) :
    user_type = request.POST.get("usertype")
    old_email = request.POST.get("email")
    db = database.child("Data").child("Signup").child(user_type).get()
    for user in db.each() :
        if user.val()['Email']==old_email and auth.get_user_by_email(old_email) : 
            return render(request , "updateuser.html" ,{"olemad_il":old_email, "user_type": user_type})
    return render(request , "checkuserupdate.html" , {"msg" : "User not Found!"})
    
def postuserupdate(request):
    email = request.POST.get("old_email")
    user_type = request.POST.get("usertype")
    db = database.child("Data").child("Signup").child(user_type).get()
    new_address = request.POST.get("newaddress")
    new_city = request.POST.get("newcity")
    new_userid = request.POST.get("newuserid")
    new_name = request.POST.get("newname")
    new_phone= request.POST.get("newphone")
    new_pincode = request.POST.get("newpincode")
    new_state = request.POST.get("newstate")
    '''user=authe.create_user_with_email_and_password(new_email,passw1)
    session_id=user['idToken']
    request.session['uid']=str(session_id)'''
    for i in db.each() :
                database.child("Data").child("Signup").child(user_type).child(i.key()).update({
                "Address" : new_address ,
                 "City"   : new_city ,
                 "User Id": new_userid ,
                 "Name"   : new_name ,
                 "Phone Number"  : new_phone ,
                 "Pincode": new_pincode ,
                 "State"  :  new_state ,
                 "Email": email,
                })
    return render(request , "adminupdate.html" , {"msg1" : "The details of the required user have been updated !!"})
        
def deleteuser(request)  :
    return render(request,"deleteuser.html")
def postdeleteuser(request):
    user_type = request.POST.get("usertype")
    email = request.POST.get("email")
    db = database.child("Data").child("Signup").child(user_type).get()
    for user in db.each() :
        if user.val()['Email']==email : 
            database.child("Data").child("Signup").child(user_type).child(user.key()).remove()
            user = auth.get_user_by_email(email)
            auth.delete_user(user.uid)
            return render(request , "deleteuser.html" , {"msg" : "The User is deleted succesfully!"})
    return render(request , "deleteuser.html" , {"msg" : "User not Found!"})
def productdetails(request):
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    compdetails=list(firebase.get("/Data/Product",None).values())
    return render (request ,"productdetails.html",{'compdetails':compdetails})


def bookingorder1 (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    companies=list(firebase.get("/Data/Company",None).values())
    compnames=[]
    for compdetails in companies:
        for eachcompkey,eachcompval in compdetails.items():
            if eachcompkey=='Company Name':
                compnames.append(eachcompval)
    present_date = date.today().strftime("%d/%m/%Y")
    return render(request, 'bookingorder1.html' , {"compnames" : compnames , "present_date": present_date})

def postbookingorder1 (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    companies=list(firebase.get("/Data/Company",None).values())
    compnames=[]
    for compdetails in companies:
        for eachcompkey,eachcompval in compdetails.items():
            if eachcompkey=='Company Name':
                compnames.append(eachcompval)
    fromcity = request.POST.get("fromcity")
    company_name = request.POST.get("compname1")
    datee = request.POST.get("date")
    docket_no = request.POST.get("docno")
    return render(request , "bookingorder.html"  , {"fromcity":fromcity , "company_name" : company_name , "datee" : datee , "docket_no" : docket_no})



'''def bookingorder(request):
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    companies=list(firebase.get("/Data/Company",None).values())
    compnames=[]
    for compdetails in companies:
        for eachcompkey,eachcompval in compdetails.items():
            if eachcompkey=='Company Name':
                compnames.append(eachcompval)
    present_date = date.today().strftime("%d/%m/%Y")
    
    return render(request, 'bookingorder.html' , {"compnames" : compnames , "present_date": present_date})'''

def postbookingorder(request):
    fromcity=request.POST.get("fromcity")
    company_name = request.POST.get("company_name")
    datee = request.POST.get("datee")
    docket_no = request.POST.get("docno")
    destination = request.POST.get("destination")
    partyname= request.POST.get("partyname")
    invoice_no = request.POST.get("invcno")
    noofpckg= request.POST.get("noofpckg")
    description = request.POST.get("description")
    # totalcost = int(cost)*int(noofpckg)
    # print(totalcost)
    bill_id = uuid.uuid4()
    return render (request , "confirmbookingorder.html" , {        
                                                                    "fromcity" : fromcity ,
                                                                    "company_name" : company_name,
                                                                    "datee" : datee , 
                                                                    "docket_no" : docket_no ,
                                                                    "destination" : destination ,
                                                                    "partyname" : partyname ,
                                                                    "invoice_no" : invoice_no ,
 
                                                                    "noofpckg" : noofpckg,
                                                                     
                                                                    "description" : description ,
                                                                    "bill_id" : bill_id    })
   

def registernewproduct(request):
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    companies=list(firebase.get("/Data/Company",None).values())
    compnames=[]
    for compdetails in companies:
        for eachcompkey,eachcompval in compdetails.items():
            if eachcompkey=='Company Name':
                compnames.append(eachcompval)
    return render(request, 'registernewproduct.html',{'compnames':compnames})
def postregisternewproduct(request):    
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    msg="Product is Registered Successfully!"
    companies=list(firebase.get("/Data/Company",None).values())
    compnames=[]
    for compdetails in companies:
        for eachcompkey,eachcompval in compdetails.items():
            if eachcompkey=='Company Name':
                compnames.append(eachcompval)
    Data={
        'Company Name': request.POST.get('compname'),
        'Product Name': request.POST.get('prodname'),
        'Product id': request.POST.get('prodid'),
        'Cost per': request.POST.get('costper'),
        'Cost' : request.POST.get('cost'),
    }
    firebase.post('/Data/Product/', Data)
    return render(request, 'registernewproduct.html',{'compnames':compnames,"msg":msg,})



def postconfirmbookingorder (request) : 

    company_name = request.POST.get("company_name")
    db9 = database.child("Data").child("Product").get()
    for i in db9.each() :
        if i.val()["Company Name"] == company_name : 
             cost=database.child("Data").child("Product").child(i.key()).child("Cost").get().val()



    bill_id = request.POST.get("bill_id")
    # totalcost= request.POST.get("totalcost")
    fromcity = request.POST.get("fromcity")
    # company_name = request.POST.get("company_name")
    datee = request.POST.get("datee")
    docket_no = request.POST.get("docket_no")
    destination = request.POST.get("destination")
    partyname = request.POST.get("partyname")
    noofpckg= request.POST.get("noofpckg")
    invcno = request.POST.get("invoice_no")    
    description = request.POST.get("description")
    totalcost = int(cost)*int(noofpckg)
    data = {
        
        "fromcity" : fromcity ,
        "company_name" : company_name ,
        "date"     : datee , 
        "docket_no" : docket_no ,
        "destination" : destination ,
        "partyname" : partyname ,
        "invcno"   : invcno , 
        "noofpckg" : noofpckg,
        "description" : description,
        "bill_id" : bill_id ,
        "totalcost" : totalcost 
    }

    database.child("Data").child("BookingOrder").child("Orders").push(data)
    msg = "Your Order Has Been Placed Successfully !!"
    return render (request , "bookingorder.html" , {"msg" : msg,"fromcity" : fromcity ,
                                                                    "company_name" : company_name,
                                                                    "datee" : datee , 
                                                                    "docket_no" : docket_no ,})

def postmis (request) :
    return render (request , "lh2.html")


def producttable (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    admindata=list(firebase.get("/Data/BookingOrder/Orders",None).values())
    
   
    #print(data[0]['address'])
    return render (request ,"producttable.html",{'admindata':admindata})


def dispatchuser (request) :
    return render (request , "lh3.html")


def postdispatchuser (request) :
    date1 = request.POST.get("date1")
    date2 = request.POST.get("date2")
    firebase1=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    dates = list(firebase1.get("Data/BookingOrder/Orders" , None).values())
    orderdates=[]
    for i in dates :
        for datename,dateval in i.items() : 
            if datename == "date" :
                orderdates.append(dateval)

                print(orderdates)
    fromcity = request.POST.get("cityname")
    booking_db1 = database.child("Data").child("BookingOrder").child("Orders").get()
    list1=[]
    temp=[]
    for x in orderdates :
        if(x>=date1 and x<=date2) :
            for bookingdb in booking_db1.each() :
                bill_id=database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("bill_id").get().val()
                if (bookingdb.val()["fromcity"] == fromcity and bookingdb.val()["date"] == x and bill_id not in temp) :   
                        list1=list1+[{"bill_id": database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("bill_id").get().val(),
                                     'from_city' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("fromcity").get().val(),
                                     'companyname12' :database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("company_name").get().val(),
                                     'datee' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("date").get().val(),
                                     'destination' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("destination").get().val(),
                                     'partyname' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("partyname").get().val(),
                                     'invcno' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("invcno").get().val()
                                     }]
                        temp.append(bill_id)
    return render (request , "dispatchuser.html", {'list1' : list1})

def confirmdispatch(request):
    bill_id=request.POST.get("bill_id")
    return render (request , "confirmdispatch.html")
