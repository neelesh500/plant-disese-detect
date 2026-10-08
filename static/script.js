document.addEventListener('DOMContentLoaded', () => {
    const dragArea = document.getElementById('drag-area');
    const fileInput = document.getElementById('file-input');
    const browseBtn = document.getElementById('browse-btn');
    const previewArea = document.getElementById('preview-area');
    const imagePreview = document.getElementById('image-preview');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resetBtn = document.getElementById('reset-btn');
    const resultsContainer = document.getElementById('results-container');
    const uploadPanel = document.getElementById('upload-panel');

    let currentFile = null;

    // --- 3D Tilt Effect on interactive panels ---
    const tiltElements = document.querySelectorAll('[data-tilt]');

    tiltElements.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            // Get mouse position relative to element center (-1 to 1)
            const x = (e.clientX - rect.left - rect.width / 2) / (rect.width / 2);
            const y = (e.clientY - rect.top - rect.height / 2) / (rect.height / 2);

            // Limit tilt angle (e.g. max 5 degrees)
            const maxTilt = 5;
            const tiltX = -y * maxTilt;
            const tiltY = x * maxTilt;

            el.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(1.02, 1.02, 1.02)`;
        });

        el.addEventListener('mouseleave', () => {
            el.style.transition = 'transform 0.4s ease'; // Smooth snap back
            el.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
            // Remove transition after it finished so hover works instantly
            setTimeout(() => {
                el.style.transition = 'border-color 0.4s ease, box-shadow 0.4s ease'; // retain original transitions
            }, 400);
        });
    });

    // --- File Upload Handling ---
    browseBtn.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', function () {
        if (this.files.length) {
            handleFile(this.files[0]);
        }
    });

    dragArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dragArea.classList.add('active');
        dragArea.querySelector('h3').textContent = "Release to Drop";
    });

    dragArea.addEventListener('dragleave', () => {
        dragArea.classList.remove('active');
        dragArea.querySelector('h3').textContent = "Upload Leaf Specimen";
    });

    dragArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dragArea.classList.remove('active');
        if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    function handleFile(file) {
        if (file && file.type.startsWith('image/')) {
            currentFile = file;
            const reader = new FileReader();
            reader.onload = () => {
                imagePreview.src = reader.result;
                dragArea.classList.add('hidden');
                previewArea.classList.remove('hidden');
                resultsContainer.classList.add('hidden');
            };
            reader.readAsDataURL(file);
        } else {
            alert("Format unsupported. Please upload a valid image file.");
        }
    }

    // --- Reset ---
    resetBtn.addEventListener('click', () => {
        currentFile = null;
        imagePreview.src = "";
        previewArea.classList.add('hidden');
        dragArea.classList.remove('hidden');
        resultsContainer.classList.add('hidden');
        dragArea.querySelector('h3').textContent = "Upload Leaf Specimen";
        fileInput.value = "";
    });

    // --- Number Animation ---
    function animateValue(obj, start, end, duration, isFloat = false) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            let val = progress * (end - start) + start;
            if (isFloat) {
                obj.innerHTML = val.toFixed(2);
            } else {
                obj.innerHTML = Math.floor(val);
            }
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    // --- Analyze Execution ---
    analyzeBtn.addEventListener('click', () => {
        if (!currentFile) return;

        // UI State update for scanning
        analyzeBtn.innerHTML = `
        <svg class="spinner" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="animation: spin 1s linear infinite;">
            <path d="M21 12a9 9 0 1 1-6.219-8.56"></path>
        </svg>
        Processing Inference...`;
        analyzeBtn.disabled = true;
        previewArea.classList.add('scanning');

        // Spin keyframe via JS dynamically
        if (!document.getElementById('dynamic-spin')) {
            const style = document.createElement('style');
            style.id = 'dynamic-spin';
            style.innerHTML = `@keyframes spin { 100% { transform: rotate(360deg); } }`;
            document.head.appendChild(style);
        }

        const formData = new FormData();
        formData.append('file', currentFile);

        // Append Multimodal Environmental Data
        if (document.getElementById('temperature-input')) {
            formData.append('temperature', document.getElementById('temperature-input').value);
            formData.append('humidity', document.getElementById('humidity-input').value);
            formData.append('soil_moisture', document.getElementById('moisture-input').value);
        }

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                // Revert state
                analyzeBtn.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>
            </svg> Init Inference`;
                analyzeBtn.disabled = false;
                previewArea.classList.remove('scanning');

                // Set content
                document.getElementById('r-disease').textContent = data.disease || "Unknown Anomaly";
                document.getElementById('r-treatment').textContent = data.treatment || "No protocol found.";

                // Extract numeric values
                let confVal = parseFloat(data.confidence) || 0;
                let latVal = parseFloat(data.latency) || 0;
                let sevVal = parseFloat(data.severity_percentage) || 0;

                // Show results
                resultsContainer.classList.remove('hidden');

                // Animate numbers
                animateValue(document.getElementById('r-confidence-val'), 0, confVal, 1500, true);
                animateValue(document.getElementById('r-latency-val'), 0, latVal, 1200, false);
                if (document.getElementById('r-severity-val')) {
                    animateValue(document.getElementById('r-severity-val'), 0, sevVal, 1500, true);
                }

                resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
            })
            .catch(error => {
                console.error('Inference Error:', error);
                analyzeBtn.textContent = "Pipeline Error. Retry.";
                analyzeBtn.disabled = false;
                previewArea.classList.remove('scanning');

                setTimeout(() => {
                    analyzeBtn.innerHTML = `
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>
                </svg> Init Inference`;
                }, 3000);
            });
    });

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

    function addMessage(text, sender = 'user') {
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
            try { recognition.start(); } catch (e) { }
        });

        agentVoiceBtn.addEventListener('click', () => {
            if (agentVoiceBtn.classList.contains('listening')) {
                recognition.stop();
            } else {
                agentVoiceBtn.classList.add('listening');
                try { recognition.start(); } catch (e) { }
            }
        });
    }

    async function processCommand(cmd) {
        // Special strict UI override for capture action specifically (if video is on)
        if (cmd.includes('click') || cmd.includes('shoot') || cmd.includes('take') || cmd.includes('capture')) {
            if (!agentCamera.classList.contains('hidden')) {
                addMessage('Capturing photo...', 'ai');
                agentCaptureBtn.click();
                return;
            }
        }

        try {
            // Show typing indicator
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message ai typing';
            typingDiv.id = 'typing-indicator';
            typingDiv.innerHTML = '<span class="dots">...</span>';
            agentMessages.appendChild(typingDiv);
            agentMessages.scrollTop = agentMessages.scrollHeight;

            const response = await fetch('/api/agent', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: cmd })
            });

            const data = await response.json();

            // Remove typing indicator
            const indicator = document.getElementById('typing-indicator');
            if (indicator) indicator.remove();

            if (data.reply) {
                addMessage(data.reply, 'ai');
            }

            // Excecute actions if commanded by Gemini
            if (data.action === "CAMERA") {
                startCamera();
            } else if (data.action === "BROWSE") {
                browseBtn.click();
            } else if (data.action === "ANALYZE") {
                analyzeBtn.click();
            } else if (data.action === "RESET") {
                resetBtn.click();
            } else if (data.action === "CLOSE") {
                setTimeout(() => agentContainer.classList.add('hidden'), 1000);
                stopCamera();
            }

        } catch (error) {
            console.error("Agent error:", error);
            const indicator = document.getElementById('typing-indicator');
            if (indicator) indicator.remove();
            addMessage("Network connection to AI brain lost. Please try again.", 'ai');
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

    // Append slider listeners
    ['temperature', 'humidity', 'moisture'].forEach(id => {
        const input = document.getElementById(`${id}-input`);
        const valSpan = document.getElementById(id === 'temperature' ? 'temp-val' : id === 'humidity' ? 'hum-val' : 'moist-val');
        if (input && valSpan) {
            input.addEventListener('input', (e) => {
                valSpan.textContent = e.target.value;
            });
        }
    });
});

// Initialize system debug logs
console.log("AgriNet UI modules loaded.");

// Graceful degradation for non-3D browsers
if (!window.requestAnimationFrame) { console.warn("RAF not supported."); }
