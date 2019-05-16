# greenoil
Used Vegetable Oil Collection System
======================================================================================
1. Oil Collector needs Used Vegetable Oil.
2. Restaurant want to waste their used oil.
3. Oil Collector support oil tank and pick up the oil.
4. Oil Collector want to know when the pickup should be done. 


You can test it at http://45.79.189.159/

Model Summary
=======================================================================================
+ Company: Company Information: name, address, location ,...
  - Restaurant: child class of Company
  - OilCollector: child class of Company, it has many Restaurant as a client
+ Role:
  - User has multi-role with company
    ex: user1 is a truck driver at OilCollector also he is a Restaurant owner at Chowon Restaurant.
+ User & UserProfile: User login Information and etc.

+ Call:
  - It is kind of user request, claim, call,...
  - Restaurant manager calls to pickup his/her oil in tank which is almost full. 
