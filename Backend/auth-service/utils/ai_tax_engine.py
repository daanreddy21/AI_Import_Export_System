import ollama
import json
import re
def get_ai_tax_rules(country, hsn_code, product, category):
    prompt = f"""
    Estimate realistic import tax rules
    for this shipment.
    Return ONLY valid JSON.
    Country: {country}
    HSN Code: {hsn_code}
    Product: {product}    
    Category: {category}
    Required JSON Format:
    {{
        "duty_percent": 0,
        "gst_percent": 0,
        "insurance_percent": 0,
        "shipping_cost": 0,
        "handling_fee": 0,
        "currency": ""
    }}
    Rules:
    - Return realistic values
    - Duty percent should match country
    - GST/VAT should match country
    - Shipping cost should be realistic
    - Return only JSON
    - Do not explain anything
    """
    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    ai_text = response[
        "message"
    ][
        "content"
    ]
    print(
        "\n========== AI TAX RESPONSE ==========\n"
    )
    print(ai_text)
    print(
        "\n=====================================\n"
    )
    try:
        json_match = re.search(
            r"\{[\s\S]*\}",
            ai_text
        )
        if not json_match:
            raise Exception(
                "No JSON Found"
            )
        json_text = json_match.group(0)
        data = json.loads(json_text)
        try:
            data["duty_percent"] = float(
                str(
                    data.get(
                        "duty_percent",
                        0
                    )
                ).replace("%", "").strip()
            )
        except:
            data["duty_percent"] = 0
        try:
            data["gst_percent"] = float(
                str(
                    data.get(
                        "gst_percent",
                        0
                    )
                ).replace("%", "").strip()
            )
        except:
            data["gst_percent"] = 0
        try:
            data["insurance_percent"] = float(
                str(
                    data.get(
                        "insurance_percent",
                        0
                    )
                ).replace("%", "").strip()
            )
        except:
            data["insurance_percent"] = 0
        try:
            data["shipping_cost"] = float(
                str(
                    data.get(
                        "shipping_cost",
                        0
                    )
                ).replace(",", "").replace("$", "").strip()
            )
        except:
            data["shipping_cost"] = 0
        try:
            data["handling_fee"] = float(
                str(
                    data.get(
                        "handling_fee",
                        0
                    )
                ).replace(",", "").replace("$", "").strip()
            )
        except:
            data["handling_fee"] = 0
        if not data.get("currency"):
            data["currency"] = "USD"
        return data
    except Exception as e:
        print( "\nAI TAX PARSE ERROR\n")
        print(e)
        return {
            "duty_percent": 10,
            "gst_percent": 18,
            "insurance_percent": 1,
            "shipping_cost": 1500,
            "handling_fee": 100,
            "currency": "USD"
        }