document.getElementById("scrapeForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("result").innerHTML = "";

  const response = await fetch("/scrape", { method: "POST", body: formData });
  const data = await response.json();

  document.getElementById("loading").classList.add("hidden");

  if (data.count === 0) {
    document.getElementById("result").innerHTML = "<p>No matches found.</p>";
  } else {
    document.getElementById("result").innerHTML = `
      <h3>Found ${data.count} results:</h3>
      <ul>${data.results.map(r => `<li>${r}</li>`).join('')}</ul>
    `;
  }
});

// Dark/Light mode toggle
const toggleBtn = document.getElementById("modeToggle");
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  const isDark = document.body.classList.contains("dark-mode");
  toggleBtn.textContent = isDark ? "Light Mode" : "Dark Mode";
});
