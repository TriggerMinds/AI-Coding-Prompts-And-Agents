# Crypto Tax Compliance POC

Deze proof-of-concept website toont een micro-niche toepassing voor crypto-belastingcompliance. De site integreert:

- **Gemini Pro** via `@google/generative-ai` voor het genereren van SEO-geoptimaliseerde content.
- **ChatGPT** via de `openai` SDK voor het beantwoorden van vragen.
- Eenvoudige affiliate-links naar crypto-gerelateerde partners.

## Installatie

1. Installeer de afhankelijkheden:
   ```bash
   npm install
   ```
2. Kopieer `.env.example` naar `.env` en vul je API-sleutels in:
   ```bash
   cp .env.example .env
   ```
3. Start de server:
   ```bash
   npm start
   ```
4. Bezoek `http://localhost:3000` in je browser.

## Tests

Draai de eenvoudige testscript:
```bash
npm test
```
