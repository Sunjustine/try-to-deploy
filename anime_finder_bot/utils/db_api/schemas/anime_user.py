from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_anime_users import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'anime_users'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(50))
    second_name = Column(String(50))
    username = Column(String(50))
    status = Column(String(30))
    phone_number = Column(BigInteger)
    # referral_id = Column(BigInteger)
    query: sql.select
