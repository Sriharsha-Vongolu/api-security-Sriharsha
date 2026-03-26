# api-security-Sriharsha

## Files
- weather.py
- .env.example
- .gitignore
- README.md

## Setup
1. Create a virtual environment
2. Install dependencies:
   pip install requests python-dotenv
3. Create a `.env` file:
   OPENWEATHER_API_KEY=your_real_api_key
4. Run:
   python weather.py

## What are the real-world consequences of exposing an API key on GitHub?
If an API key is exposed publicly, attackers can steal it, abuse the service, exhaust rate limits, and generate unexpected billing charges. It can also cause service disruption for legitimate users and may require emergency key rotation. In production, exposed secrets can lead to security incidents and reputational damage.

## Why does your company's privacy policy prohibit logging city names?
City names are location data and may qualify as personal data when linked to a user or patient context. Logging them unnecessarily increases privacy risk and can conflict with data minimisation principles under GDPR/UK GDPR. The safest approach is to avoid storing or printing location data unless it is strictly required.
