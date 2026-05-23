import os
import ollama

from groq import Groq

from sqlalchemy.orm import Session

from models.payment_model import Payment
from models.duty_calculation_model import DutyCalculation


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_groq_insight(prompt):

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:

        print("GROQ ERROR:", e)

        return None

def generate_phi3_insight(prompt):

    try:

        response = ollama.chat(

            model="phi3",

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ]
        )

        return response["message"]["content"]

    except Exception as e:

        print("PHI3 ERROR:", e)

        return " Insight Generation Failed"

def generate_ai_insights(db: Session):

    insights = []
    pending_payments = db.query(
        Payment
    ).filter(
        Payment.payment_status == "Pending"
    ).all()

    if pending_payments:

        highest_pending = max(
            pending_payments,
            key=lambda x: float(x.final_total_usd)
        )

        prompt = f"""
        Generate SHORT professional dashboard insight.

        Maximum 8 lines only.
        Do not generate reports.
        Do not use bullet points.
        Keep response concise and executive-level.

        Format exactly like this:

        Client: ...
        Pending Amount: ...
        Delay Status: ...
        Destination Country: ...

        AI Insight:
        ...

        Recommendation:
        ...

        Payment Data:

        Client:
        {highest_pending.buyer_name}

        Pending Amount:
        {highest_pending.final_total_usd}

        Country:
        {highest_pending.destination_country}
        """

        result = generate_groq_insight(prompt)

        if not result:
            result = generate_phi3_insight(prompt)

        insights.append({

            "type": "payment",

            "title": "Payment Delay Alert",

            "content": result
        })

    payments = db.query(Payment).all()

    revenue_map = {}

    for payment in payments:

        country = payment.destination_country

        revenue_map[country] = (

            revenue_map.get(country, 0)

            + float(
                payment.final_total_usd
            )
        )

    if revenue_map:

        top_country = max(
            revenue_map,
            key=revenue_map.get
        )

        prompt = f"""
        Generate SHORT professional dashboard insight.

        Maximum 8 lines only.
        Do not generate reports.
        Keep response concise and executive-level.

        Format exactly like this:

        Country: ...
        Revenue Generated: ...
        Shipment Volume: ...
        Top Category: ...

        AI Insight:
        ...

        Recommendation:
        ...

        Revenue Data:

        Country:
        {top_country}

        Revenue:
        {revenue_map[top_country]}
        """

        result = generate_groq_insight(prompt)

        if not result:
            result = generate_phi3_insight(prompt)

        insights.append({

            "type": "revenue",

            "title": "Top Revenue Country",

            "content": result
        })

    duties = db.query(
        DutyCalculation
    ).all()

    tax_map = {}

    for duty in duties:

        country = duty.destination_country

        tax_map[country] = (

            tax_map.get(country, 0)

            + float(
                duty.total_tax_usd
            )
        )

    if tax_map:

        high_tax_country = max(
            tax_map,
            key=tax_map.get
        )

        prompt = f"""
        Generate SHORT professional dashboard insight.

        Maximum 8 lines only.
        Do not generate reports.
        Keep response concise and executive-level.

        Format exactly like this:

        Country: ...
        Total Tax: ...
        Customs Charges: ...
        Import Duty Trend: ...

        AI Insight:
        ...

        Recommendation:
        ...

        Tax Data:

        Country:
        {high_tax_country}

        Total Tax:
        {tax_map[high_tax_country]}
        """

        result = generate_groq_insight(prompt)

        if not result:
            result = generate_phi3_insight(prompt)

        insights.append({

            "type": "tax",

            "title": "High Tax Country",

            "content": result
        })

    category_map = {}

    for payment in payments:

        category = payment.category or "General"

        category_map[category] = (

            category_map.get(category, 0)

            + float(
                payment.final_total_usd
            )
        )

    if category_map:

        top_category = max(
            category_map,
            key=category_map.get
        )

        prompt = f"""
        Generate SHORT professional dashboard insight.

        Maximum 8 lines only.
        Do not generate reports.
        Keep response concise and executive-level.

        Format exactly like this:

        Category: ...
        Revenue Contribution: ...
        Demand Trend: ...
        Shipment Frequency: ...

        AI Insight:
        ...

        Recommendation:
        ...

        Business Data:

        Category:
        {top_category}

        Revenue:
        {category_map[top_category]}
        """

        result = generate_groq_insight(prompt)

        if not result:
            result = generate_phi3_insight(prompt)

        insights.append({

            "type": "business",

            "title": "Business Optimization",

            "content": result
        })

    return insights