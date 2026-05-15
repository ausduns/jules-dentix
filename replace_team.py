import sys

with open('index.html', 'r') as f:
    content = f.read()

team_html = """
            <!-- Team Section -->
            <section class="w-full py-24 flex flex-col items-center">
                <!-- Header -->
                <div class="flex flex-col items-center gap-4 mb-16 text-center">
                    <span class="text-gray-500 font-medium text-sm">Our Team</span>
                    <h2 class="text-black text-5xl font-semibold tracking-tight">Meet Our Dental Experts</h2>
                    <p class="text-gray-500 text-lg max-w-[600px] leading-relaxed">
                        Our team of specialists is dedicated to providing you with the highest standard of care in a comfortable environment.
                    </p>
                </div>

                <!-- Team Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 w-full">
                    <!-- Member 1 -->
                    <div class="flex flex-col gap-4">
                        <img src="./assets/images/n897NqofjLqKqeMndhf0j5l5gY0.jpg" alt="Dr. Michael Davis" class="w-full h-[320px] object-cover rounded-[20px]">
                        <div class="flex flex-col gap-1">
                            <h3 class="text-black text-[22px] font-semibold">Dr. Michael Davis</h3>
                            <p class="text-gray-500 text-base">Implantologist & Founder</p>
                        </div>
                    </div>
                    <!-- Member 2 -->
                    <div class="flex flex-col gap-4">
                        <img src="./assets/images/rMviwDhwuq6NpD6BlBA8qDM24ms.jpg" alt="Dr. Sarah Jenkins" class="w-full h-[320px] object-cover rounded-[20px]">
                        <div class="flex flex-col gap-1">
                            <h3 class="text-black text-[22px] font-semibold">Dr. Sarah Jenkins</h3>
                            <p class="text-gray-500 text-base">Prosthodontist</p>
                        </div>
                    </div>
                    <!-- Member 3 -->
                    <div class="flex flex-col gap-4">
                        <img src="./assets/images/5nBoafEAYXgWjDvigY8paH17c.jpg" alt="Dr. Emily Roberts" class="w-full h-[320px] object-cover rounded-[20px]">
                        <div class="flex flex-col gap-1">
                            <h3 class="text-black text-[22px] font-semibold">Dr. Emily Roberts</h3>
                            <p class="text-gray-500 text-base">Endodontist</p>
                        </div>
                    </div>
                    <!-- Member 4 -->
                    <div class="flex flex-col gap-4">
                        <img src="./assets/images/R3hvELrpigktryfqc2B16nTUA94.jpg" alt="Dr. James Wilson" class="w-full h-[320px] object-cover rounded-[20px]">
                        <div class="flex flex-col gap-1">
                            <h3 class="text-black text-[22px] font-semibold">Dr. James Wilson</h3>
                            <p class="text-gray-500 text-base">Oral Surgeon</p>
                        </div>
                    </div>
                </div>
            </section>
"""

parts = content.split('            </section>')
new_content = parts[0] + '            </section>' + parts[1] + '            </section>' + parts[2] + '            </section>' + parts[3] + '            </section>' + parts[4] + '            </section>\n' + team_html + parts[5]

with open('index.html', 'w') as f:
    f.write(new_content)

