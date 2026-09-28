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

                // Show results
                resultsContainer.classList.remove('hidden');

                // Animate numbers
                animateValue(document.getElementById('r-confidence-val'), 0, confVal, 1500, true);
                animateValue(document.getElementById('r-latency-val'), 0, latVal, 1200, false);

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
});

// Initialize system debug logs
console.log("AgriNet UI modules loaded.");

// Graceful degradation for non-3D browsers
if (!window.requestAnimationFrame) { console.warn("RAF not supported."); }
