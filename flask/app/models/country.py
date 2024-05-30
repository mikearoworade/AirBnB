from app.init import db
from sqlalchemy import Column, Integer, Float, String

class Country(db.Model):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital = Column(String)
    area = Column(Float)