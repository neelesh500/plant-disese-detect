import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

agent_html = """
    <!-- AI Agent Interface -->
    <div id="ai-agent-container" class="hidden glass-panel" data-tilt>
        <div class="agent-header">
            <h4>AgriNet Agent</h4>
            <button id="agent-close-btn">&times;</button>
        </div>
        <div class="agent-messages" id="agent-messages">
            <div class="message ai">Hello! I am AgriNet AI. You can say "open camera", "upload image", "analyze", or "close".</div>
        </div>
        <video id="agent-camera" class="hidden" autoplay playsinline></video>
        <button id="agent-capture-btn" class="hidden btn-primary">Capture</button>
        <canvas id="agent-canvas" class="hidden"></canvas>
        <div class="agent-input-area">
            <input type="text" id="agent-input" placeholder="Ask or command (open, search, etc)...">
            <button id="agent-voice-btn" class="btn-ghost" title="Hold to speak">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path>
                    <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                    <line x1="12" y1="19" x2="12" y2="23"></line>
                    <line x1="8" y1="23" x2="16" y2="23"></line>
                </svg>
            </button>
            <button id="agent-send-btn" class="btn-primary">Send</button>
        </div>
    </div>
    <button id="agent-toggle-btn" class="glow-on-hover">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2a2 2 0 0 1 2 2v1h5a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2h-4v2h2v2H7v-2h2v-2H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h5V4a2 2 0 0 1 2-2z"></path>
        </svg>
    </button>
"""

content = content.replace('<script src="/static/script.js"></script>', agent_html + '\n    <script src="/static/script.js"></script>')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
