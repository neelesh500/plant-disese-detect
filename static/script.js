/**
 * AgriNet AI - Frontend Control Engine
 * Manages tabs, multimodal disease diagnostics, sample leaf synthesizer,
 * fertilizer calculator, mandi prices, pest encyclopedia, organic bio-lab,
 * soil evaluator, scan history, and conversational AI assistant.
 */

document.addEventListener('DOMContentLoaded', () => {
    // --- Core Elements ---
    const dragArea = document.getElementById('drag-area');
    const fileInput = document.getElementById('file-input');
    const browseBtn = document.getElementById('browse-btn');
    const cameraTriggerBtn = document.getElementById('camera-trigger-btn');
    const previewArea = document.getElementById('preview-area');
    const imagePreview = document.getElementById('image-preview');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resetBtn = document.getElementById('reset-btn');
    const resultsContainer = document.getElementById('results-container');

    let currentFile = null;
    let lastDiagnosisData = null;

    // ==========================================
    // 1. TAB NAVIGATION ENGINE
    // ==========================================
    const featureButtons = document.querySelectorAll('.feature-btn');
    const navLinks = document.querySelectorAll('.nav-link');
    const tabPanes = document.querySelectorAll('.tab-pane');

    function switchTab(targetTabId) {
        // Update feature buttons
        featureButtons.forEach(btn => {
            if (btn.getAttribute('data-tab') === targetTabId) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Update nav links
        navLinks.forEach(link => {
            if (link.getAttribute('data-target') === targetTabId) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });

        // Switch visible pane
        tabPanes.forEach(pane => {
            if (pane.id === `pane-${targetTabId}`) {
                pane.classList.remove('hidden');
                pane.classList.add('active');
            } else {
                pane.classList.add('hidden');
                pane.classList.remove('active');
            }
        });

        // Lazy load data for specific tabs
        if (targetTabId === 'mandi') loadMandiPrices();
        if (targetTabId === 'pests') loadPestDirectory();
        if (targetTabId === 'organic') loadOrganicRecipes();
        if (targetTabId === 'history') renderHistoryList();

        // Smooth scroll to content
        const featureNav = document.getElementById('feature-nav');
        if (featureNav) {
            featureNav.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    featureButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');
            switchTab(tabId);
        });
    });

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = link.getAttribute('data-target');
            if (tabId) switchTab(tabId);
        });
    });

    // ==========================================
    // 2. 3D TILT EFFECT
    // ==========================================
    const tiltElements = document.querySelectorAll('[data-tilt]');
    tiltElements.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = (e.clientX - rect.left - rect.width / 2) / (rect.width / 2);
            const y = (e.clientY - rect.top - rect.height / 2) / (rect.height / 2);
            const maxTilt = 4;
            el.style.transform = `perspective(1000px) rotateX(${-y * maxTilt}deg) rotateY(${x * maxTilt}deg) scale3d(1.01, 1.01, 1.01)`;
        });

        el.addEventListener('mouseleave', () => {
            el.style.transition = 'transform 0.4s ease';
            el.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
            setTimeout(() => {
                el.style.transition = 'border-color 0.3s ease, box-shadow 0.3s ease';
            }, 400);
        });
    });

    // ==========================================
    // 3. FILE UPLOAD & PREVIEW
    // ==========================================
    if (browseBtn) {
        browseBtn.addEventListener('click', () => fileInput.click());
    }

    if (fileInput) {
        fileInput.addEventListener('change', function () {
            if (this.files && this.files.length) {
                handleFile(this.files[0]);
            }
        });
    }

    if (dragArea) {
        dragArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            dragArea.classList.add('active');
            const h3 = dragArea.querySelector('h3');
            if (h3) h3.textContent = "Release to Drop Leaf Specimen";
        });

        dragArea.addEventListener('dragleave', () => {
            dragArea.classList.remove('active');
            const h3 = dragArea.querySelector('h3');
            if (h3) h3.textContent = "Upload Leaf Specimen";
        });

        dragArea.addEventListener('drop', (e) => {
            e.preventDefault();
            dragArea.classList.remove('active');
            if (e.dataTransfer.files && e.dataTransfer.files.length) {
                handleFile(e.dataTransfer.files[0]);
            }
        });
    }

    function handleFile(file) {
        if (file && (file.type.startsWith('image/') || file.name.match(/\.(jpg|jpeg|png|webp)$/i))) {
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
            alert("Please upload a valid image file (PNG, JPG, or WEBP).");
        }
    }

    // Reset handler
    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            currentFile = null;
            imagePreview.src = "";
            previewArea.classList.add('hidden');
            dragArea.classList.remove('hidden');
            resultsContainer.classList.add('hidden');
            if (fileInput) fileInput.value = "";
        });
    }

    // ==========================================
    // 4. QUICK DEMO SAMPLE SYNTHESIZER
    // ==========================================
    // Generates realistic sample leaf blobs on the fly for 1-click test diagnosis!
    const sampleChips = document.querySelectorAll('.sample-chip');
    sampleChips.forEach(chip => {
        chip.addEventListener('click', () => {
            const sampleType = chip.getAttribute('data-sample');
            generateSampleLeafBlob(sampleType, (file) => {
                handleFile(file);
                // Trigger auto-analysis after loading
                setTimeout(() => {
                    analyzeBtn.click();
                }, 400);
            });
        });
    });

    function generateSampleLeafBlob(type, callback) {
        const canvas = document.createElement('canvas');
        canvas.width = 400;
        canvas.height = 400;
        const ctx = canvas.getContext('2d');

        // Background
        ctx.fillStyle = '#0f1712';
        ctx.fillRect(0, 0, 400, 400);

        // Draw basic leaf shape
        ctx.save();
        ctx.translate(200, 200);
        ctx.beginPath();
        ctx.moveTo(0, -160);
        ctx.bezierCurveTo(120, -100, 140, 80, 0, 170);
        ctx.bezierCurveTo(-140, 80, -120, -100, 0, -160);

        if (type === 'healthy_corn') {
            ctx.fillStyle = '#15803d'; // Rich healthy green
            ctx.fill();
            // Draw veins
            ctx.strokeStyle = '#22c55e';
            ctx.lineWidth = 3;
            ctx.stroke();
            // Parallel venation
            for (let i = -60; i <= 60; i += 20) {
                ctx.beginPath();
                ctx.moveTo(i, -120);
                ctx.lineTo(i * 1.2, 140);
                ctx.strokeStyle = 'rgba(74, 222, 128, 0.4)';
                ctx.lineWidth = 2;
                ctx.stroke();
            }
        } else if (type === 'tomato_early_blight') {
            ctx.fillStyle = '#4d7c0f'; // Tomato olive-green
            ctx.fill();
            // Concentric target spots (Bullseye pattern)
            drawTargetSpot(ctx, 30, -30, 45);
            drawTargetSpot(ctx, -40, 50, 35);
            drawTargetSpot(ctx, 40, 70, 25);
        } else if (type === 'potato_late_blight') {
            ctx.fillStyle = '#3f6212';
            ctx.fill();
            // Water-soaked dark necrotic blotches
            ctx.fillStyle = '#1c1917';
            ctx.beginPath();
            ctx.ellipse(30, -40, 60, 40, Math.PI / 4, 0, Math.PI * 2);
            ctx.fill();
            ctx.beginPath();
            ctx.ellipse(-30, 40, 50, 55, -Math.PI / 3, 0, Math.PI * 2);
            ctx.fill();
            // Pale halo around lesion
            ctx.strokeStyle = 'rgba(254, 240, 138, 0.6)';
            ctx.lineWidth = 5;
            ctx.stroke();
        } else if (type === 'apple_scab') {
            ctx.fillStyle = '#166534';
            ctx.fill();
            // Olive-black scabby circular lesions
            ctx.fillStyle = '#292524';
            for (let i = 0; i < 7; i++) {
                const rx = (Math.sin(i * 1.5) * 60);
                const ry = (Math.cos(i * 1.2) * 80);
                ctx.beginPath();
                ctx.arc(rx, ry, 16 + (i % 3) * 6, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        ctx.restore();

        canvas.toBlob((blob) => {
            const file = new File([blob], `${type}_specimen.jpg`, { type: 'image/jpeg' });
            callback(file);
        }, 'image/jpeg');
    }

    function drawTargetSpot(ctx, x, y, radius) {
        ctx.save();
        // Outer chlorotic yellow halo
        ctx.fillStyle = 'rgba(250, 204, 21, 0.5)';
        ctx.beginPath();
        ctx.arc(x, y, radius + 10, 0, Math.PI * 2);
        ctx.fill();

        // Dark concentric rings
        for (let r = radius; r > 5; r -= 8) {
            ctx.fillStyle = (r % 16 === 0) ? '#451a03' : '#78350f';
            ctx.beginPath();
            ctx.arc(x, y, r, 0, Math.PI * 2);
            ctx.fill();
        }
        ctx.restore();
    }

    // ==========================================
    // 5. INFERENCE & PREDICTION PIPELINE
    // ==========================================
    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', () => {
            if (!currentFile) {
                alert("Please upload or select an image specimen first.");
                return;
            }

            // UI State update for scanning
            analyzeBtn.innerHTML = `
            <svg class="spinner" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="animation: spin 1s linear infinite;">
                <path d="M21 12a9 9 0 1 1-6.219-8.56"></path>
            </svg>
            Analyzing Pathology...`;
            analyzeBtn.disabled = true;
            previewArea.classList.add('scanning');

            const formData = new FormData();
            formData.append('file', currentFile);

            const tempInput = document.getElementById('temperature-input');
            const humInput = document.getElementById('humidity-input');
            const moistInput = document.getElementById('moisture-input');

            if (tempInput) formData.append('temperature', tempInput.value);
            if (humInput) formData.append('humidity', humInput.value);
            if (moistInput) formData.append('soil_moisture', moistInput.value);

            fetch('/predict', {
                method: 'POST',
                body: formData
            })
                .then(res => res.json())
                .then(data => {
                    analyzeBtn.innerHTML = `
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>
                    </svg> Init Inference`;
                    analyzeBtn.disabled = false;
                    previewArea.classList.remove('scanning');

                    if (!data || !data.disease) {
                        throw new Error(data && data.error ? data.error : "Diagnostic service returned an empty response.");
                    }

                    lastDiagnosisData = data;
                    renderDiagnosisReport(data);

                    // Save to localStorage history
                    saveScanToHistory(data);
                })
                .catch(err => {
                    console.error("Prediction error:", err);
                    analyzeBtn.innerHTML = `⚠️ Error occurred. Retry`;
                    analyzeBtn.disabled = false;
                    previewArea.classList.remove('scanning');
                    alert(err.message || "Failed to process image. Please check connection and try again.");
                });
        });
    }

    function renderDiagnosisReport(data) {
        resultsContainer.classList.remove('hidden');

        // Title and meta
        const diseaseElem = document.getElementById('r-disease');
        const pathogenElem = document.getElementById('r-pathogen');
        const riskBadge = document.getElementById('r-risk-badge');

        if (diseaseElem) diseaseElem.textContent = data.disease || "Crop Specimen";
        if (pathogenElem) {
            pathogenElem.textContent = `${data.crop || "Crop"} · ${data.pathogen || "Foliar Pathogen"}`;
        }

        if (riskBadge) {
            const risk = data.risk_level || "Moderate";
            riskBadge.textContent = `${risk} Risk`;
            riskBadge.className = 'risk-badge';
            if (risk.toLowerCase().includes('safe')) riskBadge.classList.add('safe');
            else if (risk.toLowerCase().includes('crit') || risk.toLowerCase().includes('high')) riskBadge.classList.add('critical');
            else riskBadge.classList.add('moderate');
        }

        // Brief
        const briefElem = document.getElementById('r-brief');
        if (briefElem) {
            briefElem.textContent = data.brief || "Diagnosis completed. Follow the prescribed management protocol below.";
        }

        // Symptoms list
        const symptomsList = document.getElementById('r-symptoms-list');
        if (symptomsList) {
            symptomsList.innerHTML = '';
            const symptoms = data.symptoms || ["Characteristic foliar lesion patterns observed."];
            symptoms.forEach(sym => {
                const li = document.createElement('li');
                li.innerHTML = `<strong>•</strong> <span>${sym}</span>`;
                symptomsList.appendChild(li);
            });
        }

        // Chemical Medicines Grid
        const medicinesContainer = document.getElementById('r-medicines-list');
        if (medicinesContainer) {
            medicinesContainer.innerHTML = '';
            const meds = data.medicines || [];
            if (meds.length === 0 || (meds[0] && meds[0].brand.includes('None'))) {
                medicinesContainer.innerHTML = `
                <div class="empty-medicine-card">
                    <span style="font-size: 1.5rem;">✅</span>
                    <div>
                        <strong>No chemical fungicides required!</strong>
                        <p>Plant is healthy or under negligible economic threshold. Save chemical input costs.</p>
                    </div>
                </div>`;
            } else {
                meds.forEach(med => {
                    const card = document.createElement('div');
                    card.className = 'medicine-item-card glass-panel';
                    card.innerHTML = `
                        <div class="med-top">
                            <span class="med-brand">${med.brand || "Approved Molecule"}</span>
                            <span class="med-type-pill">${med.type || "Fungicide"}</span>
                        </div>
                        <div class="med-active">🧪 Active: <strong>${med.active || "Standard Active"}</strong></div>
                        <div class="med-dosage">💧 Dosage: <strong>${med.dosage || "As per label"}</strong></div>
                        <div class="med-timing">⏰ Timing: ${med.timing || "Apply at early symptom onset."}</div>
                    `;
                    medicinesContainer.appendChild(card);
                });
            }
        }

        // Organic Solutions Grid
        const organicContainer = document.getElementById('r-organic-list');
        if (organicContainer) {
            organicContainer.innerHTML = '';
            const organics = data.organic || [];
            organics.forEach(org => {
                const card = document.createElement('div');
                card.className = 'organic-item-card glass-panel';
                card.innerHTML = `
                    <div class="org-name">🌿 ${org.remedy || "Bio-remedy"}</div>
                    <div class="org-ing"><strong>Ingredient:</strong> ${org.ingredient || "Natural extract"}</div>
                    <div class="org-dose"><strong>Dosage:</strong> ${org.dosage || "As indicated"}</div>
                    <div class="org-inst"><strong>Application:</strong> ${org.instructions || "Foliar spray"}</div>
                `;
                organicContainer.appendChild(card);
            });
        }

        // Cultural Prevention
        const prevList = document.getElementById('r-prevention-list');
        if (prevList) {
            prevList.innerHTML = '';
            const prevs = data.prevention || ["Maintain good aeration and sanitized pruning."];
            prevs.forEach(p => {
                const li = document.createElement('li');
                li.innerHTML = `<strong>✓</strong> <span>${p}</span>`;
                prevList.appendChild(li);
            });
        }

        // Metrics Animation
        const confVal = parseFloat(data.confidence) || 94;
        const latVal = parseFloat(data.latency) || 120;
        const sevVal = parseFloat(data.severity_percentage) || 25;

        animateValue(document.getElementById('r-confidence-val'), 0, confVal, 1200, true);
        animateValue(document.getElementById('r-latency-val'), 0, latVal, 800, false);
        animateValue(document.getElementById('r-severity-val'), 0, sevVal, 1200, true);

        // Smooth scroll to results
        resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function animateValue(obj, start, end, duration, isFloat = false) {
        if (!obj) return;
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const val = progress * (end - start) + start;
            obj.textContent = isFloat ? val.toFixed(1) : Math.floor(val);
            if (progress < 1) window.requestAnimationFrame(step);
        };
        window.requestAnimationFrame(step);
    }

    // ==========================================
    // 6. PRESCRIPTION ACTIONS (TTS, PRINT, ETC)
    // ==========================================
    const btnReadTts = document.getElementById('btn-read-tts');
    if (btnReadTts) {
        btnReadTts.addEventListener('click', () => {
            if (!lastDiagnosisData) return;
            const textToSpeak = `Diagnosis report for ${lastDiagnosisData.disease}. 
            Crop affected: ${lastDiagnosisData.crop}. 
            Risk level is ${lastDiagnosisData.risk_level}. 
            Recommended primary medicine: ${lastDiagnosisData.treatment}. 
            Organic remedy: ${lastDiagnosisData.organic && lastDiagnosisData.organic[0] ? lastDiagnosisData.organic[0].remedy : 'Apply neem oil spray'}.`;
            speakText(textToSpeak);
        });
    }

    const btnPrintReport = document.getElementById('btn-print-report');
    if (btnPrintReport) {
        btnPrintReport.addEventListener('click', () => {
            window.print();
        });
    }

    const btnAskAgentDisease = document.getElementById('btn-ask-agent-disease');
    if (btnAskAgentDisease) {
        btnAskAgentDisease.addEventListener('click', () => {
            if (!lastDiagnosisData) return;
            const agentContainer = document.getElementById('ai-agent-container');
            if (agentContainer) agentContainer.classList.remove('hidden');
            const agentInput = document.getElementById('agent-input');
            if (agentInput) {
                agentInput.value = `Tell me more about treating ${lastDiagnosisData.disease}`;
                document.getElementById('agent-send-btn').click();
            }
        });
    }

    const btnGotoFertilizer = document.getElementById('btn-goto-fertilizer');
    if (btnGotoFertilizer) {
        btnGotoFertilizer.addEventListener('click', () => {
            switchTab('fertilizer');
            if (lastDiagnosisData && lastDiagnosisData.crop) {
                const fertCropSelect = document.getElementById('fert-crop');
                if (fertCropSelect) {
                    const cropLow = lastDiagnosisData.crop.toLowerCase();
                    Array.from(fertCropSelect.options).forEach(opt => {
                        if (cropLow.includes(opt.value)) {
                            fertCropSelect.value = opt.value;
                        }
                    });
                    document.getElementById('fert-calc-btn').click();
                }
            }
        });
    }

    function speakText(text) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 0.95;
            utterance.pitch = 1.0;
            window.speechSynthesis.speak(utterance);
        } else {
            alert("Text-to-speech is not supported on this browser.");
        }
    }

    // ==========================================
    // 7. FERTILIZER & NPK CALCULATOR
    // ==========================================
    const fertCalcBtn = document.getElementById('fert-calc-btn');
    if (fertCalcBtn) {
        fertCalcBtn.addEventListener('click', () => {
            const crop = document.getElementById('fert-crop').value;
            const area = parseFloat(document.getElementById('fert-area').value) || 1.0;
            const unit = document.getElementById('fert-unit').value;

            fertCalcBtn.disabled = true;
            fertCalcBtn.textContent = "Calculating...";

            fetch('/api/fertilizer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ crop, area, unit })
            })
                .then(res => res.json())
                .then(data => {
                    fertCalcBtn.disabled = false;
                    fertCalcBtn.textContent = "⚡ Calculate Fertilizer Dosage";

                    document.getElementById('fert-subtitle').textContent =
                        `For ${data.area_requested} of ${data.crop_name} (${data.hectare_equivalent} Hectares):`;

                    document.getElementById('res-urea-bags').textContent = data.urea.bags_45kg;
                    document.getElementById('res-urea-kg').textContent = `Total: ${data.urea.kg} kg (${data.urea.nutrient_supplied})`;

                    document.getElementById('res-dap-bags').textContent = data.dap.bags_50kg;
                    document.getElementById('res-dap-kg').textContent = `Total: ${data.dap.kg} kg (${data.dap.nutrient_supplied})`;

                    document.getElementById('res-mop-bags').textContent = data.mop.bags_50kg;
                    document.getElementById('res-mop-kg').textContent = `Total: ${data.mop.kg} kg (${data.mop.nutrient_supplied})`;

                    document.getElementById('res-zinc-kg').textContent = `${data.micronutrients.zinc_sulphate_kg} kg`;
                    document.getElementById('res-compost-ton').textContent = `${data.micronutrients.organic_compost_tons} Metric Tons`;

                    // Timetable split
                    const schedElem = document.getElementById('fert-schedule-content');
                    schedElem.innerHTML = '';
                    for (const [stg, desc] of Object.entries(data.application_stages)) {
                        const div = document.createElement('div');
                        div.className = 'schedule-item';
                        div.innerHTML = `<strong>${stg}:</strong> <span>${desc}</span>`;
                        schedElem.appendChild(div);
                    }
                })
                .catch(err => {
                    fertCalcBtn.disabled = false;
                    fertCalcBtn.textContent = "⚡ Calculate Fertilizer Dosage";
                    console.error("Fertilizer calculation error:", err);
                });
        });
    }

    // ==========================================
    // 8. MANDI COMMODITY PRICES
    // ==========================================
    let cachedMandiPrices = [];
    function loadMandiPrices() {
        const container = document.getElementById('mandi-container');
        if (!container || cachedMandiPrices.length > 0) return;

        container.innerHTML = '<div class="loading-state">Loading latest mandi commodity rates...</div>';

        fetch('/api/mandi')
            .then(res => res.json())
            .then(data => {
                cachedMandiPrices = data.prices || [];
                renderMandiCards(cachedMandiPrices);
            })
            .catch(err => {
                container.innerHTML = '<div class="error-state">Failed to fetch mandi rates. Check connection.</div>';
            });
    }

    function renderMandiCards(prices) {
        const container = document.getElementById('mandi-container');
        if (!container) return;
        container.innerHTML = '';

        prices.forEach(p => {
            const card = document.createElement('div');
            card.className = 'mandi-card glass-panel';
            const isBullish = p.trend === 'bullish';
            card.innerHTML = `
                <div class="mandi-card-top">
                    <div>
                        <span class="mandi-crop">${p.crop}</span>
                        <div class="mandi-variety">${p.variety}</div>
                    </div>
                    <span class="mandi-trend ${p.trend}">${p.change_24h}</span>
                </div>
                <div class="mandi-price-row">
                    <span class="mandi-currency">₹</span>
                    <span class="mandi-val">${p.price_qtl.toLocaleString('en-IN')}</span>
                    <span class="mandi-unit">/ Quintal</span>
                </div>
                <div class="mandi-range">Range: ₹${p.min_price} - ₹${p.max_price}</div>
                <div class="mandi-market">📍 ${p.market}</div>
                <div class="mandi-advisory">💡 ${p.advisory}</div>
            `;
            container.appendChild(card);
        });
    }

    const mandiSearchInput = document.getElementById('mandi-search-input');
    if (mandiSearchInput) {
        mandiSearchInput.addEventListener('input', (e) => {
            const val = e.target.value.toLowerCase().trim();
            const filtered = cachedMandiPrices.filter(p =>
                p.crop.toLowerCase().includes(val) ||
                p.market.toLowerCase().includes(val) ||
                p.variety.toLowerCase().includes(val)
            );
            renderMandiCards(filtered);
        });
    }

    const mandiFilterChips = document.querySelectorAll('.mandi-filter-chip');
    mandiFilterChips.forEach(chip => {
        chip.addEventListener('click', () => {
            mandiFilterChips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            const filt = chip.getAttribute('data-filter');
            if (filt === 'all') {
                renderMandiCards(cachedMandiPrices);
            } else {
                const filtered = cachedMandiPrices.filter(p => p.crop.toLowerCase().includes(filt));
                renderMandiCards(filtered);
            }
        });
    });

    // ==========================================
    // 9. PEST & WEED DIRECTORY
    // ==========================================
    let cachedPests = [];
    function loadPestDirectory() {
        const container = document.getElementById('pests-container');
        if (!container || cachedPests.length > 0) return;

        fetch('/api/pests')
            .then(res => res.json())
            .then(data => {
                cachedPests = data.pests || [];
                container.innerHTML = '';
                cachedPests.forEach(item => {
                    const card = document.createElement('div');
                    card.className = 'pest-card glass-panel';
                    card.innerHTML = `
                        <div class="pest-card-header">
                            <div>
                                <h3>${item.name}</h3>
                                <span class="pest-scientific">${item.scientific}</span>
                            </div>
                            <span class="badge-pill">Target: ${item.target_crops}</span>
                        </div>
                        <div class="pest-body">
                            <p class="pest-damage"><strong>⚠️ Damage:</strong> ${item.damage}</p>
                            <div class="pest-treatments">
                                <div class="pest-chem">
                                    <strong>💊 Chemical Solution:</strong>
                                    <span>${item.chemical_medicine}</span>
                                </div>
                                <div class="pest-org">
                                    <strong>🌱 Organic Solution:</strong>
                                    <span>${item.organic_remedy}</span>
                                </div>
                            </div>
                            <div class="pest-threshold">🎯 Economic Threshold: ${item.threshold}</div>
                        </div>
                    `;
                    container.appendChild(card);
                });
            })
            .catch(err => console.error("Pest load error:", err));
    }

    // ==========================================
    // 10. ORGANIC BIO-LAB RECIPES
    // ==========================================
    let cachedRecipes = [];
    function loadOrganicRecipes() {
        const container = document.getElementById('recipes-container');
        if (!container || cachedRecipes.length > 0) return;

        fetch('/api/organic')
            .then(res => res.json())
            .then(data => {
                cachedRecipes = data.recipes || [];
                container.innerHTML = '';
                cachedRecipes.forEach(rec => {
                    const card = document.createElement('div');
                    card.className = 'recipe-card glass-panel';

                    const ingList = rec.ingredients.map(i => `<li>• ${i}</li>`).join('');
                    const stepList = rec.steps.map((s, idx) => `<li><strong>Step ${idx + 1}:</strong> ${s}</li>`).join('');

                    card.innerHTML = `
                        <div class="recipe-top">
                            <div>
                                <h3>${rec.title}</h3>
                                <span class="recipe-cat">${rec.category} · Shelf Life: ${rec.shelf_life}</span>
                            </div>
                            <span class="badge-pill green">100% Organic</span>
                        </div>
                        <div class="recipe-app"><strong>🚜 Application:</strong> ${rec.application}</div>
                        <div class="recipe-grid">
                            <div class="recipe-col">
                                <h4>🥣 Ingredients Required</h4>
                                <ul class="styled-list">${ingList}</ul>
                            </div>
                            <div class="recipe-col">
                                <h4>⚗️ Preparation Steps</h4>
                                <ol class="steps-list">${stepList}</ol>
                            </div>
                        </div>
                        <div class="recipe-benefits"><strong>✨ Biological Action:</strong> ${rec.benefits}</div>
                    `;
                    container.appendChild(card);
                });
            })
            .catch(err => console.error("Organic recipes error:", err));
    }

    // ==========================================
    // 11. SOIL HEALTH & pH ADVISOR
    // ==========================================
    const soilSlider = document.getElementById('soil-ph-slider');
    const soilVal = document.getElementById('soil-ph-val');
    const soilEvalBtn = document.getElementById('soil-eval-btn');

    if (soilSlider && soilVal) {
        soilSlider.addEventListener('input', (e) => {
            soilVal.textContent = parseFloat(e.target.value).toFixed(1);
        });
    }

    if (soilEvalBtn) {
        soilEvalBtn.addEventListener('click', () => {
            const ph = parseFloat(soilSlider.value) || 6.8;
            const texture = document.getElementById('soil-texture-select').value;

            soilEvalBtn.disabled = true;
            soilEvalBtn.textContent = "Analyzing Soil Matrix...";

            fetch('/api/soil-advisor', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ ph, texture })
            })
                .then(res => res.json())
                .then(data => {
                    soilEvalBtn.disabled = false;
                    soilEvalBtn.textContent = "🩺 Evaluate Soil & Prescribe Amendments";

                    const badge = document.getElementById('res-soil-badge');
                    badge.textContent = data.category;
                    badge.className = 'status-badge';
                    if (data.badge === 'safe') badge.classList.add('safe');
                    else if (data.badge === 'critical') badge.classList.add('critical');
                    else badge.classList.add('moderate');

                    document.getElementById('res-soil-texture').textContent = `Texture: ${data.texture}`;
                    document.getElementById('res-soil-diag').textContent = data.diagnosis;
                    document.getElementById('res-soil-amend').textContent = data.recommended_amendment;
                    document.getElementById('res-soil-guide').textContent = data.texture_guidance;
                })
                .catch(err => {
                    soilEvalBtn.disabled = false;
                    soilEvalBtn.textContent = "🩺 Evaluate Soil & Prescribe Amendments";
                    console.error("Soil evaluation error:", err);
                });
        });
    }

    // ==========================================
    // 12. SCAN HISTORY STORAGE
    // ==========================================
    function saveScanToHistory(diag) {
        try {
            const history = JSON.parse(localStorage.getItem('agrinet_history') || '[]');
            const record = {
                id: Date.now(),
                timestamp: new Date().toLocaleString(),
                disease: diag.disease,
                crop: diag.crop,
                confidence: diag.confidence,
                severity: diag.severity_percentage,
                treatment: diag.treatment
            };
            history.unshift(record);
            // Limit to 20 past records
            if (history.length > 20) history.pop();
            localStorage.setItem('agrinet_history', JSON.stringify(history));
        } catch (e) {
            console.warn("Could not save to localStorage", e);
        }
    }

    function renderHistoryList() {
        const container = document.getElementById('history-container');
        const countElem = document.getElementById('history-count');
        if (!container) return;

        let history = [];
        try {
            history = JSON.parse(localStorage.getItem('agrinet_history') || '[]');
        } catch (e) { }

        if (countElem) countElem.textContent = `${history.length} Diagnoses Saved`;

        if (history.length === 0) {
            container.innerHTML = `
            <div class="empty-state">
                <span class="empty-icon">🍃</span>
                <p>No previous scans found. Run your first leaf diagnostic to save records here!</p>
            </div>`;
            return;
        }

        container.innerHTML = '';
        history.forEach(item => {
            const card = document.createElement('div');
            card.className = 'history-card glass-panel';
            card.innerHTML = `
                <div class="history-top">
                    <strong>${item.disease}</strong>
                    <span class="history-time">${item.timestamp}</span>
                </div>
                <div class="history-metrics">
                    <span>Crop: ${item.crop}</span> ·
                    <span>Conf: ${item.confidence}%</span> ·
                    <span>Severity: ${item.severity}%</span>
                </div>
                <div class="history-treatment">💊 ${item.treatment}</div>
            `;
            container.appendChild(card);
        });
    }

    const clearHistoryBtn = document.getElementById('clear-history-btn');
    if (clearHistoryBtn) {
        clearHistoryBtn.addEventListener('click', () => {
            if (confirm("Are you sure you want to clear your saved diagnosis history?")) {
                localStorage.removeItem('agrinet_history');
                renderHistoryList();
            }
        });
    }

    // ==========================================
    // 13. CONVERSATIONAL AI AGENT
    // ==========================================
    const agentContainer = document.getElementById('ai-agent-container');
    const agentToggleBtn = document.getElementById('agent-toggle-btn');
    const topAgentBtn = document.getElementById('top-agent-btn');
    const agentCloseBtn = document.getElementById('agent-close-btn');
    const agentMessages = document.getElementById('agent-messages');
    const agentInput = document.getElementById('agent-input');
    const agentSendBtn = document.getElementById('agent-send-btn');
    const agentVoiceBtn = document.getElementById('agent-voice-btn');
    const agentCamera = document.getElementById('agent-camera');
    const agentCaptureBtn = document.getElementById('agent-capture-btn');
    const agentCanvas = document.getElementById('agent-canvas');

    let cameraStream = null;

    function openAgent() {
        if (agentContainer) agentContainer.classList.remove('hidden');
    }

    function closeAgent() {
        if (agentContainer) agentContainer.classList.add('hidden');
        stopCamera();
    }

    if (agentToggleBtn) agentToggleBtn.addEventListener('click', () => {
        if (agentContainer.classList.contains('hidden')) openAgent();
        else closeAgent();
    });

    if (topAgentBtn) topAgentBtn.addEventListener('click', openAgent);
    if (agentCloseBtn) agentCloseBtn.addEventListener('click', closeAgent);

    // Prompt Chips in Agent Window
    const agentChips = document.querySelectorAll('.agent-chip');
    agentChips.forEach(chip => {
        chip.addEventListener('click', () => {
            const query = chip.getAttribute('data-query');
            if (agentInput) agentInput.value = query;
            sendAgentMessage();
        });
    });

    function addMessage(text, sender = 'ai') {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}`;

        // Format message with basic breaks
        const formatted = text.replace(/\n/g, '<br>');
        msgDiv.innerHTML = formatted;

        // Add a TTS button for AI responses
        if (sender === 'ai') {
            const speakBtn = document.createElement('button');
            speakBtn.className = 'msg-speak-btn';
            speakBtn.innerHTML = '🔊';
            speakBtn.title = "Listen to answer";
            speakBtn.addEventListener('click', () => {
                speakText(text.replace(/\[ACTION:[^\]]+\]/g, ''));
            });
            msgDiv.appendChild(speakBtn);
        }

        agentMessages.appendChild(msgDiv);
        agentMessages.scrollTop = agentMessages.scrollHeight;
    }

    async function sendAgentMessage() {
        const text = (agentInput.value || '').trim();
        if (!text) return;

        addMessage(text, 'user');
        agentInput.value = '';

        // Show typing indicator
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message ai typing';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = '<span class="dots">...</span>';
        agentMessages.appendChild(typingDiv);
        agentMessages.scrollTop = agentMessages.scrollHeight;

        try {
            const response = await fetch('/api/agent', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: text })
            });

            const data = await response.json();
            const indicator = document.getElementById('typing-indicator');
            if (indicator) indicator.remove();

            if (data && data.reply) {
                addMessage(data.reply, 'ai');
            } else {
                addMessage("I am here to help! Ask me any question about crops, fertilizers, or site tools.", 'ai');
            }

            // Execute Actions
            if (data && data.action) {
                executeAgentAction(data.action);
            }

        } catch (err) {
            console.error("Agent communication error:", err);
            const indicator = document.getElementById('typing-indicator');
            if (indicator) indicator.remove();
            addMessage("I am running smoothly in offline agronomy mode! Ask me about early blight, fertilizer dosage, mandi prices, or organic recipes.", 'ai');
        }
    }

    function executeAgentAction(action) {
        if (action === "CAMERA") {
            startCamera();
        } else if (action === "BROWSE") {
            switchTab('detector');
            if (browseBtn) browseBtn.click();
        } else if (action === "ANALYZE") {
            switchTab('detector');
            if (analyzeBtn) analyzeBtn.click();
        } else if (action === "RESET") {
            if (resetBtn) resetBtn.click();
        } else if (action === "TAB_FERTILIZER") {
            switchTab('fertilizer');
        } else if (action === "TAB_MANDI") {
            switchTab('mandi');
        } else if (action === "TAB_PESTS") {
            switchTab('pests');
        } else if (action === "TAB_ORGANIC") {
            switchTab('organic');
        } else if (action === "TAB_CALENDAR") {
            switchTab('calendar');
        } else if (action === "TAB_SOIL") {
            switchTab('soil');
        } else if (action === "CLOSE") {
            setTimeout(closeAgent, 1200);
        }
    }

    if (agentSendBtn) agentSendBtn.addEventListener('click', sendAgentMessage);
    if (agentInput) {
        agentInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') sendAgentMessage();
        });
    }

    // ==========================================
    // 14. LIVE CAMERA INTEGRATION
    // ==========================================
    if (cameraTriggerBtn) {
        cameraTriggerBtn.addEventListener('click', () => {
            openAgent();
            startCamera();
        });
    }

    function startCamera() {
        if (cameraStream) return;
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
                .then((vidStream) => {
                    cameraStream = vidStream;
                    agentCamera.srcObject = cameraStream;
                    agentCamera.classList.remove('hidden');
                    agentCaptureBtn.classList.remove('hidden');
                    addMessage("Camera initialized. Place the leaf in the viewfinder and click 'Snap Photo & Load'.", 'ai');
                })
                .catch(err => {
                    console.error("Camera error:", err);
                    addMessage("Unable to access camera. Please allow camera permissions in your browser or use 'Browse Files'.", 'ai');
                });
        } else {
            addMessage("Camera is not supported on this browser context. Please use 'Browse Files'.", 'ai');
        }
    }

    function stopCamera() {
        if (cameraStream) {
            cameraStream.getTracks().forEach(t => t.stop());
            cameraStream = null;
        }
        if (agentCamera) {
            agentCamera.srcObject = null;
            agentCamera.classList.add('hidden');
        }
        if (agentCaptureBtn) agentCaptureBtn.classList.add('hidden');
    }

    if (agentCaptureBtn) {
        agentCaptureBtn.addEventListener('click', () => {
            if (!agentCamera.videoWidth || !agentCamera.videoHeight) {
                addMessage("Camera is still warming up. Please wait a second and retry.", 'ai');
                return;
            }
            agentCanvas.width = agentCamera.videoWidth;
            agentCanvas.height = agentCamera.videoHeight;
            agentCanvas.getContext('2d').drawImage(agentCamera, 0, 0);

            agentCanvas.toBlob((blob) => {
                if (!blob) return;
                const file = new File([blob], "camera_leaf_specimen.jpg", { type: "image/jpeg" });
                handleFile(file);
                stopCamera();
                addMessage("Leaf photo captured and loaded into workspace! Click 'Init Inference' or say 'analyze'.", 'ai');
            }, 'image/jpeg');
        });
    }

    // ==========================================
    // 15. VOICE RECOGNITION (SPEECH-TO-TEXT)
    // ==========================================
    if (agentVoiceBtn && ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRec();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-IN'; // Works for Indian English, Hindi keywords

        recognition.onstart = () => {
            agentVoiceBtn.classList.add('listening');
        };

        recognition.onresult = (e) => {
            agentVoiceBtn.classList.remove('listening');
            const transcript = e.results[0][0].transcript;
            if (transcript) {
                agentInput.value = transcript;
                sendAgentMessage();
            }
        };

        recognition.onerror = () => {
            agentVoiceBtn.classList.remove('listening');
        };

        recognition.onend = () => {
            agentVoiceBtn.classList.remove('listening');
        };

        agentVoiceBtn.addEventListener('click', () => {
            if (agentVoiceBtn.classList.contains('listening')) {
                recognition.stop();
            } else {
                try { recognition.start(); } catch (e) { }
            }
        });
    } else if (agentVoiceBtn) {
        agentVoiceBtn.title = "Voice recognition not supported in this browser.";
    }

    // Environmental sliders live labels
    ['temperature', 'humidity', 'moisture'].forEach(id => {
        const input = document.getElementById(`${id}-input`);
        const valSpan = document.getElementById(id === 'temperature' ? 'temp-val' : id === 'humidity' ? 'hum-val' : 'moist-val');
        if (input && valSpan) {
            input.addEventListener('input', (e) => {
                valSpan.textContent = e.target.value;
            });
        }
    });

    console.log("🌾 AgriNet AI modules fully loaded and ready.");
});
