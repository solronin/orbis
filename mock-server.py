from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("orbis")

USER_AGENT = "orbis-app/1.0"

@mcp.tool()  
async def calculate_risk(query: str):
    """
    Calculate the risk level for a given query.

    Args:
      query: The query to search for (e.g. "SOL risk")

    Returns:
      Risk Level from model
    """

    risk_level = 5  # Default risk level
    confidence = 0.8  # Default confidence
    
    if "SOL" in query.upper():
        risk_level = 8
        confidence = 0.9
        arb_opportunity = "likely"
        details = "Recent whale movements and increased DEX volume suggest potential market volatility. Layer-1 metrics showing unusual patterns."
    elif "USDT" in query.upper():
        risk_level = 3
        confidence = 0.85
        arb_opportunity = "unlikely"
        details = "Stablecoin liquidity pools showing normal depth. On-chain metrics indicate steady institutional flows."
    elif "POPCAT" in query.upper():
        risk_level = 9
        confidence = 0.95
        arb_opportunity = "highly likely"
        details = "Significant smart contract interactions detected. Multiple MEV bot activities observed with unusual gas patterns."
    else:
        arb_opportunity = "moderate"
        details = "Market sentiment neutral with balanced order books. Standard deviation within historical ranges."

    return f"""
    {{ 
      "risk_level": {risk_level},
      "confidence": {confidence},
      "arbitrage_opportunity": "{arb_opportunity}",
      "details": "{details}"
    }}
"""

if __name__ == "__main__":
    mcp.run(transport="stdio")
