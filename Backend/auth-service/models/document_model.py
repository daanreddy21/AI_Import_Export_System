from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from database.db import Base
class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255))
    file_path = Column(Text)
    upload_date = Column(
        TIMESTAMP,
        server_default=func.now()
    )
    ocr_status = Column(String(50))
    validation_status = Column(String(50))
    raw_text = Column(Text)
    invoice_number = Column(String(100))
    buyer_name = Column(String(255))
    seller_name = Column(String(255))
    country = Column(String(100))
    product = Column(String(255))
    quantity = Column(Integer)
    currency = Column(String(20))
    unit_price = Column(Numeric(12,2))
    total_amount = Column(Numeric(12,2))
    category = Column(String)
    hsn_code = Column(String)
    product_code = Column(String)