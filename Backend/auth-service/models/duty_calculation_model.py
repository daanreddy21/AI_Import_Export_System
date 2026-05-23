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


class DutyCalculation(Base):

    __tablename__ = "duty_calculations"

    id = Column(
        Integer,
        primary_key=True
    )

    origin_country = Column(
        String
    )

    destination_country = Column(
        String
    )

    hsn_code = Column(
        String
    )

    product = Column(
        String
    )

    category = Column(
        String
    )

    quantity = Column(
        Integer
    )

    shipment_mode = Column(
        String
    )

    incoterm = Column(
        String
    )

    base_currency = Column(
        String
    )

    destination_currency = Column(
        String
    )

    exchange_rate = Column(
        Numeric(12,4)
    )

    unit_price_usd = Column(
        Numeric(12,2)
    )

    unit_price_local = Column(
        Numeric(12,2)
    )

    base_total_usd = Column(
        Numeric(12,2)
    )

    base_total_local = Column(
        Numeric(12,2)
    )

    shipping_cost_usd = Column(
        Numeric(12,2)
    )

    shipping_cost_local = Column(
        Numeric(12,2)
    )

    insurance_cost_usd = Column(
        Numeric(12,2)
    )

    insurance_cost_local = Column(
        Numeric(12,2)
    )

    cif_value_usd = Column(
        Numeric(12,2)
    )

    cif_value_local = Column(
        Numeric(12,2)
    )

    bcd_percent = Column(
        Numeric(5,2)
    )

    bcd_amount_usd = Column(
        Numeric(12,2)
    )

    bcd_amount_local = Column(
        Numeric(12,2)
    )

    igst_percent = Column(
        Numeric(5,2)
    )

    igst_amount_usd = Column(
        Numeric(12,2)
    )

    igst_amount_local = Column(
        Numeric(12,2)
    )

    vat_percent = Column(
        Numeric(5,2)
    )

    vat_amount_usd = Column(
        Numeric(12,2)
    )

    vat_amount_local = Column(
        Numeric(12,2)
    )

    sws_percent = Column(
        Numeric(5,2)
    )

    sws_amount_usd = Column(
        Numeric(12,2)
    )

    sws_amount_local = Column(
        Numeric(12,2)
    )

    anti_dumping_percent = Column(
        Numeric(5,2)
    )

    anti_dumping_amount_usd = Column(
        Numeric(12,2)
    )

    anti_dumping_amount_local = Column(
        Numeric(12,2)
    )

    safeguard_percent = Column(
        Numeric(5,2)
    )

    safeguard_amount_usd = Column(
        Numeric(12,2)
    )

    safeguard_amount_local = Column(
        Numeric(12,2)
    )

    total_tax_usd = Column(
        Numeric(12,2)
    )

    total_tax_local = Column(
        Numeric(12,2)
    )

    final_total_usd = Column(
        Numeric(12,2)
    )

    final_total_local = Column(
        Numeric(12,2)
    )

    trade_agreement = Column(
        String
    )

    exemption_type = Column(
        String
    )

    compliance_status = Column(
        String
    )

    compliance_score = Column(
        Numeric(5,2)
    )

    restricted_flag = Column(
        String
    )

    prohibited_flag = Column(
        String
    )

    missing_documents = Column(
        Text
    )

    customs_hold_status = Column(
        String
    )

    hold_reason = Column(
        Text
    )

    ai_recommendation = Column(
        Text
    )
    uploaded_document = Column(Text)

    document_uploaded = Column(String)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )