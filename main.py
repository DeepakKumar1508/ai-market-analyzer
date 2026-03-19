from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Market Analyzer API Running"}

@app.get("/analyze/{sector}")
def analyze_sector(sector: str):
    analysis = f"""
    📊 Market Analysis Report: {sector.upper()} Sector

    🔹 Overview:
    The {sector} sector is growing rapidly with strong demand.

    📈 Growth Drivers:
    - Digital transformation
    - Investments
    - Innovation

    ⚠️ Challenges:
    - Competition
    - Regulations

    🚀 Opportunities:
    - Global expansion
    - AI adoption

    💡 Conclusion:
    The {sector} sector has strong future potential.
    """
    return {"sector": sector, "analysis": analysis.strip()}