from app import db, app, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))

# The Users database model
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    times_rented = db.Column(db.Integer, default=0)
    # Relationship to Orders and Payment methods
    orders = db.relationship('Orders', backref='user', lazy=True)
    payment_methods = db.relationship('Payment_Methods', backref='user', lazy=True)

    def get_reset_token(self, expires_seconds=3600):
        s = Serializer(app.config['SECRET_KEY'], expires_seconds)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)

# The Staff database model
class Staff(db.Model, UserMixin):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    # Foreign keys
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)

# The Bikes database model
class Bikes(db.Model):
    __tablename__ = 'bikes'
    id = db.Column(db.Integer, primary_key=True)
    days_used = db.Column(db.Integer, default=0)
    times_rented = db.Column(db.Integer, default=0)
    times_repaired = db.Column(db.Integer, default=0)
    available = db.Column(db.Boolean, default=True)  # If it is booked/sent for repairs
    # Foreign keys
    bike_type_id = db.Column(db.Integer, db.ForeignKey('bike_types.id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)
    # Relationship to Rented Bikes and repairs
    rented_bikes = db.relationship('Rented_Bikes', backref='bike', lazy=True)
    repairs = db.relationship('Repairs', backref='bike', lazy=True)

# The Bike_Types database model
class Bike_Types(db.Model):
    __tablename__ = 'bike_types'
    id = db.Column(db.Integer, primary_key=True)
    gears = db.Column(db.Integer, default=0)
    weight = db.Column(db.Float, default=0.0)
    brand = db.Column(db.String(50),nullable=False)
    model = db.Column(db.String(50),nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    colour = db.Column(db.String(50),nullable=False)
    user_type = db.Column(db.String(100),nullable=False)
    use_type = db.Column(db.String(100),nullable=False)
    times_rented = db.Column(db.Integer, default=0)
    # Relationships to Bikes and Rental_Rates
    bikes = db.relationship('Bikes', backref='bike_type', lazy=True)
    rental_rates = db.relationship('Rental_Rates', backref='bike_type', lazy=True)

# The Rental_Rates database model
class Rental_Rates(db.Model):
    __tablename__ = 'rental_rates'
    id = db.Column(db.Integer, primary_key=True)
    daily_rate = db.Column(db.Float, default=0.0)
    weekly_rate = db.Column(db.Float, default=0.0)
    monthly_rate = db.Column(db.Float, default=0.0)
    # Foreign keys
    bike_type_id = db.Column(db.Integer, db.ForeignKey('bike_types.id'), nullable=False)

# The Shops database model
class Shops(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(100), unique=True, nullable=False)
    latitude = db.Column(db.Float, default=0.0)
    longitude = db.Column(db.Float, default=0.0)
    address = db.Column(db.String(100), unique=True, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    # Relationship to Bikes
    bikes = db.relationship('Bikes', backref='shop', lazy=True)

# The Repairs database model
class Repairs(db.Model):
    __tablename__ = 'repairs'
    id = db.Column(db.Integer, primary_key=True)
    date_complete = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String(500), nullable=False)
    cost = db.Column(db.Float, default=0.0)
    # Foreign key
    bike_id = db.Column(db.Integer, db.ForeignKey('bikes.id'), nullable=False)

# The Rented_Bikes database model
# (Bookings of a single bike)
class Rented_Bikes(db.Model):
    __tablename__ = 'rented_bikes'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, default=0.0)
    # Foreign keys
    bike_id = db.Column(db.Integer, db.ForeignKey('bikes.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)

# The Orders database model
# (May consist of several Rented_Bikes)
class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_price = db.Column(db.Float, default=0.0)
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Relationship to Rented_Bikes
    rented_bikes = db.relationship('Rented_Bikes', backref='order', lazy=True)

# The Payment Methods database model
class Payment_Methods(db.Model):
    __tablename__ = 'payment_methods'
    id = db.Column(db.Integer, primary_key=True)
    online = db.Column(db.Boolean, default=True) # Whether it was paid online or in store
    card_number = db.Column(db.String)
    expiration_month = db.Column(db.String)
    expiration_year = db.Column(db.String)
    cvv = db.Column(db.String)
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
