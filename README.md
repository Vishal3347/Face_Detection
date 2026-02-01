# Face_Detection
A real-time computer vision pipeline that uses Haar Cascade classifiers to detect human presence and trigger automated, event-based video recording and photo capture.

📖 Overview

This project implements a low-latency surveillance system designed to bridge the gap between simple motion detection and intelligent event-based recording.

Unlike standard security software that records continuously, this system utilizes Haar Cascade Classifiers to identify specific human features, triggering storage protocols only when relevant subjects are present.

🔬 Core Concepts & Theory

1. The Viola-Jones Framework (Object Detection)
The system relies on the Viola-Jones algorithm, which utilizes "Haar-like features" to identify human faces and bodies.

Edge & Line Features: The algorithm scans for gradients in brightness (e.g., the bridge of the nose is typically lighter than the eye sockets).

Cascaded Classifiers: To maintain a high frame rate, the system uses a "Cascade." It applies simple filters first to quickly discard non-face regions, only moving to complex computations if a potential match is found.

2. Digital Signal Processing & Optimization
   
To achieve the "Low-Latency" performance, the pipeline applies several optimization techniques:

Grayscale Conversion: Reduces input data from 24-bit color to 8-bit intensity. This decreases the computational load by approximately 66% without losing the structural data required for detection.

Spatial Downsampling: Frames are processed at a reduced scale before upscaling detection coordinates, striking a balance between detection range and CPU utilization.

Neighborhood Verification: Using a minNeighbors threshold ensures detection clusters are dense enough to be valid, effectively filtering out "ghost" detections or background noise.

3. State-Machine Logic for Event-Based Recording
   
The application functions as a Finite State Machine (FSM) with three distinct phases:

Monitoring State: A continuous loop analyzing frame buffers for potential matches.

Triggered State: Transitions when detection probability exceeds the threshold. It instantiates a VideoWriter object using the MP4V codec.

Temporal Buffer (Cooldown): When a subject leaves the frame, the system enters a "Persistence" phase. It continues recording for 5 seconds to account for momentary occlusions, ensuring a seamless video clip.

4. Throttling & Resource Management
   
In the photo-evidence module, a Temporal Throttling mechanism is implemented. This prevents "Data Flooding" by enforcing a mandatory cooldown period between file writes. This ensures storage efficiency while capturing necessary high-quality evidence.

🛠️ System Architecture

Input Layer: High-speed frame acquisition via cv2.VideoCapture.

Processing Layer: Pre-processing involving Gray-scaling and Histogram Equalization.

Inference Layer: Multi-scale object detection using trained XML models.

Storage Layer: Conditional file I/O for asynchronous video writing and timestamped image persistence.

📈 Key Achievements
Reduced Storage Overhead: By implementing event-based recording, the system saves up to 90% more disk space compared to 24/7 recording.

Low CPU Footprint: Optimized for edge devices (like laptops or Raspberry Pis) by minimizing per-frame calculations.
