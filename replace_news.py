import sys

with open('index.html', 'r') as f:
    content = f.read()

news_html = """
            <!-- News Section -->
            <section class="w-full py-24 flex flex-col items-center">
                <!-- Header -->
                <div class="flex flex-row items-end justify-between w-full mb-12">
                    <div class="flex flex-col gap-4">
                        <span class="text-gray-500 font-medium text-sm">Our Blog</span>
                        <h2 class="text-black text-5xl font-semibold tracking-tight">Latest News & Articles</h2>
                    </div>
                    <a href="#" class="hidden md:inline-block bg-black text-white font-semibold text-base py-4 px-8 rounded-full hover:bg-gray-800 transition-colors">
                        All Articles
                    </a>
                </div>

                <!-- Articles Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full">
                    <!-- Article 1 -->
                    <div class="flex flex-col gap-6 group cursor-pointer">
                        <div class="w-full h-[280px] overflow-hidden rounded-[20px]">
                            <img src="./assets/images/ZUrYFSjw34S5aoakErg7x52HLg.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="flex flex-col gap-3">
                            <span class="text-gray-500 text-sm font-medium">Dental Care • 5 min read</span>
                            <h3 class="text-black text-2xl font-semibold group-hover:text-[#0252D3] transition-colors">How to maintain your dental implants for a lifetime</h3>
                        </div>
                    </div>
                    <!-- Article 2 -->
                    <div class="flex flex-col gap-6 group cursor-pointer">
                        <div class="w-full h-[280px] overflow-hidden rounded-[20px]">
                            <img src="./assets/images/lW0gFXBltpg3jFjCrbeimGiyTI.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="flex flex-col gap-3">
                            <span class="text-gray-500 text-sm font-medium">Treatments • 4 min read</span>
                            <h3 class="text-black text-2xl font-semibold group-hover:text-[#0252D3] transition-colors">The truth about teeth whitening: What works best?</h3>
                        </div>
                    </div>
                    <!-- Article 3 -->
                    <div class="flex flex-col gap-6 group cursor-pointer">
                        <div class="w-full h-[280px] overflow-hidden rounded-[20px]">
                            <img src="./assets/images/f22WJf9yNd0BO2Obq9Kn7Fb9RM.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="flex flex-col gap-3">
                            <span class="text-gray-500 text-sm font-medium">Oral Health • 6 min read</span>
                            <h3 class="text-black text-2xl font-semibold group-hover:text-[#0252D3] transition-colors">Understanding the link between oral health and overall wellness</h3>
                        </div>
                    </div>
                </div>
            </section>
"""

parts = content.split('            </section>')
new_content = parts[0] + '            </section>' + parts[1] + '            </section>' + parts[2] + '            </section>' + parts[3] + '            </section>' + parts[4] + '            </section>' + parts[5] + '            </section>\n' + news_html + parts[6]

with open('index.html', 'w') as f:
    f.write(new_content)

