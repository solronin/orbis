# Orbis MCP Server: DeFi Lending Pool Risk Analyzer

## Overview

Orbis is a Model Context Protocol (MCP) server designed to provide intelligent insights and analysis for navigating the risks associated with DeFi lending pools.  It's built to empower users and Language Model Models (LLMs) with the data-driven context needed for informed decisions regarding DeFi lending.

**Currently, Orbis is specifically focused on providing risk analysis for investing in different lending pools, particularly those on platforms like Kamino and Drift.**

Orbis does **not** execute trades or manage funds. It is purely an analytical tool, delivering insights to other systems or users.

## Functionality

Orbis MCP Server provides the following key functionalities:

*   **Lending Pool Risk Assessment:**  Analyzes various DeFi lending pools (currently focusing on Kamino and Drift, with potential for expansion).
    *   Calculates risk scores based on volatility, liquidity, and protocol-specific risks.
    *   Provides metrics and insights to understand the risk profile of each pool.
*   **Data-Driven Insights:** Employs an inference engine to process raw data and generate actionable intelligence.
    *   Offers insights into lending pool stability, utilization, and potential vulnerabilities.
    *   Helps users understand the risk-reward balance in different lending opportunities.
*   **MCP Tooling:**  Exposes tools accessible via the Model Context Protocol (MCP), allowing seamless integration with MCP-compatible clients and LLMs.
*   **Customizable Risk Profiles:**  Allows for configuration of risk parameters to align with individual user preferences and risk tolerance levels.

## Use Cases

Here are a few examples of how Orbis can be used:

*   **Informed DeFi Lending Decisions:** LLMs can use Orbis to provide users with contextual information and risk assessments before they invest in DeFi lending pools.
    *   Example Prompt to an LLM: "Using Orbis, analyze the risk of investing in the USDC lending pool on Kamino with a moderate risk tolerance."
*   **DeFi Portfolio Risk Management:**  Applications can integrate Orbis to continuously monitor the risk levels of a user's DeFi lending portfolio.
    *   Example Application Function:  Display a dashboard showing the Orbis-calculated risk scores for each lending position in a user's wallet.
*   **Algorithmic Trading Strategy Development (Analytical Input):**  Traders can use Orbis's risk assessments as a crucial input for developing more sophisticated algorithmic trading strategies that involve DeFi lending.
    *   Example Strategy Component:  An algorithm that automatically adjusts lending allocations based on Orbis's real-time risk scores.
*   **DeFi Research and Education:**  Researchers and educators can use Orbis to explore and understand the risk dynamics within DeFi lending markets.
    *   Example Educational Use:  Use Orbis output to illustrate the impact of utilization rate or volatility on the overall risk of a lending pool.

## Know-How / Getting Started (For Users of Orbis via MCP)

To use Orbis, you will need an MCP-compatible client (like Claude for Desktop or a custom-built application). Once you have a client set up:

1.  **Install and Run Orbis MCP Server:** Follow the installation instructions in the full documentation to set up and run the Orbis MCP server.
2.  **Configure your MCP Client:** Configure your MCP client to connect to the Orbis server (refer to your client's documentation for instructions on adding MCP servers).
3.  **Use MCP Tools via your Client:** Your MCP client should now recognize the Orbis MCP server and its available tools. You can then interact with Orbis through your client using natural language prompts or application interfaces.

**Example Interaction (via an MCP-compatible LLM Client):**

**User Prompt:** "Orbis, tell me about the risk of lending DAI on Drift."

**Expected LLM Response (Powered by Orbis):** "Based on Orbis's analysis, the Drift DAI lending pool currently has a moderate risk score. Key factors contributing to this score include [mention specific risk metrics from Orbis, e.g., utilization rate is at 85%, volatility is medium based on recent APY fluctuations, protocol audit score is high].  While the APY is currently [mention APY], potential risks to consider are [mention specific risks identified by Orbis, e.g., high utilization could lead to lower liquidity during peak demand]."

**For Developers:**

For detailed technical documentation, API references, and instructions on setting up and extending the Orbis MCP server, please refer to the [Full Orbis MCP Server Documentation](solronin.gitbook.io/orbis)

