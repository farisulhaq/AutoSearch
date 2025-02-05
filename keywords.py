keyword = [
    "Python", "Machine learning", "Artificial intelligence", "Web development",
    "Data science", "Linux", "Automation", "Edge browser", "Programming",
    "Open source", "Cloud computing", "Cybersecurity", "IoT", "Big data",
    "DevOps", "GitHub", "Docker", "Kubernetes", "JavaScript", "React",
    "Node.js", "API", "REST", "GraphQL", "Database", "SQL", "NoSQL",
    "Blockchain", "Cryptocurrency", "Quantum computing", "Robotics",
    "Testing", "UI/UX", "Agile"
]

import random
# Fungsi untuk membuat query pencarian panjang dengan menggabungkan beberapa kata kunci
def generate_long_query():
    num_keywords = random.randint(2, 5)  # Ambil 2 sampai 5 kata kunci
    selected_keywords = random.sample(keyword, num_keywords)    
    return " ".join(selected_keywords)