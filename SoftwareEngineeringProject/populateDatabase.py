from config import SQLALCHEMY_DATABASE_URI
from app import db, models, bcrypt
import os.path
import random
import datetime
from datetime import timedelta
import time


def calculateRentPrice(numberOfDays,rentalRates):
    # we have a start date
    # and an end date
    # so we can find out the number of days
    # we have a a daily rate, weekly rate and monthly rate

    # we round the rental rate to the nearest 10p
    # so it isn't as bad for the user

    # less than a week case
    if(numberOfDays < 7):
        # return the number of days * the weekly raet
        return rentalRates.daily_rate * numberOfDays

    # less than a month case
    if(numberOfDays < 28):
        # we divide the weekly rate by seven and multiply my number of days
        return round((rentalRates.weekly_rate/7) * numberOfDays,1)

    # more than a month
    # so we take the monthly rate / 28 and multiply by number of days
    return round((rentalRates.monthly_rate/28) * numberOfDays,1)

def readFromCSV():
    bikeData = open("bikeSpreadsheet.csv").read()  # read from the database
    bikeData = bikeData.split(",") # split by commas

    # since the last column ends with a \n, remove these newlines, which
    # is a litle bit difficult since ["price\n14"] -> ["price","14"]
    # which will cause some indexing errors, so we have to be careful.
    i = 0
    while(i<len(bikeData)):
        if("\n" in bikeData[i]):
            bikeData = bikeData[:i] + [bikeData[i].split("\n")[0]] + [bikeData[i].split("\n")[1]] + bikeData[i+1:]
        i+=1
    # remove the header and the last item which is just ''
    bikeData = bikeData[9:-1]

    return bikeData

def addBikeTypes():
    bikeData = open("bikeSpreadsheet.csv").read()  # read from the database
    bikeData = bikeData.split(",") # split by commas

    # since the last column ends with a \n, remove these newlines, which
    # is a litle bit difficult since ["price\n14"] -> ["price","14"]
    # which will cause some indexing errors, so we have to be careful.
    i = 0
    while(i<len(bikeData)):
        if("\n" in bikeData[i]):
            bikeData = bikeData[:i] + [bikeData[i].split("\n")[0]] + [bikeData[i].split("\n")[1]] + bikeData[i+1:]
        i+=1
    # remove the header and the last item which is just ''
    bikeData = bikeData[9:-1]


    # now printout the information
    for i in range(0,len(bikeData),9):
        print(bikeData[i],bikeData[i+1],bikeData[i+2],bikeData[i+3],bikeData[i+4],bikeData[i+5],bikeData[i+6],bikeData[i+7],bikeData[i+8])
        newBike = models.Bike_Types(gears=bikeData[i],weight=bikeData[i+1],brand=bikeData[i+2],model=bikeData[i+3],image=bikeData[i+4],colour=bikeData[i+5],user_type=bikeData[i+6],use_type=bikeData[i+7],times_rented=0)
        db.session.add(newBike)

    db.session.commit()
    time.sleep(2)

def addShops():
    # this function creates all the details for the stores
    names = ["Leeds University Union","Headingley","City Centre"]
    addresses = ["Lifton Place, Leeds, LS2 9JZ","2 St Michael's Road, Leeds LS6 3AW","Unit 1, New Station St, Leeds LS1 5DE"]
    numbers = ["01133801400","01132785836","01132469132"]
    latitudes = ["53.807348","53.819343","53.795557"]
    longitudes = ["-1.558362","-1.577345","-1.544413"]
    for i in range(3):
        print("Adding Shop: ",names[i])
        newShop = models.Shops(location_name=names[i],
                               address=addresses[i],
                               contact_number=numbers[i],
                               latitude=latitudes[i],
                               longitude=longitudes[i])
        db.session.add(newShop)
        db.session.commit()
    time.sleep(2)

def addIndividualBikes():
    print("Now Adding invididual bikes")
    numOfBikesToAdd = 72 # so we get one of every bike in the store
    numberOfShops = 3  # every store we have

    # get all ID's
    bikeIDs = []
    allBikes = models.Bike_Types.query.all()
    for bike in allBikes:
        bikeIDs.append(bike.id)

    # get all shops
    shopIDs = []
    allShops = models.Shops.query.all()
    for shop in allShops:
        shopIDs.append(shop.id)

    # create the initial bikes, simulating how many times they have been rented in the past
    for shopID in range(numberOfShops):
        for i in range(numOfBikesToAdd):
            daysUsed = random.randint(10,100)
            timesRented = int(daysUsed / (random.randint(1,5)))
            timesRepaired = random.randint(0,10)
            newBike = models.Bikes(days_used=daysUsed,times_rented=timesRented,times_repaired=timesRepaired,available=True,bike_type_id=bikeIDs[i],shop_id=shopIDs[shopID])
            print("Adding Bike: " + str(bikeIDs[i]) + "," + str(shopIDs[shopID]))
            db.session.add(newBike)

    db.session.commit()
    time.sleep(2)

def addRentalRates():
    # for every bike, we can see how much it costs to rent it
    # rental Rental_Rates (percentage of bike price)
    #
    # day 2%
    # week 8%
    # month 20%
    dayPercent = 0.02
    weekPercent = 0.08
    monthPercent = 0.2
    bikeIDs = []
    allBikeData = readFromCSV()
    allBikes = models.Bike_Types.query.all()
    for bike in allBikes:
        bikeIDs.append(bike.id)
    for i in range(0,len(allBikeData),9):
        print("Adding bike rental rate " + str(bikeIDs[i//9]))
        bikePrice = int(allBikeData[i+8])
        newRentalRate = models.Rental_Rates(daily_rate=round(bikePrice*dayPercent),
                                            weekly_rate=round(bikePrice*weekPercent),
                                            monthly_rate=round(bikePrice*monthPercent),
                                            bike_type_id=bikeIDs[i//9]
                                            )
        db.session.add(newRentalRate)
    db.session.commit()
    time.sleep(2)

def addStaff():

    names = ["Jonathan","Matthew","Slavyana","Domantas","Ciaran","Andy"]
    secondNames = ["Alderson","Cumber","Chervenkondeva","Dilys","Brennan","Parkes"]
    addresses = ["70 Royal Park Road","The Tannery Flat 31","Charles Morris","Leodis","Liberty Dock","Wokefield"]

    for i in range(len(names)):
        print("Adding staff member " + names[i] + " " + secondNames[i])
        # adding all the members of staff with a hashed password, they are all the same for testing
        # purposes. All members of staff are people from our project
        newStaff = models.Staff(email=names[i] + secondNames[i] + "@gmail.com",
                              password= bcrypt.generate_password_hash("password").decode('utf-8'),
                              contact_number="07" + str(random.randint(100000000,999999999)),
                              name=names[i] + " " + secondNames[i],
                              address = addresses[i],
                              admin=True,
                              shop_id = (i+2)//2)
        db.session.add(newStaff)
    db.session.commit()
    time.sleep(2)

def addUsersAndRentals():

    # add all the users
    numberOfUsers = 72*3 # one user for each bike

    names = ["Tom","Alice","Peter","Gabriel","Tohfah","Della","June","Matthew","Conor","Thomas","James","Stephen","Max","Mac","Clarissa","Jane","Richard","Lisa","Paul","Allen","Sam","Jennifer","Jane","Imogen","Rowena"]
    secondNames = ["Alderson","Carey","Yates","Robinson","Faucher","Acaster","Brimm","Gunn","DeMarco","Beckett","Fuhn","Amis","McNiel","Hacket","Calle","Court","Smith","Birch","Parkes","Dilys","Liddle","King","Hearne","Thor"]
    for i in range(numberOfUsers):
        firstName = random.choice(names)
        secondName = random.choice(secondNames)
        print("i = " + str(i) + " Adding " + firstName + " " + secondName)
        newUser = models.Users(email=firstName + secondName + str(random.randint(0,10000)) + "@gmail.com",
                              password=bcrypt.generate_password_hash("password").decode('utf-8'),
                              contact_number="07" + str(random.randint(100000000,999999999)),
                              times_rented=random.randint(0,10))
        db.session.add(newUser)

        # add a random payment method to each user
        cardNumber = str(random.randint(1111111111111111,9999999999999999))
        lastFourDigits = cardNumber[-4:] # the last four digits
        cardNumber = bcrypt.generate_password_hash(cardNumber).decode('utf-8') + "##cardname=" + lastFourDigits # so we have something to show to the user
        print("Card number = ",cardNumber)
        newPaymentMethod = models.Payment_Methods(  card_number = cardNumber,
                                                    expiration_month = str(random.randint(1,12)),
                                                    expiration_year = str(random.randint(2019,2023)),
                                                    cvv = bcrypt.generate_password_hash(str(random.randint(111,999))).decode('utf-8'),
                                                    user_id = i+1)
        db.session.add(newPaymentMethod)

    db.session.commit()

    allBikes = models.Bikes.query.all()
    allRentalRates = models.Rental_Rates.query.all()
    numberOfBikes = 72*3

    # making it so that every user has one 'order' in the system.
    # that one order contains exactly one bike.
    # this is so that the system is full of users and we can make
    # graphs.
    for i in range(numberOfUsers):
            year = 2019 # this year, so we can see how changing the dates effect things
            month = random.randint(1,12)
            day = random.randint(1,27)
            startDate = datetime.date(year,month,day)
            daysToRent = random.randint(5,70)
            endDate = startDate + timedelta(days=daysToRent)

            # find the price of the order from the rental rates
            bikeID = allBikes[i].id
            bikeTypeID = allBikes[i].bike_type_id

            thisRentalRate = -1
            for rentalRate in allRentalRates:
                if(rentalRate.bike_type_id == bikeTypeID):
                    thisRentalRate = rentalRate

            price = calculateRentPrice(daysToRent,thisRentalRate)

            # add the order for the customer
            print("i = " + str(i) + " Adding order " + str(year) + "/" + str(month) + "/" + str(day) + ": " + str(price))
            print("Renting bikeID: " + str(bikeID) + " with rental rates " + str(thisRentalRate.daily_rate) + ":" + str(thisRentalRate.weekly_rate) + ":" + str(thisRentalRate.monthly_rate))
            print("For " + str(daysToRent) + " days")
            print("bikeTypeID: " + str(bikeTypeID))

            # add the order
            newOrder = models.Orders(date=startDate,
                                    total_price=price,
                                    user_id=i+1,)

            db.session.add(newOrder)

            # add the rental for the customer
            newRental = models.Rented_Bikes(start_date = startDate,
                                            end_date= endDate,
                                            price = price,
                                            bike_id=bikeID,
                                            order_id=i+1)
            db.session.add(newRental)


    db.session.commit()
    time.sleep(2)



addShops()
addBikeTypes()
addIndividualBikes()
addRentalRates()
addUsersAndRentals()
addStaff()
