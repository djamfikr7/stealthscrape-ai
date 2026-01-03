/**
 * StealthScrape AI - Frontend Application
 * Modern web scraping dashboard with real-time updates
 */

// API Configuration
const API_BASE_URL = 'http://localhost:8000';

// Application State
const appState = {
  currentPage: 'dashboard',
  theme: 'dark',
  notifications: 3,
  activeSessions: [],
  logs: [],
  isFollowingLogs: false
};

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  initializeApp();
  initializeChart();
  startRealtimeUpdates();
  setupEventListeners();
  checkFirstTimeUser();
});

/**
 * Initialize the application
 */
function initializeApp() {
  console.log('StealthScrape AI initializing...');
  loadTheme();
  updateDashboardStats();
}

/**
 * Initialize Chart.js
 */
function initializeChart() {
  const ctx = document.getElementById('detection-chart');
  if (!ctx) return;

  const chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      datasets: [{
        label: 'Bypass Success Rate',
        data: [98.5, 97.8, 99.2, 98.7, 99.5, 98.9, 98.7],
        borderColor: 'rgba(138, 43, 226, 1)',
        backgroundColor: 'rgba(138, 43, 226, 0.1)',
        tension: 0.4,
        fill: true,
        pointBackgroundColor: 'rgba(0, 198, 255, 1)',
        pointBorderColor: '#fff',
        pointBorderWidth: 2,
        pointRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          min: 95,
          max: 100,
          grid: {
            color: 'rgba(255, 255, 255, 0.1)'
          },
          ticks: {
            color: 'rgba(224, 224, 255, 0.7)'
          }
        },
        x: {
          grid: {
            color: 'rgba(255, 255, 255, 0.1)'
          },
          ticks: {
            color: 'rgba(224, 224, 255, 0.7)'
          }
        }
      }
    }
  });
}

/**
 * Setup Event Listeners
 */
function setupEventListeners() {
  // Navigation
  document.querySelectorAll('.main-nav li').forEach(item => {
    item.addEventListener('click', (e) => {
      const page = e.currentTarget.dataset.page;
      navigateTo(page);
    });
  });

  // Theme Toggle
  document.querySelectorAll('.theme-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const theme = e.currentTarget.dataset.theme;
      setTheme(theme);
    });
  });

  // Quick Actions
  document.querySelectorAll('.action-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const platform = e.currentTarget.classList.contains('facebook') ? 'facebook' :
                      e.currentTarget.classList.contains('tiktok') ? 'tiktok' :
                      e.currentTarget.classList.contains('instagram') ? 'instagram' : 'twitter';
      handleQuickAction(platform);
    });
  });

  // Session Controls
  document.querySelectorAll('.session-control-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const sessionItem = e.currentTarget.closest('.session-item');
      if (e.currentTarget.classList.contains('pause')) {
        pauseSession(sessionItem);
      } else if (e.currentTarget.classList.contains('stop')) {
        stopSession(sessionItem);
      }
    });
  });

  // Menu Toggle (Mobile)
  document.querySelector('.menu-toggle')?.addEventListener('click', () => {
    document.querySelector('.sidebar').classList.toggle('mobile-open');
  });

  // Log Controls
  document.querySelector('.card-footer .card-btn')?.addEventListener('click', (e) => {
    if (e.currentTarget.textContent.trim() === 'Clear Logs') {
      clearLogs();
    } else if (e.currentTarget.textContent.trim() === 'Follow Logs') {
      toggleLogFollowing();
    }
  });

  // Notification Button
  document.querySelector('.notification-btn')?.addEventListener('click', () => {
    showNotifications();
  });
}

/**
 * Navigate to a different page
 */
function navigateTo(page) {
  appState.currentPage = page;
  
  // Update active state in navigation
  document.querySelectorAll('.main-nav li').forEach(item => {
    item.classList.remove('active');
    if (item.dataset.page === page) {
      item.classList.add('active');
    }
  });

  // Update page title
  const pageTitle = document.querySelector('.page-title h1');
  const pageSubtitle = document.querySelector('.page-title p');
  
  const titles = {
    dashboard: { title: 'Dashboard', subtitle: 'Monitor your scraping operations in real-time' },
    targets: { title: 'Targets', subtitle: 'Manage your target websites' },
    scrapers: { title: 'Scrapers', subtitle: 'Configure and manage scrapers' },
    results: { title: 'Results', subtitle: 'View and export scraped data' },
    proxies: { title: 'Proxies', subtitle: 'Manage proxy configurations' },
    settings: { title: 'Settings', subtitle: 'Configure application settings' }
  };

  if (titles[page]) {
    pageTitle.textContent = titles[page].title;
    pageSubtitle.textContent = titles[page].subtitle;
  }
}

/**
 * Set theme
 */
function setTheme(theme) {
  appState.theme = theme;
  localStorage.setItem('theme', theme);

  document.querySelectorAll('.theme-btn').forEach(btn => {
    btn.classList.remove('active');
    if (btn.dataset.theme === theme) {
      btn.classList.add('active');
    }
  });

  document.body.classList.remove('dark-mode', 'light-mode');
  document.body.classList.add(`${theme}-mode`);
}

/**
 * Load theme from localStorage
 */
function loadTheme() {
  const savedTheme = localStorage.getItem('theme') || 'dark';
  setTheme(savedTheme);
}

/**
 * Update dashboard statistics
 */
async function updateDashboardStats() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/dashboard`);
    const stats = await response.json();
    
    // Update UI with stats
    updateResourceMonitors(stats.system_status);
  } catch (error) {
    console.error('Failed to fetch dashboard stats:', error);
  }
}

/**
 * Update resource monitors
 */
function updateResourceMonitors(systemStatus) {
  if (!systemStatus) return;

  const updates = [
    { selector: '.resource-fill.cpu', value: systemStatus.cpu_usage || 42 },
    { selector: '.resource-fill.memory', value: (systemStatus.memory_usage || 42) * 1.5 },
    { selector: '.resource-fill.bandwidth', value: systemStatus.network_bandwidth || 65 },
    { selector: '.resource-fill.connections', value: 48 }
  ];

  updates.forEach(update => {
    const element = document.querySelector(update.selector);
    if (element) {
      element.style.width = `${Math.min(update.value, 100)}%`;
    }
  });
}

/**
 * Start real-time updates
 */
function startRealtimeUpdates() {
  // Update dashboard stats every 30 seconds
  setInterval(updateDashboardStats, 30000);

  // Simulate real-time logs
  setInterval(addRandomLog, 8000);
}

/**
 * Add random log entry
 */
function addRandomLog() {
  const logs = document.querySelector('.logs-container');
  if (!logs) return;

  const logTypes = ['success', 'info', 'warning', 'error'];
  const sources = ['FacebookScraper', 'TikTokScraper', 'ProxyManager', 'CDPHandler', 'InstagramScraper'];
  const messages = [
    'Successfully bypassed anti-bot system',
    'Rotated to new residential proxy',
    'Detected Cloudflare challenge',
    'Retrieved profile data',
    'Session completed successfully',
    'Proxy connection timeout, retrying',
    'CAPTCHA solved successfully'
  ];

  const logType = logTypes[Math.floor(Math.random() * logTypes.length)];
  const source = sources[Math.floor(Math.random() * sources.length)];
  const message = messages[Math.floor(Math.random() * messages.length)];
  const time = new Date().toLocaleTimeString('en-US', { hour12: false });

  const logEntry = document.createElement('div');
  logEntry.className = `log-item ${logType}`;
  logEntry.innerHTML = `
    <span class="log-time">${time}</span>
    <span class="log-source">${source}</span>
    <span class="log-message">${message}</span>
  `;

  logs.insertBefore(logEntry, logs.firstChild);

  // Keep only last 50 logs
  while (logs.children.length > 50) {
    logs.removeChild(logs.lastChild);
  }

  // Auto-scroll if following logs
  if (appState.isFollowingLogs) {
    logs.scrollTop = 0;
  }
}

/**
 * Handle quick action
 */
async function handleQuickAction(platform) {
  const url = prompt(`Enter ${platform.charAt(0).toUpperCase() + platform.slice(1)} URL to scrape:`);
  if (!url) return;

  try {
    const response = await fetch(`${API_BASE_URL}/api/scrape`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        url: url,
        platform: platform,
        stealth_level: 'maximum'
      })
    });

    const result = await response.json();
    
    if (result.session_id) {
      showNotification(`${platform.charAt(0).toUpperCase() + platform.slice(1)} scraping started!`, 'success');
      addSessionCard(result);
    }
  } catch (error) {
    showNotification('Failed to start scraping session', 'error');
  }
}

/**
 * Add session card to dashboard
 */
function addSessionCard(sessionData) {
  const sessionGrid = document.querySelector('.session-grid');
  if (!sessionGrid) return;

  const platformIcons = {
    facebook: 'fab fa-facebook',
    tiktok: 'fab fa-tiktok',
    instagram: 'fab fa-instagram',
    twitter: 'fab fa-twitter'
  };

  const sessionItem = document.createElement('div');
  sessionItem.className = 'session-item';
  sessionItem.innerHTML = `
    <div class="session-header">
      <div class="session-icon">
        <i class="${platformIcons[sessionData.platform] || 'fas fa-globe'}"></i>
      </div>
      <div class="session-title">
        <h4>${sessionData.platform.charAt(0).toUpperCase() + sessionData.platform.slice(1)} Scraper</h4>
        <p>${sessionData.url}</p>
      </div>
    </div>
    <div class="session-progress">
      <div class="progress-bar">
        <div class="progress-fill" style="width: 0%"></div>
      </div>
      <div class="progress-stats">
        <span>0% complete</span>
        <span>0 items</span>
      </div>
    </div>
    <div class="session-controls">
      <button class="session-control-btn pause">
        <i class="fas fa-pause"></i>
      </button>
      <button class="session-control-btn stop">
        <i class="fas fa-stop"></i>
      </button>
    </div>
  `;

  sessionGrid.appendChild(sessionItem);
  
  // Start polling for session updates
  pollSessionProgress(sessionData.session_id, sessionItem);
}

/**
 * Poll session progress
 */
async function pollSessionProgress(sessionId, sessionElement) {
  const interval = setInterval(async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/session/${sessionId}`);
      const status = await response.json();

      // Update progress
      const progressFill = sessionElement.querySelector('.progress-fill');
      const progressStats = sessionElement.querySelector('.progress-stats');
      
      if (progressFill) {
        progressFill.style.width = `${status.progress}%`;
      }
      
      if (progressStats) {
        progressStats.innerHTML = `
          <span>${status.progress}% complete</span>
          <span>${status.items_scraped} items</span>
        `;
      }

      // Stop polling if session is complete or failed
      if (status.status === 'completed' || status.status === 'failed' || status.status === 'closed') {
        clearInterval(interval);
        showNotification(`${status.status === 'completed' ? 'Session completed' : 'Session ended'}`, status.status === 'completed' ? 'success' : 'info');
      }
    } catch (error) {
      console.error('Failed to poll session progress:', error);
      clearInterval(interval);
    }
  }, 2000);
}

