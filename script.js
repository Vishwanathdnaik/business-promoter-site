let progress = 0;
const progressBar = document.getElementById("progressBar");
const progressText = document.getElementById("progressText");

function simulateBuild() {
  if (progress < 100) {
    progress += 1;
    progressBar.style.width = progress + "%";
    progressText.textContent = progress + "%";
    setTimeout(simulateBuild, 80); // speed of loading
  } else {
    document.querySelector('.tagline').textContent = "✅ Build Complete. Welcome!";
  }
}

simulateBuild();