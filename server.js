import express from 'express';
import dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';
import OpenAI from 'openai';

dotenv.config();

const app = express();
app.use(express.json());
app.use(express.static('public'));

const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);
const geminiModel = genAI.getGenerativeModel({ model: 'gemini-pro' });

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.post('/api/generate-seo', async (req, res) => {
  try {
    const { topic } = req.body;
    const result = await geminiModel.generateContent({
      contents: [{
        role: 'user',
        parts: [{ text: `Schrijf SEO-geoptimaliseerde content over ${topic} voor een crypto-tax-compliance website.` }]
      }]
    });
    res.json({ content: result.response.text() });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/ask', async (req, res) => {
  try {
    const { question } = req.body;
    const completion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: question }]
    });
    res.json({ answer: completion.choices[0].message.content });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/affiliate-links', (req, res) => {
  res.json([
    { name: 'Coinbase', url: 'https://www.coinbase.com/?affiliate=example' },
    { name: 'Ledger', url: 'https://shop.ledger.com/?r=example' }
  ]);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
