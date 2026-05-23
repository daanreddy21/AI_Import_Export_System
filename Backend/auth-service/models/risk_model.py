from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    TIMESTAMP,
    Text
)
from sqlalchemy.sql import func
from database.db import Base
class RiskAnalysis(Base):
    __tablename__ = "risk_analysis"
    id = Column(Integer, primary_key=True)
    buyer_name = Column(String)
    country = Column(String)
    hsn_code = Column(String)
    product = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    unit_price = Column(Numeric(12,2))
    pending_payments = Column(Integer)
    overdue_payments = Column(Integer)
    total_pending_amount = Column(Numeric(12,2))
    shipment_risk = Column(Integer)
    client_risk = Column(Integer)
    final_risk = Column(Integer)
    risk_level = Column(String)
    risk_reasons = Column(Text)
    recommendation = Column(Text)
    created_at = Column( TIMESTAMP, server_default=func.now() )
