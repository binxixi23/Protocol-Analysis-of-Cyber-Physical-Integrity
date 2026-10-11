"""
SecureRAG-Field & Cyber-Physical Security Architecture
Module: Disaggregated Serving Optimization and Resource Management
Author: Cuong Dang (Tri Thuc Goc Architecture Contributor)
"""

import logging
from core.config import EDGE_BATTERY_CRITICAL_LEVEL, NETWORK_LATENCY_MAX_MS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [OFFLOAD-OPTIMIZER] - %(levelname)s - %(message)s')

class EdgeOptimizationNode:
    def __init__(self):
        pass

    def evaluate_offload_policy(self, task_type: str, network_telemetry: dict, drone_hardware: dict) -> dict:
        """
        Thực thi Hướng 3: Tối ưu hóa hạ tầng tính toán phân tán (Disaggregated Serving).
        Ra quyết định xử lý cục bộ hay đẩy về Shared GPU Pool ở mặt đất để cứu pin.
        """
        battery_level = drone_hardware.get("battery_pct", 100.0)
        latency_ms = network_telemetry.get("latency_ms", 10.0)
        network_stable = network_telemetry.get("stable", True)

        # Tiêu chí đẩy tác vụ về trạm mặt đất: 
        # Khi pin yếu HOẶC khi gặp tác vụ nhận diện/định giá tài sản rất nặng cần mô hình LLM lớn
        is_resource_critical = (battery_level < EDGE_BATTERY_CRITICAL_LEVEL or task_type == "DEEP_ASSET_VALUATION")
        is_network_capable = (latency_ms < NETWORK_LATENCY_MAX_MS and network_stable)

        if is_resource_critical:
            if is_network_capable:
                logging.info(f"DISAGGREGATED SERVING ACTIVATED: Offloading matrix tasks to Shared GPU Pool. Latency: {latency_ms}ms.")
                return {
                    "policy": "OFFLOAD_TO_GROUND_POOL",
                    "compress_data": False,
                    "target": "REMOTE_CLUSTER"
                }
            else:
                # Trực tiếp giải quyết bài toán mâu thuẫn hạ tầng: Pin yếu nhưng mạng nghẽn
                logging.warning("OPTIMIZATION BOTTLENECK: Network latency exceeds safety threshold. Offload blocked.")
                logging.info("ACTION: Compressing neural network layers. Forcing local quantized fallback execution.")
                return {
                    "policy": "LOCAL_COMPRESSED_EXECUTION",
                    "compress_data": True,
                    "target": "LOCAL_DRONE_NPU"
                }

        # Mặc định: Giữ các tác vụ bay, né vật cản thời gian thực xử lý trực tiếp tại biên
        return {
            "policy": "LOCAL_EDGE_COMPUTE",
            "compress_data": False,
            "target": "LOCAL_DRONE_NPU"
        }
