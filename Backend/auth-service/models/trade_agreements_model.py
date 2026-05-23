from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Date
)

from database.db import Base


class TradeAgreement(Base):

    __tablename__ = "trade_agreements"

    id = Column(
        Integer,
        primary_key=True
    )

    origin_country = Column(
        String(100)
    )

    destination_country = Column(
        String(100)
    )

    agreement_name = Column(
        String(100)
    )

    hsn_code = Column(
        String(50)
    )

    reduced_duty = Column(
        Numeric(5,2)
    )

    exemption_type = Column(
        String(50)
    )

    valid_from = Column(
        Date
    )

    valid_to = Column(
        Date
    )