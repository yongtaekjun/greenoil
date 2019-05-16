TUPLE1_TANK_SIZES = (
    (   16, '  4 Gallon (  16 L ) Pail' ),
    (  200, ' 55 Gallon ( 200 L ) Drum' ),
    (  400, '110 Gallon ( 400 L ) Bin' ),
    (  600, '158 Gallon ( 600 L ) Bin' ),
    (  800, '211 Gallon ( 800 L ) Bin' ),
    ( 1000, '264 Gallon (1000 L ) Bin' ),
)


TUPLE1_DIVISIONS = (
    (  0, 'North' ),
    ( 45, 'North East' ),
    ( 90, 'East' ),
    (135, 'South East' ),
    (180, 'South' ),
    (225, 'South West' ),
    (270, 'West' ),
    (315, 'North West' ),
)

TUPLE1_USER_TITLES = (
    (1, 'Mr.'),    
    (2, 'Miz'),
    (3, 'Miss'),
    (4, 'Mrs'),
)
TUPLE1_COMPANY_TYPES = (
    (1, 'Restaurant'),    
    (2, 'Oil Collector'),
)

TUPLE2_USER_ROLES = (
    ('Company', ( 
            ( 111, 'Owner/CEO'), 
            ( 113, 'Manager'),
            ( 115, 'Receptionist'),
            ( 117, 'Marketer'),
            ( 119, 'Sales Person'),
            ( 121, 'Accountant'),
            ( 123, 'Director'),
            ( 125, 'Vice President'),
            ( 127, 'HR Specialist'),
            ( 141, 'System Operator'),
    )),
    # ('Restaurant', ( 
    #         ( 211, 'Chef'), 
    #         ( 212, 'Waiter/Waitress'), 
    # )),
    ('Oil Collector', ( 
            ( 211, 'Truck Driver'), 
            ( 213, 'Tank Installer'), 
            ( 217, 'Welder'),
            ( 218, 'In-house Handler'),
            ( 219, 'Dispatcher'),
    )),
    # ('Trading', ( 
    #     ( 321, 'Accountant'),
    #     ( 323, 'Marketer'),
    #     ( 325, 'Sales Person'),
    #     ( 327, 'Director'),
    #     ( 331, 'CEO/President'),
    #     ( 341, 'System Operator'),
    # )),
    # ('Consulting', ( 
    #     ( 423, 'Consultant'),
    #     ( 425, 'Project Manager'),
    #     ( 431, 'CEO/President'),
    # )),
    ('Information Technology', ( 
            ( 912, 'Server Administrator'),
            ( 914, 'Graphic Designer'),
            ( 916, 'Project Manager'),
            ( 918, 'Consultant'),
            ( 921, 'Business Logic Analyzer'),

            ( 923, 'Data Model Designer'),
            ( 951, 'Programmer'),
            ( 953, 'WEB Front-End Programmer'),
            ( 955, 'Android Programmer'),
            ( 957, 'iOS Programmer'),
            ( 961, 'Back-End Programmer'),
            ( 962, 'Fullstack Programmer'),
            ( 971, 'System Architect'),
    )),
)

#------------------------------------------------------------------------------
TUPLE2_CLIENT_REQUESTS = (
    ( 'Contract', ( (  1,  'Request Contract'), ) ),
    ( 'Pickup',   ( (  3,  'Pickup'), ) ),
    ( 'Tank',     ( (  5,  'Install Tank'),( 7, 'Repair Tank'),( 9,    'Return Tank'), ) ),
    ( 'Payment',  ( ( 11,  'Show Bill'), ) ),
    # ( 'Ordering',  ( ( ORDERING,   'Order product'), ) ),
)

#------------------------------------------------------------------------------
TUPLE2_UINT_SYMBOLS = (
    ('Volume', ( ( 1, 'Litter'), ( 2, 'Gallon'), ) ),
    ('Weight', ( (11, 'Kg'),     (12, 'Pound'), (13, 'Ton'), (14, 'Ounce'),) ),
    ('Area',   ( (21, 'sq. cm'), (22, 'sq. ft'), ) ),
)

#------------------------------------------------------------------------------
TUPLE1_PAID_METHODS = (
    ( 1, 'Cash'),
    ( 3, 'Credit Card'),
    ( 5, 'Cheque'),
    ( 7, 'Paypal'),
)

#------------------------------------------------------------------------------
TUPLE1_PROCESSING_STATUS = (
    ( 1,    'Scheduled'),
    ( 3,    'Completed'),
    ( 5,         'Paid'),
)

"""
DICT2 means 2 dimensional dictionary
TUPLE2 means 2 dimensional tuple

dict1 change '2 dimensional dictionary or 2 dimensional tuple' to 1 dimensional dictionary
It is useful to show string value instead of integer key.
ex: What is youe role in the company : 111 (Bad for display, Good for database)
ex: What is youe role in the company : 'Manager' (Good for display, Bad for database)

Use builtin dict function for 1 dimensional tuple
"""
def dict1 ( DICT2_OR_TUPLE2 ):
    DICT1 = {}

    if type(DICT2_OR_TUPLE2) == dict:
        { DICT1.update ( DICT2_OR_TUPLE2[v1]) for v1 in DICT2_OR_TUPLE2 }
    else:
        for k, v in DICT2_OR_TUPLE2:
            for k1, v1 in v:
                DICT1.update ( {k1:v1}  )
    return DICT1
