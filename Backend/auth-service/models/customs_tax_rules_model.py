from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Date
)

from database.db import Base


class CustomsTaxRule(Base):

    __tablename__ = "customs_tax_rules"

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

    hsn_code = Column(
        String(50)
    )

    product_category = Column(
        String(100)
    )

    basic_custom_duty = Column(
        Numeric(5,2)
    )

    igst = Column(
        Numeric(5,2)
    )

    vat = Column(
        Numeric(5,2)
    )

    social_welfare_surcharge = Column(
        Numeric(5,2)
    )

    anti_dumping_duty = Column(
        Numeric(5,2)
    )

    safeguard_duty = Column(
        Numeric(5,2)
    )

    port_charge = Column(
        Numeric(12,2)
    )

    customs_handling_fee = Column(
        Numeric(12,2)
    )

    customs_clearance_fee = Column(
        Numeric(12,2)
    )

    effective_date = Column(
        Date
    )

    status = Column(
        String(50)
    )