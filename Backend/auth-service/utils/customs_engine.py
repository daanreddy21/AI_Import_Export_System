def calculate_customs_duty(

    quantity,
    unit_price,
    rule

):

    quantity = float(quantity)

    if quantity <= 0:

        quantity = 1

    unit_price = float(unit_price)

    exchange_rates = {

        "India": {
            "currency": "INR",
            "rate": 83
        },

        "UAE": {
            "currency": "AED",
            "rate": 3.67
        },

        "Japan": {
            "currency": "JPY",
            "rate": 156
        },

        "Germany": {
            "currency": "EUR",
            "rate": 0.92
        },

        "UK": {
            "currency": "GBP",
            "rate": 0.78
        },

        "Singapore": {
            "currency": "SGD",
            "rate": 1.35
        },

        "Australia": {
            "currency": "AUD",
            "rate": 1.52
        },

        "Canada": {
            "currency": "CAD",
            "rate": 1.37
        }

    }

    destination_country = getattr(

        rule,
        "destination_country",
        "USA"

    )

    currency_data = exchange_rates.get(

        destination_country,

        {
            "currency": "USD",
            "rate": 1
        }

    )

    destination_currency = (
        currency_data["currency"]
    )

    exchange_rate = (
        currency_data["rate"]
    )

    base_total = (
        quantity * unit_price
    )

    shipping_cost = (
        base_total * 0.05
    )

    insurance_cost = (
        base_total * 0.02
    )

    handling_fee = float(
        rule.customs_handling_fee
    )

    subtotal_before_tax = (

        base_total
        + shipping_cost
        + insurance_cost
        + handling_fee

    )

    cif_value = (
        subtotal_before_tax
    )

    trade_agreement = (
        "No Agreement"
    )

    exemption_type = (
        "None"
    )

    reduced_duty_percent = float(
        rule.basic_custom_duty
    )

    if destination_country == "India":

        trade_agreement = (
            "ASEAN-India FTA"
        )

        exemption_type = (
            "Reduced Import Duty"
        )

    bcd_amount = (

        cif_value
        * reduced_duty_percent

    ) / 100

    sws_amount = (

        bcd_amount
        * float(
            rule.social_welfare_surcharge
        )

    ) / 100

    taxable_value = (

        cif_value
        + bcd_amount
        + sws_amount

    )

    igst_amount = (

        taxable_value
        * float(rule.igst)

    ) / 100

    vat_amount = (

        taxable_value
        * float(rule.vat)

    ) / 100

    anti_dumping_amount = (

        taxable_value
        * float(
            rule.anti_dumping_duty
        )

    ) / 100

    safeguard_amount = (

        taxable_value
        * float(
            rule.safeguard_duty
        )

    ) / 100

    total_tax = (

        bcd_amount
        + sws_amount
        + igst_amount
        + vat_amount
        + anti_dumping_amount
        + safeguard_amount

    )

    final_total = (

        cif_value
        + total_tax
        + float(rule.port_charge)
        + float(rule.customs_clearance_fee)

    )

    unit_price_local = (
        unit_price * exchange_rate
    )

    base_total_local = (
        base_total * exchange_rate
    )

    shipping_cost_local = (
        shipping_cost * exchange_rate
    )

    insurance_cost_local = (
        insurance_cost * exchange_rate
    )

    cif_value_local = (
        cif_value * exchange_rate
    )

    bcd_amount_local = (
        bcd_amount * exchange_rate
    )

    sws_amount_local = (
        sws_amount * exchange_rate
    )

    igst_amount_local = (
        igst_amount * exchange_rate
    )

    vat_amount_local = (
        vat_amount * exchange_rate
    )

    anti_dumping_amount_local = (
        anti_dumping_amount * exchange_rate
    )

    safeguard_amount_local = (
        safeguard_amount * exchange_rate
    )

    total_tax_local = (
        total_tax * exchange_rate
    )

    final_total_local = (
        final_total * exchange_rate
    )

    compliance_status = (
        "APPROVED"
    )

    compliance_score = 96

    customs_hold_status = (
        "CLEAR"
    )

    restricted_flag = (
        "NO"
    )

    prohibited_flag = (
        "NO"
    )

    missing_documents = []

    ai_recommendation = (

        "Shipment compliant "
        "for customs clearance."

    )

    if destination_country == "India":

        missing_documents = [
            "BIS Certificate"
        ]

        customs_hold_status = (
            "ON HOLD"
        )

        compliance_status = (
            "PENDING"
        )

        ai_recommendation = (

            "Upload BIS Certificate "
            "before customs filing."

        )

    return {

        "quantity":
            quantity,

        "base_currency":
            "USD",

        "destination_currency":
            destination_currency,

        "exchange_rate":
            exchange_rate,

        "unit_price_usd":
            round(unit_price, 2),

        "unit_price_local":
            round(unit_price_local, 2),

        "base_total_usd":
            round(base_total, 2),

        "base_total_local":
            round(base_total_local, 2),

        "shipping_cost_usd":
            round(shipping_cost, 2),

        "shipping_cost_local":
            round(shipping_cost_local, 2),

        "insurance_cost_usd":
            round(insurance_cost, 2),

        "insurance_cost_local":
            round(insurance_cost_local, 2),

        "cif_value_usd":
            round(cif_value, 2),

        "cif_value_local":
            round(cif_value_local, 2),

        "bcd_percent":
            reduced_duty_percent,

        "bcd_amount_usd":
            round(bcd_amount, 2),

        "bcd_amount_local":
            round(bcd_amount_local, 2),

        "sws_percent":
            float(
                rule.social_welfare_surcharge
            ),

        "sws_amount_usd":
            round(sws_amount, 2),

        "sws_amount_local":
            round(sws_amount_local, 2),

        "igst_percent":
            float(rule.igst),

        "igst_amount_usd":
            round(igst_amount, 2),

        "igst_amount_local":
            round(igst_amount_local, 2),

        "vat_percent":
            float(rule.vat),

        "vat_amount_usd":
            round(vat_amount, 2),

        "vat_amount_local":
            round(vat_amount_local, 2),

        "anti_dumping_percent":
            float(
                rule.anti_dumping_duty
            ),

        "anti_dumping_amount_usd":
            round(
                anti_dumping_amount,
                2
            ),

        "anti_dumping_amount_local":
            round(
                anti_dumping_amount_local,
                2
            ),

        "safeguard_percent":
            float(
                rule.safeguard_duty
            ),

        "safeguard_amount_usd":
            round(
                safeguard_amount,
                2
            ),

        "safeguard_amount_local":
            round(
                safeguard_amount_local,
                2
            ),

        "total_tax_usd":
            round(total_tax, 2),

        "total_tax_local":
            round(total_tax_local, 2),

        "final_total_usd":
            round(final_total, 2),

        "final_total_local":
            round(final_total_local, 2),

        "trade_agreement":
            trade_agreement,

        "exemption_type":
            exemption_type,

        "compliance_status":
            compliance_status,

        "compliance_score":
            compliance_score,

        "customs_hold_status":
            customs_hold_status,

        "restricted_flag":
            restricted_flag,

        "prohibited_flag":
            prohibited_flag,

        "missing_documents":
            missing_documents,

        "ai_recommendation":
            ai_recommendation
    }