/**
 * Pause session
 */
function pauseSession(sessionItem) {
  const pauseBtn = sessionItem.querySelector('.session-control-btn.pause');
  const icon = pauseBtn.querySelector('i');
  
  if (icon.classList.contains('fa-pause')) {
    icon.classList.remove('fa-pause');
    icon.classList.add('fa-play');
    showNotification('Session paused', 'info');
  } else {
    icon.classList.remove('fa-play');
    icon.classList.add('fa-pause');
    showNotification('Session resumed', 'success');
  }
}

/**
 * Stop session
 */
async function stopSession(sessionItem) {
  if (confirm('Are you sure you want to stop this session?')) {
    // Remove from UI
    sessionItem.style.opacity = '0.5';
    showNotification('Session stopped', 'warning');
  }
}

/**
 * Clear logs
 */
function clearLogs() {
  const logsContainer = document.querySelector('.logs-container');
  if (logsContainer) {
    logsContainer.innerHTML = '';
    showNotification('Logs cleared', 'success');
  }
}

/**
 * Toggle log following
 */
function toggleLogFollowing() {
  appState.isFollowingLogs = !appState.isFollowingLogs;
  const btn = document.querySelector('.card-footer .card-btn.primary');
  if (btn) {
    btn.textContent = appState.isFollowingLogs ? 'Stop Following' : 'Follow Logs';
  }
}

