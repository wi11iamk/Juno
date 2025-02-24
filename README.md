# Juno

**Juno** is a machine-learning-enabled system designed to optimise scheduling and planning for motor and physical rehabilitation timetables. The system ensures that patients grouped together for therapy have similar impairment and cognitive levels, improving rehabilitation outcomes. It also features an LLM-powered interface for physician interaction, allowing real-time scheduling queries and overrides.

---

## **Features**

- Automated Patient Clustering – Uses hierarchical clustering with Gower distance to group patients with similar impairments.
- Dynamic Scheduling – Adjusts therapy groups as new patient data becomes available.
- LLM-Powered Interaction – Physicians can query schedules, request explanations, and override assignments.
- Structured Override System – Ensures traceability of manual scheduling adjustments.
- Comprehensive Reporting – Generates cluster summaries, rehabilitation schedules, and adjustment logs.
- Robust Logging & Testing – Integrated logging system and a full test suite using PyTest.

---

## **Installation**

### **Prerequisites**
- Python 3.8+
- `pip`
- Virtual environment (optional but recommended)

### **Setup**
```sh
# Clone the repository
git clone https://github.com/wi11iamk/juno.git
cd juno

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## **Usage**

### **Running Juno**
```sh
python main.py
```

### **Running Tests**
To execute all unit and integration tests:
```sh
pytest tests/
```

---

## **Project Structure**
```plaintext
juno/
├── data_processing/        # Handles data loading, preprocessing, and feature engineering
├── clustering/             # Clustering models for patient grouping
├── reporting/              # Report and visualization generation
├── llm_interface/          # LLM-powered physician interaction module
├── utils/                  # Logging, config, and data utilities
├── tests/                  # Unit and integration tests
├── main.py                 # Entry point for execution
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

---

## **LLM-Powered Query System**
The system integrates an LLM API, allowing physicians to interact with schedules and clusters. Queries include:
- "Why was Patient X assigned to Group Y?"
- "Which patients are scheduled for therapy tomorrow?"
- "Override Patient X's assignment due to clinical considerations."

The LLM provides structured responses with additional context when needed.

---

## **Configuration**
System parameters are stored in `utils/config.py`. Key settings include:
```python
# Clustering
DEFAULT_CLUSTERING_METHOD = "hierarchical"
MAX_CLUSTERS = 10

# LLM API
LLM_API_KEY = "your-api-key-here"
LLM_MODEL = "gpt-4"

# Data Handling
MISSING_DATA_HANDLING = "impute"
NUMERIC_SCALING_METHOD = "min-max"
CATEGORICAL_ENCODING = "label"
```

---

## **License**
This project is licensed under the MIT License.

---

## Contributions
If you're interested in improving Juno, feel free to submit a pull request or open an issue.

**Maintainers**: `@wi11iamk`

---

## **Acknowledgments**
Special thanks to the researchers and clinicians in rehabilitation science @UCLH National Hospital for Neurology and Neurosurgery (NHNN), Queen Square for inspiring and contributing to this project.
