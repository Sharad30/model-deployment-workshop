#!/bin/bash
# start.sh

# Start Flask API
python api.py &

# Start Streamlit UI
streamlit run ui.py
