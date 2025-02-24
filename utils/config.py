"""Configuration file for system parameters and settings."""

# Logging Configuration
LOG_FILE = "logs/system.log"
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Clustering Settings
DEFAULT_CLUSTERING_METHOD = "hierarchical"  # Options: hierarchical, k-means, fuzzy
CLUSTERING_THRESHOLD = 1.5  # Max deviation for override validation
MAX_CLUSTERS = 10  # Upper limit for number of clusters

# Override Rules
OVERRIDE_ALLOWED_DEVIATION = 1.5  # Standard deviation multiplier for override validation
OVERRIDE_LOGGING_ENABLED = True  # Track all override actions

# LLM API Settings
LLM_API_KEY = "your-api-key-here"
LLM_MODEL = "gpt-4"
LLM_MAX_TOKENS = 150  # Limit on generated token length
LLM_TEMPERATURE = 0.7  # Controls randomness in responses
LLM_FALLBACK_ON_FAILURE = True  # Use structured response if API fails

# Scheduling Settings
DEFAULT_SESSION_DURATION = 60  # Minutes per rehab session
MAX_PATIENTS_PER_SESSION = 5  # Limit for group therapy
THERAPIST_ASSIGNMENT_METHOD = "auto"  # Options: auto, manual

# Data Handling
MISSING_DATA_HANDLING = "impute"  # Options: impute, drop, flag
NUMERIC_SCALING_METHOD = "min-max"  # Options: standard, min-max, robust
CATEGORICAL_ENCODING = "label"  # Options: one-hot, label, ordinal
