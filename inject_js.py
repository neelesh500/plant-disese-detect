import re

with open('static/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

agent_js = """
    // --- AI Agent Logic ---
    const agentContainer = document.getElementById('ai-agent-container');
    const agentToggleBtn = document.getElementById('agent-toggle-btn');
    const agentCloseBtn = document.getElementById('agent-close-btn');
    const agentMessages = document.getElementById('agent-messages');
    const agentInput = document.getElementById('agent-input');
    const agentSendBtn = document.getElementById('agent-send-btn');
    const agentVoiceBtn = document.getElementById('agent-voice-btn');
    const agentCamera = document.getElementById('agent-camera');
    const agentCaptureBtn = document.getElementById('agent-capture-btn');
    const agentCanvas = document.getElementById('agent-canvas');
    let stream = null;

    function addMessage(text, sender='user') {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message ' + sender;
        msgDiv.textContent = text;
        agentMessages.appendChild(msgDiv);
        agentMessages.scrollTop = agentMessages.scrollHeight;
    }

    agentToggleBtn.addEventListener('click', () => {
        agentContainer.classList.toggle('hidden');
    });

    agentCloseBtn.addEventListener('click', () => {
        agentContainer.classList.add('hidden');
        stopCamera();
    });

    agentSendBtn.addEventListener('click', () => {
        const text = agentInput.value.trim().toLowerCase();
        if (text) {
            addMessage(text, 'user');
            agentInput.value = '';
            processCommand(text);
        }
    });

    agentInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            agentSendBtn.click();
        }
    });

    // Voice Recognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition = null;
    if (SpeechRecognition) {
        recognition = new SpeechRecognition();
        recognition.lang = 'en-US'; // Can be 'hi-IN' or auto, but let's stick to en-US / hi-IN for robust matching
        recognition.interimResults = false;

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript.toLowerCase();
            addMessage(transcript, 'user');
            processCommand(transcript);
        };

        recognition.onend = () => {
            agentVoiceBtn.classList.remove('listening');
        };

        agentVoiceBtn.addEventListener('mousedown', () => {
            agentVoiceBtn.classList.add('listening');
            try { recognition.start(); } catch(e) {}
        });
        
        agentVoiceBtn.addEventListener('click', () => {
            if (agentVoiceBtn.classList.contains('listening')) {
                recognition.stop();
            } else {
                agentVoiceBtn.classList.add('listening');
                try { recognition.start(); } catch(e) {}
            }
        });
    }

    function processCommand(cmd) {
        // Simple NLP Matching
        if (cmd.includes('close') || cmd.includes('band')) {
            addMessage('Closing AI Agent.', 'ai');
            setTimeout(() => agentContainer.classList.add('hidden'), 1000);
            stopCamera();
        } 
        else if (cmd.includes('upload') || cmd.includes('browse') || cmd.includes('file')) {
            addMessage('Opening file browser.', 'ai');
            browseBtn.click();
        }
        else if (cmd.includes('detect') || cmd.includes('analyze') || cmd.includes('check') || cmd.includes('disease')) {
            addMessage('Initializing Inference...', 'ai');
            analyzeBtn.click();
        }
        else if (cmd.includes('reset') || cmd.includes('clear')) {
            addMessage('Resetting workspace.', 'ai');
            resetBtn.click();
        }
        else if (cmd.includes('camera') || cmd.includes('photo') || cmd.includes('capture') || cmd.includes('khicho')) {
            addMessage('Opening camera. Say "click photo" or press Capture.', 'ai');
            startCamera();
        }
        else if (cmd.includes('click') || cmd.includes('shoot') || cmd.includes('take')) {
            if (!agentCamera.classList.contains('hidden')) {
                addMessage('Capturing photo...', 'ai');
                agentCaptureBtn.click();
            } else {
                addMessage('Camera is not open. Please open camera first.', 'ai');
            }
        }
        else {
            addMessage('Apologies, I could not understand. Try: "open camera", "upload image", "analyze", or "reset".', 'ai');
        }
    }

    function startCamera() {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true }).then((vidStream) => {
                stream = vidStream;
                agentCamera.srcObject = stream;
                agentCamera.classList.remove('hidden');
                agentCaptureBtn.classList.remove('hidden');
            }).catch(err => {
                addMessage("Unable to access camera.", 'ai');
            });
        }
    }

    function stopCamera() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            stream = null;
        }
        agentCamera.classList.add('hidden');
        agentCaptureBtn.classList.add('hidden');
    }

    agentCaptureBtn.addEventListener('click', () => {
        agentCanvas.width = agentCamera.videoWidth;
        agentCanvas.height = agentCamera.videoHeight;
        agentCanvas.getContext('2d').drawImage(agentCamera, 0, 0);
        
        agentCanvas.toBlob((blob) => {
            const file = new File([blob], "camera_capture.jpg", { type: "image/jpeg" });
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            fileInput.files = dataTransfer.files;
            
            // Re-use handleFile from the main script scope
            if (typeof handleFile === 'function') {
                handleFile(file);
            }
            stopCamera();
            addMessage("Image captured and loaded to workspace.", 'ai');
        }, 'image/jpeg');
    });

"""

# We'll replace the last "});" with the new agent code, then append "});"
js_content = js_content.rsplit("});", 1)
new_js_content = js_content[0] + agent_js + "\\n});" + (js_content[1] if len(js_content) > 1 else "")

with open('static/script.js', 'w', encoding='utf-8') as f:
    f.write(new_js_content)
