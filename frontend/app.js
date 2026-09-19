const API_URL = "https://career-connect-ai-1.onrender.com";

const queryInput = document.getElementById("careerQuery");
const analyzeBtn = document.getElementById("analyzeBtn");
const results = document.getElementById("results");
const loading = document.getElementById("loading");
const errorBox = document.getElementById("error");

function fillList(id, items) {
  document.getElementById(id).innerHTML = (items || [])
    .map(item => `<li>${escapeHtml(item)}</li>`)
    .join("");
}

function escapeHtml(value) {
  const div = document.createElement("div");
  div.textContent = value ?? "";
  return div.innerHTML;
}

function renderResults(data) {
  const target = data.target || {};
  const recommendation = data.career_recommendation || {};

  document.getElementById("targetTitle").textContent =
    [target.company, target.role].filter(Boolean).join(" · ") || "Career Guidance";
  document.getElementById("targetIntent").textContent =
    `Analyzed query: "${data.query}"`;

  fillList("skillsList", recommendation.skills_to_learn);
  fillList("projectsList", recommendation.suggested_projects);
  fillList("interviewList", recommendation.interview_topics);
  fillList("roadmapList", recommendation.roadmap);

  const matches = data.matches || [];
  document.getElementById("matchesList").innerHTML = matches.length
    ? matches.map(person => `
      <article class="person">
        <div class="avatar">${escapeHtml((person.name || "?").charAt(0).toUpperCase())}</div>
        <h3>${escapeHtml(person.name)}</h3>
        <p class="muted">${escapeHtml(person.role)} · ${escapeHtml(person.company)}</p>
        <p class="muted">${escapeHtml(person.university || "University not specified")}</p>
        <span class="score">Relevance: ${person.match_score ?? 0}</span>
      </article>`).join("")
    : "<p>No matching employees found.</p>";

  const messages = data.networking_messages || [];
  document.getElementById("messagesList").innerHTML = messages.length
    ? messages.map(item => `
      <article class="message">
        <strong>Message for ${escapeHtml(item.employee_name)}</strong>
        <span>${escapeHtml(item.message)}</span>
      </article>`).join("")
    : "<p>No networking messages generated.</p>";

  results.classList.remove("hidden");
  results.scrollIntoView({ behavior: "smooth", block: "start" });
}

async function analyzeCareer() {
  const query = queryInput.value.trim();
  if (query.length < 3) {
    showError("Please enter a career question.");
    return;
  }

  errorBox.classList.add("hidden");
  results.classList.add("hidden");
  loading.classList.remove("hidden");
  analyzeBtn.disabled = true;
  analyzeBtn.textContent = "Analyzing...";

  try {
    const response = await fetch(`${API_URL}/api/career/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    if (!response.ok) throw new Error(`API returned ${response.status}`);
    renderResults(await response.json());
  } catch (error) {
    showError("Could not connect to the backend. Start the FastAPI server on port 8000 and try again.");
  } finally {
    loading.classList.add("hidden");
    analyzeBtn.disabled = false;
    analyzeBtn.innerHTML = 'Analyze <span>→</span>';
  }
}

function showError(message) {
  errorBox.textContent = message;
  errorBox.classList.remove("hidden");
}

analyzeBtn.addEventListener("click", analyzeCareer);
queryInput.addEventListener("keydown", event => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    analyzeCareer();
  }
});

document.querySelectorAll(".examples button").forEach(button => {
  button.addEventListener("click", () => {
    queryInput.value = button.dataset.query;
    queryInput.focus();
  });
});
