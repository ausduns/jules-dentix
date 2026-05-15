import sys

with open('index.html', 'r') as f:
    content = f.read()

footer_html = """
            <!-- Footer -->
            <footer class="w-full bg-[#0252D3] rounded-[20px] p-12 mt-24 mb-12 flex flex-col gap-16 relative overflow-hidden">
                <img src="./assets/images/1gXLHzwx9XdhUodHBIuXNEqNhUo.png" alt="Sparkle Icon" class="absolute top-12 right-12 w-[80px] h-[70px] opacity-20">
                
                <div class="flex flex-col md:flex-row justify-between items-start md:items-end w-full gap-8 relative z-10">
                    <div class="flex flex-col gap-6 max-w-[500px]">
                        <h2 class="text-white text-5xl font-semibold leading-[1.1] tracking-tight">
                            Ready to restore your smile?
                        </h2>
                        <p class="text-white/90 text-lg">
                            Schedule a free consultation and let our experts guide you to a healthier, brighter smile.
                        </p>
                    </div>
                    <div>
                        <a href="#" class="inline-block bg-white text-black font-semibold text-base py-4 px-8 rounded-full hover:bg-gray-100 transition-colors">
                            Book Online
                        </a>
                    </div>
                </div>

                <div class="flex flex-col md:flex-row justify-between items-center border-t border-white/20 pt-8 mt-8 w-full relative z-10 gap-6">
                    <div class="flex items-center gap-2">
                        <img src="./assets/images/6tTbkXggWgQCAJ4DO2QEdXXmgM.svg" alt="Dentix Logo" class="h-6 brightness-0 invert">
                        <span class="text-white font-semibold text-xl">Dentix</span>
                    </div>
                    <div class="flex flex-row gap-6">
                        <a href="#" class="text-white/80 hover:text-white transition-colors">Home</a>
                        <a href="#" class="text-white/80 hover:text-white transition-colors">Services</a>
                        <a href="#" class="text-white/80 hover:text-white transition-colors">Our Clinic</a>
                        <a href="#" class="text-white/80 hover:text-white transition-colors">Dentists</a>
                        <a href="#" class="text-white/80 hover:text-white transition-colors">News</a>
                    </div>
                    <div class="text-white/60 text-sm">
                        © 2026 Dentix. All rights reserved.
                    </div>
                </div>
            </footer>
"""

parts = content.split('            </section>')
new_content = parts[0] + '            </section>' + parts[1] + '            </section>' + parts[2] + '            </section>' + parts[3] + '            </section>' + parts[4] + '            </section>' + parts[5] + '            </section>' + parts[6] + '            </section>\n' + footer_html + parts[7]

with open('index.html', 'w') as f:
    f.write(new_content)

