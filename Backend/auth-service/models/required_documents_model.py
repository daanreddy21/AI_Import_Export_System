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


class RequiredDocument(Base):

    __tablename__ = "required_documents"

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

    product_category = Column(
        String(255)
    )

    required_document = Column(
        String(255)
    )

    document_type = Column(
        String(100)
    )

    issuing_authority = Column(
        String(255)
    )

    mandatory_status = Column(
        String(50)
    )

    customs_hold_if_missing = Column(
        Boolean
    )

    compliance_level = Column(
        String(50)
    )

    notes = Column(
        Text
    )

    effective_date = Column(
        Date
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )
