from groq import Groq
from dotenv import load_dotenv
from datetime import (
    datetime,
    timedelta
)
import os
import json
import re
load_dotenv()
client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)
def analyze_shipment_ai(data):
    product = data.get( "product", "")
    destination_country = data.get( "destination_country", "")
    destination_port = data.get( "destination_port", "")
    origin_port = data.get( "origin_port", "")
    transport_mode = data.get( "transport_mode", "")
    shipment_value = data.get( "shipment_value", "")
    today = datetime.now()
    estimated_days = 5
    if transport_mode.lower() == "sea":
        estimated_days += 8
    elif transport_mode.lower() == "air":
        estimated_days += 3
    elif transport_mode.lower() == "road":
        estimated_days += 6
    if destination_country.lower() == "iran":
        estimated_days += 6
    elif destination_country.lower() == "uae":
        estimated_days += 2
    elif destination_country.lower() == "usa":
        estimated_days += 5
    elif destination_country.lower() == "china":
        estimated_days += 4
    if "electronic" in product.lower():
        estimated_days += 2
    if "battery" in product.lower():
        estimated_days += 4
    if "food" in product.lower():
        estimated_days += 3
    predicted_delivery = (
        today +
        timedelta(days=estimated_days)
    ).strftime("%Y-%m-%d")
    gst_level = "Moderate"
    duty_level = "Moderate"
    if destination_country.lower() == "india":
        gst_level = "High"
        duty_level = "Moderate"
    elif destination_country.lower() == "uae":
        gst_level = "Low"
        duty_level = "Low"
    elif destination_country.lower() == "iran":
        gst_level = "High"
        duty_level = "High"
    elif destination_country.lower() == "usa":
        gst_level = "Low"
        duty_level = "Moderate"
    elif destination_country.lower() == "china":
        gst_level = "Moderate"
        duty_level = "Moderate"
    port_status = "Operational"
    if "bandar" in destination_port.lower():
        port_status = (
            "Moderate congestion and regional route monitoring detected"
        )
    elif "dubai" in destination_port.lower():
        port_status = (
            "Heavy cargo traffic but stable operations"
        )
    elif "los angeles" in destination_port.lower():
        port_status = (
            "High port traffic and customs congestion possible"
        )
    prompt = f"""
    You are a real-time enterprise shipment
    intelligence AI system.
    Analyze this shipment like a real
    logistics officer.
    Shipment Details:
    Product:{product}
    Destination Country:{destination_country}
    Destination Port:{destination_port}
    Origin Port:{origin_port}
    Transport Mode:{transport_mode}
    Shipment Value:{shipment_value}
    Predicted Delivery:{predicted_delivery}
    GST Level:{gst_level}
    Duty Level:{duty_level}
    Port Status: {port_status}
    Instructions:
    - Keep response short
    - Keep response realistic
    - Use operational logistics language
    - Mention customs conditions
    - Mention route conditions
    - Mention delivery impact
    - Mention GST and duty conditions
    - Mention port condition realistically
    - Electronics may require customs verification
    - Iran shipments may face geopolitical delays
    - Sea cargo may face congestion delays
    Return ONLY valid JSON.
    Required JSON format:
    {{
        "shipment_advisory": "",
        "customs_observation": "",
        "delivery_expectation": "",
        "tax_observation": "",
        "port_analysis": "",
        "recommendation": "",
        "possible_issues": []
    }}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content":
                """
                You are an AI shipment
                intelligence engine.
                Return ONLY valid JSON.
                """
            },
            {
                "role": "user",
               "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=700
    )
    ai_text = (
        response
        .choices[0]
        .message
        .content
    )
    print("\n========== SHIPMENT AI RESPONSE ==========\n")
    print(ai_text)
    print("\n==========================================\n")
    try:
        json_match = re.search(r"\{.*\}",ai_text,re.DOTALL)
        if not json_match:
            raise Exception("No JSON Found")                               
        json_text = json_match.group(0)
        json_text = re.sub(
            r",\s*}",
            "}",
            json_text
        )
        data = json.loads(json_text)
        if not isinstance(
            data.get("possible_issues"),
            list
        ):
            data["possible_issues"] = []
        return data
    except Exception as e:
        print( "\nSHIPMENT AI PARSE ERROR\n")   
        print(e)
        return {
            "shipment_advisory":
            "Shipment may experience operational delays during transit.",
            "customs_observation":
            "Additional customs verification may be required.",
            "delivery_expectation":
            f"Expected delivery within {estimated_days} business days.",
            "tax_observation":
            f"GST level is {gst_level} and import duty is {duty_level}.",
            "port_analysis": port_status,
            "recommendation":
            "Monitor shipment movement and customs clearance closely.",
            "possible_issues": [
                "Customs verification",
                "Port congestion",
                "Transit delay"
            ]
        }