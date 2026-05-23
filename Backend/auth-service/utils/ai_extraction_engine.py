from groq import Groq
from dotenv import load_dotenv
import os
import json
import re
load_dotenv()
client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)
def extract_invoice_ai(text):

    text = text.replace(
        "\n",
        " "
    )

    prompt = f"""

    Extract invoice data from this document.

    Return ONLY STRICT VALID JSON.

    DO NOT:
    - explain
    - add comments
    - add notes
    - add markdown
    - add assumptions

    Never leave fields empty.

    If value missing:
    intelligently predict probable value.

    ONLY return pure JSON.

    Required JSON format:

    {{
        "invoice_number": "",
        "buyer_name": "",
        "seller_name": "",
        "country": "",
        "currency": "",
        "product": "",
        "category": "",
        "hsn_code": "",
        "quantity": 0,
        "unit_price": 0,
        "total_amount": 0
    }}

    Rules:

    - Predict suitable product category
    - Predict appropriate HSN code
    - HSN should match product category
    - Quantity must be integer
    - Unit price must be number only
    - Total amount must be number only
    - Country should represent importing country
    - Extract invoice currency
    - Return ONLY JSON

    Invoice Text:

    {text}

    """

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[

            {

                "role": "system",

                "content":
                """
                You are an enterprise invoice extraction AI.

                Return ONLY valid JSON.

                Never explain anything.
                """
            },

            {

                "role": "user",

                "content": prompt

            }

        ],

        temperature=0.1,

        max_tokens=400

    )

    ai_text = response.choices[0].message.content

    print("\n========== AI RESPONSE ==========\n")

    print(ai_text)

    print("\n=================================\n")

    try:

        json_match = re.search(

            r"\{.*\}",

            ai_text,

            re.DOTALL

        )

        if not json_match:

            raise Exception(
                "No JSON Found"
            )

        json_text = json_match.group(0)

        # Remove trailing commas

        json_text = re.sub(

            r",\s*}",

            "}",

            json_text

        )

        data = json.loads(json_text)

        # Clean Quantity

        try:

            data["quantity"] = int(

                str(
                    data.get(
                        "quantity",
                        0
                    )
                )

                .replace(",", "")

                .strip()

            )

        except:

            data["quantity"] = 0

        # Clean Unit Price

        try:

            data["unit_price"] = float(

                str(
                    data.get(
                        "unit_price",
                        0
                    )
                )

                .replace("$", "")

                .replace(",", "")

                .replace("USD", "")

                .strip()

            )

        except:

            data["unit_price"] = 0

        # Clean Total Amount

        try:

            data["total_amount"] = float(

                str(
                    data.get(
                        "total_amount",
                        0
                    )
                )

                .replace("$", "")

                .replace(",", "")

                .replace("USD", "")

                .strip()

            )

        except:

            data["total_amount"] = 0

        return data

    except Exception as e:

        print("\nJSON PARSE ERROR:\n")

        print(e)

        return {

            "invoice_number": None,

            "buyer_name": None,

            "seller_name": None,

            "country": None,

            "currency": None,

            "product": None,

            "category": None,

            "hsn_code": None,

            "quantity": 0,

            "unit_price": 0,

            "total_amount": 0

        }