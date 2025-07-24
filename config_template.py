# Configuration template for PFF data query
# Copy this file to config.py and fill in your actual values

SUMMARY_URL = "https://premium.pff.com/api/v1/facet/offense/summary"

# Replace these with your actual PFF authentication cookies
COOKIES = {
    "_premium_key": "YOUR_PREMIUM_KEY_HERE",
    "c_groot_access_token": "YOUR_ACCESS_TOKEN_HERE",
    "c_groot_access_ts": "YOUR_ACCESS_TS_HERE",
    "c_groot_refresh_token": "YOUR_REFRESH_TOKEN_HERE"
}

# Alternative: Use environment variables for sensitive data
# Uncomment the lines below and set environment variables instead
# import os
#
# SUMMARY_URL = "https://premium.pff.com/api/v1/facet/offense/summary"
# COOKIES = {
#     "_premium_key": os.getenv("PFF_PREMIUM_KEY"),
#     "c_groot_access_token": os.getenv("PFF_ACCESS_TOKEN"),
#     "c_groot_access_ts": os.getenv("PFF_ACCESS_TS"),
#     "c_groot_refresh_token": os.getenv("PFF_REFRESH_TOKEN")
# }
