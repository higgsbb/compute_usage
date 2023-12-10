import streamlit as st
import psutil
import time

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    return cpu_percent, memory_info.percent

def main():
    st.title("System Monitor")

    # Initialize empty lists to store data for plotting
    cpu_data = []
    memory_data = []

    # Create a Streamlit line chart
    cpu_chart = st.line_chart(data=cpu_data, use_container_width=True)
    memory_chart = st.line_chart(data=memory_data, use_container_width=True)

    while True:
        cpu_percent, memory_percent = get_system_info()

        # Append new data to the lists
        cpu_data.append(cpu_percent)
        memory_data.append(memory_percent)

        # Keep only the last 60 data points for better visualization
        cpu_data = cpu_data[-60:]
        memory_data = memory_data[-60:]

        # Update the Streamlit line charts
        cpu_chart.line_chart(data=cpu_data)
        memory_chart.line_chart(data=memory_data)

        # Add a short delay to control the update frequency
        time.sleep(1)

if __name__ == "__main__":
    main()
