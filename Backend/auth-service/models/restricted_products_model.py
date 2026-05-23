from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    TIMESTAMP,
    Text
)

from sqlalchemy.sql import func

from database.db import Base


class RestrictedProduct(Base):

    __tablename__ = "restricted_products"

    id = Column(
        Integer,
        primary_key=True
    )

    destination_country = Column(
        String(100)
    )

    hsn_code = Column(
        String(20)
    )

    product_name = Column(
        String(255)
    )

    restriction_type = Column(
        String(100)
    )

    restriction_level = Column(
        String(50)
    )

    restriction_reason = Column(
        Text
    )

    special_license_required = Column(
        Boolean
    )

    restricted_authority = Column(
        String(255)
    )

    penalty_notes = Column(
        Text
    )

    compliance_action = Column(
        Text
    )

    effective_date = Column(
        Date
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )
