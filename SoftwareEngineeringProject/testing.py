import os
import unittest
from app import db, models
addUser = models.Users(email="testemail@gmail.com", password="Password", contact_number="3784748433")
addStaff = models.Staff(email="testemail@gmail.com", password="Password", contact_number="47832917438", name="John Smith", address="23 fakelane, leeds", shop_id=1)
addBikeType = models.Bike_Types(gears=7, weight=17.5, brand="test brand", model="test model", colour="blue", user_type="adult", use_type="manual")
addBike = models.Bikes(bike_type_id=0, shop_id=1)

def logIn(user, password):
    for users in models.Users.query.all():
        if users.email == user\
            and users.password == password:
                    return True
    return False

def register(user, password, number):
    if user and password and number:
        for users in models.Users.query.all():
            if users.email == user:
                return False
        return True
    else:
        return False

def changePass(user, oldPass, pass1, pass2):
    currentUser = models.Users.query.filter_by(email=user).first()
    if oldPass == currentUser.password and pass1 == pass2:
        return True
    else:
        return False

def addBike(gears, weight, brand, model, colour, user_type, use_type):
    exists = models.Bike_Types.query.filter_by(model=model).first()
    if exists:
        return False
    else:
        bikeToAdd = models.Bike_Types(gears=gears, weight=weight, brand=brand, model=model, colour=colour, user_type=user_type, use_type=use_type)
        db.session.add(bikeToAdd)
        db.session.rollback()
        return True

def addStaffMem(user, password, number, name, address, shop_id):
    if user and password and number and name and address:
        for users in models.Staff.query.all():
            if users.email == user or users.name == name or users.address == address:
                return False
        return True
    else:
        return False

class LogIn(unittest.TestCase):
    def setUp(self):
        db.session.add(addUser)
    def tearDown(self):
        db.session.rollback()
    def test_successful_login(self):
        assert logIn("testemail@gmail.com", "Password") == True
    def test_wrong_username(self):
        assert logIn("fakeemail@gmail.com", "Password") == False
    def test_successful_password(self):
        assert logIn("testemail@gmail.com", "Password123") == False

class Register(unittest.TestCase):
    def setUp(self):
        db.session.add(addUser)
    def tearDown(self):
        db.session.rollback()
    def test_successful_register(self):
        assert register("uniqueemail@gmail.com", "Password", "3784748433") == True
    def test_nonunique_name(self):
        assert register("testemail@gmail.com", "Password", "3784748433") == False
    def test_no_password(self):
        assert register("nopassword", "", "3784748433") == False
    def test_no_number(self):
        assert register("nopassword", "Password", "") == False
    def test_no_name(self):
        assert register("", "noname", "3784748433") == False
    def test_no_info(self):
        assert register("", "", "") == False

class ChangePassword(unittest.TestCase):
    def setUp(self):
        db.session.add(addUser)
    def tearDown(self):
        db.session.rollback()
    def test_successful_change(self):
        assert changePass("testemail@gmail.com", "Password", "newpassword", "newpassword") == True
    def test_wrong_old_password(self):
        assert changePass("testemail@gmail.com", "wrongpassword", "newpassword", "newpassword") == False
    def test_mismatched_passwords(self):
        assert changePass("testemail@gmail.com", "Password", "newpassword", "otherpassword") == False

class AddABike(unittest.TestCase):
    def setUp(self):
        db.session.add(addBikeType)
    def tearDown(self):
        db.session.rollback()
    def test_successful_add(self):
        assert addBike(8, 17.0, "other test brand", "other test model", "red", "child", "electric") == True
    def test_bike_already_exists(self):
        assert addBike(7, 17.5, "test brand", "test model", "red", "adult", "manual") == False

class AddStaff(unittest.TestCase):
    def setUp(self):
        db.session.add(addStaff)
    def tearDown(self):
        db.session.rollback()
    def test_successful_add(self):
        assert addStaffMem("otheremail@gmail.com", "Password", "67434534", "Alan Smith", "25 fakelane, leeds", shop_id=1) == True
    def test_duplicate_email(self):
        assert addStaffMem("testemail@gmail.com", "Password", "67434534", "Alan Smith", "25 fakelane, leeds", shop_id=1) == False
    def test_duplicate_name(self):
        assert addStaffMem("otheremail@gmail.com", "Password", "47832917438", "John Smith", "25 fakelane, leeds", shop_id=1) == False
    def test_duplicate_address(self):
        assert addStaffMem("otheremail@gmail.com", "Password", "47832917438", "Alan Smith", "23 fakelane, leeds", shop_id=1) == False
    def test_no_email(self):
        assert addStaffMem("", "Password", "67434534", "Alan Smith", "25 fakelane, leeds", shop_id=1) == False
    def test_no_password(self):
        assert addStaffMem("otheremail@gmail.com", "", "67434534", "Alan Smith", "25 fakelane, leeds", shop_id=1) == False
    def test_no_number(self):
        assert addStaffMem("otheremail@gmail.com", "Password", "", "Alan Smith", "25 fakelane, leeds", shop_id=1) == False
    def test_no_name(self):
        assert addStaffMem("otheremail@gmail.com", "Password", "67434534", "", "25 fakelane, leeds", shop_id=1) == False
    def test_no_address(self):
        assert addStaffMem("otheremail@gmail.com", "Password", "67434534", "Alan Smith", "", shop_id=1) == False

if __name__ == '__main__':
    unittest.main()
