def validate_invoice_data(data):

    errors = []

    # Invoice Number

    if (

        not data.get("invoice_number")

        or

        len(
            str(
                data.get(
                    "invoice_number"
                )
            ).strip()
        ) < 3

    ):

        errors.append(
            "Invoice Number Missing"
        )

    # Buyer Name

    if (

        not data.get("buyer_name")

        or

        str(
            data.get(
                "buyer_name"
            )
        ).strip() == ""

    ):

        errors.append(
            "Buyer Name Missing"
        )

    # Seller Name

    if (

        not data.get("seller_name")

        or

        str(
            data.get(
                "seller_name"
            )
        ).strip() == ""

    ):

        errors.append(
            "Seller Name Missing"
        )

    # Country

    if (

        not data.get("country")

        or

        str(
            data.get(
                "country"
            )
        ).strip() == ""

    ):

        errors.append(
            "Country Missing"
        )

    # Currency

    if (

        not data.get("currency")

        or

        str(
            data.get(
                "currency"
            )
        ).strip() == ""

    ):

        errors.append(
            "Currency Missing"
        )

    # Product

    if (

        not data.get("product")

        or

        str(
            data.get(
                "product"
            )
        ).strip() == ""

    ):

        errors.append(
            "Product Missing"
        )

    # Quantity

    try:

        quantity = int(
            data.get(
                "quantity",
                0
            )
        )

        if quantity <= 0:

            errors.append(
                "Invalid Quantity"
            )

    except:

        errors.append(
            "Invalid Quantity"
        )

    # Unit Price

    try:

        unit_price = float(
            data.get(
                "unit_price",
                0
            )
        )

        if unit_price <= 0:

            errors.append(
                "Invalid Unit Price"
            )

    except:

        errors.append(
            "Invalid Unit Price"
        )

    # Total Amount

    try:

        total_amount = float(
            data.get(
                "total_amount",
                0
            )
        )

        if total_amount <= 0:

            errors.append(
                "Invalid Total Amount"
            )

    except:

        errors.append(
            "Invalid Total Amount"
        )

    # HSN Code

    if (

        not data.get("hsn_code")

        or

        len(
            str(
                data.get(
                    "hsn_code"
                )
            ).strip()
        ) < 4

    ):

        errors.append(
            "Invalid HSN Code"
        )

    # Final Result

    if len(errors) == 0:

        return {

            "status": "Passed",

            "errors": []

        }

    else:

        return {

            "status": "Failed",

            "errors": errors

        }