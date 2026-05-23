from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Numeric
)
from database.db import Base
class CountryMaster(Base):
    __tablename__ = "country_master"
    id = Column( Integer,primary_key=True)
    country_name = Column(String(100))
    country_code = Column(String(10))
    currency = Column(String(20))
    tax_system = Column(String(50))
    customs_authority = Column(String(100))
    default_vat = Column(Numeric(5,2))
    risk_level = Column(String(50))
    sanction_flag = Column(Boolean,default=False)