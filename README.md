# greenoil
Used Vegetable Oil Collection System
=====================================================================================

This is on going project for Oil Collection Company in Toronto, Ontario.
I tested with GO-GraphQL, Dart-Flutter, PHP-CodeIgnitor, Python-Django.
First of all, I would like to select GO-GraphQL framework but example is not enough.
Second, Dart-Flutter-socket was selected good framework. However, it is not good choice for
upgrading frequently.
Third, I decided to choose Progressive Web App platform. Trend was Python.
Django is best framework than others (CodeIgnitor, Flask, ... )
I had not considered Java because I feel it has not much benifit than C++.

Requirements.
=====================================================================================
1. Oil Collector buy Used Vegetable Oil.
2. Restaurant want to sell their used oil.
3. Oil Collector support oil tank and pick up the oil.
4. Oil Collector want to know when the pickup start by daily base. 

Version 0.70 (Current)
======================================================================================
1. Oil Collector Registration
2. Restaurant Registration.
3. User Registration.
4. Oil Collector want to know when the pickup should be done. 
4.1: Batch program to creat (insert) test data for PostgreSQL.

Version 0.73 ( will be implemented May 2019 )
======================================================================================
5. Thus, it needs auto daily pickup scheduling system too. (I build it using crontab)
  - I already implemented it but not tested yet.


Version 0.80 ( will be implemented June 2019 )
=======================================================================================
6. Sometimes, both side need receit to prove their transaction
  I will implement it with javascript for signature.
  
Version 1.00 ( will be implemented Sep. 2019 )
=======================================================================================
7. Connect google map which helps to build routing path for truck driver.

You can test it at http://45.79.189.159/

Model Summary
=======================================================================================
+ City: address information.
+ Company: Company Information: name, address, location ,...
  - Restaurant: child class of Company
  - OilCollector: child class of Company, it has many Restaurant as a client
+ UserRole:
  - User has multi-role with company
    ex: user1 is a truck driver at OilCollector also he is a Restaurant owner at Chowon Restaurant.
+ User & UserProfile: User login Information and etc.

+ Call:
  - It is kind of user request, claim, call,...
  - Restaurant manager calls to pickup his/her oil in tank which is almost full. 
+ Receipt & BillStatement
  - A Receipt will be issued once a month
  - A Receipt is consist of more than one ReceiptStatement.
+ ClientRequest : will be depricated.
+ ProcessingStatus: ..... I am not sure
 
+ ReceiptStatement: will be depricated.
+ PickupHistory: will be depricated. will be replaced with ProcessingStatus
