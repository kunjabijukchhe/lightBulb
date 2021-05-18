import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyDj-epa6wHzWuxTqKIINk2d1zaE0RoyQD4",
    'authDomain': "apps-adccc.firebaseapp.com",
    'databaseURL': "https://apps-adccc-default-rtdb.firebaseio.com",
    'projectId': "apps-adccc",
    'storageBucket': "apps-adccc.appspot.com",
    'messagingSenderId': "468281552905",
    'appId': "1:468281552905:web:5ab99a52c80977acdc08d8",
    'measurementId': "G-H9YMW1C8P3"
}

firebase=pyrebase.initialize_app(firebaseConfig);
db=firebase.database()
auth=firebase.auth()
# storage=firebase.storage()

# # #login
# # email=input("Enter your email:")
# # password=input("Enter your password:")
# # try:
# #     auth.sign_in_with_email_and_password(email, password)
# #     print("successfully signed in!")
# # except:
# #     print("invalid")

# # #signup
# # email=input("Enter your email:")
# # password=input("Enter your password:")
# # cpassword=input("Confirm password:")
# # if password==cpassword:
# #     try:
# #         auth.create_user_with_email_and_password(email, password)
# #         print("successfully done!")
# #     except:
# #         print("Something error")

# #Database

# data={
#   'age':20,
#   'address':"Kathamandu",
#   'employee':True,
#   'name':"Kunja Bijukchhe"
# }
# ## Create
# # db.child("detail").push(data)
# # db.child("detail").child("myownid").set(data)

# ##Update
# # db.child('detail').child('myownid').update({'name':'Sudan Thapa'})
# # db.child('detail').child('myownid').update({'f_name':'Sudan'})
# # db.child('detail').child('myownid').update({'l_name':' Thapa'})

# # a=db.child('detail').get()
# # for i in a.each():
# #   # print(i.val())
# #   # print(i.key())
# #   if i.val()['name']=='Sudan Thapa':
# #     db.child('detail').child(i.key()).update({'name':'Kunja Bijukchhe'})

# ##Delete
# # db.child('detail').child('myownid').child('l_name').remove()

# ##Read
# # a=db.child('detail').child('myownid').get()
# a=db.child('bulb').child('lightOne').get()
# print(a)

# # db.child('bulb').update({'lightOne':'true'})

