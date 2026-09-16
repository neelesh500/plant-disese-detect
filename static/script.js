const dragArea = document.getElementById('drag-area');
const fileInput = document.getElementById('file-input');
const browseBtn = document.getElementById('browse-btn');
const previewArea = document.getElementById('preview-area');
const imagePreview = document.getElementById('image-preview');
const analyzeBtn = document.getElementById('analyze-btn');
const resetBtn = document.getElementById('reset-btn');
const resultsContainer = document.getElementById('results-container');

let file;

// Browse button click
browseBtn.addEventListener('click', () => {
    fileInput.click();
});

// File input change
fileInput.addEventListener('change', function () {
    file = this.files[0];
    showPreview();
});

// Drag and drop events
dragArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dragArea.classList.add('active');
    dragArea.querySelector('h3').textContent = "Release to Upload";
});

dragArea.addEventListener('dragleave', () => {
    dragArea.classList.remove('active');
    dragArea.querySelector('h3').textContent = "Drag & Drop Leaf Image Here";
});

dragArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dragArea.classList.remove('active');
    file = e.dataTransfer.files[0];
    showPreview();
});

function showPreview() {
    if (file && file.type.startsWith('image/')) {
        const fileReader = new FileReader();
        fileReader.onload = () => {
            const fileURL = fileReader.result;
            imagePreview.src = fileURL;
            dragArea.classList.add('hidden');
            previewArea.classList.remove('hidden');
            resultsContainer.classList.add('hidden'); // hide results if re-uploading
        };
        fileReader.readAsDataURL(file);
    } else {
        alert("Please upload an image file.");
    }
}

// Reset button
resetBtn.addEventListener('click', () => {
    file = null;
    imagePreview.src = "";
    previewArea.classList.add('hidden');
    dragArea.classList.remove('hidden');
    resultsContainer.classList.add('hidden');
    dragArea.querySelector('h3').textContent = "Drag & Drop Leaf Image Here";
});

// Analyze Button Interaction (Connect to Python Backend)
analyzeBtn.addEventListener('click', () => {
    if (!file) return;

    analyzeBtn.textContent = "Processing via ResNet-50 & C++ Engine...";
    analyzeBtn.disabled = true;

    const formData = new FormData();
    formData.append('file', file);

    // Call Python backend
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            analyzeBtn.textContent = "Analyze with Hybrid ML/CNN";
            analyzeBtn.disabled = false;

            // Show results
            resultsContainer.classList.remove('hidden');
            document.getElementById('r-disease').textContent = data.disease;
            document.getElementById('r-confidence').textContent = data.confidence;
            document.getElementById('r-latency').textContent = data.latency;
            document.getElementById('r-treatment').textContent = data.treatment;

            // Scroll to results
            resultsContainer.scrollIntoView({ behavior: 'smooth' });
        })
        .catch(error => {
            console.error('Error:', error);
            analyzeBtn.textContent = "Error! Try Again.";
            analyzeBtn.disabled = false;
            setTimeout(() => { analyzeBtn.textContent = "Analyze with Hybrid ML/CNN"; }, 2000);
        });
});
