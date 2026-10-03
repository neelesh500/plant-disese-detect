with open('static/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- AI Agent UI --- */
#agent-toggle-btn {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--brand-secondary);
    border: 2px solid var(--brand-primary);
    color: white;
    cursor: pointer;
    box-shadow: 0 5px 20px rgba(0,0,0,0.5);
    z-index: 1000;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
}
#agent-toggle-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
}

#ai-agent-container {
    position: fixed;
    bottom: 6rem;
    right: 2rem;
    width: 350px;
    height: 500px;
    display: flex;
    flex-direction: column;
    z-index: 999;
    background: rgba(14, 23, 17, 0.85);
    border: 1px solid var(--brand-primary);
    padding: 0;
    overflow: hidden;
}

#ai-agent-container.hidden {
    display: none !important;
}

.agent-header {
    background: rgba(16, 185, 129, 0.2);
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--panel-border);
}

.agent-header h4 {
    margin: 0;
    font-size: 1.1rem;
    color: var(--brand-cyan);
}

#agent-close-btn {
    background: transparent;
    border: none;
    color: var(--text-primary);
    font-size: 1.5rem;
    cursor: pointer;
}

.agent-messages {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}

.message {
    padding: 0.5rem 1rem;
    border-radius: 12px;
    max-width: 80%;
    word-wrap: break-word;
    font-size: 0.9rem;
}

.message.ai {
    background: rgba(16, 185, 129, 0.15);
    align-self: flex-start;
    border-bottom-left-radius: 2px;
}

.message.user {
    background: rgba(255, 255, 255, 0.1);
    align-self: flex-end;
    border-bottom-right-radius: 2px;
}

#agent-camera {
    width: 100%;
    max-height: 200px;
    background: #000;
    object-fit: cover;
}

.agent-input-area {
    display: flex;
    padding: 0.8rem;
    border-top: 1px solid var(--panel-border);
    gap: 0.5rem;
    background: rgba(14, 23, 17, 0.95);
}

#agent-input {
    flex: 1;
    background: transparent;
    border: 1px solid var(--text-muted);
    border-radius: 8px;
    padding: 0.5rem 0.8rem;
    color: var(--text-primary);
    font-family: var(--font-main);
    outline: none;
}

#agent-input:focus {
    border-color: var(--brand-primary);
}

#agent-voice-btn {
    padding: 0.5rem;
}

#agent-voice-btn.listening {
    color: red;
    animation: pulse 1s infinite alternate;
}
@keyframes pulse {
    0% { transform: scale(1); }
    100% { transform: scale(1.1); }
}
''')
