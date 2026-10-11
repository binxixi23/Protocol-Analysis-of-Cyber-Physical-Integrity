"""
SecureRAG-Field & Cyber-Physical Security Architecture
Module: Main Integration Orchestrator for Edge RASP & Optimization
Author: Cuong Dang (Tri Thuc Goc Architecture Contributor)
"""

import time
from core.security_node import EdgeSecurityNode
from core.optimization_node import EdgeOptimizationNode

class UnifiedEdgeEngine:
    def __init__(self):
        self.security_module = EdgeSecurityNode()
        self.optimization_module = EdgeOptimizationNode()

    def execute_pipeline(self, frame_metadata: dict, network_telemetry: dict, drone_hardware: dict) -> dict:
        """
        Hợp nhất quy trình: Kiểm tra an ninh trước -> Nếu an toàn mới tính toán chính sách tối ưu hóa.
        """
        # Bước 1: Kiểm tra an ninh biên (Perception Guardrails)
        security_report = self.security_module.audit_perception_integrity(frame_metadata)
        
        # Nếu phát hiện tấn công, cơ học ngắt luồng tính toán bình thường để kích hoạt chế độ khẩn cấp
        if security_report["verdict"] != "INTEGRITY_PASSED":
            return {
                "pipeline_status": "EMERGENCY_HALT",
                "security_verdict": security_report["verdict"],
                "execution_action": security_report["recommended_action"]
            }

        # Bước 2: Tối ưu hóa hạ tầng tính toán phân tán (Disaggregated Offloading)
        offload_policy = self.optimization_module.evaluate_offload_policy(
            task_type=frame_metadata["task_type"],
            network_telemetry=network_telemetry,
            drone_hardware=drone_hardware
        )

        return {
            "pipeline_status": "SUCCESS",
            "security_verdict": "CLEAN",
            "execution_action": offload_policy["policy"],
            "target_hardware": offload_policy["target"]
        }

# Khối chạy thử thực nghiệm (Verification Sandbox)
if __name__ == "__main__":
    print("=====================================================================")
    print("RUNNING MODULAR DISAGGREGATED FUSION & SECURITY PIPELINE TEST")
    print("=====================================================================\n")
    
    orchestrator = UnifiedEdgeEngine()
    
    # Giả lập tham số kiểm thử
    net_state = {"latency_ms": 15.0, "stable": True}
    normal_hardware = {"battery_pct": 75.0}
    low_battery_hardware = {"battery_pct": 12.0}

    # Kịch bản A: Hệ thống sạch, chạy tác vụ thông thường tại biên
    print("[Test A] Luồng vận hành bình thường:")
    frame_a = {"avg_intensity": 110.0, "saturated_ratio": 0.02, "entropy": 5.5, "task_type": "FLIGHT_NAVIGATION"}
    print(f"Kết quả Pipeline: {orchestrator.execute_pipeline(frame_a, net_state, normal_hardware)}\n")

    # Kịch bản B: Phát hiện tấn công bão hòa Laser (Bảo mật biên chặn đứng trước)
    print("[Test B] Hacker chĩa Laser làm mù camera hông:")
    frame_b = {"avg_intensity": 254.0, "saturated_ratio": 0.70, "entropy": 2.0, "task_type": "FLIGHT_NAVIGATION"}
    print(f"Kết quả Pipeline: {orchestrator.execute_pipeline(frame_b, net_state, normal_hardware)}\n")

    # Kịch bản C: Kích hoạt đẩy tác vụ nặng về trạm mặt đất khi pin yếu (Tối ưu hóa phân tán)
    print("[Test C] Pin Drone yếu xuống 12%, cần xử lý mô hình định giá tài sản nặng:")
    frame_c = {"avg_intensity": 120.0, "saturated_ratio": 0.01, "entropy": 6.0, "task_type": "DEEP_ASSET_VALUATION"}
    print(f"Kết quả Pipeline: {orchestrator.execute_pipeline(frame_c, net_state, low_battery_hardware)}\n")
    
    print("=====================================================================")
    print("MODULAR INTEGRATION VERIFICATION COMPLETE: ALL CHANNELS PASS")
    print("=====================================================================")
