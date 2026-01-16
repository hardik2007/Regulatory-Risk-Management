import pandas as pd

risky_data = [
    {"Company": "Vodafone Idea",       "Ticker": "IDEA.NS",          "Sector": "Telecom",    "Risk_Label": 1},
    {"Company": "Yes Bank",            "Ticker": "YESBANK.NS",       "Sector": "Banking",    "Risk_Label": 1},
    {"Company": "Punjab National Bank","Ticker": "PNB.NS",           "Sector": "Banking",    "Risk_Label": 1},
    {"Company": "Indiabulls Housing",  "Ticker": "INDIABULLSHSG.NS", "Sector": "Finance",    "Risk_Label": 1},
    {"Company": "SpiceJet",            "Ticker": "SPICEJET.NS",      "Sector": "Aviation",   "Risk_Label": 1},
    {"Company": "PC Jeweller",         "Ticker": "PCJEWELLER.NS",    "Sector": "Consumer",   "Risk_Label": 1},
    {"Company": "Suzlon Energy",       "Ticker": "SUZLON.NS",        "Sector": "Energy",     "Risk_Label": 1},
    {"Company": "Vedanta",             "Ticker": "VEDL.NS",          "Sector": "Mining",     "Risk_Label": 1},
    {"Company": "Sun TV Network",      "Ticker": "SUNTV.NS",         "Sector": "Media",      "Risk_Label": 1},
    {"Company": "DLF",                 "Ticker": "DLF.NS",           "Sector": "Realty",     "Risk_Label": 1}
]

safe_data = [
    {"Company": "TCS",                 "Ticker": "TCS.NS",           "Sector": "IT",         "Risk_Label": 0},
    {"Company": "Infosys",             "Ticker": "INFY.NS",          "Sector": "IT",         "Risk_Label": 0},
    {"Company": "HDFC Bank",           "Ticker": "HDFCBANK.NS",      "Sector": "Banking",    "Risk_Label": 0},
    {"Company": "ICICI Bank",          "Ticker": "ICICIBANK.NS",     "Sector": "Banking",    "Risk_Label": 0},
    {"Company": "Hindustan Unilever",  "Ticker": "HINDUNILVR.NS",    "Sector": "FMCG",       "Risk_Label": 0},
    {"Company": "ITC",                 "Ticker": "ITC.NS",           "Sector": "FMCG",       "Risk_Label": 0},
    {"Company": "Reliance Industries", "Ticker": "RELIANCE.NS",      "Sector": "Energy",     "Risk_Label": 0},
    {"Company": "NTPC",                "Ticker": "NTPC.NS",          "Sector": "Energy",     "Risk_Label": 0},
    {"Company": "Larsen & Toubro",     "Ticker": "LT.NS",            "Sector": "Infra",      "Risk_Label": 0},
    {"Company": "Sun Pharma",          "Ticker": "SUNPHARMA.NS",     "Sector": "Pharma",     "Risk_Label": 0},
    {"Company": "Maruti Suzuki",       "Ticker": "MARUTI.NS",        "Sector": "Auto",       "Risk_Label": 0},
    {"Company": "Titan",               "Ticker": "TITAN.NS",         "Sector": "Consumer",   "Risk_Label": 0},
    {"Company": "Bharti Airtel",       "Ticker": "BHARTIARTL.NS",    "Sector": "Telecom",    "Risk_Label": 0},
    {"Company": "Asian Paints",        "Ticker": "ASIANPAINT.NS",    "Sector": "Consumer",   "Risk_Label": 0},
    {"Company": "Bajaj Finance",       "Ticker": "BAJFINANCE.NS",    "Sector": "Finance",    "Risk_Label": 0},
    {"Company": "UltraTech Cement",    "Ticker": "ULTRACEMCO.NS",    "Sector": "Infra",      "Risk_Label": 0},
    {"Company": "Nestle India",        "Ticker": "NESTLEIND.NS",     "Sector": "FMCG",       "Risk_Label": 0},
    {"Company": "HCL Tech",            "Ticker": "HCLTECH.NS",       "Sector": "IT",         "Risk_Label": 0},
    {"Company": "Cipla",               "Ticker": "CIPLA.NS",         "Sector": "Pharma",     "Risk_Label": 0},
    {"Company": "Kotak Mahindra",      "Ticker": "KOTAKBANK.NS",     "Sector": "Banking",    "Risk_Label": 0}
]

neutral_data = [
    {"Company": "Ashok Leyland",       "Ticker": "ASHOKLEY.NS",      "Sector": "Auto",       "Risk_Label": 0},
    {"Company": "TVS Motor",           "Ticker": "TVSMOTOR.NS",      "Sector": "Auto",       "Risk_Label": 0},
    {"Company": "Voltas",              "Ticker": "VOLTAS.NS",        "Sector": "Durables",   "Risk_Label": 0},
    {"Company": "Marico",              "Ticker": "MARICO.NS",        "Sector": "FMCG",       "Risk_Label": 0},
    {"Company": "SRF",                 "Ticker": "SRF.NS",           "Sector": "Chemicals",  "Risk_Label": 0},
    {"Company": "Apollo Tyres",        "Ticker": "APOLLOTYRE.NS",    "Sector": "Auto Anc",   "Risk_Label": 0},
    {"Company": "IRB Infra",           "Ticker": "IRB.NS",           "Sector": "Infra",      "Risk_Label": 0},
    {"Company": "IDFC First Bank",     "Ticker": "IDFCFIRSTB.NS",    "Sector": "Banking",    "Risk_Label": 0},
    {"Company": "L&T Finance",         "Ticker": "L&TFH.NS",         "Sector": "Finance",    "Risk_Label": 0},
    {"Company": "Persistent Systems",  "Ticker": "PERSISTENT.NS",    "Sector": "IT",         "Risk_Label": 0}
]

fullData = risky_data + safe_data + neutral_data
df = pd.DataFrame(fullData)

fileName = "Project_scope_final.xlsx"
df.to_excel(fileName, index = False)

print(f"Total Companies: {len(df)}")
print(f"Risky: {len(df[df['Risk_Label']==1])}")
print(f"Safe/Neutral: {len(df[df['Risk_Label']==0])}")