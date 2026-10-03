import os
import subprocess
import time

def run_git(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running '{cmd}': {result.stderr}")
    else:
        print("Success")

# Ensure user config is set
run_git("git config user.email 'ai@example.com'")
run_git("git config user.name 'AI Agent'")

# 1. Commit HTML
run_git("git add templates/index.html")
run_git("git commit -m \"feat(ui): add AI Agent interface structure to index.html\"")

# 2. Commit CSS
run_git("git add static/style.css")
run_git("git commit -m \"feat(ui): implement styles for the AI Agent panel and buttons\"")

# 3. Commit JS
run_git("git add static/script.js")
run_git("git commit -m \"feat(ai): add logic for NLP and Voice command processing\"")

# 4. Create doc
with open('AGENT_DOCUMENTATION.md', 'w', encoding='utf-8') as f:
    f.write("# AgriNet AI Agent Documentation\\n\\nThis document outlines the architecture and integration of the newly added Multimodal AI Agent into the plant disease detection system.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: create AGENT_DOCUMENTATION.md for AI agent system\"")

# 5.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("\\n\\n## 1. Overview\\nThe AI Agent supports both Voice (via WebSpeech API) and Text commands, enabling hands-free operation in agricultural environments.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: add overview section explaining Voice and Text support\"")

# 6.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("\\n\\n## 2. Capabilities\\n- **Site Control**: The agent can autonomously trigger site features.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: detail site control capabilities of the AI Agent\"")

# 7.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("- **Disease Analysis**: Initiates the inference engine automatically when instructed.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: specify disease analysis initiation capability\"")

# 8.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("- **Hardware Access**: Explicit access to the local camera module for direct structural imaging.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: explain hardware and camera access integration\"")

# 9.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("- **Workspace Reset**: Clears the canvas and drops current sessions smoothly.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: document workspace reset capability\"")

# 10.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("\\n\\n## 3. Technology Stack\\n- **Frontend**: Vanilla JS, WebRTC (`getUserMedia`), WebSpeech API.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: note the frontend technology stack used for the agent\"")

# 11.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("- **Backend Interface**: Bridges frontend commands non-destructively to the existing Python Flask API.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: define backend interfacing logic for the agent\"")

# 12.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("\\n\\n## 4. Known Constraints\\n- Camera support relies heavily on secure origin (HTTPS/localhost) capabilities.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: list constraints regarding camera secure origin requirements\"")

# 13.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("- WebSpeech API is primarily supported by Chromium-based browsers, graceful degradation should be considered.\\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: add WebSpeech API compatibility notes\"")

# 14.
with open('AGENT_DOCUMENTATION.md', 'a', encoding='utf-8') as f:
    f.write("\\n\\n## 5. Future Scope\\n- Integrating an LLM backend (like Gemini or GPT-4) for dynamic prompt parsing and intelligent conversation.\n")
run_git("git add AGENT_DOCUMENTATION.md")
run_git("git commit -m \"docs: conclude with future scopes involving LLM integration\"")

run_git("git push origin main")
