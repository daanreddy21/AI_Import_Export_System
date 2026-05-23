from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    TIMESTAMP,
    Text,
    Date, Boolean
)
from sqlalchemy.sql import func
from database.db import Base
class Shipment(Base):
    __tablename__ = "shipments"
    id = Column(Integer, primary_key=True)
    tracking_id = Column(String)
    invoice_number = Column(String)
    buyer_name = Column(String)
    country = Column(String)
    origin_country = Column(String)
    destination_country = Column(String)
    origin_port = Column(String)
    destination_port = Column(String)
    hsn_code = Column(String)
    product = Column(String)
    shipment_value = Column(Numeric(12,2))
    shipping_company = Column(String)
    container_number = Column(String)
    origin_port = Column(String)
    destination_port = Column(String)
    transport_mode = Column(String)
    shipment_status = Column(String)
    estimated_delivery = Column(Date)
    actual_delivery = Column(Date)
    delay_days = Column(Integer, default=0)
    is_delayed = Column(Boolean, default=False)
    approval_status = Column(String, default="Pending")
    approved_by = Column(String)
    approved_at = Column(TIMESTAMP)
    hold_reason = Column(Text)
    remarks = Column(Text)
    created_at = Column( TIMESTAMP, server_default=func.now() )
