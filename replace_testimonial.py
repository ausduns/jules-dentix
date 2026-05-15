import sys

with open('index.html', 'r') as f:
    content = f.read()

testimonial_html = """
            <!-- Testimonial Section -->
            <section class="w-full flex flex-col md:flex-row gap-8 py-24">
                
                <!-- Image -->
                <div class="w-full md:w-1/2 flex items-center justify-center">
                    <img src="./assets/images/rzlzHy3I6STZ9IgJLALZ6E7wnY.jpg" alt="Happy Patient" class="w-[512px] h-[624px] object-cover rounded-3xl">
                </div>

                <!-- Testimonial Content -->
                <div class="w-full md:w-1/2 bg-[#0252D3] rounded-3xl p-12 flex flex-col justify-between">
                    <div class="flex flex-col gap-6">
                        <h2 class="text-white text-[32px] leading-tight font-medium">
                            "A truly exceptional clinic. The staff is welcoming, and Dr. Davis made sure I was comfortable the whole visit. They didn't rush anything. Every option was explained clearly."
                        </h2>
                        <p class="text-white text-lg opacity-90">
                            – Sara, 57
                        </p>
                    </div>

                    <div class="flex flex-row gap-3 pt-12 flex-wrap">
                        <span class="border border-white/30 text-white rounded-full px-4 py-2 text-sm">Dental implants</span>
                        <span class="border border-white/30 text-white rounded-full px-4 py-2 text-sm">Crowns</span>
                        <span class="border border-white/30 text-white rounded-full px-4 py-2 text-sm">Whitening</span>
                    </div>
                </div>

            </section>
"""

services_end_marker = '            </section>'
parts = content.split('            </section>')
# Hero, About, Visit, Services
new_content = parts[0] + '            </section>' + parts[1] + '            </section>' + parts[2] + '            </section>' + parts[3] + '            </section>\n' + testimonial_html + parts[4]

with open('index.html', 'w') as f:
    f.write(new_content)

