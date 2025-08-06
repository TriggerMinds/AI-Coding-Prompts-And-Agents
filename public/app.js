async function generateSEO() {
  const topic = document.getElementById('seo-topic').value;
  const res = await fetch('/api/generate-seo', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ topic })
  });
  const data = await res.json();
  document.getElementById('seo-result').textContent = data.content || data.error;
}

async function askQuestion() {
  const question = document.getElementById('question').value;
  const res = await fetch('/api/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question })
  });
  const data = await res.json();
  document.getElementById('qa-result').textContent = data.answer || data.error;
}

async function loadAffiliates() {
  const res = await fetch('/api/affiliate-links');
  const data = await res.json();
  const ul = document.getElementById('affiliate-links');
  data.forEach(link => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = link.url;
    a.textContent = link.name;
    a.target = '_blank';
    li.appendChild(a);
    ul.appendChild(li);
  });
}

document.getElementById('seo-btn').addEventListener('click', generateSEO);
document.getElementById('qa-btn').addEventListener('click', askQuestion);
loadAffiliates();
