from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)

# HTML content for the main page
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Page with Background</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background-image: url('https://iili.io/2qcueHP.jpg');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .glowing-box {
            position: relative;
            display: inline-block;
            padding: 20px 40px;
            border: 2px solid transparent;
            border-radius: 8px;
            margin-bottom: 1em;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(255, 255, 0, 0.5);
        }

        .glowing-box h1 {
            font-size: 2.5em;
            font-weight: bold;
            color: #ffeb3b;
            margin: 0;
            text-shadow: 0 0 10px #ffeb3b, 0 0 15px #ff9800;
        }

        .glowing-box::before {
            content: "";
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            border-radius: 8px;
            background: linear-gradient(120deg, transparent, #ffeb3b, transparent);
            animation: smooth-glow 3s ease-in-out infinite;
            z-index: -1;
        }

        @keyframes smooth-glow {
            0% { transform: rotate(0deg); }
            50% { transform: rotate(180deg); }
            100% { transform: rotate(360deg); }
        }

        p {
            font-size: 1.5em;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
            margin-bottom: 1em;
        }

        .button {
            display: block;
            padding: 10px 20px;
            background-color: red;
            color: white;
            border: none;
            font-size: 1.2em;
            cursor: pointer;
            border-radius: 5px;
            transition: 0.3s;
            margin: 10px auto;
            width: 200px;
        }

        .button:hover {
            box-shadow: 0 0 10px 3px red, 0 0 15px 5px #ff4d4d;
        }

        /* Styles for the new page */
        .new-page {
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 20px;
            overflow: hidden;
        }

        .new-page img {
            max-width: 80%; /* Adjusted size for better visibility */
            height: auto;
            margin-bottom: 20px;
            border: 3px solid #ffeb3b;
            border-radius: 8px;
            cursor: pointer;
        }

        .intro-text {
            font-size: 1.2em;
            margin: 10px 0;
            display: none; /* Initially hidden */
        }

        .nav-buttons {
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin-top: 20px;
        }

        .contact-links {
            margin-top: 20px;
            font-size: 1em;
        }

        .contact-links a {
            color: #ffeb3b;
            text-decoration: none;
            margin: 5px;
            display: inline-block;
            transition: color 0.3s;
        }

        .contact-links a:hover {
            color: white;
        }
    </style>
</head>
<body>
    <div class="glowing-box">
        <h1>FAIZU X3 WAQAS</h1>
    </div>
    <p>Select an Option:</p>
    <button class="button" onclick="alert('Multi Selected!')">Multi</button>
    <button class="button" onclick="showIntroOwners()">Intro Owners</button>

    <div class="new-page" id="introPage">
        <img id="introImage" src="https://iili.io/2qckZxe.jpg" alt="Intro Image" onclick="showDescription()">
        <div id="descriptionContainer" class="intro-text"></div>
        <div class="nav-buttons">
            <button class="button" id="prevButton" onclick="showPreviousImage()" style="display:none;">Previous</button>
            <button class="button" id="nextButton" onclick="showNextImage()">Next</button>
        </div>
        <button class="button" onclick="closeIntroPage()">Close</button>
        <div class="contact-links">
            <h2>Contact Us:</h2>
            <a href="https://www.facebook.com/The.drugs.ft.chadwick.67" target="_blank">Profile 1</a>
            <a href="https://www.facebook.com/AlShaitaanH3R3" target="_blank">Profile 2</a>
            <a href="https://www.facebook.com/oprabhu.prabhu.14" target="_blank">Profile 3</a>
            <a href="https://www.facebook.com/profile.php?id=100088283280432" target="_blank">Profile 4</a>
            <a href="https://www.facebook.com/profile.php?id=61554311372080" target="_blank">Profile 5</a>
        </div>
    </div>

    <script>
        const images = [
            "https://iili.io/2qckZxe.jpg", // Image 1
            "https://iili.io/2qcpZ8B.jpg", // Image 2
            "https://iili.io/2qlKJYG.jpg", // Image 3
            "https://iili.io/2qlKUu4.jpg", // Image 4
            "https://iili.io/2qlKaG1.jpg"  // Image 5
        ];

        const descriptions = [
            "Hello guys! This is the APK <strong>Faizu</strong> that I created for you. If you face any issues with it, please let us know!", // Image 1
            "Hello guys! This is the APK <strong>Faizu</strong> that I created for you. If you face any issues with it, please let us know!", // Image 2
            "Hello guys! This is the APK <strong>Faizu</strong> that I created for you. If you face any issues with it, please let us know!", // Image 3
            "Hello guys! This is the APK <strong>Faizu</strong> that I created for you. If you face any issues with it, please let us know!", // Image 4
            "Hello guys! This is the APK <strong>Faizu</strong> that I created for you. If you face any issues with it, please let us know!"  // Image 5
        ];

        let currentImageIndex = 0;

        function showIntroOwners() {
            document.querySelector('.new-page').style.display = 'flex';
            showImage(currentImageIndex);
        }

        function closeIntroPage() {
            document.querySelector('.new-page').style.display = 'none';
        }

        function showImage(index) {
            const introImage = document.getElementById("introImage");
            const descriptionContainer = document.getElementById("descriptionContainer");

            introImage.src = images[index];
            descriptionContainer.innerHTML = ""; // Clear previous description
            descriptionContainer.style.display = 'none'; // Hide description initially

            // Update button visibility
            document.getElementById("prevButton").style.display = index === 0 ? "none" : "block";
            document.getElementById("nextButton").style.display = index === images.length - 1 ? "none" : "block";
        }

        function showDescription() {
            const descriptionContainer = document.getElementById("descriptionContainer");
            descriptionContainer.innerHTML = descriptions[currentImageIndex];
            descriptionContainer.style.display = 'block'; // Show the description
        }

        function showNextImage() {
            if (currentImageIndex < images.length - 1) {
                currentImageIndex++;
                showImage(currentImageIndex);
                document.getElementById("descriptionContainer").style.display = 'none'; // Hide description
            }
        }

        function showPreviousImage() {
            if (currentImageIndex > 0) {
                currentImageIndex--;
                showImage(currentImageIndex);
                document.getElementById("descriptionContainer").style.display = 'none'; // Hide description
            }
        }
    </script>
</body>
</html>
"""

# Define the route for the homepage
@app.route('/')
def index():
    return render_template_string(html_content)

# Start the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)