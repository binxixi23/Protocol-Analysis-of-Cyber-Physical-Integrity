"""
SecureRAG-Field & Cyber-Physical Security Architecture
Module: System Edge Configurations and Hardware Thresholds
Author: Cuong Dang (Tri Thuc Goc Architecture Contributor)
"""

# Ngưỡng bảo mật chống bão hòa quang học (Exploit 4: Laser Blinding)
SATURATION_THRESHOLD = 250.0        # Điểm ảnh tiến gần ngưỡng trắng xóa (255)
MAX_SATURATED_PIXEL_RATIO = 0.40    # Nếu >40% khung hình bị cháy sáng -> Bị tấn công
MIN_REQUIRED_ENTROPY = 1.0          # Ngưỡng entropy tối thiểu để chống Replay Attack

# Ngưỡng tối ưu hóa hạ tầng tính toán phân tán (Disaggregated Serving)
EDGE_BATTERY_CRITICAL_LEVEL = 20.0  # Phần trăm pin cảnh báo của Drone
NETWORK_LATENCY_MAX_MS = 50.0       # Độ trễ mạng tối đa cho phép truyền về Shared GPU Pool

# Cấu hình mạng trạm mặt đất
SHARED_GPU_POOL_URL = "https://hcc.edu"
