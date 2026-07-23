const state = {
  config: null,
  repositories: [],
  activity: [],
};

const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => [...document.querySelectorAll(selector)];

function logActivity(message) {
  state.activity.unshift({ at: new Date(), message });
  state.activity = state.activity.slice(0, 30);
  renderActivity();
}

function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

async function loadConfig() {
  const response = await fetch('./portfolio.json', { cache: 'no-store' });
  if (!response.ok) throw new Error(`portfolio.json returned ${response.status}`);
  state.config = await response.json();
  state.repositories = state.config.repositories.map((repo) => ({ ...repo, metadata: null }));
}

async function fetchPublicMetadata() {
  const button = $('#refresh');
  const connection = $('#connection-state');
  button.disabled = true;
  connection.textContent = 'Refreshing';
  connection.className = 'status warn';
  logActivity('Started public GitHub metadata refresh.');

  const owner = state.config.owner;
  const results = await Promise.allSettled(
    state.repositories.map(async (repo) => {
      const response = await fetch(`https://api.github.com/repos/${owner}/${repo.name}`, {
        headers: { Accept: 'application/vnd.github+json' },
      });
      if (!response.ok) throw new Error(`${repo.name}: HTTP ${response.status}`);
      const data = await response.json();
      repo.metadata = {
        description: data.description,
        stars: data.stargazers_count,
        forks: data.forks_count,
        openIssues: data.open_issues_count,
        updatedAt: data.updated_at,
        language: data.language,
        visibility: data.visibility,
        archived: data.archived,
      };
      return repo.name;
    })
  );

  const successes = results.filter((result) => result.status === 'fulfilled').length;
  const failures = results.length - successes;
  connection.textContent = failures ? `${successes} refreshed, ${failures} unavailable` : `${successes} repositories refreshed`;
  connection.className = failures ? 'status warn' : 'status good';
  button.disabled = false;
  logActivity(`Metadata refresh completed: ${successes} succeeded and ${failures} failed.`);
  renderAll();
}

function renderMetrics() {
  const total = state.repositories.length;
  const featured = state.repositories.filter((repo) => repo.featured).length;
  const holds = state.repositories.filter((repo) => /hold|required|clarification/i.test(repo.status)).length;
  const refreshed = state.repositories.filter((repo) => repo.metadata).length;
  $('#metrics').innerHTML = [
    [total, 'Configured repositories'],
    [featured, 'Featured integrations'],
    [holds, 'Architectural decisions'],
    [refreshed, 'Live metadata records'],
  ].map(([value, label]) => `<div class="metric"><strong>${value}</strong><span>${label}</span></div>`).join('');
}

function repositoryUrl(name) {
  return `https://github.com/${encodeURIComponent(state.config.owner)}/${encodeURIComponent(name)}`;
}

function renderFeatured() {
  $('#featured-repositories').innerHTML = state.repositories
    .filter((repo) => repo.featured)
    .map((repo) => `
      <a class="repo-row" href="${repositoryUrl(repo.name)}">
        <div><strong>${escapeHtml(repo.name)}</strong><p>${escapeHtml(repo.role)}</p></div>
        <span class="badge">${escapeHtml(repo.status)}</span>
      </a>
    `).join('');
}

function renderRepositories() {
  const query = ($('#repo-filter')?.value || '').trim().toLowerCase();
  const filtered = state.repositories.filter((repo) =>
    [repo.name, repo.role, repo.status, repo.metadata?.description, repo.metadata?.language]
      .filter(Boolean)
      .some((value) => String(value).toLowerCase().includes(query))
  );
  $('#repo-count').textContent = `${filtered.length} of ${state.repositories.length}`;
  $('#repository-grid').innerHTML = filtered.map((repo) => {
    const metadata = repo.metadata;
    const details = metadata
      ? `${metadata.language || 'No primary language'} · ${metadata.stars} stars · ${metadata.openIssues} open items`
      : 'Static configuration · metadata not refreshed';
    return `
      <article class="panel repo-card">
        <header><h2>${escapeHtml(repo.name)}</h2><span class="badge">${escapeHtml(repo.status)}</span></header>
        <p>${escapeHtml(metadata?.description || repo.role)}</p>
        <p class="muted">${escapeHtml(details)}</p>
        <footer>
          <span class="muted">${metadata?.updatedAt ? `Updated ${new Date(metadata.updatedAt).toLocaleDateString()}` : 'Read-only'}</span>
          <a href="${repositoryUrl(repo.name)}">Open repository →</a>
        </footer>
      </article>
    `;
  }).join('');
}

function renderActivity() {
  const container = $('#activity-log');
  if (!container) return;
  container.innerHTML = state.activity.length
    ? state.activity.map((item) => `<div class="activity-item"><time>${item.at.toLocaleTimeString()}</time><span>${escapeHtml(item.message)}</span></div>`).join('')
    : '<p class="muted">No activity yet. This log exists only in memory for the current browser session.</p>';
}

function renderAll() {
  renderMetrics();
  renderFeatured();
  renderRepositories();
  renderActivity();
}

function selectView(viewName) {
  const titles = {
    overview: 'Portfolio overview',
    repositories: 'Repository directory',
    architecture: 'Integration architecture',
    activity: 'Session activity',
    settings: 'Connections',
  };
  $$('.view').forEach((view) => {
    const active = view.id === viewName;
    view.hidden = !active;
    view.classList.toggle('active-view', active);
  });
  $$('.nav-item').forEach((item) => item.classList.toggle('active', item.dataset.view === viewName));
  $('#view-title').textContent = titles[viewName] || 'AionUi Console';
  history.replaceState(null, '', `#${viewName}`);
  logActivity(`Opened ${titles[viewName] || viewName}.`);
}

async function init() {
  try {
    await loadConfig();
    renderAll();
    logActivity('Loaded static portfolio configuration.');
  } catch (error) {
    $('#connection-state').textContent = 'Configuration error';
    $('#connection-state').className = 'status warn';
    logActivity(`Failed to load configuration: ${error.message}`);
    return;
  }

  $$('.nav-item').forEach((item) => item.addEventListener('click', () => selectView(item.dataset.view)));
  $('#refresh').addEventListener('click', fetchPublicMetadata);
  $('#repo-filter').addEventListener('input', renderRepositories);

  const requested = location.hash.replace('#', '');
  if (requested && document.getElementById(requested)) selectView(requested);
}

init();
