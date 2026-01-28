# Oxygen Storage Capacity (OSC) Modeling & Visualization

This project models the **Oxygen Storage Capacity (OSC)** of an automotive catalytic converter and generates **lookup tables (LUTs)** and **visualizations** used for calibration and analysis in fuel injection and emissions control systems.

The code computes OSC based on **catalyst geometry and washcoat chemistry**, and visualizes the sensitivity of OSC to key parameters using **contour plots and 3D surface plots**.

---

## 📌 Physical Background

The OSC is modeled as a function of:

- Catalyst volume  
- Washcoat loading  
- Ceria (CeO₂) weight fraction  
- Oxygen utilization efficiency  

### Assumptions & Constants

- Cell density: **750 CPSI**
- Geometry factor (`k`): **5.5**
- Oxygen storage capacity of CeO₂:  
  **1 g CeO₂ stores 0.11 g O₂**
- Catalyst volume range: **0.86 – 1.0 L**

---

## 🧮 OSC Model

The OSC is computed using:
Washcoat mass = Volume × Washcoat loading
CeO₂ mass = Washcoat mass × CeO₂ wt fraction
Stored O₂ = CeO₂ mass × 0.11 × η
Geometric factor = CPSI × k × Volume

OSC = Geometric factor × Stored O₂

---

## 📊 Outputs Generated

Running the script generates the following:

### 1️⃣ Contour Plots
- **Volume vs Washcoat Loading**
- **Volume vs CeO₂ Weight Fraction**
- **Volume vs Utilisation Efficiency**

Each contour represents constant OSC levels.

### 2️⃣ Filled OSC Contour Plot
- Explicit **OSC contour plot** for  
  **Volume vs Washcoat Loading**

### 3️⃣ 3D Surface Plot
- **Volume × Washcoat → OSC**  
  Useful for sensitivity and trend analysis.

### 4️⃣ Lookup Table (LUT)
- 10-point LUT generated using:
  - Volume
  - Washcoat loading
  - CeO₂ wt fraction
  - Utilisation efficiency
- Exported as:
  osc_lookup_table.csv

  This LUT can be directly used for **ECU calibration or interpolation**.

  ---

## 🗂 Project Structure
```
.
├── main.py
├── osc_lookup_table.csv
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies
```bash
pip install numpy pandas matplotlib
```

2. Run the Script
python main.py

🧠 Applications

Fuel injection strategy tuning

Lambda control logic

OSC-based air–fuel ratio correction

Catalyst sizing and material optimization

Emissions calibration studies

🚀 Future Extensions

Temperature-dependent OSC

Catalyst aging effects

Sulfur poisoning models

Real-time 2D LUT interpolation for ECUs

📄 License

This project is intended for educational and research purposes.
Feel free to modify and extend it for academic or internal engineering use.

👤 Author

Developed for catalytic converter OSC modeling and visualization using Python.