/**
 * Show notification
 */
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification-toast ${type}`;
  notification.innerHTML = `
    <i class="fas ${type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle'}"></i>
    <span>${message}</span>
  `;

  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: var(--surface);
    color: var(--text-primary);
    padding: 16px 24px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    z-index: 10000;
    animation: slideIn 0.3s ease;
    border-left: 4px solid ${type === 'success' ? 'var(--success)' : type === 'error' ? 'var(--error)' : 'var(--warning)'};
  `;

  document.body.appendChild(notification);

  setTimeout(() => {
    notification.style.animation = 'slideOut 0.3s ease';
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

/**
 * Show notifications panel
 */
function showNotifications() {
  showNotification('Notifications feature coming soon!', 'info');
}

/**
 * Check first-time user
 */
function checkFirstTimeUser() {
  const hasVisited = localStorage.getItem('hasVisited');
  if (!hasVisited) {
    setTimeout(() => {
      showNotification('Welcome to StealthScrape AI! Click Quick Actions to start scraping.', 'success');
      localStorage.setItem('hasVisited', 'true');
    }, 1000);
  }
}

// Add slide-in animation styles
const style = document.createElement('style');
style.textContent = `
  @keyframes slideIn {
    from {
      transform: translateX(400px);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
  
  @keyframes slideOut {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(400px);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);

/**
 * Particle Background Animation System
 */
class ParticleBackground {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    
    this.ctx = this.canvas.getContext('2d');
    this.particles = [];
    this.mouse = { x: null, y: null };
    this.colors = [
      'rgba(138, 43, 226, 0.7)',
      'rgba(0, 198, 255, 0.7)',
      'rgba(255, 0, 136, 0.7)',
      'rgba(124, 252, 0, 0.7)'
    ];
    
    this.init();
    this.animate();
    
    // Mouse tracking
    document.addEventListener('mousemove', (e) => {
      this.mouse.x = e.clientX;
      this.mouse.y = e.clientY;
    });
    
    window.addEventListener('resize', () => this.resize());
  }
  
  init() {
    this.resize();
    for (let i = 0; i < 80; i++) {
      this.particles.push(new Particle(this));
    }
  }
  
  resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }
  
  animate() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    // Draw connections
    for (let i = 0; i < this.particles.length; i++) {
      for (let j = i + 1; j < this.particles.length; j++) {
        const dx = this.particles[i].x - this.particles[j].x;
        const dy = this.particles[i].y - this.particles[j].y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        
        if (distance < 150) {
          this.ctx.beginPath();
          this.ctx.strokeStyle = `rgba(138, 43, 226, ${1 - distance / 150})`;
          this.ctx.lineWidth = 1;
          this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
          this.ctx.lineTo(this.particles[j].x, this.particles[j].y);
          this.ctx.stroke();
        }
      }
      
      // Draw particles
      this.particles[i].update();
      this.particles[i].draw();
    }
    
    requestAnimationFrame(() => this.animate());
  }
}

class Particle {
  constructor(background) {
    this.background = background;
    this.radius = Math.random() * 3 + 1;
    this.x = Math.random() * this.background.canvas.width;
    this.y = Math.random() * this.background.canvas.height;
    this.color = this.background.colors[Math.floor(Math.random() * this.background.colors.length)];
    this.speedX = (Math.random() - 0.5) * 2;
    this.speedY = (Math.random() - 0.5) * 2;
    this.mass = 1;
  }
  
  draw() {
    this.background.ctx.beginPath();
    this.background.ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    this.background.ctx.fillStyle = this.color;
    this.background.ctx.fill();
  }
  
  update() {
    // Mouse interaction
    if (this.background.mouse.x && this.background.mouse.y) {
      const dx = this.background.mouse.x - this.x;
      const dy = this.background.mouse.y - this.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      
      if (distance < 100) {
        const force = 10 / distance;
        this.speedX -= (dx / distance) * force;
        this.speedY -= (dy / distance) * force;
      }
    }
    
    // Edge bouncing
    if (this.x + this.radius > this.background.canvas.width || 
        this.x - this.radius < 0) {
      this.speedX = -this.speedX;
    }
    
    if (this.y + this.radius > this.background.canvas.height || 
        this.y - this.radius < 0) {
      this.speedY = -this.speedY;
    }
    
    // Update position
    this.x += this.speedX;
    this.y += this.speedY;
  }
}

/**
 * Interactive Tutorial System
 */
class InteractiveTutorial {
  constructor() {
    this.steps = [
      {
        title: "Welcome to StealthScrape",
        content: "This interactive tour will guide you through all the powerful features of our platform.",
        element: 'body'
      },
      {
        title: "Dashboard Overview",
        content: "Monitor all your scraping sessions in real-time with our advanced dashboard.",
        element: '.dashboard-grid'
      },
      {
        title: "Quick Actions",
        content: "Scrape popular platforms like Facebook and TikTok with a single click.",
        element: '.quick-actions-grid'
      },
      {
        title: "Active Sessions",
        content: "Track the progress of your scraping sessions with real-time updates.",
        element: '.session-grid'
      },
      {
        title: "Real-time Logs",
        content: "Monitor system events and scraping activities in real-time.",
        element: '.logs-container'
      },
      {
        title: "Ready to Start?",
        content: "Click the button below to create your first scraping session.",
        element: '.card-btn.primary',
        button: {
          text: "Create Your First Session",
          action: () => document.querySelector('.card-btn.primary')?.click()
        }
      }
    ];
    this.currentStep = 0;
  }
  
  start() {
    this.showStep(this.currentStep);
  }
  
  showStep(stepIndex) {
    this.currentStep = stepIndex;
    
    // Remove existing overlay
    const existingOverlay = document.querySelector('.tutorial-overlay');
    if (existingOverlay) existingOverlay.remove();
    
    // Remove existing highlights
    document.querySelectorAll('.tutorial-highlight').forEach(el => el.classList.remove('tutorial-highlight'));
    document.querySelectorAll('.tutorial-spotlight').forEach(el => el.remove());
    
    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'tutorial-overlay';
    overlay.innerHTML = `
      <div class="tutorial-modal">
        <div class="tutorial-header">
          <h3>${this.steps[stepIndex].title}</h3>
          <button class="tutorial-close">&times;</button>
        </div>
        <div class="tutorial-content">
          ${this.steps[stepIndex].content}
        </div>
        <div class="tutorial-footer">
          <span class="tutorial-progress">${stepIndex + 1} of ${this.steps.length}</span>
          <div class="tutorial-buttons">
            ${stepIndex > 0 ? '<button class="tutorial-prev">Previous</button>' : ''}
            ${stepIndex < this.steps.length - 1 ? 
              '<button class="tutorial-next neomorphic-btn primary">Next</button>' : 
              (this.steps[stepIndex].button ? 
                `<button class="tutorial-action neomorphic-btn primary">${this.steps[stepIndex].button.text}</button>` : 
                '<button class="tutorial-done neomorphic-btn primary">Done</button>'
              )
            }
          </div>
        </div>
      </div>
    `;
    
    document.body.appendChild(overlay);
    
    // Highlight target element
    if (this.steps[stepIndex].element) {
      const targetElement = document.querySelector(this.steps[stepIndex].element);
      if (targetElement) {
        targetElement.classList.add('tutorial-highlight');
        
        // Create spotlight effect
        const spotlight = document.createElement('div');
        spotlight.className = 'tutorial-spotlight';
        document.body.appendChild(spotlight);
        
        // Position spotlight
        const rect = targetElement.getBoundingClientRect();
        spotlight.style.left = `${rect.left + window.scrollX}px`;
        spotlight.style.top = `${rect.top + window.scrollY}px`;
        spotlight.style.width = `${rect.width}px`;
        spotlight.style.height = `${rect.height}px`;
      }
    }
    
    // Add event listeners
    document.querySelector('.tutorial-close').addEventListener('click', () => this.end());
    document.querySelector('.tutorial-overlay').addEventListener('click', (e) => {
      if (e.target === document.querySelector('.tutorial-overlay')) {
        this.end();
      }
    });
    
    if (stepIndex > 0) {
      document.querySelector('.tutorial-prev').addEventListener('click', () => this.previousStep());
    }
    
    if (stepIndex < this.steps.length - 1) {
      document.querySelector('.tutorial-next').addEventListener('click', () => this.nextStep());
    }
    
    if (this.steps[stepIndex].button) {
      document.querySelector('.tutorial-action').addEventListener('click', () => {
        this.steps[stepIndex].button.action();
        this.end();
      });
    }
    
    if (stepIndex === this.steps.length - 1 && !this.steps[stepIndex].button) {
      document.querySelector('.tutorial-done').addEventListener('click', () => this.end());
    }
  }
  
  nextStep() {
    this.showStep(this.currentStep + 1);
  }
  
  previousStep() {
    this.showStep(this.currentStep - 1);
  }
  
  end() {
    const overlay = document.querySelector('.tutorial-overlay');
    if (overlay) overlay.remove();
    
    document.querySelectorAll('.tutorial-highlight').forEach(el => el.classList.remove('tutorial-highlight'));
    document.querySelectorAll('.tutorial-spotlight').forEach(el => el.remove());
    
    // Mark tutorial as completed
    localStorage.setItem('tutorial_completed', 'true');
  }
}

/**
 * Initialize advanced features
 */
function initializeAdvancedFeatures() {
  // Initialize particle background
  setTimeout(() => {
    if (document.getElementById('particle-canvas')) {
      new ParticleBackground('particle-canvas');
    }
  }, 500);
  
  // Check for tutorial start button
  const startTutorialBtn = document.getElementById('start-tutorial');
  if (startTutorialBtn) {
    startTutorialBtn.addEventListener('click', () => {
      const tutorial = new InteractiveTutorial();
      tutorial.start();
    });
  }
  
  // Auto-start tutorial for first-time users
  if (!localStorage.getItem('tutorial_completed')) {
    setTimeout(() => {
      const tutorial = new InteractiveTutorial();
      tutorial.start();
    }, 2000);
  }
}

// Call advanced features initialization
initializeAdvancedFeatures();
