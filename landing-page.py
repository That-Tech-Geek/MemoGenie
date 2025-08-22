<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MemoGenie - Automate Investment Memos</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #121212;
            color: #E0E0E0;
        }
        .container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }
    </style>
</head>
<body class="antialiased">

    <!-- Navbar -->
    <nav class="bg-transparent py-4">
        <div class="container flex justify-between items-center">
            <a href="#" class="flex items-center text-xl font-bold text-gray-200 hover:text-white transition-colors duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2 text-purple-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"></path>
                </svg>
                MemoGenie
            </a>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="hidden md:block bg-purple-600 hover:bg-purple-700 text-white font-medium py-2 px-6 rounded-full transition-all duration-300 transform hover:scale-105 shadow-lg">
                Get Started
            </a>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="py-16 md:py-24 text-center">
        <div class="container">
            <h1 class="text-4xl md:text-6xl font-extrabold text-white leading-tight mb-4">
                Automate Due Diligence, <br> Accelerate Decisions.
            </h1>
            <p class="text-lg md:text-2xl text-gray-400 mb-8 max-w-2xl mx-auto">
                MemoGenie is your AI-powered co-founder, turning raw startup data into actionable,
                VC-grade investment memos in hours, not weeks.
            </p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-8 rounded-full transition-all duration-300 transform hover:scale-105 shadow-xl">
                Start Building Memos
            </a>
        </div>
    </header>

    <!-- Features Section -->
    <section id="features" class="py-16 md:py-20">
        <div class="container">
            <h2 class="text-3xl md:text-4xl font-bold text-center text-white mb-12">The Engine Behind the Decisions</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Feature 1 -->
                <div class="bg-gray-800 p-8 rounded-2xl shadow-lg border border-gray-700">
                    <div class="flex items-center justify-center h-12 w-12 rounded-full bg-purple-600 text-white mb-4">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <path d="M14 2v6h6"></path>
                            <path d="M12 18V12M9 15h6"></path>
                        </svg>
                    </div>
                    <h3 class="text-xl font-semibold text-white mb-2">Automated Memo Generation</h3>
                    <p class="text-gray-400">
                        Convert unstructured data from pitch decks and financials into a structured, comprehensive investment memo.
                    </p>
                </div>
                <!-- Feature 2 -->
                <div class="bg-gray-800 p-8 rounded-2xl shadow-lg border border-gray-700">
                    <div class="flex items-center justify-center h-12 w-12 rounded-full bg-purple-600 text-white mb-4">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
                            <path d="M13 2v7h7"></path>
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h8"></path>
                            <circle cx="17" cy="17" r="3"></circle>
                            <path d="M17 19.5V22"></path>
                            <path d="M17 14.5V12"></path>
                        </svg>
                    </div>
                    <h3 class="text-xl font-semibold text-white mb-2">OCR & Metadata Parsing</h3>
                    <p class="text-gray-400">
                        Seamlessly process non-downloadable decks and PDFs, extracting key insights with proprietary OCR technology.
                    </p>
                </div>
                <!-- Feature 3 -->
                <div class="bg-gray-800 p-8 rounded-2xl shadow-lg border border-gray-700">
                    <div class="flex items-center justify-center h-12 w-12 rounded-full bg-purple-600 text-white mb-4">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 10h-1.5a2.5 2.5 0 0 0 0 5h1.5a2.5 2.5 0 0 0 0-5H16"></path>
                            <path d="M21 6V4a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-2"></path>
                            <path d="M6 10h1.5a2.5 2.5 0 0 1 0 5H6"></path>
                        </svg>
                    </div>
                    <h3 class="text-xl font-semibold text-white mb-2">Proprietary Valuation Model</h3>
                    <p class="text-gray-400">
                        Get a data-backed valuation using comparative multiple modeling, integrated directly into the memo.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section id="contact" class="py-16 md:py-20 text-center">
        <div class="container">
            <div class="bg-purple-600 p-8 rounded-3xl shadow-2xl">
                <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">
                    Ready to 10x Your Due Diligence?
                </h2>
                <p class="text-lg md:text-xl text-purple-200 mb-8">
                    Stop wasting time on manual work. Get the intel you need, faster than ever.
                </p>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXMbAaHSCNuMt-AKI1kCpFfag5Eezp-bXabptdDhim9qN9Yg/viewform?usp=dialog" class="bg-white text-purple-600 font-bold py-3 px-8 rounded-full transition-all duration-300 transform hover:scale-105 shadow-xl">
                    Get Access
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-8 text-center text-gray-500">
        <div class="container">
            <p>&copy; 2025 MemoGenie. All rights reserved.</p>
        </div>
    </footer>

</body>
</html>
