// Simple frontend client: sends code to backend and renders response

async function analyzeCode() {
  const language = document.getElementById('language').value;
  const code = document.getElementById('code').value;
  const out = document.getElementById('output');
  out.textContent = 'Analyzing...';

  try {
    const resp = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ language, code }),
    });
    const data = await resp.json();
    out.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    out.textContent = 'Error: ' + err.message;
  }
}

function insertExample() {
  const example = `# Example: IndexError in Python\narr = [1,2,3]\nprint(arr[3])`;
  document.getElementById('code').value = example;
}
