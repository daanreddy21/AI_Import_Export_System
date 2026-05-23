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
def generate_risk_analysis(
    buyer_name,
    pending_payments,
    overdue_payments,
    risk_score,
    total_pending_amount
):
    prompt = f"""
    You are an AI Import Export Risk Analyst.
    Analyze the client payment behavior and generate realistic business risk analysis.
    Return ONLY valid JSON.
    Buyer Name: {buyer_name}
    Pending Payments: {pending_payments}
    Overdue Payments: {overdue_payments}
    Current Calculated Risk Score: {risk_score}
    Total Pending Amount: {total_pending_amount}
    Required JSON Format:
    {{
        "risk_score": 0,
        "risk_level": "",
        "risk_reasons": "",
        "recommendation": ""
    }}
Rules:
- Use the given risk score
- Risk score should be between 0 to 100
- HIGH if many overdue payments
- MEDIUM if some pending payments
- LOW if payment history is good
- Recommendation should be professional
- Return ONLY valid JSON
- Do not use markdown
- Do not use nested JSON objects
- recommendation must be plain text string
- risk_reasons must be plain text string
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    ai_text = (
        response
        .choices[0]
        .message
        .content
    )
    print(
        "\n========== AI RISK RESPONSE ==========\n"
    )
    print(ai_text)
    print(
        "\n======================================\n"
    )
    try:
        json_match = re.search(
            r"\{[\s\S]*\}",
            ai_text
        )
        if json_match:
            json_text = json_match.group(0)
            data = json.loads(json_text)
            return {
                "risk_score": data.get("risk_score", risk_score),
                "risk_level": data.get("risk_level", "MEDIUM"),
                "risk_reasons":
                    data.get(
                        "risk_reasons",
                        "Unable to analyze properly"
                    ),
                "recommendation":
                    data.get(
                        "recommendation",
                        "Manual review recommended"
                    )
            }
        else:
            raise Exception(
                "No JSON Found"
            )
    except Exception as e:
        print( "\nAI RISK PARSE ERROR\n")
        print(e)
        return {
            "risk_score": risk_score,
            "risk_level": "MEDIUM",
            "risk_reasons": "Unable to analyze risk properly",
            "recommendation": "Manual review recommended"
        }