# Protocol Analysis of Cyber-Physical Integrity
### Framework: Project AI_Trung_Sinh (The Regenerative Riemannian Field Model)
### Contributor: Cuong Dang (Tri Thuc Goc Architecture Contributor)

[![License: MIT](https://shields.io)](https://opensource.org)
[![Python: 3.10+](https://shields.io)](https://python.org)
[![Posture: Standalone Edge](https://shields.io)]()

---

## 🌌 1. Theoretical Foundation: Escaping the Ouroboros Paradox

The current paradigm of Autonomous Vehicles (AVs) and Connected Electric Vehicles (EVs) relies on an architectural illusion: the belief that the system is secure if the over-the-air cellular boundary is encrypted. 

As early-stage LLMs and automated generation systems flood the internet with degraded, synthetic tokens, autonomous agents face **Model Collapse** (The Ouroboros Paradox). Brute-force data mining is dead. Autonomous entities cannot safely evolve by passively consuming unverified raw environmental data.

**Project AI_Trung_Sinh** rejects the view of AI as an unmanaged matrix multiplication engine. Instead, we model data distributions as a dynamic *Information Energy Field*. When AI leaves the digital screen and operates real-world mechanical actuators (Powertrain, BMS, ESC), the physical environment itself becomes an adversarial input vector (Layer 0). Kely adversaries no longer target software vulnerabilities over Wi-Fi/Bluetooth; they use the deterministic laws of physics—lasers, acoustics, and high-power microwaves—to corrupt the sensor feedback loop (*Sensor Loops DoS*).

This framework enforces absolute data integrity at the edge, preserving the pure **Tri Thức Gốc (Core Knowledge Vector)** even under catastrophic sensor degradation or multi-sensor signal poisoning.

---

## 🏛️ 2. Comprehensive System Architecture

This repository maps out an enterprise-grade defense-in-depth matrix dividing the vehicle's automated footprint into three isolated, gateway-monitored execution vectors:

┌────────────────────────────────────────────────────────┐
│     LAYER 1: PERIMETER COMMUNICATION DOMAIN            │
│       (LTE/5G, BLE, eSIM, OAuth Fleet API Tokens)      │
└───────────────────────────┬────────────────────────────┘
▼ [Link-Layer Cryptographic Gateway]
┌────────────────────────────────────────────────────────┐
│     LAYER 2: EDGE PERCEPTION PROCESSING BRAIN          │
│       (Pure Vision Neural Nets, ROS2 Middleware, ViT)  │
└───────────────────────────┬────────────────────────────┘
▼ [Physical Plausibility RASP Engine]
┌────────────────────────────────────────────────────────┐
│     LAYER 3: KINETIC & POWERTAIN MECHANICAL CORE       │
│       (CAN Bus Architecture, BMS Core, ESC Actuators)  │
└────────────────────────────────────────────────────────┘

By placing our defensive software at the boundary between Layer 2 (Perception) and Layer 3 (Kinetics), we block malicious environmental telemetry from reaching mechanical controllers, shifting from reactive software updates to proactive runtime isolation.

---

## 🛠️ 3. Repository File Structure

```unset
Protocol-Analysis-of-Cyber-Physical-Integrity/
│
├── COGNITIVE SABOTAGE.pdf      # Complete academic manuscript detailing 11 exploit vectors
├── Cyber_Physical_System.pdf   # Theoretical reference models mapping multi-sensor data fusion
├── README.md                   # System manifest and technical deployment map
│
└── core/
    └── sensor_fusion_rasp.py   # Production Python edge-module executing multi-variable RASP filters
```

---

## 🚀 4. Technical Deep-Dive: Localized Edge Defense Engine

The active runtime enforcement engine is written in production-grade Python within `core/sensor_fusion_rasp.py`. It implements real-time, physics-bound validation to defend against three high-priority vulnerabilities:

### 🔋 A. Thermodynamic Plausibility Verification (Defeating BMS Saturation)
*   **The Threat:** High-Power Microwave (HPM) pulses target low-voltage internal wiring chassis, creating parasitic currents that force false, extreme battery reads (e.g., jumping to 500°C within 1µs) to force an immediate vehicle shutdown via emergency fuses.
*   **The Mitigation:** The engine calculates real-time thermal acceleration curves (\(dT/dt\)). If a signal jumps faster than physical thermodynamics allow, the RASP logic isolates the noisy telemetry stream and activates a pre-cached safe operation profile to keep the powertrain online.

### 🚗 B. Spatial Metric Fusion Validation (Defeating Acoustic MEMS Exploitation)
*   **The Threat:** Directional ultrasonic devices match the native mechanical resonant frequency of silicon MEMS yaw-rate sensors, causing them to vibrate and output false lateral spin telemetry. This deceives the Electronic Stability Control (ESC) into executing a hard unilateral brake lockup, causing a high-velocity crash.
*   **The Mitigation:** The engine runs a multi-sensor validation loop cross-checking the MEMS sensor against optical flow data and wheel-speed metrics. If the camera registers a linear trajectory but the chip indicates a spinning event, the ESC intervention is suspended to preserve steering control.

### 🛞 C. Link-Layer Cryptographic Rolling Validation (Defeating TPMS Spoofing)
*   **The Threat:** Attackers harvest Tire-Pressure Monitoring System (TPMS) Sensor IDs using Software-Defined Radios (SDR) and broadcast spoofed blowout packets (0 PSI) to trigger autonomous emergency braking.
*   **The Mitigation:** The logic drops unauthenticated frames lacking a dynamic Message Authentication Code (MAC) and checks the packet against physical chassis tilt metrics before executing automated deceleration maneuvers.

---

## 💻 5. Verification Deployment

To verify the runtime compliance of the edge RASP node within an isolated environment, execute the test script directly from your terminal:

```bash
# Navigate to the project root directory
cd C:\Users\16154\Desktop\MyGitProjects\Protocol-Analysis-of-Cyber-Physical-Integrity

# Execute the core validation test suite
python core/sensor_fusion_rasp.py
```

### Expected Output Matrix:
```unset
=====================================================================
INITIALIZING CYBER-PHYSICAL EDGE RASP INTEGRITY ENGINE VERIFICATION
=====================================================================

[Simulation] Step 1: Feeding normal thermodynamic data...
{'status': 'VALIDATED_PASS', 'validated_temperature': 26.5, 'alert_triggered': False}

[Simulation] Step 2: Simulating Exploit 5 (High-Power Microwave Injection)...
WARNING:root:CRITICAL ANOMALY DETECTED: Thermal acceleration rate of 4.7e+02°C/s violates thermodynamics.
INFO:root:ACTION: Triggering Semantic Mitigation. Isolating telemetry stream. Dropping pyro-fuse command.
Resulting Action Matrix: {'status': 'COMPROMISED_REJECT', 'validated_temperature': 26.5, 'alert_triggered': True}

[Simulation] Step 3: Simulating Exploit 6 (Acoustic MEMS Resonance Targeting ESC Core)...
ERROR:root:KINETIC INJECTION ATTACK INDICATION: MEMS yaw rate (45.2) conflicts with Physics Domain.
INFO:root:ACTION: Mechanically suspending automated ESC intervention. Returning raw mechanical control to operator.
Resulting Action Matrix: {'status': 'SENSOR_COMPROMISE_ISOLATE', 'execute_braking': False, 'raise_dashboard_alarm': True}

=====================================================================
VERIFICATION TESTING COMPLETED: CORE SYSTEMS SAFE WITH ZERO RUNTIME FAULTS
=====================================================================
```

---
## 📄 License
This repository is open-sourced under the terms of the **MIT License**. 